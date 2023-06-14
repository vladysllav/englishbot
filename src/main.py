from telegram import Update, InlineKeyboardMarkup, InlineKeyboardButton
from telegram.ext import Application, CommandHandler, MessageHandler, filters, CallbackContext, CallbackQueryHandler
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()


class EnglishSkillsBot:
    def __init__(self):
        self.app = Application.builder().token(os.getenv("TELEGRAM_TOKEN")).build()

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

    async def statistics(self, update: Update, context: CallbackContext):
        """
        Handles the /stat command and sends statistic info.
        """
        # {user_id: user_result}
        user_info_test = {324552: 50, 323552: 10, 322552: 50, 321552: 40, 327552: 60, 327542: 20, 324542: 30}

        users_worse_result = [userid for userid in user_info_test if user_info_test[userid] < user_info_test[324552]]
        await context.bot.send_message(chat_id=update.effective_chat.id,
                                       text=f"You have passed this test better than "
                                            f"{int(len(users_worse_result) / len(user_info_test) * 100)}"
                                            f"% of participants")

    async def handle_text(self, update: Update, context: CallbackContext):
        # Process the user's message here and check their English skills
        response = self.check_english_skills(update.message.text)
        await context.bot.send_message(chat_id=update.effective_chat.id, text=response)

    async def choose_level_callback(self, update: Update, context: CallbackContext):
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
        statistics_handler = CommandHandler('stat', self.statistics)
        text_handler = MessageHandler(filters.TEXT & ~filters.COMMAND, self.handle_text)
        callback_handler = CallbackQueryHandler(self.choose_level_callback)

        self.app.add_handler(start_handler)
        self.app.add_handler(text_handler)
        self.app.add_handler(callback_handler)
        self.app.add_handler(statistics_handler)

        self.app.run_polling()


bot = EnglishSkillsBot()
bot.start_bot()
