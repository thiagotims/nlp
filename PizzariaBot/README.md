
# 🍕 PizzariaBot — Chatbot Inteligente com Dialogflow CX + Vertex AI (Gemini)

[![Google Cloud](https://img.shields.io/badge/Google%20Cloud-Platform-blue?logo=googlecloud)](https://chatgpt.com/c/691355b3-c11c-832b-b89e-917b737c61ae#)  
[![Dialogflow CX](https://img.shields.io/badge/Dialogflow-CX-orange?logo=googlecloud)](https://chatgpt.com/c/691355b3-c11c-832b-b89e-917b737c61ae#)  
[![Vertex AI](https://img.shields.io/badge/Vertex%20AI-Gemini-purple?logo=googlecloud)](https://chatgpt.com/c/691355b3-c11c-832b-b89e-917b737c61ae#)  
[![Cloud Run](https://img.shields.io/badge/Cloud%20Run-Serverless-darkblue?logo=googlecloud)](https://chatgpt.com/c/691355b3-c11c-832b-b89e-917b737c61ae#)  
[![Node.js](https://img.shields.io/badge/Node.js-18.x-green?logo=node.js)](https://chatgpt.com/c/691355b3-c11c-832b-b89e-917b737c61ae#)  
[![Shell Script](https://img.shields.io/badge/Shell%20Script-Automation-lightgrey?logo=gnu-bash)](https://chatgpt.com/c/691355b3-c11c-832b-b89e-917b737c61ae#)  
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://chatgpt.com/c/691355b3-c11c-832b-b89e-917b737c61ae#)

---
## 🧠 Visão Geral

O **PizzariaBot** é um chatbot completo desenvolvido sobre **Dialogflow CX**, com capacidade de combinar:

- **Fluxos determinísticos** (intents, páginas, parâmetros estruturados)
    
- **Fallback generativo avançado** usando **Vertex AI — Gemini**
    
- **Lógica customizada** através de um **webhook Node.js** hospedado no **Cloud Run**
    
- **Automação completa de infraestrutura** via script `setup_pizzariabot.sh`
    
O objetivo é mostrar como construir um assistente conversacional **profissional**, com arquitetura robusta, seguindo boas práticas de **engenharia, cloud e IA generativa**.

Este projeto demonstra competências essenciais para um ambiente moderno:

- 👨‍💻 Desenvolvimento orientado à arquitetura
    
- ☁️ Provisionamento automatizado
    
- 🤖 IA híbrida (estruturada + generativa)
    
- 🧩 Integração com APIs e webhooks
    
- 🔧 Cloud Google de ponta a ponta

---
## 🏗️ Arquitetura Geral

```
┌──────────────────────────────┐
│        Usuário Final         │
└───────────────┬──────────────┘
                │
                ▼
┌─────────────────────────────────────────────┐
│       Dialogflow CX (Agente Pizzaria)       │
│                                             │
│  • Intents estruturadas                     │
│  • Páginas e parâmetros                     │
│  • Gestão de contexto                       │
│  • Fallback generativo (Vertex AI)          │
└───────────────┬─────────────────────────────┘
                │ (Fulfillment)
                ▼
┌─────────────────────────────────────────────┐
│            Webhook Node.js (Cloud Run)      │
│                                             │
│  • Processamento de pedidos                 │
│  • Verificação de disponibilidade           │
│  • Integrações e lógica avançada            │
└───────────────┬─────────────────────────────┘
                │
                ▼
┌─────────────────────────────────────────────┐
│        Vertex AI — Gemini (Fallback IA)     │
│  • Respostas naturais a perguntas abertas   │
│  • Contenção sem quebrar o fluxo            │
└─────────────────────────────────────────────┘
```

---
## 🔩 Tecnologias Utilizadas

|Categoria|Ferramenta|
|---|---|
|NLP|Dialogflow CX|
|IA Generativa|Vertex AI — Gemini|
|Backend Webhook|Node.js + Express|
|Cloud Serverless|Google Cloud Run|
|DevOps|gcloud CLI + Shell Script|
|Autenticação|Google IAM / Service Accounts|
|Infraestrutura|Cloud Platform APIs|

---
# 🚀 Como rodar o projeto

Este projeto foi estruturado para ser **executado com um único script**, simulando o fluxo profissional de automação.

## 1️⃣ Instalar o Google Cloud CLI

[https://cloud.google.com/sdk/docs/install](https://cloud.google.com/sdk/docs/install)

---
## 2️⃣ Autenticar

```bash
gcloud auth login
gcloud auth application-default login
```

---
## 3️⃣ Executar o script de automação

O script está na raiz do projeto:

```bash
chmod +x setup_pizzariabot.sh
./setup_pizzariabot.sh
```

Ele executa:

- ativação das APIs
    
- criação de conta de serviço
    
- deploy do webhook
    
- criação/importação do agente CX
    
- configuração do fallback generativo
    
- link entre o webhook e o DF CX
    
### ❗ Resultado:

Você **não precisa criar nada manualmente** no Google Cloud ou no Dialogflow CX.  

O ambiente inteiro é provisionado sozinho.

---
# 🧪 Testando o Bot

Após o script terminar:

1. Acesse o Console do Dialogflow CX
    
2. Abra o agente gerado
    
3. Clique em **Test Agent**
    
4. Teste as conversas:
    
### Exemplos:

- “Quero pedir uma pizza de calabresa.”

- “Vocês abrem amanhã?”
    
- “Tem estacionamento no local?” (→ Gemini responde)
    
- “Qual o endereço da pizzaria?”
    
- “Pode repetir meu pedido?”
    
---
# 📁 Estrutura do Repositório

```
PizzariaBot/
│
├── webhook/
│   ├── index.js        (lógica principal)
│   ├── package.json
│   └── ...
│
├── intents/            (fluxos/treinamentos do CX)
│
├── generative_settings.json
├── setup_pizzariabot.sh
│
├── README.md
└── .gitignore
```

---

# 🧠 Detalhes técnicos importantes

### ✔ Dialogflow CX para controle determinístico

CX foi escolhido por oferecer:

- páginas
    
- state machine
    
- versionamento
    
- condições avançadas
    
- webhooks dinâmicos
    
- melhores práticas empresariais
    
### ✔ Gemini como “fallback inteligente”

Quando o usuário sai do fluxo, o bot não trava — o Gemini:

- interpreta perguntas abertas
    
- responde de forma natural
    
- mantém contexto do agente
    
- devolve o controle ao fluxo principal
    
### ✔ Webhook com Node.js

Código organizado com:

- Express
    
- tratamento de intents
    
- logs estruturados
    
- JSON limpo
    
- endpoint único para DF CX
    
### ✔ Deploy em Cloud Run

- automático
    
- escalável
    
- HTTPS por padrão
    
- sem necessidade de servidor próprio
    
---
# 🔮 Melhorias futuras

- Painel web de pedidos
    
- Integração com Google Sheets
    
- Base de conhecimento externa
    
- Notificações via WhatsApp API
    
- Dashboard de métricas
    
- Suporte multilíngue
    
- Testes automatizados (Jest)
    
---
# 🧑‍💼 Autor

**Thiago Tim**  
Desenvolvedor com foco em LLMs, automação e soluções em Inteligência Articial e Machine Learning.

Contribuições são bem-vindas!  Entre em contato:
[![LinkedIn](https://img.shields.io/badge/LinkedIn-0A66C2?style=flat&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/devtim/) [![Gmail](https://img.shields.io/badge/Gmail-D14836?style=flat&logo=gmail&logoColor=white)](mailto:thiagotimdev@gmail.com)

---
# 📄 Licença MIT

Uso livre para estudos, modificações e fork.

---

