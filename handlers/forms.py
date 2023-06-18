
from sqlite3 import IntegrityError
from aiogram import types, Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher.filters.state import State, StatesGroup
from . import keyboards
from database.bot_db import sql_command_insert


class FSMAdmin(StatesGroup):
    name = State()
    age = State()
    gender = State()
    region = State()
    photo = State()
    submit = State()

async def fsm_start(message: types.Message):
    if message.chat.type == 'private':
        await FSMAdmin.name.set()
        await message.answer("Ваша имя?", reply_markup=keyboards.cancel_markup)
    else:
        await message.answer("Пиши в личке")

async def load_name(message: types.Message, state:FSMContext):
    async with state.proxy() as data:
        data ['id'] = message.from_user.id
        data ['username'] = f"@{message.from_user.username}" if message.from_user.username else None
        data['name'] = message.text
    await FSMAdmin.next()
    await message.answer("Ваш возраст?")


async def load_age(message: types.Message, state:FSMContext):
    if not message.text.isdigit():
      await message.answer("Введите число!!!",reply_markup=keyboards.cancel_markup)
    elif not 15 < int(message.text) < 60:
        await message.answer("доступ воспрещен! Возраст должен c 15 до 60")
    else:
      async with state.proxy() as data:
          data['age'] = message.text
      await FSMAdmin.next()
      await message.answer("Ваш пол?", reply_markup=keyboards.gender_markup)


async def load_gender(message: types.Message, state:FSMContext):
    async with state.proxy() as data:
        data['gender'] = message.text
    await FSMAdmin.next()
    await message.answer("место проживание", reply_markup=keyboards.cancel_markup)


async def load_region(message: types.Message, state:FSMContext):
    async with state.proxy() as data:
        data['region'] = message.text
    await FSMAdmin.next()
    await message.answer("Ваша фото")


async def load_photo(message: types.Message, state:FSMContext):
    async with state.proxy() as data:
        data['photo'] = message.photo[0].file_id
        await message.answer_photo(
            data['photo'],
            caption=f"{data['name']} {data['age']} {data['gender']} {data['region']}\n{data['username']}"
          )
    await FSMAdmin.next()
    await message.answer("Все верно?", reply_markup=keyboards.submit_markup)


async def submit(message: types.Message, state:FSMContext):
    if message.text.lower() == 'да':
      try:
        await sql_command_insert(state)
        await message.answer("все ваши данные сохранены ")
      except IntegrityError:
          await message.answer("У тебя уже есть аккаунт")
      await state.finish()
      
    elif message.text.lower() == 'нет':
        await FSMAdmin.name.set()
        await message.answer("Ваша имя?")
    else:
        await message.answer("не понял!")

async def cansel_form(message: types.Message, state: FSMContext):
  current_state = await state.get_state()
  if current_state:
      await state.finish()
      await message.answer("Вы вышли из регистрации")



def register_handlers_forms(dp:Dispatcher):
    dp.register_message_handler(cansel_form, state='*', commands=['cancel'])
    dp.register_message_handler(cansel_form,Text(equals='отмена', ignore_case=True),state='*')
    dp.register_message_handler(fsm_start, Text(equals='регистрация', ignore_case=True))
    dp.register_message_handler(load_name, state=FSMAdmin.name)
    dp.register_message_handler(load_age, state=FSMAdmin.age)
    dp.register_message_handler(load_gender, state=FSMAdmin.gender)
    dp.register_message_handler(load_region, state=FSMAdmin.region)
    dp.register_message_handler(load_photo, state=FSMAdmin.photo,
                                content_types=['photo'])
    dp.register_message_handler(submit, state=FSMAdmin.submit)
