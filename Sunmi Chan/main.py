import Constants as keys
from telegram.ext import *
import responses
#contains the bot mainframe.
#do not mess with this code unless you know what you're doing
print("bot started...")
def start_command(update,context):
    update.message.reply_text("type random shit to get the bot started")
def help_command(update,context):
    update.message.reply_text("The bot can respond to certain phrases, like 'hello', or 'tell me about yourself' ")
def handle_message(update,context):
    text=str(update.message.text).lower()
    response=responses.s_responses(text)
    update.message.reply_text(response)
def error(update,context):
    print("Update{update} caused error {context.error}")



def main():
    updater=Updater(keys.api_key, use_context=True)
    dp=updater.dispatcher
    dp.add_handler(CommandHandler("start", start_command))
    dp.add_handler(CommandHandler("help", help_command))
    dp.add_handler(MessageHandler(Filters.text, handle_message))
    dp.add_error_handler(error)
    updater.start_polling()
    updater.idle()

main()
