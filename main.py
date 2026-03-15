import os
import re
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes

TOKEN = os.getenv("TOKEN")

def decode_hash(hash_string):
    number = int(hash_string, 16)
    result = number % 18

    if 4 <= result <= 10:
        tx = "XỈU"
    elif 11 <= result <= 17:
        tx = "TÀI"
    else:
        tx = "BỘ BA"

    return result, tx


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🎲 CASINO AI\n\nGửi HASH để giải mã mod18."
    )


async def handle(update: Update, context: ContextTypes.DEFAULT_TYPE):

    text = update.message.text

    if re.fullmatch(r"[0-9a-fA-F]{32,64}", text):

        result, tx = decode_hash(text)

        await update.message.reply_text(
            f"""
🎲 GIẢI MÃ HASH

Hash:
{text}

Kết quả: {result}

➡️ {tx}
"""
        )

    else:
        await update.message.reply_text("❌ Hash không hợp lệ")


app = ApplicationBuilder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle))

app.run_polling()
