# ✒️ Text Generator AI

![Python](https://img.shields.io/badge/Python-3.12-blue)

![Streamlit](https://img.shields.io/badge/Streamlit-1.28+-red)

![LangChain](https://img.shields.io/badge/LangChain-Latest-green)

![License](https://img.shields.io/badge/License-MIT-yellow)

Um assistente inteligente para geração automatizada de conteúdo otimizado para marketing digital, utilizando LLMs (Large Language Models) e uma interface intuitiva.

---

## 🎯 Sobre o Projeto

O **Text Generator AI** é uma ferramenta desenvolvida para automatizar e otimizar o processo de criação de conteúdo para marketing digital. Através de inteligência artificial, a aplicação gera textos personalizados e otimizados para SEO, adaptados ao público-alvo e à plataforma de divulgação.

------------
## ❌ O Problema

  Equipes de marketing e criadores de conteúdo enfrentam diversos desafios no dia a dia:

- **⏰ Tempo Escasso**: Horas são gastas criando conteúdos manuais que nem sempre geram conversão

- **💰 Recursos Limitados**: Falta de verba e equipe para produção contínua de conteúdo

- **📚 Expertise Necessária**: Demanda conhecimento especializado em copywriting, SEO e adaptação ao público

- **🔄 Repetitividade**: Tarefas repetitivas que poderiam ser automatizadas

- **🎭 Adaptação Constante**: Necessidade de ajustar tom, estilo e formato para diferentes plataformas

Embora LLMs como ChatGPT estejam disponíveis, o fluxo de trabalho através de websites genéricos não é otimizado para as necessidades específicas de criação de conteúdo estratégico.

---------
## ✅ A Solução

O Text Generator AI oferece um assistente automatizado que:

- 🎨 Adapta o texto ao público-alvo e canal de divulgação específicos

- ⚡ Otimiza o fluxo de criação através de uma interface dedicada

- 🎯 Permite customização completa de parâmetros (tom, tamanho, CTA, etc.)

- 🤖 Automatiza demandas repetitivas de produção de conteúdo

- 📊 Integra otimização SEO diretamente no processo

----
## 🚀 Funcionalidades

### Parâmetros Personalizáveis

- **📝 Tema**: Defina o assunto do conteúdo

- **📱 Plataforma**: Instagram, Facebook, LinkedIn, Blog ou E-mail

- **🎭 Tom**: Normal, Informativo, Inspirador, Urgente ou Informal

- **📏 Tamanho**: Curto, Médio ou Longo

- **👥 Público-alvo**: Geral, Adolescentes, Jovens adultos, Famílias ou Idosos

- **🎯 CTA Personalizado**: Defina sua própria chamada para ação

- **#️⃣ Hashtags**: Geração automática de hashtags relevantes

- **🔍 Palavras-chave SEO**: Otimização para mecanismos de busca

### Vantagens

1. **Interface Intuitiva**: Campos práticos e fáceis de usar

2. **Fluxo Otimizado**: Geração de conteúdo em segundos

3. **Customização Infinita**: Adapte todos os parâmetros conforme necessário

4. **Automação Inteligente**: Reduza tempo gasto em tarefas repetitivas

5. **Resultados Profissionais**: Textos otimizados e persuasivos

----
## 🛠️ Tecnologias

- **[Python 3.12+](https://www.python.org/)**: Linguagem de programação

- **[Streamlit](https://streamlit.io/)**: Framework para interface web

- **[LangChain](https://www.langchain.com/)**: Framework para aplicações com LLMs

- **[Groq](https://groq.com/)**: Infraestrutura de inferência de IA

- **[Llama 3.3 70B](https://ai.meta.com/llama/)**: Modelo de linguagem da Meta

- **[Python-dotenv](https://pypi.org/project/python-dotenv/)**: Gerenciamento de variáveis de ambiente

-----
## 📦 Instalação

### Pré-requisitos

- Python 3.12 ou superior

- pip (gerenciador de pacotes Python)

- Conta e API key da [Groq](https://console.groq.com/)

### Passo a Passo

1. **Clone o repositório e acesse o projeto**

```bash
git clone https://github.com/thiagotims/nlp.git

cd nlp/text-generator
```

2. **Crie um ambiente virtual** (recomendado)

```bash

python -m venv venv

source venv/bin/activate # Linux/Mac

# ou

venv\Scripts\activate # Windows

```

3. **Instale as dependências**

```bash

pip install streamlit langchain-groq langchain-core python-dotenv

```


4. **Configure as variáveis de ambiente**

Crie um arquivo `.env` na raiz do projeto:

```env

GROQ_API_KEY=sua_api_key_aqui

```

---
## 🎮 Uso

1. **Inicie a aplicação**

```bash
streamlit run content_generator.py
```


2. **Acesse no navegador**

```
http://localhost:8501
```

  
3. **Preencha os campos**

- Defina o tema do seu conteúdo

- Selecione a plataforma de publicação

- Escolha o tom e o tamanho desejados

- Defina o público-alvo

- (Opcional) Adicione CTA personalizado, hashtags e palavras-chave


4. **Clique em "Gerar conteúdo"**

- O texto será gerado instantaneamente

- Copie e utilize conforme necessário

-----
## 🖼️ Interface de Usuário

![img](https://github.com/thiagotims/nlp/blob/main/text-generator/img/text-generator-ai.png)

----
## 🤝 Contribuindo

Contribuições são bem-vindas! Sinta-se à vontade para:

1. Fazer um fork do projeto

2. Criar uma branch para sua feature (`git checkout -b feature/NovaFuncionalidade`)

3. Commit suas mudanças (`git commit -m 'Adiciona nova funcionalidade'`)

4. Push para a branch (`git push origin feature/NovaFuncionalidade`)

5. Abrir um Pull Request
----
## 📄 Licença

Este projeto está sob a licença MIT. Veja o arquivo `LICENSE` para mais detalhes.

----
## 🧑‍💻 Autor / Contato
**Thiago Tim**  

Desenvolvido com ❤️ para otimizar a criação de conteúdo digital.

Entre em contato:
[![LinkedIn](https://img.shields.io/badge/LinkedIn-0A66C2?style=flat&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/devtim/) [![Gmail](https://img.shields.io/badge/Gmail-D14836?style=flat&logo=gmail&logoColor=white)](mailto:thiagotimdev@gmail.com)

---

⭐ Se este projeto foi útil para você, considere dar uma estrela!



