# 📚 Converse com Documentos

Este projeto é um chatbot interativo que permite aos usuários fazer perguntas sobre documentos PDF enviados. Utilizando técnicas de Recuperação Aumentada por Geração (RAG), ele processa, indexa e busca informações relevantes para responder às perguntas dos usuários de forma eficiente.

## 📊 Ficha Técnica

| 🔍                        |                                                                                                   | **Item** | 📝 **Descrição** |
| ------------------------- | ------------------------------------------------------------------------------------------------- | -------- | ---------------- |
| **🛠️ Tecnologias**       | Python, LangChain, Streamlit, FAISS, Hugging Face Transformers                                    |          |                  |
| **📦 Dependências**       | streamlit, langchain, faiss-cpu, torch, langchain-community, langchain-huggingface, python-dotenv |          |                  |
| **⚙️ Funcionalidade**     | Chatbot para responder perguntas sobre documentos PDF usando RAG                                  |          |                  |
| **💊 Modelos Utilizados** | Meta-Llama-3-8B-Instruct (Hugging Face), GPT-4o-mini (OpenAI), Phi-3 (Ollama)                     |          |                  |
| **🎨 Embeddings**         | Modelo "BAAI/bge-m3" para vetorização de textos                                                   |          |                  |
| **🌐 Interface**          | Desenvolvida com Streamlit                                                                        |          |                  |
| **📖 Entrada de Dados**   | Upload de arquivos PDF                                                                            |          |                  |
| **🔄 Busca**              | Vetorização via FAISS e recuperação de contexto                                                   |          |                  |
| **🛡️ Autenticação**      | Suporte a OpenAI API Key e Hugging Face Token                                                     |          |                  |

## 📒 Como Funciona

1. O usuário envia um ou mais arquivos PDF.
2. O sistema processa e divide os documentos em partes menores.
3. Cada parte é transformada em vetores usando embeddings.
4. As perguntas dos usuários são analisadas e reformuladas para uma busca eficiente.
5. A resposta é gerada utilizando um modelo de IA que consulta os trechos mais relevantes dos documentos.

## ⚡ Como Executar

1. Clone o repositório:
   ```bash
   git clone https://github.com/seu-usuario/converse-com-documentos.git
   cd converse-com-documentos
   ```
2. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```
3. Configure as chaves de API no arquivo `.env`:
   ```env
   OPENAI_API_KEY=your_openai_key
   HUGGINGFACEHUB_API_TOKEN=your_huggingface_token
   ```
4. Execute o aplicativo:
   ```bash
   streamlit run chatbot_docs.py
   ```

Agora, basta fazer upload dos documentos e conversar com o chatbot! 💬

