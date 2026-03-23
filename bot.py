import asyncio
from telegram import Bot, Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters
from telegram.request import HTTPXRequest

TOKEN = "8452923553:AAFMZ1tNikAablHak4IUWtc4rAxCTef5fuc"
CHANNEL_ID = -1002930020998
YOUR_ID = 631917030  # твой ID

# Если нужно использовать прокси (только SOCKS5 или HTTP)
# request = HTTPXRequest(proxy="socks5://ip:port")
# application = Application.builder().token(TOKEN).request(request).build()

application = Application.builder().token(TOKEN).build()

async def echo_to_channel(update: Update, context):
    user_id = update.effective_user.id
    if user_id != YOUR_ID:
        await update.message.reply_text("Доступ запрещён")
        return
    # Пересылаем текст в канал
    await context.bot.send_message(chat_id=CHANNEL_ID, text=update.message.text)

def main():
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo_to_channel))
    print("Бот запущен")
    application.run_polling()

if __name__ == "__main__":
    main()
