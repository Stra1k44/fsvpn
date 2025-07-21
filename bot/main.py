import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
import os
from dotenv import load_dotenv

# Загружаем переменные окружения
load_dotenv()
TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")

# Инициализируем бота и диспетчер
bot = Bot(token=TELEGRAM_TOKEN)
dp = Dispatcher()

@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    # Ответ пользователю на команду /start
    await message.answer("Привет! Это VPN-бот. Введите ваш номер телефона.")

async def main():
    # Запуск диспетчера в режиме поллинга
    await dp.start_polling(bot)

# Запускаем цикл
if __name__ == "__main__":
    try:
        asyncio.run(main())
    except (KeyboardInterrupt, SystemExit):
        print("Бот завершён")
