import os
import random
from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, CommandHandler, ContextTypes, filters

TOKEN = os.getenv("BOT_TOKEN")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🤖 BOT AI TÀI XỈU\n\n"
        "Gửi HASH để giải mã kết quả."
    )

async def decode(update: Update, context: ContextTypes.DEFAULT_TYPE):

    text = update.message.text.strip()

    try:
        # chuyển hash sang số
        value = int(text, 16)

        # tính mod
        mod = value % 18

        if mod < 3:
            mod += 3

        # xác định kết quả
        if mod >= 11:
            result = "TÀI"
            percent = random.randint(60, 95)
        else:
            result = "XỈU"
            percent = random.randint(60, 95)

        msg = (
            "📊 KẾT QUẢ PHÂN TÍCH\n\n"
            f"🎯 Dự đoán: {result}\n"
            f"📈 Tỷ lệ: {percent}%"
        )

        await update.message.reply_text(msg)

    except:
        await update.message.reply_text("❌ Hash không hợp lệ")

def main():

    app = ApplicationBuilder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & (~filters.COMMAND), decode))

    print("Bot đang chạy...")

    app.run_polling()

if __name__ == "__main__":
    main()
