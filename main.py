# Це бот адмін для  адміністрування чату в telegram
import config
import logging
import asyncio
import time
from filters import IsAdminFilter
from aiogram import Bot, Dispatcher, executor, types

# Задаємо рівень логування
logging.basicConfig(level=logging.INFO)

# ініціалізуємо бота
bot = Bot(token=config.token)
dp = Dispatcher(bot)

MSG = "Чи ти програмував сьогодні,{}?"
b_list = ['бля', 'гандон', 'гніда', 'говно', 'дроч', 'еба', 'ёба', 'ёбн', 'ёбы', 'ёпт', 'жопа', 'залупа', 'конч', 'лох', 'мразь', 'мудак', 'мудак', 'педик', 'пидор', 'підр', 'пизд', 'поскуд', 'сать', 'сосать', 'сука', 'вебан', 'хер', 'хуё', 'хует', 'хуит', 'хуй', 'хуя', 'шалава', 'шлюха']
# with open("b_list.txt") as my_file:
#     b_list = my_file.read().split(',')
#     print(b_list)

@dp.message_handler(commands=["start"])
async def start_hendler(message: types.Message):
    user_id = message.from_user.id
    user_name = message.from_user.first_name
    user_full_name = message.from_user.full_name
    # logging.info(f'{time.asctime()} {user_id} {user_full_name} {message.text}')
    if "Привіт" in message.text:
        await message.reply(f"Привіт, {user_full_name}!")

    for i in range(7):
        await asyncio.sleep(60*60*24)
        await bot.send_message(user_id, MSG.format(user_name))


# @dp.message_handler()
# async def echo(message: types.Message):
#     await message.answer(message.text)

dp.filters_factory.bind(IsAdminFilter)


@dp.message_handler(is_admin=True, commands=["бан"], commands_prefix="!/")
async def cmd_ban(message: types.Message):
    if not message.reply_to_message:
        await message.reply("це має бути відповідь на повідомлення")
        return
    await bot.kick_chat_member(chat_id=message.chat.id, user_id=message.reply_to_message.from_user.id)
    await message.delete()
    await message.reply_to_message.reply("користувача покарано за мат!")


@dp.message_handler(content_types=["new_chat_members"])
async def on_user_joined(message: types.Message):
    await message.delete()


@dp.message_handler()
async def filter_messages(message: types.Message):
    user_id = message.from_user.id
    user_full_name = message.from_user.full_name
    for word in b_list:
        if word in message.text.lower():
            logging.info(f'{time.asctime()} {user_id} {user_full_name} {message.text}')
            await message.delete()



if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
