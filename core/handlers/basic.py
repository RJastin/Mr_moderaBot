from aiogram import Bot
from aiogram.types import Message
import logging
import time
import json


async def get_start(message: Message, bot: Bot):
    await bot.send_message(message.from_user.id, f'<b>Привіт {message.from_user.first_name}</b>')
    await message.answer(f'<s>Привіт {message.from_user.first_name}</s>')
    await message.reply(f'<tg-spoiler>Привіт {message.from_user.first_name}</tg-spoiler>')


async def get_photo(message: Message, bot: Bot):
    await message.answer(f'Ти відправив мені картинку, я збережу її собі.')
    file = await bot.get_file(message.photo[-1].file_id)
    await bot.download_file(file.file_path, 'photo.jpg')


async def get_hello(message: Message, bot: Bot):
    user_id = message.from_user.id
    user_name = message.from_user.first_name
    user_full_name = message.from_user.full_name
    await message.reply(f"Привіт, {user_full_name}!")
    logging.info(f'{time.asctime()} {user_id} {user_full_name} {message.text}')
    # json_str = json.dumps(message.dict(), default=str)
    # print(json_str)


async def on_user_joined(message: Message, bot: Bot):
    await message.delete()


async def on_user_leave(message: Message, bot: Bot):
    await message.delete()


async def cmd_ban(message: Message, bot: Bot):
    if not message.reply_to_message:
        await message.reply("це має бути відповідь на повідомлення")
        return
    await bot.kick_chat_member(chat_id=message.chat.id, user_id=message.reply_to_message.from_user.id)
    await message.delete()
    await message.reply_to_message.reply("користувача покарано за мат!")
