from abc import ABC, abstractmethod
from datetime import datetime
import textwrap


# ================= CLIENTES =================
class Cliente:
    def __init__(self, endereco):
        self.endereco = endereco
        self.contas = []

    def realizar_transacao(self, conta, transacao):
        transacao.registrar(conta)

    def abrir_conta(self, conta):
        self.contas.append(conta)


class PessoaFisica(Cliente):
    def __init__(self, nome, cpf, endereco, data_nascimento):
        super().__init__(endereco)
        self.nome = nome
        self.cpf = cpf
        self.data_nascimento = data_nascimento


# ================= CONTAS =================
class Conta:
    def __init__(self, numero, cliente):
        self._numero = numero
        self._cliente = cliente
        self._agencia = "0001"
        self._saldo = 0
        self._historico = Historico()

    @classmethod
    def nova_conta(cls, cliente, numero):
        return cls(numero, cliente)

    @property
    def numero(self):
        return self._numero

    @property
    def agencia(self):
        return self._agencia

    @property
    def cliente(self):
        return self._cliente

    @property
    def saldo(self):
        return self._saldo

    @property
    def historico(self):
        return self._historico

    def depositar(self, valor):
        if valor > 0:
            self._saldo += valor
            print(f"Depósito de R${valor} realizado com sucesso.")
            return True
        print("Operação falhou! Valor inválido.")
        return False

    def sacar(self, valor):
        if valor > self._saldo:
            print("Saldo insuficiente.")
            return False
        if valor <= 0:
            print("Valor inválido.")
            return False

        self._saldo -= valor
        print(f"Saque de R${valor} realizado com sucesso.")
        return True


class ContaCorrente(Conta):
    def __init__(self, numero, cliente, limite=200, limite_saque=5):
        super().__init__(numero, cliente)
        self._limite = limite
        self._limite_saque = limite_saque

    def sacar(self, valor):
        numero_saques = len(
            [t for t in self.historico.transacoes if t["tipo"] == "Saque"]
        )

        if numero_saques >= self._limite_saque:
            print("Limite de saques atingido.")
            return False

        if valor > (self.saldo + self._limite):
            print("Saldo + limite insuficiente.")
            return False

        return super().sacar(valor)

    def __str__(self):
        return (
            f"Agência: {self.agencia} | Conta: {self.numero} | "
            f"Cliente: {self.cliente.nome} | Saldo: R${self.saldo:.2f}"
        )


# ================= HISTÓRICO =================
class Historico:
    def __init__(self):
        self._transacoes = []

    @property
    def transacoes(self):
        return self._transacoes

    def adicionar_transacao(self, transacao):
        self._transacoes.append({
            "tipo": transacao.__class__.__name__,
            "valor": transacao.valor,
            "data": datetime.now().strftime("%d/%m/%Y %H:%M:%S"),
        })


# ================= TRANSAÇÕES =================
class Transacao(ABC):
    @property
    @abstractmethod
    def valor(self):
        pass

    @abstractmethod
    def registrar(self, conta):
        pass


class Saque(Transacao):
    def __init__(self, valor):
        self._valor = valor

    @property
    def valor(self):
        return self._valor

    def registrar(self, conta):
        if conta.sacar(self.valor):
            conta.historico.adicionar_transacao(self)


class Deposito(Transacao):
    def __init__(self, valor):
        self._valor = valor

    @property
    def valor(self):
        return self._valor

    def registrar(self, conta):
        if conta.depositar(self.valor):
            conta.historico.adicionar_transacao(self)


# ================= FUNÇÕES =================
def filtrar_cliente(cpf, clientes):
    return next((c for c in clientes if c.cpf == cpf), None)


def recuperar_conta(cliente):
    return cliente.contas[0] if cliente.contas else None


def criar_cliente(clientes):
    cpf = input("CPF: ")
    if filtrar_cliente(cpf, clientes):
        print("Cliente já existe.")
        return

    nome = input("Nome: ")
    nascimento = input("Nascimento: ")
    endereco = input("Endereço: ")

    cliente = PessoaFisica(nome, cpf, endereco, nascimento)
    clientes.append(cliente)


def abrir_conta(clientes, contas):
    cpf = input("CPF: ")
    cliente = filtrar_cliente(cpf, clientes)

    if not cliente:
        print("Cliente não encontrado.")
        return

    numero = len(contas) + 1
    conta = ContaCorrente.nova_conta(cliente, numero)

    contas.append(conta)
    cliente.abrir_conta(conta)


def depositar(clientes):
    cpf = input("CPF: ")
    cliente = filtrar_cliente(cpf, clientes)

    if not cliente:
        print("Cliente não encontrado.")
        return

    conta = recuperar_conta(cliente)
    valor = float(input("Valor: "))

    cliente.realizar_transacao(conta, Deposito(valor))


def sacar(clientes):
    cpf = input("CPF: ")
    cliente = filtrar_cliente(cpf, clientes)

    if not cliente:
        print("Cliente não encontrado.")
        return

    conta = recuperar_conta(cliente)
    valor = float(input("Valor: "))

    cliente.realizar_transacao(conta, Saque(valor))


def extrato(clientes):
    cpf = input("CPF: ")
    cliente = filtrar_cliente(cpf, clientes)

    if not cliente:
        print("Cliente não encontrado.")
        return

    conta = recuperar_conta(cliente)

    print("\nEXTRATO")
    for t in conta.historico.transacoes:
        print(f"{t['data']} - {t['tipo']} R${t['valor']}")

    print(f"Saldo: R${conta.saldo:.2f}")


# ================= MAIN =================
def main():
    clientes = []
    contas = []

    while True:
        print("\n1-Criar Cliente\n2-Abrir Conta\n3-Depositar\n4-Sacar\n5-Extrato\n6-Sair")
        op = input("Opção: ")

        if op == "1":
            criar_cliente(clientes)
        elif op == "2":
            abrir_conta(clientes, contas)
        elif op == "3":
            depositar(clientes)
        elif op == "4":
            sacar(clientes)
        elif op == "5":
            extrato(clientes)
        elif op == "6":
            break


main()