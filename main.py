import os
import threading
from flask import Flask
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

# lấy token từ Environment
TOKEN = os.getenv("BOT_TOKEN")

app = Flask(__name__)

@app.route("/")
def home():
    return "BOT TX ONLINE"

# lệnh /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("🤖 Bot tài xỉu đang hoạt động!")

# lệnh /ping
async def ping(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("🏓 PONG - Bot vẫn sống!")

def run_bot():
    bot = ApplicationBuilder().token(TOKEN).build()

    bot.add_handler(CommandHandler("start", start))
    bot.add_handler(CommandHandler("ping", ping))

    print("Telegram bot started...")
    bot.run_polling()

# chạy bot song song flask
threading.Thread(target=run_bot).start()

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
