# 📦 Sistema de Controle de Estoque

Sistema de controle de estoque desenvolvido em Python com interface gráfica.  
O projeto permite cadastrar, buscar, atualizar e excluir produtos, integrando um banco de dados para armazenamento das informações e visualização em tabela.

## 🚀 Funcionalidades

- Cadastro de produtos
- Busca de produtos por nome
- Atualização de dados
- Exclusão de produtos
- Visualização em tabela
- Atualização automática dos dados na interface

## 🛠️ Tecnologias Utilizadas

- Python
- Tkinter
- ttkbootstrap
- MySQL

## 🖥️ Interface do Sistema

O sistema possui uma interface gráfica simples e funcional, permitindo ao usuário gerenciar produtos de forma rápida através de botões de ação e visualização em tabela.
<img width="842" height="727" alt="Captura de tela 2026-03-04 163434" src="https://github.com/user-attachments/assets/1448a30f-5ca1-426f-a780-b89fcd0ee807" />


## 📂 Estrutura do Projeto
projeto_estoque/
│
├── main.py
├── README.md

## ⚙️ Banco de Dados
Tabela utilizada no MySQL:

```sql
CREATE TABLE venda (
    idprodutos INT AUTO_INCREMENT PRIMARY KEY,
    nome_produto VARCHAR(100),
    valor DECIMAL(10,2),
    quantidade INT
);

▶️ Como Executar o Projeto
Instale as dependências:

pip install ttkbootstrap
pip install mysql-connector-python

Configure o banco de dados MySQL.

Execute o arquivo:

python main.py

🎯 Objetivo do Projeto
Este projeto foi desenvolvido com o objetivo de praticar:

CRUD em Python

Integração com banco de dados

Desenvolvimento de interface gráfica

Estruturação de aplicações desktop

📌 Autor

Luiz Fernando Guizani

Projeto desenvolvido para fins de estudo e aprimoramento em desenvolvimento back-end.
