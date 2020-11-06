from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandHelp

from loader import dp
from utils.misc import rate_limit


@rate_limit(5, 'help')
@dp.message_handler(CommandHelp())
async def bot_help(message: types.Message):
    await message.answer_sticker('CAACAgIAAxkBAAIjTV-HK8Pypz4IpAo9QvKAwUOE2umvAAKkAQACEBptIhi1Zrk_9x-NGwQ')
    text = [
        'Список команд: ',
        '/start - Начать диалог',
        '/help - Получить справку',
        '/get - Получить',
        '/about - Получить about',
        '/sub - Получить рассылочкy :B',
        '/unsub - He Получить рассылочкy :(',
        '/goquiz - Начать quiz',
    ]
    await message.answer('\n'.join(text))
