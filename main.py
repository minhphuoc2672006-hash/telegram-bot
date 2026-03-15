from flask import Flask
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import threading

TOKEN = 8695119555:AAHgO_ep9tUc0nkGCq9DD-w7fLVhVMnb-kA

app = Flask(__name__)

@app.route("/")
def home():
    return "BOT TX ONLINE"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Bot tài xỉu đã hoạt động!")

def run_bot():
    bot = ApplicationBuilder().token(TOKEN).build()
    bot.add_handler(CommandHandler("start", start))
    bot.run_polling()

threading.Thread(target=run_bot).start()

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
