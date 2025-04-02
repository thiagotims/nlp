# Natural Language Processing
repository for natural language processing projects and scripts

1. 📄 **NLP_guide1.ipynb** [🔗](https://github.com/thiagotims/nlp/blob/main/NLP_guide1.ipynb)
  - Guide with basic commands for text preprocessing in NLP.
2. 📄 **NLP01_Spacy.ipynb** [🔗](https://github.com/thiagotims/nlp/blob/main/NLP01_Spacy.ipynb)
  - Guided activity on natural language processing using the SpaCy library for the course Neural Processing of Natural Language in Portuguese I (University of São Paulo).
3. 📄 **text_generation_hugginface.ipynb** [🔗](https://github.com/thiagotims/nlp/blob/main/text_generation_hugginface.ipynb)
  - Text generation with a model from Meta's LLaMA family, using quantization to optimize execution on GPUs with less VRAM.
4. 📄 **text-generation_huggingface-gemma.ipynb** [🔗](https://github.com/thiagotims/nlp/blob/main/text-generation_huggingface_gemma.ipynb)
  - Text generation with a model from Google's Gemma family, built for instruction tasks and using quantization to optimize execution on GPUs with less VRAM.
5. 📄 **temperature_comparison.ipynb** [🔗](https://github.com/thiagotims/nlp/blob/main/temperature_comparison.ipynb)
  - This project demonstrates the *impact of temperature* on text generation by large-scale language models (LLMs). We use the `Phi-3-mini-4k-instruct` model.
6.  📄 **text-generation_lcel+runnables.ipynb** [🔗](https://github.com/thiagotims/nlp/blob/main/text_generation_lcel%2Brunnables.ipynb)
  - This project implements a text generation pipeline using LangChain Expression Language (LCEL) and Runnables with Meta's Llama 2 model. Through this approach, it is possible to create structured prompts, optimize model execution, and add custom functions such as word count in the generated text.
7.  📄 **text-generation_lcel+functions.ipynb** [🔗](https://github.com/thiagotims/nlp/blob/main/text_generation_lcel%2Bfunctions.ipynb)
  - This project implements a text generation pipeline using LangChain Expression Language (LCEL) and Runnables with Meta's Llama 2 model. In addition to the structured prompt-based text generation functionality, this version includes additional custom functions using Runnables that process the model's output. In addition to the word count functionality, there is a text complexity calculation, measuring the average number of words per sentence.
8. 📁 **llm_local** [🔗](https://github.com/thiagotims/nlp/tree/main/llm_local)
  - This project presents two experiments for implementing Large-Scale Language Models (LLMs) on a local machine. 1. Hugging Face: The Meta-Llama-3-8B-Instruct model was accessed through the Hugging Face Hub API, using LangChain to facilitate integration. Here, the model runs in the Hugging Face cloud, without the need for local processing. 2. Ollama: The Phi-3 model was executed locally through Ollama, allowing inference without relying on external servers.
9. 📄 **RAG_project.ipynb**  [🔗](https://github.com/thiagotims/nlp/blob/main/RAG_project.ipynb)
  - This project implements an AI-based Q&A system using Meta’s Llama 3 8B model, combined with RAG (Retrieval-Augmented Generation) to fetch and retrieve information before generating answers. The pipeline includes: 1. Testing without RAG: the model answers based only on the knowledge embedded in it. 2. Testing with RAG: the model first fetches information from a vector database (ChromaDB) and uses this context to generate more accurate answers.
10. 📄 **transcricao_resumo_videos.ipynb**  [🔗](https://github.com/thiagotims/nlp/blob/main/transcricao_resumo_videos.ipynb)
  - This project enables automatic transcription and content analysis of YouTube videos. It allows you to obtain detailed information about a video without having to watch it in its entirety. The system combines transcription APIs with language models (LLMs) for content summarization and analysis.
11. 📁 **virtual_assistant** [🔗](https://github.com/thiagotims/nlp/tree/main/virtual_assistant)
  - This project is an interactive virtual assistant developed in Python with Streamlit, integrating multiple language models (OpenAI, Ollama and Hugging Face) to answer questions and interact with users. The system allows dynamic model selection, storing conversation history for a continuous flow of interaction.
