from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart

from loader import dp


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    # await message.answer(f'Привет, {message.from_user.full_name}!')
    await message.answer_photo('https://sun9-47.userapi.com/impf/LM2J22G2tGJMaoL267yHoebYvW_opYzhd35uPA/THlKdVFu9zs.jpg?size=2352x1672&quality=90&proxy=1&sign=de2a047201d88f1fb45430509f099cee',
                               caption=f'Привет, {message.from_user.full_name}!\nМожешь сразу просить /help')
