import asyncio
import logging
import os
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from dotenv import load_dotenv

# Загружаем переменные из .env
load_dotenv()


TOKEN = os.getenv("BOT_TOKEN")
assert TOKEN, "Токен не найден в .env!"

# Настраиваем логирование
logging.basicConfig(level=logging.INFO)

# Создаем бота и диспетчер
bot = Bot(token=TOKEN)
dp = Dispatcher()

# Обработчик команды /start
@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    await message.answer("Привет! Я твой Todo бот. Пока я учусь.")

# Главная функция запуска
async def main():
    print("Бот запущен...")
    await dp.start_polling(bot)

# Запуск
if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("Бот выключен")