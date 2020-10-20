from aiogram import types
from loader import dp

from utils.dump import GetVK


@dp.message_handler(commands=["get"])
async def take_me_photo(message: types.Message):
    text = [
        'Список команд: ',
        '/photo X - Получить фотографии, X количество'
    ]
    await message.answer('\n'.join(text))


@dp.message_handler(lambda message: message.text.startswith('/photo'))
async def del_expense(message: types.Message):
    numb = message.text[7:]

    if numb.isdigit():
        await message.reply(f"Posting {numb} photos")

        posts = GetVK('kerokerokerokerokero', int(numb))
        photos = posts.get_photos()

        for photo in photos:
            await message.answer_photo(photo)
    else:
        await message.reply('Не корректно, пример:\n/photo 34')
