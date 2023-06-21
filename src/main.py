import os

from telegram import Update, InlineKeyboardMarkup, InlineKeyboardButton
from telegram.ext import Application, CommandHandler, MessageHandler, filters, CallbackContext, CallbackQueryHandler
from dotenv import load_dotenv

from src.utils import fake_user_data
from src.user_statistics import UserService


# Load environment variables from .env file
load_dotenv()


class EnglishSkillsBot:
    def __init__(self):
        self.token = os.getenv("TELEGRAM_TOKEN")
        self.app = Application.builder().token(self.token).build()
        self.users_data = fake_user_data()
        self.user_service = UserService(self.users_data)

    def create_start_button(self):
        """
        Create Start button
        :return: InlineKeyboardMarkup Start button
        """
        buttons = [
            [InlineKeyboardButton("Start", callback_data="start")],
            [InlineKeyboardButton("Statistics", callback_data="statistics")]
        ]
        return InlineKeyboardMarkup(buttons)

    def create_lvl_button(self):
        """
        Create level changed buttons
        :return: InlineKeyboardMarkup buttons with lvl selection
        """
        buttons = [
            [InlineKeyboardButton("Beginner", callback_data="lvl_beginner")],
            [InlineKeyboardButton("Intermediate", callback_data="lvl_intermediate")],
            [InlineKeyboardButton("Advanced", callback_data="lvl_advanced")]
        ]
        return InlineKeyboardMarkup(buttons)

    def check_user_exist(self, user_id: int) -> bool:
        user = filter(lambda x: x.id == user_id, self.users_data)
        return bool(list(user))

    async def start(self, update: Update, context: CallbackContext):
        """
        Handles the /start command and sends a welcome message with the start button.
        :param update: The incoming update.
        :param context: The context object for handlers.
        """
        user_id = update.message.from_user.id
        reply_answer = None  # TODO: remove later
        if self.check_user_exist(user_id):
            pass  # TODO: Create buttons with options get stats and pass ex again
        else:
            pass   # TODO: Create buttons for test
        await context.bot.send_message(chat_id=update.effective_chat.id,
                                       text="Welcome to the English Skills Bot! How can I assist you?",  # TODO: customize message depending on result
                                       reply_markup=reply_answer)

    async def statistics(self, update: Update, context: CallbackContext):
        """
        Handles the /stat command and sends statistic info.
        """
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
        user_id = 327542
        query = update.callback_query
        if query.data == "start":
            reply_answer = self.create_lvl_button()
            await query.message.reply_text("Please select your English level", reply_markup=reply_answer)
        elif query.data == "statistics":
            if self.user_service.check_user_exist(user_id):
                await self.statistics(update, context)
            else:
                await context.bot.send_message(chat_id=update.effective_chat.id,
                                               text="You have to answer the questions first!")
        else:
            level = query.data
            await self.send_question(update, context, level)

    async def send_question(self, update: Update, context: CallbackContext, level: str):
        questions = self.get_questions(level)

        for question in questions:
            question_text = question['question']
            options = question['options']

            keyboard = [
                [InlineKeyboardButton(option, callback_data=option)] for option in options
            ]
            reply_markup = InlineKeyboardMarkup(keyboard)
            await context.bot.send_message(chat_id=update.effective_chat.id, text=question_text,
                                           reply_markup=reply_markup)

    def get_questions(self, level: str):
        if level == "Beginner":
            return [
                {
                    'question': 'Question 1 for beginners',
                    'options': ['A', 'B', 'C'],
                    'correct_answer': 'B'
                },
                {
                    'question': 'Question 2 for beginners',
                    'options': ['A', 'B', 'C'],
                    'correct_answer': 'A'
                },
            ]
        elif level == "Intermediate":
            return [
                {
                    'question': 'Question 1 for intermediate level',
                    'options': ['A', 'B', 'C'],
                    'correct_answer': 'B'
                },
                {
                    'question': 'Question 2 for intermediate level',
                    'options': ['A', 'B', 'C'],
                    'correct_answer': 'A'
                },
            ]
        elif level == "Advanced":
            return [
                {
                    'question': 'Question 1 for advanced level',
                    'options': ['A', 'B', 'C'],
                    'correct_answer': 'C'
                },
                {
                    'question': 'Question 2 for advanced level',
                    'options': ['A', 'B', 'C'],
                    'correct_answer': 'A'
                },
            ]
        else:
            return []

    def check_english_skills(self, text):
        # Add your English skills checking logic here
        # You can use libraries like NLTK, spaCy, or any other NLP tools

        # Placeholder response for demonstration purposes
        return "Your English skills are impressive!"

    def start_bot(self):
        start_handler = CommandHandler('start', self.start)
        text_handler = MessageHandler(filters.TEXT & ~filters.COMMAND, self.handle_text)
        other_callback = CallbackQueryHandler(self.other_callback, pattern='^advanced_q1*')
        callback_handler = CallbackQueryHandler(self.choose_level_callback, pattern='^lvl_*')

        self.app.add_handler(start_handler)
        self.app.add_handler(text_handler)
        self.app.add_handler(other_callback)
        self.app.add_handler(callback_handler)

        self.app.run_polling()


if __name__ == '__main__':
    bot = EnglishSkillsBot()
    bot.start_bot()
