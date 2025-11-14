require('dotenv').config();
const express = require('express');
const bodyParser = require('body-parser');
const app = express();
app.use(bodyParser.json());
app.post('/webhook', (req, res) => {
  const body = req.body;
  const intent = body.fulfillmentInfo?.tag || null;
  if (intent === 'InformacoesDoLocal') {
    return res.json({
      "fulfillment_response": {
        "messages": [{ "text": { "text": ["Sim — temos salão para clientes com capacidade para até 40 pessoas. Deseja reservar?"] } }]
      }
    });
  }
  return res.json({
    "fulfillment_response": {
      "messages": [{ "text": { "text": ["Desculpe, não entendi — pode reformular?"] } }]
    }
  });
});
const PORT = process.env.PORT || 8080;
app.listen(PORT, () => console.log(`Webhook rodando na porta ${PORT}`));