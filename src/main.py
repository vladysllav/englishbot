from telegram import Update, InlineKeyboardMarkup, InlineKeyboardButton
from telegram.ext import Application, CommandHandler, MessageHandler, filters, CallbackContext, CallbackQueryHandler
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()


class EnglishSkillsBot:
    def __init__(self):
        self.app = Application.builder().token(os.getenv("TELEGRAM_TOKEN")).build()
        self.callback_handler = CallbackQueryHandler(self.handle_callback)

    def create_start_button(self):
        """
        Create Start button
        :return: InlineKeyboardMarkup Start button
        """
        return InlineKeyboardMarkup([[InlineKeyboardButton("Start", callback_data="start")]])

    def create_lvl_button(self):
        """
        Create level changed buttons
        :return: InlineKeyboardMarkup buttons with lvl selection
        """
        buttons = [
            [InlineKeyboardButton("Beginner", callback_data="Beginner")],
            [InlineKeyboardButton("Intermediate", callback_data="Intermediate")],
            [InlineKeyboardButton("Advanced", callback_data="Advanced")]
        ]
        return InlineKeyboardMarkup(buttons)

    async def start(self, update: Update, context: CallbackContext):
        """
        Handles the /start command and sends a welcome message with the start button.
        :param update: The incoming update.
        :param context: The context object for handlers.
        """
        reply_answer = self.create_start_button()
        await context.bot.send_message(chat_id=update.effective_chat.id,
                                       text="Welcome to the English Skills Bot! How can I assist you?",
                                       reply_markup=reply_answer)

    async def handle_text(self, update: Update, context: CallbackContext):
        # Process the user's message here and check their English skills
        response = self.check_english_skills(update.message.text)
        await context.bot.send_message(chat_id=update.effective_chat.id, text=response)

    async def handle_callback(self, update: Update, context: CallbackContext):
        """
        Handle the callback query from buttons level
        :param update: The incoming update.
        :param context: The context object for handlers.
        """
        query = update.callback_query
        if query.data == "start":
            reply_answer = self.create_lvl_button()
            await query.message.reply_text("Please select your English level", reply_markup=reply_answer)
        else:
            await query.answer("You selected level: " + query.data)

    def check_english_skills(self, text):
        # Add your English skills checking logic here
        # You can use libraries like NLTK, spaCy, or any other NLP tools

        # Placeholder response for demonstration purposes
        return "Your English skills are impressive!"

    def start_bot(self):
        start_handler = CommandHandler('start', self.start)
        text_handler = MessageHandler(filters.TEXT & ~filters.COMMAND, self.handle_text)

        self.app.add_handler(start_handler)
        self.app.add_handler(text_handler)
        self.app.add_handler(self.callback_handler)

        self.app.run_polling()


bot = EnglishSkillsBot()
bot.start_bot()
