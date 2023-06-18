from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

start_markup = ReplyKeyboardMarkup(
    resize_keyboard=True,
    one_time_keyboard=True,
    row_width=4
)

register = KeyboardButton("РЕГИСТРАЦИЯ")
quiz = KeyboardButton("/quiz")
info = KeyboardButton("/info")
start = KeyboardButton("/start")

start_markup.add(register,quiz,info,start)

cancel_markup = ReplyKeyboardMarkup(
    resize_keyboard=True,
    one_time_keyboard=True,
)
cancel = KeyboardButton("отмена")
cancel_markup.add(cancel)


gender_markup = ReplyKeyboardMarkup(
    resize_keyboard=True,
    one_time_keyboard=True,
).add(
    KeyboardButton("WOMEN"),
    KeyboardButton("MAN"),
    cancel
)

submit_markup = ReplyKeyboardMarkup(
    resize_keyboard=True,
    one_time_keyboard=True,
).add(
    KeyboardButton("ДА"),
    KeyboardButton("НЕТ"),
    cancel
)


