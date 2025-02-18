from aiogram import Bot, Dispatcher, types
from aiogram.types import Message
from aiogram.filters import Command
from hints import sendPhotoHint
from pars_details import check_product_api_items_avd as get_avd 
from pars_details import check_product_api_autopiter as get_autopiter
from time import sleep
import os
from dotenv import load_dotenv

load_dotenv()
# Читаем токен
TOKEN = os.getenv("BOT_TOKEN")

# Создаем бота и диспетчер
bot = Bot(token=TOKEN)
dp = Dispatcher()

# Регистрация обработчиков
@dp.message(Command("start"))
async def process_start_command(message: Message):
    await message.answer("Привет!\nЗагрузите сюда текстовый документ с арктикулами в строку, либо же напишите сюда 1 арктикул, пример фото ниже")
    await sendPhotoHint(message)
    
@dp.message(Command("help"))
async def process_help_command(message: Message):
    await message.answer("Я жду...")

# Вызов проверки наличия арктикула 
@dp.message()
async def echo_message(message: Message):
    if (message.document and message.document.mime_type == 'text/plain'):
        pass
    else:
        try:
            avd: str = get_avd(message.text)
            await message.answer("Доступные товары\n" + avd)
        except: await message.answer("Что-то пошло не так на сайте https://www.avdmotors.ru")
        sleep(1)
        try:
            autopiter = get_autopiter(message.text)
            await message.answer("Доступные товары\n" + autopiter)
        except: await message.answer("Что-то пошло не так на сайте https://autopiter.ru")

# Запуск бота
async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    import asyncio
    asyncio.run(main())
