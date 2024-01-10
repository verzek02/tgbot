from datetime import datetime, timedelta
from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove
from apscheduler.schedulers.asyncio import AsyncIOScheduler

from config import TOKEN_API
from variables import *

scheduler = AsyncIOScheduler()
bot = Bot(TOKEN_API)
dp = Dispatcher(bot)
button_help = KeyboardButton('/help')
button2 = KeyboardButton('image')

kb = ReplyKeyboardMarkup(resize_keyboard=True)
kb.add(button_help).add(button2)


async def on_startup(_):
    print('Бот был успешно запущен!')


@dp.message_handler(commands=['start'])
async def start_command(message: types.Message):
    await message.answer('hi, welcome', reply_markup=kb)
    await message.delete()


@dp.message_handler(commands=['help'])
async def help_command(message: types.Message):
    await bot.send_message(chat_id=message.chat.id, text=HELP_COMMAND, parse_mode='HTML',
                           reply_markup=ReplyKeyboardRemove())
    await message.delete()


@dp.message_handler(commands=['description'])
async def description_command(message: types.Message):
    await message.reply(text=DESCRIPTION_BOT)
    await message.delete()


@dp.message_handler(commands=['give'])
async def give_command(message: types.Message):
    await message.answer('Рассенган')
    await bot.send_sticker(chat_id=message.chat.id,
                           sticker='CAACAgIAAxkBAAEKuVVlTewloGAtgwcn1hrd5aC59x8tuwACjAADPeGrFy4ugf0qp4vQMwQ')
    await message.delete()


@dp.message_handler(commands=['count'])
async def check_count(message: types.Message):
    global count
    await message.answer(f'COUNT: {count}')
    count += 1
    await message.delete()


@dp.message_handler(content_types=['sticker'])
async def send_sticker_id(message: types.Message):
    await message.answer(message.sticker.file_id)
    await message.delete()


async def send_image_wrapper():
    message = types.Message(chat=types.Chat(id=1173847253))  # Замените <your_chat_id> на фактический идентификатор вашего чата
    await send_image(message)


@dp.message_handler(commands=['image'])
async def send_image(message: types.Message):
    await bot.send_photo(chat_id=message.chat.id,
                         photo='https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fwwwoldi.ru%2F800%2F600%2Fhttps%2Fpbs.twimg.com%2Fmedia%2FCzpLRDAXAAANr9H.jpg&f=1&nofb=1&ipt=c82260aa57cc8f616d0e1880e0695533eb32efb0a75919d82cf1045b89d4d979&ipo=images',
                         reply_markup=ReplyKeyboardRemove())
    await message.delete()


@dp.message_handler(commands=['location'])
async def send_location(message: types.Message):
    await bot.send_location(chat_id=message.chat.id, latitude=55, longitude=74)
    await message.delete()


scheduler.add_job(send_image_wrapper, trigger='date', run_date=datetime.now() + timedelta(seconds=10))
scheduler.start()

if __name__ == '__main__':
    executor.start_polling(dp, on_startup=on_startup, skip_updates=True)

"""
Эта функция проверяет считает количество галочек в сообщении пользователя
"""
# @dp.message_handler()
# async def check_in_emoji(message: types.Message):
#     await message.answer(text=str(message.text.count('✅')))

"""Эта функция проверяет сообщение на наличие цифры 0"""
# @dp.message_handler()
# async def check_in_numbers(message: types.Message):
#     if '0' in message.text:
#         await message.answer('Yes')
#     else:
#         await message.answer('No')


"""Эта функция отпрвляет в ответ красной сердечке черный"""
# @dp.message_handler()
# async def emogi_send(message: types.Message):
#     if message.text == '❤️':
#         await message.reply('🖤')

# await message.reply(message.text + '😘')


"""Если сообщение пользователя содержит слово Привет то он поздоровается"""
# @dp.message_handler()
# async def start_command(message: types.Message):
#     if message.text == 'Привет':
#         await message.answer('hi chelovek')
#         await message.delete()


"""Отправляет на сообщение пользователя рандомные буквы из латинского алфавита"""
# @dp.message_handler()
# async def send_random_letter(message: types.Message):
#     await message.reply(random.choice(string.ascii_letters))
