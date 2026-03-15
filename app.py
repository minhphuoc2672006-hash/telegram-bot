from flask import Flask, request
import requests
import os

TOKEN = os.getenv("TOKEN")

app = Flask(__name__)

def decode_hash(hash_string):
    try:
        number = int(hash_string, 16)
        mod18 = number % 18

        if mod18 == 0:
            mod18 = 18

        if mod18 >= 11:
            tx = "TÀI"
        else:
            tx = "XỈU"

        return mod18, tx

    except:
        return None, None


@app.route("/")
def home():
    return "AI TOOL HASH TX RUNNING"


@app.route("/webhook", methods=["POST"])
def webhook():
    data = request.json

    if "message" in data:
        chat_id = data["message"]["chat"]["id"]
        text = data["message"].get("text", "")

        mod18, tx = decode_hash(text)

        if mod18:
            msg = f"""
🎲 GIẢI MÃ HASH

HASH: {text}

MOD 18 = {mod18}

➡️ KẾT QUẢ: {tx}
"""
        else:
            msg = "❌ Gửi HASH hợp lệ để giải mã"

        requests.post(
            f"https://api.telegram.org/bot{TOKEN}/sendMessage",
            json={
                "chat_id": chat_id,
                "text": msg
            }
        )

    return "ok"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
