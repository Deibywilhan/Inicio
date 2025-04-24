import time
import requests
from tradingview_ta import TA_Handler, Interval

TELEGRAM_BOT_TOKEN = "8041376394:AAFAJ9kuswBwuCS8qz9ZHn2KVcqbQyGjRXk"
TELEGRAM_CHAT_ID   = "-1002414678271"

def enviar_telegram(msg):
    url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"
    requests.post(url, json={"chat_id": TELEGRAM_CHAT_ID, "text": msg})

def pega_e_envia():
    handler = TA_Handler(
        symbol="BTCUSDT",
        screener="crypto",
        exchange="BINANCE",
        interval=Interval.INTERVAL_1_HOUR
    )
    analysis = handler.get_analysis()
    summary = analysis.summary

    if summary["BUY"] > summary["SELL"]:
        enviar_telegram("🔔 Sinal de COMPRA em BTCUSDT!")
    elif summary["SELL"] > summary["BUY"]:
        enviar_telegram("🔔 Sinal de VENDA em BTCUSDT!")
    # else: nenhum sinal claro

if __name__ == "__main__":
    while True:
        pega_e_envia()
        time.sleep(60 * 30)
