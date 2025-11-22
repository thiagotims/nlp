# carregando bibliotecas
import streamlit as st
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
load_dotenv()

# conexão com a LLM
id_model = "llama-3.3-70b-versatile" #llama3-70b-8192 - deprecated
llm = ChatGroq(
    model=id_model,
    temperature=0.7,
    max_tokens=None,
    timeout=None,
    max_retries=2,
)

# função de geração de conteúdo
def llm_generate(llm, prompt):
  template = ChatPromptTemplate.from_messages([
      ("system", "Você é um especialista em marketing digital com foco em SEO e escrita persuasiva."),
      ("human", "{prompt}"),
  ])

  chain = template | llm | StrOutputParser()

  res = chain.invoke({"prompt": prompt})
  return res

# interface do usuário com Streamlit
st.set_page_config(page_title = "Gerador de conteúdo", page_icon="🤖")
st.title("✒️ Text Generator AI")

# campos do formulário
topic = st.text_input("Tema:", placeholder="Ex: cuidados com a pele, dicas de passeios, alimentação saudável etc.")
platform = st.selectbox("Plataforma:", ['Instagram', 'Facebook', 'LinkedIn', 'Blog', 'E-mail'])
tone = st.selectbox("Tom:", ['Normal', 'Informativo', 'Inspirador', 'Urgente', 'Informal'])
length = st.selectbox("Tamanho:", ['Curto', 'Médio', 'Longo'])
audience = st.selectbox("Público-alvo:", ['Geral', 'Adolescentes', 'Jovens adultos', 'Famílias', 'Idosos'])
cta = st.text_input("Chamada para Ação (CTA):", placeholder="Ex: Inscreva-se para receber dicas exclusivas!")
hashtags = st.checkbox("Gerar Hashtags")
keywords = st.text_area("Palavras-chave (SEO):", placeholder="Ex: dieta saudável, skincare...")

# acionando a geração de conteúdo
if st.button("Gerar conteúdo"):
  prompt = f"""
  Escreva um texto com SEO otimizado sobre o tema '{topic}'.
  Retorne na sua resposta apenas o texto final e não inclua ele dentro de aspas.
  - Onde será publicado: {platform}.
  - Tom: {tone}.
  - Público-alvo: {audience}.
  - Comprimento: {length}.
  - {"Inclua ao final do texto esta chamada para ação:" + cta if cta else "Não inclua chamada para ação."}
  - {"Retorne ao final do texto hashtags relevantes." if hashtags else "Não inclua hashtags."}
  - {"Palavras-chave que devem estar presentes nesse texto (para SEO): " + keywords if keywords else ""}
  """
  try:
      res = llm_generate(llm, prompt)
      st.markdown(res)
  except Exception as e:
      st.error(f"Erro: {e}")


