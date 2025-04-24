from flask import Flask, request
import requests

app = Flask(__name__)

TELEGRAM_BOT_TOKEN = "8041376394:AAFAJ9kuswBwuCS8qz9ZHn2KVcqbQyGjRXk"
TELEGRAM_CHAT_ID = "-1002414678271"

def enviar_telegram(mensagem):
    url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"
    payload = {
        "chat_id": TELEGRAM_CHAT_ID,
        "text": mensagem
    }
    requests.post(url, json=payload)

@app.route("/webhook", methods=["POST"])
def webhook():
    data = request.get_json()
    tipo = data.get("tipo", "sinal")
    ativo = data.get("ativo", "ativo-desconhecido")
    preco = data.get("preco", "")
    hora = data.get("hora", "")

    mensagem = (
        f"📈 Sinal de {tipo.upper()} detectado!\n"
        f"Ativo: {ativo}\n"
        f"Preço: {preco}\n"
        f"Hora: {hora}"
    )

    enviar_telegram(mensagem)
    return "OK", 200

if __name__ == "__main__":
    app.run(port=5000)
