from aiogram import types
from loader import dp

from utils.misc import rate_limit
from utils.db_api import SQLightM

db = SQLightM('data/users.db')


@rate_limit(5, 'sub')
@dp.message_handler(commands=['sub'])
async def subscribe(message: types.Message):
    if(not db.subscriber_exists(message.from_user.id)):
        db.add_subscriber(message.from_user.id)
        await message.answer('Спасибо что присоеденились! :B')
    else:
        db.update_subscription(message.from_user.id, True)
        await message.answer_sticker('CAACAgIAAxkBAAIjNF-HGLjQOj-5TfQLC7uQU83s5Pq-AAJWAQACEBptIuUbjC73kpD2GwQ')
        await message.answer('Спасибо что вернулись! :B')


@rate_limit(5, 'unsub')
@dp.message_handler(commands=['unsub'])
async def unsubscribe(message: types.Message):
    if(not db.subscriber_exists(message.from_user.id)):
        db.add_subscriber(message.from_user.id, False)
        await message.answer_sticker('CAACAgIAAxkBAAIjHV-HFEg-H2Ynrg8dJG6TFHsfaz2jAAKsAQACEBptInjWW-Ya5ObHGwQ')
        await message.answer('Вы не были подписаны :(')
    else:
        db.update_subscription(message.from_user.id, False)
        await message.answer_sticker('CAACAgIAAxkBAAIjMV-HFxMAAQoFeJPIUCw8HfGBTdj97AACXwEAAhAabSLLoLkqsC4-oxsE')
        await message.answer('Job\'s done!')
