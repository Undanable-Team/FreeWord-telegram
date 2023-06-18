from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from .keyboards import start_markup
import requests
from config import  bot
from aiogram import types, Dispatcher
from persel.shyni import parser



async def start_polling(message: types.Message):
  await message.answer(f'Здраствуйте {message.from_user.full_name}',reply_markup=start_markup)


async def get_wheels(message: types.Message):
    wheels = parser()
    for i in wheels:
        await message.answer(
            f"{i['link']}\n\n"
            f"{i['title']}\n\n"
            f"{i['price']}\n\n"
            f"{i['size']}\n\n"
        )


async def mem_command_handler(message: types.Message):
    response = requests.get("https://picsum.photos/200/300")
    if response.status_code == 200:
        image_url = response.url

        await bot.send_photo(message.chat.id, image_url)
    else:
        await message.answer("Произошла ошибка при получении изображения.")




async def quiz(message: types.Message):
  markup = InlineKeyboardMarkup()
  button_1 = InlineKeyboardButton('Next', callback_data='button_1')
  markup.add(button_1)

  question = "Какое из перечисленных прав является основным правом каждого человека?"
  answers = [
    'Право на образование',
    'Право на жилье',
    'Право на жизнь',
    'Право на труд'
  ]


  await bot.send_poll(
    chat_id=message.from_user.id,
    question=question,
    options=answers,
    is_anonymous=False,
    type='quiz',
    correct_option_id=2,
    reply_markup=markup
  )

def register_handlers_commands(dp: Dispatcher):
  dp.register_message_handler(start_polling, commands=['start'])
  dp.register_message_handler(quiz, commands=['quiz'])
  dp.register_message_handler(get_wheels, commands=["info"])