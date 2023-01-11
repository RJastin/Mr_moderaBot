from aiogram.filters import BaseFilter
from aiogram.types import Message


class IsMat(BaseFilter):
    async def __call__(self, message: Message) -> bool:
        b_list = ['бля', 'гандон', 'гніда', 'говно', 'дроч', 'еба', 'ёба', 'ёбн', 'ёбы', 'ёпт', 'жопа', 'залупа',
                  'конч', 'лох', 'мразь', 'мудак', 'мудак', 'педик', 'пидор', 'підр', 'пизд', 'поскуд', 'сать',
                  'сосать', 'сука', 'вебан', 'хер', 'хуё', 'хует', 'хуит', 'хуй', 'хуя', 'шалава', 'шлюха', 'жопісти']
        try:
            for word in b_list:
                if word in message.text.lower():
                    return True
        except:
            return False
