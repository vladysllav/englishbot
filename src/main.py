from telegram import Update
from telegram.ext import CommandHandler, MessageHandler, filters, ContextTypes, Application
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Welcome to the English Skills Bot! How can I assist you?")


async def handle_text(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # Process the user's message here and check their English skills
    response = check_english_skills(update.message.text)
    await update.message.reply_text(response)


def check_english_skills(text):
    # Add your English skills checking logic here
    # You can use libraries like NLTK, spaCy, or any other NLP tools

    # Placeholder response for demonstration purposes
    return "Your English skills are impressive!"


if __name__ == '__main__':
    print("Starting bot...")
    app = Application.builder().token(os.getenv("TELEGRAM_TOKEN")).build()

    app.add_handler(CommandHandler('start', start))

    app.add_handler(MessageHandler(filters.TEXT, handle_text))

    print("Polling...")
    app.run_polling(poll_interval=3)
