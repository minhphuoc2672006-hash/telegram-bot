import os
from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, CommandHandler, ContextTypes, filters

TOKEN = os.getenv("BOT_TOKEN")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("BOT AI TÀI XỈU\nGửi seed để decode")

async def decode(update: Update, context: ContextTypes.DEFAULT_TYPE):

    text = update.message.text.strip()

    try:
        decimal = int(text,16)

        mod18 = decimal % 18
        if mod18 < 3:
            mod18 += 3

        result = "XỈU"
        if mod18 >= 11:
            result = "TÀI"

        dice=[]
        for i in range(0,6,2):
            part=text[i:i+2]
            num=int(part,16)
            dice.append(num%6+1)

        total=sum(dice)

        msg=f"""
SEED: {text}

MOD18: {mod18}

XÚC XẮC: {dice[0]}-{dice[1]}-{dice[2]}
TỔNG: {total}

KẾT QUẢ: {result}
"""

        await update.message.reply_text(msg)

    except:
        await update.message.reply_text("Seed không hợp lệ")

app = ApplicationBuilder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, decode))

app.run_polling()
