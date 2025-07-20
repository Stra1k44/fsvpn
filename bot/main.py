import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from dotenv import load_dotenv
import os

# Загружаем переменные окружения из файла .env
load_dotenv()
TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")

# Инициализируем бота и диспетчер событий
bot = Bot(token=TELEGRAM_TOKEN)
dp = Dispatcher()

@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    """
    Обработчик команды /start.
    Приветствует пользователя и объясняет, как начать работу с VPN-ботом.
    """
    await message.answer(
        "Добро пожаловать в VPN-сервис!\n"
        "Для регистрации пришлите свой номер телефона."
    )

async def main():
    # Запуск бота в асинхронном режиме
    await dp.start_polling(bot)

if __name__ == "__main__":
    # Точка входа — запуск основного цикла асинхронно
    asyncio.run(main())
