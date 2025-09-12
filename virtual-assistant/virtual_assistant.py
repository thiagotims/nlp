# VIRTUAL ASSISTANT (v.0.1-beta)


# ==================== Imports ====================
import os
import webbrowser
import platform
from datetime import datetime
import threading
import time
import requests
import wikipedia
from gtts import gTTS
import sounddevice as sd
import numpy as np
import speech_recognition as sr
from googletrans import Translator
from xml.etree import ElementTree
import unicodedata
import random
import feedparser #noticias

wikipedia.set_lang("pt")

# ==================== Normalização ====================
def normalizar(texto):
    """Remove acentos e converte para minúsculas."""
    return ''.join(c for c in unicodedata.normalize('NFD', texto)
                   if unicodedata.category(c) != 'Mn').lower()

# ==================== Áudio ====================
def falar(texto, slow=False):
    """Converte texto em fala e espera terminar antes de continuar."""
    if not texto:
        return
    arquivo = "voz.mp3"
    try:
        os.remove(arquivo)
    except:
        pass
    tts = gTTS(text=texto, lang="pt", slow=slow)
    tts.save(arquivo)
    sistema = platform.system()
    if sistema == "Windows":
        os.system(f'start /wait mplay32 "{arquivo}"')
    else:
        os.system(f"play {arquivo} >/dev/null 2>&1")

# ==================== Captura de Áudio ====================
r = sr.Recognizer()

def ouvir(duracao=6, fs=16000):
    """Grava áudio do microfone e converte para texto."""
    print("Estou ouvindo...")
    grava = sd.rec(int(duracao*fs), samplerate=fs, channels=1, dtype='int16')
    sd.wait()
    audio_bytes = np.squeeze(grava).tobytes()
    audio_data = sr.AudioData(audio_bytes, fs, 2)
    try:
        texto = r.recognize_google(audio_data, language="pt-BR")
        print(f"Você disse: {texto}")
        return texto
    except:
        return ""

# ==================== Lista de Piadas ====================
piadas = [
    "Por que o livro de matemática se suicidou? Porque tinha muitos problemas.",
    "Qual é o cúmulo do elétron? Estar sempre negativo.",
    "Por que o computador foi ao médico? Porque pegou um vírus.",
    "Como deixar alguém curioso? Eu conto amanhã.",
    "Por que a plantinha não foi atendida no hospital? Porque só tinha médico de plantão." 
]

def contar_piadas():
    piada = random.choice(piadas)
    print(piada)
    falar(piada)

# ==================== Comandos ====================
def abrir_youtube():
    falar("O que você deseja buscar no YouTube?")
    termo = ouvir(duracao=6)
    if termo:
        webbrowser.open(f"https://www.youtube.com/results?search_query={termo}")
        falar(f"Aqui está o que encontrei sobre {termo} no YouTube.")

def buscar_wikipedia():
    falar("O que deseja pesquisar na Wikipédia?")
    termo = ouvir(duracao=8)
    if not termo:
        falar("Não consegui ouvir o que você disse.")
        return
    print(f"[DEBUG] Termo capturado: {termo}")
    try:
        resultados = wikipedia.search(termo)
        if resultados:
            titulo = resultados[0]
            resumo = wikipedia.summary(titulo, sentences=3)
            print(f"[DEBUG] Título encontrado: {titulo}")
            print(resumo)
            falar("Segundo a Wikipédia: " + resumo, slow=True)
        else:
            falar("Não encontrei nada na Wikipédia.")
    except Exception as e:
        print(f"[ERRO] {e}")
        falar("Ocorreu um erro ao buscar na Wikipédia.")

def farmacia_perto():
    webbrowser.open("https://www.google.com/maps/search/farmacia+perto+de+mim")
    falar("Mostrando farmácias próximas no mapa.")

def previsao_tempo():
    try:
        resp = requests.get("https://wttr.in/Sao+Paulo?format=j1", timeout=5)
        dados = resp.json()
        cond = dados["current_condition"][0]
        temp = cond["temp_C"]
        desc = cond["weatherDesc"][0]["value"]
        falar(f"Em São Paulo agora faz {temp} graus, {desc}.")
    except:
        falar("Não consegui obter a previsão do tempo.")

def dizer_horas():
    hora = datetime.now().strftime("%H:%M")
    falar(f"Agora são {hora} horas.")

def falar_texto():
    falar("Digite o texto que deseja ouvir:")
    texto = input("Texto: ")
    falar(texto, slow=True)

