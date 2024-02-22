from typing import Final
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes
from deep_translator import GoogleTranslator



TOKEN: Final = ''
BOT_USERNAME: Final = '@UnwireddBot'


async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('I can translate phrases from every language to russian, made mostly for me to learn it.')





def handle_response(text):
    processed = text.lower()

    tlumaczenie = GoogleTranslator(source='auto', target='ru').translate(processed)

    return tlumaczenie


async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    message_type: str = update.message.chat.type
    text: str = update.message.text

    print(f'User ({update.message.chat.id}) in {message_type}: "{text}"')

    if message_type == 'group':
        if BOT_USERNAME in text:
            response: str = handle_response(text)
            return response
        else:
            return 0
    else:
        response: str = handle_response(text)

        print('Bot:', response)
        await update.message.reply_text(response)


async def error(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print(f'Update {update} caused error {context.error}')


if __name__ == '__main__':
    print('Starting')
    app = Application.builder().token(TOKEN).build()

    app.add_handler(CommandHandler('start', start_command))
    app.add_handler(MessageHandler(filters.TEXT, handle_message))

    app.add_error_handler(error)

    print('Polling')
    app.run_polling(poll_interval=3)