#!/bin/bash
set -e

# ============================================================
# CONFIGURAÇÕES INICIAIS
# ============================================================
PROJECT_ID="pizzariabot-project"
REGION="southamerica-east1"
AGENT_NAME="PizzariaBot"
SERVICE_ACCOUNT_NAME="dialogflow-bot-sa"
WEBHOOK_NAME="pizzariabot-webhook"
ZIP_PATH="./PizzariaBot_Template.zip"
GENERATIVE_FILE="./generative_settings.json"
# ============================================================

echo "🚀 Iniciando configuração do projeto $PROJECT_ID ..."

# Criar projeto (caso ainda não exista)
gcloud projects create $PROJECT_ID || echo "Projeto já existe"
gcloud config set project $PROJECT_ID

# Ativar APIs necessárias
echo "🔧 Ativando APIs..."
gcloud services enable dialogflow.googleapis.com \
    dialogflowcx.googleapis.com \
    aiplatform.googleapis.com \
    run.googleapis.com \
    cloudfunctions.googleapis.com \
    storage.googleapis.com

# Criar Service Account
echo "👤 Criando Service Account..."
gcloud iam service-accounts create $SERVICE_ACCOUNT_NAME \
  --display-name="Dialogflow Bot Service Account" || echo "Já existe"

# Conceder permissões
echo "🔐 Atribuindo papéis à Service Account..."
gcloud projects add-iam-policy-binding $PROJECT_ID \
  --member="serviceAccount:${SERVICE_ACCOUNT_NAME}@${PROJECT_ID}.iam.gserviceaccount.com" \
  --role="roles/dialogflow.admin"

gcloud projects add-iam-policy-binding $PROJECT_ID \
  --member="serviceAccount:${SERVICE_ACCOUNT_NAME}@${PROJECT_ID}.iam.gserviceaccount.com" \
  --role="roles/aiplatform.user"

# Gerar chave JSON
echo "🔑 Gerando chave da service account..."
gcloud iam service-accounts keys create ./service-account.json \
  --iam-account="${SERVICE_ACCOUNT_NAME}@${PROJECT_ID}.iam.gserviceaccount.com"

# Criar bucket para armazenar exportação (se necessário)
BUCKET_NAME="${PROJECT_ID}-cx-bucket"
gsutil mb -l $REGION gs://$BUCKET_NAME/ || echo "Bucket já existe"

# Criar agente Dialogflow CX
echo "🤖 Criando agente $AGENT_NAME..."
gcloud beta dialogflow cx agents create $AGENT_NAME \
  --display-name=$AGENT_NAME \
  --default-language-code=pt-BR \
  --time-zone="America/Sao_Paulo" \
  --location=$REGION \
  --project=$PROJECT_ID || echo "Agente já existe"

# Importar o template
echo "📦 Importando template do agente..."
gcloud beta dialogflow cx agents import \
  --agent=$AGENT_NAME \
  --location=$REGION \
  --source=$ZIP_PATH \
  --project=$PROJECT_ID \
  --merge-import

# Aplicar as configurações generativas
echo "🧠 Aplicando generative settings..."
gcloud beta dialogflow cx agents generative-settings import \
  --agent=$AGENT_NAME \
  --location=$REGION \
  --source=$GENERATIVE_FILE \
  --project=$PROJECT_ID

# Fazer deploy do webhook
echo "🌐 Fazendo deploy do webhook no Cloud Run..."
cd webhook
gcloud run deploy $WEBHOOK_NAME \
  --source . \
  --region=$REGION \
  --allow-unauthenticated \
  --service-account="${SERVICE_ACCOUNT_NAME}@${PROJECT_ID}.iam.gserviceaccount.com" \
  --project=$PROJECT_ID
cd ..

echo "✅ Tudo pronto!"
echo "➡️ Acesse o agente no Console: https://dialogflow.cloud.google.com/cx/projects/${PROJECT_ID}/locations/${REGION}/agents"
echo "⚙️ Configure o webhook no Dialogflow CX → Fulfillment → Webhook URL com o endpoint gerado pelo Cloud Run."

