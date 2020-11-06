from aiogram import types
from loader import dp


@dp.message_handler()
async def bot_echo(message: types.Message):
    # await message.answer(message.text)
    await message.answer_sticker('CAACAgIAAxkBAAIkX1-IhRHPL_m63dRhOutqKUDTiKoGAAJgAQACEBptIsq5BfpP9_oHGwQ')
    await message.answer('FUCK! I CAN\'T READ JAPANESE')
