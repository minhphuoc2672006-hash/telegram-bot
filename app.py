from flask import Flask, request
import requests

TOKEN = "BOT_TOKEN_CUA_BAN"

app = Flask(__name__)

@app.route("/")
def home():
    return "Bot running"

@app.route("/webhook", methods=["POST"])
def webhook():
    data = request.json

    if "message" in data:
        chat_id = data["message"]["chat"]["id"]
        text = data["message"].get("text","")

        requests.post(
            f"https://api.telegram.org/bot{TOKEN}/sendMessage",
            json={
                "chat_id": chat_id,
                "text": "Bạn gửi: " + text
            }
        )

    return "ok"

app.run(host="0.0.0.0", port=10000)
