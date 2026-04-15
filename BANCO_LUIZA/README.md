# 🏦 Sistema Bancário — Bootcamp Luiza Labs

Projeto desenvolvido como atividade prática do bootcamp da **Luiza Labs**, com o objetivo de aplicar os conceitos de **Programação Orientada a Objetos (POO)** em Python através de um sistema bancário funcional via terminal.

---

## 📌 Sobre o projeto

A ideia aqui foi ir além de uma simples calculadora de saldo. O sistema simula operações reais de um banco: criação de clientes, abertura de contas correntes, depósitos, saques com limite e histórico de transações com data e hora.

Tudo foi estruturado usando os pilares da POO — herança, abstração, encapsulamento e polimorfismo — de forma que cada responsabilidade fica bem separada e o código fica fácil de manter e expandir.

---

## 🗂️ Estrutura das classes

```
├── Cliente
│   └── PessoaFisica
├── Conta
│   └── ContaCorrente
├── Historico
├── Transacao (ABC)
│   ├── Deposito
│   └── Saque
```

### O que cada uma faz

**`Cliente` / `PessoaFisica`**  
Representa quem usa o banco. `PessoaFisica` estende `Cliente` adicionando nome, CPF e data de nascimento. Um cliente pode ter várias contas e realizar transações em qualquer uma delas.

**`Conta` / `ContaCorrente`**  
`Conta` é a base com saldo, agência, número e histórico. `ContaCorrente` herda dela e adiciona um **limite de crédito** (padrão R$200) e um **limite de saques diários** (padrão 5). O método `sacar` foi sobrescrito para checar essas regras antes de delegar para a classe pai.

**`Historico`**  
Guarda todas as transações realizadas em uma conta, com tipo, valor e timestamp. Simples e objetivo.

**`Transacao` (classe abstrata)**  
Define o contrato que `Deposito` e `Saque` precisam seguir. Qualquer nova transação no futuro já sabe o que precisa implementar.

---

## ⚙️ Funcionalidades

- [x] Criar cliente (CPF, nome, endereço, data de nascimento)
- [x] Abrir conta corrente vinculada a um cliente
- [x] Realizar depósito
- [x] Realizar saque (com controle de limite e número de saques)
- [x] Visualizar extrato com histórico de transações
- [x] Validações básicas (saldo insuficiente, valor inválido, CPF duplicado)

---

## 🚀 Como rodar

Você precisa ter o **Python 3.8+** instalado.

```bash
# Clone o repositório
git clone https://github.com/cristyann-rd/SISTEMA_BANCARIO.git

# Acesse a pasta
cd BANCO_LUIZA

# Execute o script
python Banco_luiza_labs.py
```

Nenhuma dependência externa — só a biblioteca padrão do Python.

---

## 🖥️ Exemplo de uso

```
1-Criar Cliente
2-Abrir Conta
3-Depositar
4-Sacar
5-Extrato
6-Sair
Opção: 1

CPF: 12345678900
Nome: Ana Souza
Nascimento: 15/04/1995
Endereço: Rua das Flores, 42 - Recife/PE
```

```
Opção: 3
CPF: 12345678900
Valor: 500
Depósito de R$500 realizado com sucesso.
```

```
Opção: 5
CPF: 12345678900

EXTRATO
15/04/2026 10:32:11 - Deposito R$500
Saldo: R$500.00
```

---

## 📚 Conceitos aplicados

| Conceito | Onde aparece |
|---|---|
| **Herança** | `PessoaFisica` → `Cliente`, `ContaCorrente` → `Conta` |
| **Abstração** | Classe `Transacao` com métodos abstratos |
| **Encapsulamento** | Atributos protegidos com `_` e acesso via `@property` |
| **Polimorfismo** | Método `sacar` sobrescrito em `ContaCorrente` |
| **Composição** | `Conta` possui um `Historico`; `Cliente` possui lista de `Conta`s |

---

## 🔭 Possíveis melhorias futuras

- Persistência de dados (JSON ou banco de dados)
- Interface gráfica ou web
- Suporte a múltiplas contas por cliente com seleção interativa
- Relatórios de extrato por período
- Autenticação com senha

---

## 👩‍💻 Autor

Desenvolvido durante o **Bootcamp Luiza Labs**.
Por mim Cristyann Rodrigo
Feito com Python e bastante vontade de aprender. 🐍
