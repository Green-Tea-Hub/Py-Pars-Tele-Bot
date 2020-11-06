from aiogram import types
from loader import dp


@dp.message_handler(commands=['about'])
async def process_about_command(message: types.Message):
    await message.answer_sticker('CAACAgIAAxkBAAIkm1-IqHilf3wJ0c6x8ljE02mYlPFXAAJ4AQACEBptIl-UcbYgoPzoGwQ')
    await message.answer('А ты догадался!\nМои контакты: тут, тут, немного тут, здесь оставлю, и сюда добавлю!\nНе, все не так просто ...')