def ler_agenda():
    arquivo = os.path.join(os.path.dirname(os.path.abspath(__file__)), "agenda.txt")
    if not os.path.exists(arquivo):
        falar("Não encontrei nenhum arquivo de agenda.")
        return
    falar("Itens da agenda para hoje:", slow=True)
    with open(arquivo, "r", encoding="utf-8") as f:
        for linha in f:
            linha = linha.strip()
            if linha:
                print(linha)
                falar(linha, slow=True)

def pesquisar_google():
    falar("O que deseja pesquisar no Google?")
    termo = ouvir(duracao=6)
    if termo:
        webbrowser.open(f"https://www.google.com/search?q={termo}")
        falar(f"Aqui está o que encontrei sobre {termo} no Google.")


def noticias_dia():
    url = "https://feeds.folha.uol.com.br/emcimadahora/rss091.xml"
    feed = feedparser.parse(url)

    if not feed.entries:
        falar("Não consegui obter notícias hoje.")
        return

    falar("As principais notícias de hoje são:", slow=True)
    for i, entry in enumerate(feed.entries[:6]):
        titulo = entry.title
        print(titulo)
        falar(f"Notícia {i+1}: {titulo}", slow=True)


def traduzir_texto():
    falar("Fale a frase que deseja traduzir para inglês.")
    frase = ouvir(duracao=8)
    if not frase:
        falar("Não consegui ouvir a frase.")
        return
    try:
        tradutor = Translator()
        resultado = tradutor.translate(frase, dest='en')
        print(f"{frase} -> {resultado.text}")

        # Fala em inglês usando gTTS com lang='en'
        arquivo = "voz_en.mp3"
        try:
            os.remove(arquivo)
        except:
            pass
        tts = gTTS(text=resultado.text, lang='en', slow=False)
        tts.save(arquivo)
        sistema = platform.system()
        if sistema == "Windows":
            os.system(f'start /wait mplay32 "{arquivo}"')
        else:
            os.system(f"play {arquivo} >/dev/null 2>&1")

    except Exception as e:
        print(f"[ERRO] {e}")
        falar("Ocorreu um erro na tradução.")


# ==================== Lembretes ====================
def checar_lembretes():
    """Checa a agenda a cada minuto e avisa 5 minutos antes."""
    arquivo = os.path.join(os.path.dirname(os.path.abspath(__file__)), "agenda.txt")
    if not os.path.exists(arquivo):
        return
    while True:
        agora = datetime.now()
        with open(arquivo, "r", encoding="utf-8") as f:
            for linha in f:
                linha = linha.strip()
                if "-" in linha:
                    horario_str, tarefa = linha.split("-", 1)
                    horario_str = horario_str.strip()
                    tarefa = tarefa.strip()
                    try:
                        h, m = map(int, horario_str.split(":"))
                        tarefa_time = agora.replace(hour=h, minute=m, second=0, microsecond=0)
                        delta = (tarefa_time - agora).total_seconds()
                        if 0 < delta <= 300:  # 5 minutos antes
                            falar(f"Lembrete: {tarefa} em 5 minutos.")
                            time.sleep(301)  # evita repetir
                    except:
                        continue
        time.sleep(60)

# ==================== Comandos por palavra-chave ====================
def executar_comando(texto):
    comando_norm = normalizar(texto)

    if "previsao" in comando_norm:
        previsao_tempo()
    elif "youtube" in comando_norm:
        abrir_youtube()
    elif "wikipedia" in comando_norm:
        buscar_wikipedia()
    elif "piada" in comando_norm:
        contar_piadas()
    elif "agenda" in comando_norm:
        ler_agenda()
    elif "pesquisar google" in comando_norm:
        pesquisar_google()
    elif "noticias" in comando_norm:
        noticias_dia()
    elif "traduzir" in comando_norm:
        traduzir_texto()
    elif "horas" in comando_norm:
        dizer_horas()
    elif "falar texto" in comando_norm:
        falar_texto()
    elif "sair" in comando_norm:
        falar("Até logo!")
        return False
    else:
        falar("Comando não reconhecido.")
    return True

# ==================== Loop Principal ====================
if __name__ == "__main__":
    threading.Thread(target=checar_lembretes, daemon=True).start()
    falar("Assistente iniciado. Diga TED e o comando.")

    while True:
        texto = ouvir()
        if texto:
            texto_norm = normalizar(texto)
            if "ted" in texto_norm:  # pode estar em qualquer posição
                if not executar_comando(texto):
                    break



