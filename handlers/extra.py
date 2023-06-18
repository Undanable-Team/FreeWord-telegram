
from aiogram import types, Dispatcher



async def echo(message: types.Message):
  bad_words = ["сука","дурак","козел","долбаеб","петух","дибил","блять","жинди","pizza"]
  username = f"@{message.from_user.username}"\
    if message.from_user.username else message.from_user.full_name
  for word in bad_words:
    if word in message.text.lower().replace(' ', ''):
        await message.delete()
        await message.answer(
          f"Не матерись {username}, сам ты {word}!"
          )
     

      


def register_handlers_extra(dp: Dispatcher):
  dp.register_message_handler(echo)