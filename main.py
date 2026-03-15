import os
import hashlib
import random
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes

TOKEN = os.getenv("BOT_TOKEN")

# lệnh start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🤖 BOT PHÂN TÍCH TÀI XỈU\n\n"
        "Gửi mã MD5 để phân tích.\n"
        "Ví dụ:\n"
        "d92536f3bc8f702032445261cdf4767c"
    )

# xử lý tin nhắn
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text.strip()

    try:
        # chuyển md5 → số
        value = int(text, 16)

        # mod 18
        mod = value % 18

        if mod < 3:
            mod += 3

        # xác định tài xỉu
        if mod >= 11:
            result = "TÀI"
            percent = random.randint(60, 90)
        else:
            result = "XỈU"
            percent = random.randint(60, 90)

        msg = (
            "📊 KẾT QUẢ PHÂN TÍCH\n\n"
            f"🎯 Dự đoán: {result}\n"
            f"📈 Tỷ lệ: {percent}%"
        )

        await update.message.reply_text(msg)

    except:
        await update.message.reply_text("❌ Mã không hợp lệ")

def main():

    app = ApplicationBuilder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    print("Bot dang chay...")

    app.run_polling()

if __name__ == "__main__":
    main()
