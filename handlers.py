import random
import string
import time

from apsched import send_message, send_message_morning
from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup
from apscheduler.schedulers.asyncio import AsyncIOScheduler

from config import TOKEN_API
from variables import PUZZLESS

bot = Bot(TOKEN_API)
dp = Dispatcher(bot)
button_help = KeyboardButton('/help')

kb = ReplyKeyboardMarkup(resize_keyboard=True)
keyboard = InlineKeyboardMarkup(resize_keyboard=True)

kb.add(button_help)


async def on_startup(_):
    print('Бот был успешно запущен!')


@dp.message_handler(commands=['start'])
async def start_command(message: types.Message):
    await message.answer('Здравствуйте, мадам!', reply_markup=kb)
    await message.delete()


@dp.message_handler(commands=['puzzles'])
async def puzzles(message: types.Message):
    keys = PUZZLESS.keys()
    randomkeys = random.choice(list(keys))
    values = PUZZLESS.get(randomkeys)
    await message.answer(randomkeys)
    await message.delete()
    time.sleep(10)
    await message.answer(values)


scheduler = AsyncIOScheduler(timezone='Asia/Bishkek')

scheduler.add_job(send_message, trigger='interval', hours=2,
                  kwargs={'bot': bot})
scheduler.add_job(send_message_morning, trigger='cron', hour=9, minute=0, second=0,
                  kwargs={'bot': bot})
scheduler.start()

if __name__ == '__main__':
    executor.start_polling(dp, on_startup=on_startup, skip_updates=True)
