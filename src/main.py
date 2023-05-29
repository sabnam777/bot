from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from bot import Bot

import config

def start(update, context):
    bot = Bot(update.message.chat_id)
    bot.send_start_message()

def help(update, context):
    bot = Bot(update.message.chat_id)
    bot.send_help_message()

def about(update, context):
    bot = Bot(update.message.chat_id)
    bot.send_about_message()

def ping(update, context):
    bot = Bot(update.message.chat_id)
    bot.send_ping_message()

def handle_image(update, context):
    bot = Bot(update.message.chat_id)
    bot.handle_image(update.message)

def main():
    updater = Updater(config.TELEGRAM_BOT_TOKEN, use_context=True)

    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", help))
    dp.add_handler(CommandHandler("about", about))
    dp.add_handler(CommandHandler("ping", ping))

    dp.add_handler(MessageHandler(Filters.photo | Filters.document, handle_image))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
