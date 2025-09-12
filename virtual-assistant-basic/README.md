# 🤖 Assistente Virtual em Python

Um assistente virtual em Python capaz de ouvir comandos de voz, responder com áudio, executar pesquisas, ler notícias, gerenciar uma agenda e avisar sobre compromissos. Este projeto foi desenvolvido para ser leve, funcional e sem depender de bibliotecas complexas que causam problemas de compatibilidade. Esse projeto foi implementado como "_desafio de projeto_" do curso _BairesDev - Machine Learning Training_ promovido pela BairesDev em parceria com a Dio.

---
## ⚙️ Funcionalidades

O assistente oferece as seguintes funcionalidades:
1. **Pesquisa na Wikipédia**
    - Pesquisa um assunto na Wikipédia.
    - Lê um resumo do resultado em português.
    
2. **Abrir YouTube**
    - Pesquisa vídeos de acordo com o comando de voz.
    
3. **Previsão do tempo**
    - Informa temperatura e condições atuais de São Paulo.
        
4. **Pesquisar no Google**
    - Pesquisa termos diretamente no Google e abre os resultados.
        
5. **Piadas**
    - Conta piadas prontas selecionadas aleatoriamente.
        
6. **Dizer as horas**
    - Informa a hora atual.
        
7. **Falar texto digitado**
    - Lê qualquer texto digitado pelo usuário.
        
8. **Ler agenda**
    - Lê um arquivo `agenda.txt` com os compromissos do dia.
    - Exemplo de formato:
        ```
        14:30 - Reunião com equipe
        16:00 - Consulta médica
        ```
        
9. **Avisar lembretes 5 minutos antes**
    - Monitoramento contínuo da agenda.
    - Alerta automático antes de compromissos.
        
10. **Traduzir texto**
    - Tradução de frases faladas em português para o inglês.
    - Lê a tradução em inglês com voz sintetizada.
        
11. **Notícias do dia**
    - Lê manchetes de notícias de um feed RSS confiável (BBC ou outro feed configurado).
    - Limita a 5-6 manchetes por execução.
        
12. **Comando principal**
    - O assistente só executa funções quando você inicia o comando com a palavra **`TED`**:  
        Exemplo: `"TED me fala a previsão do tempo"`.
        
13. **Sair**
    - Comando `"ted-sair"` para encerrar o assistente.
    
---
## 🛠️ Instalação

1. Clone o repositório:
    ```bash
    git clone <URL_DO_SEU_REPOSITORIO>
    cd <PASTA_DO_REPOSITORIO>
    ```
    
2. Crie um ambiente virtual (recomendado):
    ```bash
    python -m venv venv
    source venv/bin/activate  # Linux / macOS
    venv\Scripts\activate     # Windows
    ```
    
3. Instale as dependências:
    ```bash
    pip install -r requirements.txt
    ```
    
4. (Opcional) Instale o player de áudio no Linux:
    ```bash
    sudo apt-get install sox
    ```
    
    > No Windows, a reprodução de áudio é feita pelo `mplay32`.
    

---
## 📦 Dependências

As principais bibliotecas usadas no projeto:

|Biblioteca|Versão sugerida|Função|
|---|---|---|
|`requests`|2.31.0|Obter previsão do tempo e feeds RSS|
|`wikipedia`|1.4.0|Buscar artigos na Wikipédia|
|`gTTS`|2.3.2|Síntese de voz (texto para fala)|
|`sounddevice`|0.4.8|Captura de áudio do microfone|
|`numpy`|1.27.5|Processamento de áudio|
|`SpeechRecognition`|3.10.0|Reconhecimento de voz via Google Speech API|
|`googletrans`|4.0.0-rc1|Tradução de texto|
|`feedparser`|6.0.10|Leitura de feeds RSS|
|`unicodedata`|nativo do Python|Normalização de texto|
|`threading`|nativo do Python|Execução de tarefas paralelas (ex.: lembretes)|
|`os`, `platform`, `time`, `datetime`, `webbrowser`|nativos|Funções utilitárias|

---
## 🚀 Como Executar

1. Execute o assistente:
    ```bash
    python virtual_assistant.py
    ```
    
2. Fale uma frase contendo o comando pre-configurado iniciando com **`TED`**:
    - `"TED me fala a previsão do tempo"`
    - `"TED abrir YouTube"`
    - `"TED me diga as notícias"`
    - `"TED traduzir frase"`
        
3. Para encerrar:
    - `"TED sair"`
        
4. Crie um arquivo `agenda.txt` na mesma pasta com seus compromissos.
    - Exemplo:
        ```
        09:00 - Reunião com o time
        15:00 - Revisar relatório
        18:00 - Academia
        ```
        
    - O assistente avisará automaticamente 5 minutos antes de cada compromisso.
---
## 📋 Observações
- O comando de voz reconhece a palavra-chave **`TED`** para identificar que você deseja executar uma ação.
- Para melhor precisão, fale de forma clara e próxima ao microfone. O assistente funciona melhor em ambientes silenciosos para reduzir erros de reconhecimento.
- Notícias são obtidas de feeds RSS; é possível configurar outra fonte no código (como BBC ou G1).
- ---
## 🔮 Melhorias Futuras
• Adicionar mais comandos e funcionalidades bem como a integração com outros serviços  (ex: email, calendário).
• Implementar uma interface de usuário (GUI) amigável.
• Melhorar a robustez do reconhecimento de voz (ex: lidar com ruído de fundo)
• Melhorar a gestão de erros e exceções
• Melhorar a função de notícias: definindo algum tipo de especificação de temas ou curadoria

----
## 📃 Licença
Este projeto está sob a licença [MIT](LICENSE).

--------
## 🧑‍💻 Autor / Contato
**Thiago Tim**  

Contribuições são bem-vindas!  Entre em contato:
[![LinkedIn](https://img.shields.io/badge/LinkedIn-0A66C2?style=flat&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/devtim/) [![Gmail](https://img.shields.io/badge/Gmail-D14836?style=flat&logo=gmail&logoColor=white)](mailto:thiagotimdev@gmail.com)

---

