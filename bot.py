import sys
import asyncio
from telegram import Bot, Update
from telegram.ext import Application, MessageHandler, filters

print("Бот запущен", file=sys.stderr)  # принудительный вывод в stderr

TOKEN = "8452923553:AAFMZ1tNikAablHak4IUWtc4rAxCTef5fuc"
CHANNEL_ID = -1002930020998
EDITOR_ID = 217812453

application = Application.builder().token(TOKEN).build()

async def publish_from_editor(update: Update, context):
    if update.effective_user.id != EDITOR_ID:
        return
    if update.message.text:
        await context.bot.send_message(chat_id=CHANNEL_ID, text=update.message.text)

def main():
    print("Запуск поллинга", file=sys.stderr)
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, publish_from_editor))
    application.run_polling()
    print("Поллинг завершён", file=sys.stderr)

if __name__ == "__main__":
    main()
