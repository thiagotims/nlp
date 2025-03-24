#  Implementação de LLMs em Máquina Local: Hugging Face vs. Ollama

# %% Instalação de bibliotecas
"""
pip install langchain langchain_community langchain-huggingface
pip install python-dotenv # carregar variáveis de ambiente
pip install -q langchain_ollama
"""

# %% Importação de bibliotecas
from langchain_huggingface import ChatHuggingFace
from langchain_community.llms import HuggingFaceHub
from langchain_ollama import ChatOllama
from langchain_core.prompts import ChatPromptTemplate
from dotenv import load_dotenv

# %% Carregar variáveis de ambiente
load_dotenv() 
#as variáveis de ambiente ficam disponíveis no ambiente do sistema e podem ser acessadas diretamente por qualquer pacote projetado pra procurá-las, por isso não é necessário usar os.getenv().

# %% Definir template de prompt
system_prompt = "Você é um assistente prestativo e está respondendo perguntas gerais."
user_prompt = "{input}" # a variável {input} funciona como um placeholder e não precisa ser substituída por input_text diretamente. O ChatPromptTemplate usa {input} como uma variável dinâmica que será preenchida quando chamarmos chain.invoke({"input": input_text}).Se colocássemos input_text isso fixaria o input na construção do prompt, impedindo que o modelo aceitasse diferentes entradas dinamicamente.

# Tokens para estrutura do prompt
token_s, token_e = "<|begin_of_text|><|start_header_id|>system<|end_header_id|>", "<|eot_id|><|start_header_id|>assistant<|end_header_id|>"

# Criar template do prompt
prompt = ChatPromptTemplate.from_messages([
    ("system", token_s + system_prompt),
    ("user", user_prompt + token_e)
])

# %% Entrada do usuário
input_text = "Explique em até 2 parágrafos o conceito de entropia em algoritmos de inteligência artificial, de forma clara e objetiva"

# %% Exemplo com Hugging Face
llm_hf = HuggingFaceHub(
    repo_id="meta-llama/Meta-Llama-3-8B-Instruct",
    model_kwargs={
        "temperature": 0.1,
        "return_full_text": False,
        "max_new_tokens": 512,
        #"stop": ["<|eot_id|>"],
    }
)

# Criar cadeia de inferência com Hugging Face
chain_hf = prompt | llm_hf

# Invocar cadeia de inferência (Hugging Face)
res_hf = chain_hf.invoke({"input": input_text})
print(res_hf)
print("-----")

# %% Exemplo com Ollama
##### instalar o Ollama na máquina local com: ollama.com
##### run ollama: ollama serve / run phi3: ollama run phi3

llm_ollama = ChatOllama(
    model="phi3",
    temperature=0.1
)

# Criar cadeia de inferência com Ollama
chain_ollama = prompt | llm_ollama

# Executar modelo Ollama
res_ollama = chain_ollama.invoke({"input": input_text})
print(res_ollama.content)
