# Natural Language Processing
repository for natural language processing projects and scripts

📄 NLP_guide1.ipynb 
- Guide with basic commands for text preprocessing in NLP.

📄 NLP01_Spacy.ipynb 
- Guided activity on natural language processing using the SpaCy library for the course Neural Processing of Natural Language in Portuguese I (University of São Paulo).

📄 text_generation_hugginface.ipynb 
- Text generation with a model from Meta's LLaMA family, using quantization to optimize execution on GPUs with less VRAM.

📄 text-generation_huggingface-gemma.ipynb 
- Text generation with a model from Google's Gemma family, built for instruction tasks and using quantization to optimize execution on GPUs with less VRAM.

📄 temperature_comparison.ipynb 
- This project demonstrates the impact of temperature on text generation by large-scale language models (LLMs). We use the Phi-3-mini-4k-instruct model.

📄 text-generation_lcel+runnables.ipynb 
- This project implements a text generation pipeline using LangChain Expression Language (LCEL) and Runnables with Meta's Llama 2 model. Through this approach, it is possible to create structured prompts, optimize model execution, and add custom functions such as word count in the generated text.

📄 text-generation_lcel+functions.ipynb 
- This project implements a text generation pipeline using LangChain Expression Language (LCEL) and Runnables with Meta's Llama 2 model. In addition to the structured prompt-based text generation functionality, this version includes additional custom functions using Runnables that process the model's output. In addition to the word count functionality, there is a text complexity calculation, measuring the average number of words per sentence.

📁 llm_local 
- This project presents two experiments for implementing Large-Scale Language Models (LLMs) on a local machine. 1. Hugging Face: The Meta-Llama-3-8B-Instruct model was accessed through the Hugging Face Hub API, using LangChain to facilitate integration. Here, the model runs in the Hugging Face cloud, without the need for local processing. 2. Ollama: The Phi-3 model was executed locally through Ollama, allowing inference without relying on external servers.

📄 RAG_project.ipynb 
- This project implements an AI-based Q&A system using Meta’s Llama 3 8B model, combined with RAG (Retrieval-Augmented Generation) to fetch and retrieve information before generating answers. The pipeline includes: 1. Testing without RAG: the model answers based only on the knowledge embedded in it. 2. Testing with RAG: the model first fetches information from a vector database (ChromaDB) and uses this context to generate more accurate answers.

📄 transcricao_resumo_videos.ipynb 
- This project enables automatic transcription and content analysis of YouTube videos. It allows you to obtain detailed information about a video without having to watch it in its entirety. The system combines transcription APIs with language models (LLMs) for content summarization and analysis.

📁 virtual_assistant 
- This project is an interactive virtual assistant developed in Python with Streamlit, integrating multiple language models (OpenAI, Ollama and Hugging Face) to answer questions and interact with users. The system allows dynamic model selection, storing conversation history for a continuous flow of interaction.

📁 RAG-documents
- This project is an interactive chatbot that allows users to ask questions about submitted PDF documents. Using Retrieval Augmented Generation (RAG) techniques, it processes, indexes, and searches relevant information to answer user questions efficiently.





