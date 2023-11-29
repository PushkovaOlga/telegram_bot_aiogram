from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor

try:
    with open("sp_gr.txt", "r", encoding="utf-8") as file:
        all_student = [line.rstrip("\n") for line in file]
        all_student = list(filter(None, all_student))
except FileNotFoundError:
    print(f"Запрашиваемый файл 'sp_gr.txt' не найден")

try:
    with open("zadaniya.txt", "r", encoding="utf-8") as file:
        zadaniya = [line.rstrip("\n") for line in file]
        zadaniya = list(filter(None, zadaniya))
except FileNotFoundError:
    print(f"Запрашиваемый файл 'zadaniya.txt' не найден")

bot = Bot(token="your token")
dp = Dispatcher(bot)

HELP_COMMAND = """
Этот бот даст каждому студенту даст задание для зачета :) 
Нажмите /start, чтобы начать работу.
/help - список команд 🫠
/start - начать работу с ботом ❤️
/rules - правила для всех ✨ 
"""


@dp.message_handler(commands=["help"])
async def help_command(message: types.Message):
    await message.reply(text=HELP_COMMAND)


@dp.message_handler(commands=["rules"])
async def rules_command(message: types.Message):
    await message.answer(
        text="Правила для всех: \nТелеграм-бот должен быть написан на aiogram и выложен на github в публичной директории \n"
             "В боте должны быть доступны команды: \n/start - начать работу с ботом \n/help - список команд \n"
             "Обязательны следующие пункты: использование кнопок, работа с файлами, обработка исключений. Удачи!")
    await message.delete()


@dp.message_handler(commands=["help"])
async def help_command(message: types.Message):
    await message.reply(text=HELP_COMMAND)


@dp.message_handler(commands=["start"])
async def start_command(message: types.Message):
    await message.answer(text="Введите свою фамилию, чтобы бот дал Вам задание.")


@dp.message_handler()
async def send_zadanie(message: types.Message):
    import random

    z = random.choice(zadaniya)
    found = False
    for name in all_student:
        if name.startswith(message.text):
            found = True
            break
    if found:
        await message.answer(text=z)
    else:
        await message.answer(text="Такого студента нет в списке. Введите фамилию с большой буквы")


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
