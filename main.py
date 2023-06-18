
from aiogram.utils import executor
import logging
from config import dp, bot
from handlers import commands, extra, callback, forms
from database.bot_db import sql_create

async def on_startup(dp):
  sql_create()



callback.register_handlers_callback(dp)
commands.register_handlers_commands(dp)
forms.register_handlers_forms(dp)
extra.register_handlers_extra(dp)










if __name__ == '__main__':
  
  logging.basicConfig(level=logging.INFO)
  from aiogram import executor
  executor.start_polling(dp, skip_updates=True, on_startup=on_startup)