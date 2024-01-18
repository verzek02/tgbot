import random

from aiogram import Bot


def random_schedule():
    with open('expression.txt', 'r') as file:
        line = file.readlines()
        random_line = random.choice(line)
    return random_line


async def send_message(bot: Bot):
    await bot.send_message(chat_id=1173847253, text=random_schedule())


def random_morning():
    with open('morning.txt', 'r') as file:
        line = file.readlines()
        r_line = random.choice(line)
    return r_line


async def send_message_morning(bot: Bot):
    await bot.send_message(chat_id=1173847253, text=random_morning())
