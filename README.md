# SmartFinance

![Python](https://img.shields.io/badge/Python-3.x-blue)
![Status](https://img.shields.io/badge/status-%20concluido-green)
![License](https://img.shields.io/badge/license-MIT-yellow)

O **SmartFinance** é um assistente pessoal de gestão financeira que utiliza Inteligência Artificial para permitir consultas de gastos e receitas de forma rápida e intuitiva, usando linguagem natural.

Diferente de soluções tradicionais baseadas em nuvem, o SmartFinance processa tudo **localmente**, garantindo que seus dados financeiros nunca saiam do seu computador.

---

## 📌 Diferencial

O grande diferencial do SmartFinance é o uso de **IA local (via Ollama)**, garantindo:

*  Privacidade total dos dados
*  Respostas rápidas sem dependência de internet
*  Interpretação inteligente de linguagem natural

---

## Funcionalidades

### Consultas em Linguagem Natural

Faça perguntas como:

* "Quanto gastei com lanche?"
* "Qual meu saldo este mês?"

E receba respostas diretas do sistema.

---

### Privacidade Total

* Integração com modelo **Phi-3 via Ollama**
* Nenhum dado é enviado para servidores externos

---

### Interface Intuitiva
  
* Interface moderna desenvolvida com **CustomTkinter**
* Experiência simples e direta para o usuário

---

### Buscas Inteligentes

Filtros automáticos por:

* Categoria
* Descrição
* Tipo (Receita/Despesa)
* Períodos temporais

Utilizando SQL gerado dinamicamente pela IA.

---

## Tecnologias Utilizadas

* Python 3.x
* Ollama (IA Local - Modelo Phi-3)
* SQLite (Banco de dados local)
* SQLAlchemy (ORM para manipulação de dados)
* CustomTkinter (Interface gráfica)

---

## 📁 Estrutura do Projeto

```
SmartFinance/
│
├── gui.py                  # Interface gráfica principal
├── requirements.txt        # Dependências do projeto
├── README.md               # Documentação
│
├── tests/                  # Testes automatizados
│
├── models/                 # Modelos de dados (SQLAlchemy)
│   └── __init__.py
│
├── database/               # Configuração do banco SQLite
│   └── db.py
│
├── services/               # Regras de negócio
│   └── __init__.py
│
├── ai/                     # Integração com IA (Ollama / Phi-3)
│   └── interpreter.py
│
├── utils/                  # Funções auxiliares
│   └── __init__.py
│
└── assets/                 # Recursos visuais (ícones, imagens, etc.)
```

---

## Como Instalar e Rodar

### 1. Pré-requisitos

* Python instalado
* Ollama instalado com o modelo Phi-3:

```bash
ollama run phi3
```

---

### 2. Instalação

```bash
git clone https://github.com/Gory-Ra/SmartFinance.git
cd SmartFinance

# Criar ambiente virtual
python -m venv venv

# Ativar (Windows)
.\venv\Scripts\activate

# Instalar dependências
pip install -r requirements.txt
```

---

### 3. Executar

```bash
python gui.py
```

---

## Segurança e Privacidade

O SmartFinance foi desenvolvido seguindo o princípio de **Privacy-by-Design**:

* Dados armazenados localmente em `.db`
* Processamento de IA offline
* Código aberto para auditoria

---

##  Testes

A pasta `tests/` contém testes automatizados do sistema.

Para executar:

```bash
pytest
```
---

## Licença

Este projeto está sob a licença MIT.

---

## 📌 Observações

Este projeto foi desenvolvido como estudo e portfólio, com foco em:

* Aplicação de IA local
* Boas práticas em Python
* Arquitetura de software

---

## Autor

Desenvolvido por **Gory-Ra**
