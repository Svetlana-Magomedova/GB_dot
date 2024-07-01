import logging
import asyncio
import random

from aiogram import Bot, Dispatcher, types, F
from aiogram.filters import Command
import config

API_TOKEN = config.token

# Создание кнопок
button_info = types.KeyboardButton(text='Информация')
button_greeting = types.KeyboardButton(text='Приветствие')
kb = [
    [button_info, button_greeting],
]
keyboard = types.ReplyKeyboardMarkup(keyboard=kb, resize_keyboard=True)

# Включаем логирование, чтобы видеть сообщения в консоли
logging.basicConfig(level=logging.INFO)

# Инициализация бота и диспетчера
bot = Bot(token=API_TOKEN)
dp = Dispatcher()

@dp.message(Command("start"))
async def command_start(message: types.Message):
    await message.answer("Привет! Я эхобот на aiogram 3. Отправь мне любое сообщение, и я повторю его.", reply_markup=keyboard)

@dp.message(Command("info"))
async def command_info(message: types.Message):
    number = random.randint(1, 7)
    await message.answer("Я тестовый бот")
    await message.answer(f"Твое число {number}")

@dp.message(Command("user"))
async def command_user(message: types.Message):
    await message.answer("Приветствую, пользователь.")

@dp.message(lambda message: message.text and message.text.lower() == "стоп!")
async def stop_command(message: types.Message):
    await message.reply("Стоп машина!!")

@dp.message(lambda message: message.text and message.text.lower() == "начать!")
async def start_command(message: types.Message):
    await message.reply("Поехали!")

@dp.message(lambda message: message.animation)
async def echo_gif(message: types.Message):
    await message.reply_animation(message.animation.file_id)

@dp.message(F.text == "Информация")
async def info_button(message: types.Message):
    number = random.randint(1, 7)
    await message.answer("Я тестовый бот")
    await message.answer(f"Твое число {number}")

@dp.message(F.text == "Приветствие")
async def greeting_button(message: types.Message):
    await message.answer("Приветствую, пользователь.")

@dp.message(F.text)
async def msg_echo(message: types.Message):
    print(message.text)
    name = message.chat.first_name
    if 'hello' in message.text.lower():
        await message.reply(f"И тебе привет, {name}")
    elif 'by' in message.text.lower():
        await message.reply(f"Пока, {name}")
    else:
        await message.answer(message.text)  # Это добавлено для повторения сообщений

async def main():
    await dp.start_polling(bot, skip_updates=True)

if __name__ == '__main__':
    asyncio.run(main())
