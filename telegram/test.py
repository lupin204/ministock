import logging
from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, ConversationHandler, CallbackContext

# Set up logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)

# Define states for the conversation
START, TEST = range(2)

# Define a function to start the conversation
def start(update: Update, context: CallbackContext) -> int:
    update.message.reply_text("Send 'test' to get 'aaa'.")
    return TEST

# Define a function to handle the 'test' message
def test(update: Update, context: CallbackContext) -> int:
    if update.message.text.lower() == 'test':
        update.message.reply_text("aaa")
    else:
        update.message.reply_text("Send 'test' to get 'aaa'.")
    return ConversationHandler.END

def main():
    # Replace 'YOUR_BOT_TOKEN' with your actual bot token
    updater = Updater(token='YOUR_BOT_TOKEN', use_context=True)
    dispatcher = updater.dispatcher

    # Create a conversation handler
    conv_handler = ConversationHandler(
        entry_points=[CommandHandler('start', start)],
        states={
            TEST: [MessageHandler(Filters.text & ~Filters.command, test)],
        },
        fallbacks=[],
    )

    # Add the conversation handler to the dispatcher
    dispatcher.add_handler(conv_handler)

    # Start the bot
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()