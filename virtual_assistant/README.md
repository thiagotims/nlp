# Impl


## 📝 **Descrição**
Este projeto apresenta dois experimentos de implementação de Modelos de Linguagem de Grande Escala (LLMs) em uma máquina local.  

- **Hugging Face:** O modelo **Meta-Llama-3-8B-Instruct** foi acessado através da API do Hugging Face Hub, utilizando o LangChain para facilitar a integração. Aqui, o modelo roda na nuvem da Hugging Face, sem necessidade de processamento local.  
- **Ollama:** O modelo **Phi-3** foi executado **localmente** através do Ollama, permitindo inferência sem depender de servidores externos.  

- Em suma, a principal diferença entre os experimentos é que o Hugging Face utiliza a **API na nuvem**, enquanto o Ollama permite rodar o modelo **diretamente na máquina local**, garantindo mais privacidade e independência de servidores externos.  

---

## **Ficha Técnica**

| 🔍 **Item**           | 📄 **Descrição** |
|---------------------|----------------|
| **🛠️ Tecnologias** | Python, LangChain, Ollama, Hugging Face Hub |
| **📦 Dependências** | `langchain`, `langchain_community`, `langchain-huggingface`, `langchain_ollama`, `python-dotenv` |
| **⚙️ Funcionalidade** | Comparação entre execução de LLMs na nuvem (Hugging Face) e localmente (Ollama) |
| **📌 Modelos Utilizados** | `meta-llama/Meta-Llama-3-8B-Instruct` (Hugging Face) e `phi3` (Ollama) |
| **🌐 Execução na Nuvem** | Hugging Face Hub (requisição via API) |
| **💻 Execução Local** | Ollama (modelo rodando no próprio hardware) |
| **🔑 Autenticação** | API Key do Hugging Face via `.env` |


