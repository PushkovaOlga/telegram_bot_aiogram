from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor

bot = Bot(token="Your token")
dp = Dispatcher(bot)


@dp.message_handler(commands=["start"])
async def process_start_command(message: types.Message):
    kb = [[types.KeyboardButton(text="Рандомное число")],
          [types.KeyboardButton(text="Что-то")]]
    keyboard = types.ReplyKeyboardMarkup(keyboard=kb)
    await message.reply("Привет, я бот в тг", reply_markup=keyboard)


@dp.message_handler(lambda message: message.text == "Рандомное число")
async def process_button_click(message: types.Message):
    import random

    a = random.randint(1, 100)
    await bot.send_message(message.from_user.id, str(a))


@dp.message_handler()
async def echo_message(message: types.Message):
    await bot.send_message(message.from_user.id, message.text)


if __name__ == "__main__":
    executor.start_polling(dp)
