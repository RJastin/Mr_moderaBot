from aiogram.types import Message
from aiogram import Bot
import logging
import time


async def get_mat(message: Message, bot: Bot):
    user_id = message.from_user.id
    user_full_name = message.from_user.full_name
    logging.info(f'{time.asctime()} {user_id} {user_full_name} {message.text}')
    await message.delete()
