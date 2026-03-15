async def decode(update, context):

    text = update.message.text.strip()

    try:
        decimal = int(text, 16)

        mod18 = decimal % 18
        if mod18 < 3:
            mod18 += 3

        result = "XỈU"
        if mod18 >= 11:
            result = "TÀI"

        dice = []
        for i in range(0,6,2):
            part = text[i:i+2]
            num = int(part,16)
            dice.append(num % 6 + 1)

        total = sum(dice)

        await update.message.reply_text(
f"""SEED
{text}

MOD18: {mod18}

XÚC XẮC: {dice[0]}-{dice[1]}-{dice[2]}
TỔNG: {total}

KẾT QUẢ: {result}"""
        )

    except:
        await update.message.reply_text("Seed không hợp lệ")
