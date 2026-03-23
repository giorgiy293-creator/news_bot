import asyncio
from telegram import Bot, Update
from telegram.ext import Application, MessageHandler, filters

TOKEN = "8452923553:AAFMZ1tNikAablHak4IUWtc4rAxCTef5fuc"
CHANNEL_ID = -1002930020998
EDITOR_ID = 217812453  # мой ID, теперь бот будет слушать меня

application = Application.builder().token(TOKEN).build()

async def publish_from_editor(update: Update, context):
    # Проверяем, что сообщение пришло от меня
    if update.effective_user.id != EDITOR_ID:
        return
    # Если это ответ на сообщение (можно игнорировать), или просто текст
    if update.message.text:
        await context.bot.send_message(chat_id=CHANNEL_ID, text=update.message.text)

def main():
    # Слушаем все текстовые сообщения
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, publish_from_editor))
    application.run_polling()

if __name__ == "__main__":
    main()
