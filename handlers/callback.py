
from config import dp, bot
from aiogram import types, Dispatcher





async def quiz_1(call: types.CallbackQuery):
  question = "Какое право гарантирует свободу выражения мнения?"
  answers = [
    'Право на труд',
    'Право на образование',
    'Право на свободу слова'
    'Право на здравоохранение'
  ]
  await bot.send_poll(
    chat_id=call.from_user.id,
    question=question,
    options=answers,
    is_anonymous=False,
    type='quiz',
    correct_option_id=2,
  )

def register_handlers_callback(dp:Dispatcher):
  dp.register_callback_query_handler(quiz_1, text="button_1")
