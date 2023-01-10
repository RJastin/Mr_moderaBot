from aiogram import Bot, Dispatcher
from aiogram.types import Message
import asyncio
token = "5891161770:AAECuOQNCO94nuO9vIDm0yaY9RTJNgMWhLk"


async def get_start(message: Message, bot: Bot):
    await bot.send_message(message.from_user.id, f'Привіт {message.from_user.first_name}.Радий тебе бачити!')
    await message.answer(f'Привіт {message.from_user.first_name}.Радий тебе бачити!')
    await message.reply(f'Привіт {message.from_user.first_name}.Радий тебе бачити!')


async def start():
    bot = Bot(token=token)

    dp = Dispatcher()
    dp.message.register(get_start)
    try:
        await dp.start_polling(bot)
    finally:
        await bot.session.close()

if __name__ == "__main__":
    asyncio.run(start())




