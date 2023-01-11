from aiogram import Bot, Dispatcher
from aiogram.types import Message, ContentType
from core.handlers.basic import get_start, get_photo, get_hello, on_user_joined, on_user_leave, cmd_ban
from core.filters.mat import IsMat
from core.handlers.getmat import get_mat
import asyncio
import logging
from core.settings import settings
from aiogram.filters import Command, CommandStart
from aiogram import F


async def start_bot(bot: Bot):
    await bot.send_message(settings.bots.admin_id, text='Бота запущено!')


async def stop_bot(bot: Bot):
    await bot.send_message(settings.bots.admin_id, text='Бота зупинено!')


async def start():
    logging.basicConfig(level=logging.INFO,
                        format="%(asctime)s - [%(levelname)s] -  %(name)s - (%(filename)s).%(funcName)s(%(lineno)d) - %(message)s"
                        )

    bot = Bot(token=settings.bots.bot_token, parse_mode='HTML')

    dp = Dispatcher()
    dp.startup.register(start_bot)
    dp.shutdown.register(stop_bot)
    dp.message.register(get_mat, IsMat())
    dp.message.register(get_photo, F.photo)
    dp.message.register(get_hello, F.text == 'Привіт')
    dp.message.register(on_user_joined, F.new_chat_members)
    dp.message.register(on_user_leave, F.left_chat_member)
    dp.message.register(get_start, Command(commands=['start', 'run']))
    dp.message.register(cmd_ban, Command(commands=['ban']))

    try:
        await dp.start_polling(bot)
    finally:
        await bot.session.close()

if __name__ == "__main__":
    asyncio.run(start())
