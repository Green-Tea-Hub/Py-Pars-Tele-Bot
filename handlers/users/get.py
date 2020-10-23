from aiogram import types
from loader import dp

from utils.vk_api import GetVK


@dp.message_handler(commands=["get"])
async def take_me_photo(message: types.Message):
    text = [
        'Просматривает посты групп по:',
        '/photo число id(ссылка)',
        '/text число id(ссылка)',
        # '/video число id(ссылка)'
        'Пример:',
        '/p 1501 https://vk.com/copypastme',
        'Просматривает посты, не в каждом из них может быть картинка или текст',
    ]
    await message.answer('\n'.join(text))


@dp.message_handler(lambda message: message.text.startswith('/photo'))
async def get_photos(message: types.Message):
    # numb = message.text[7:]
    stroke = message.text.split(' ')

    numb = stroke[1]
    vk_id = stroke[-1].split('/')[3]

    if numb.isdigit():
        await message.answer(f"Получение {numb} картинки из {vk_id}")
        posts = GetVK(vk_id, int(numb))
        photos = posts.get_photos()
        for photo in photos:
            await message.answer_photo(photo)
    else:
        await message.reply('Не корректно. /get')


@dp.message_handler(lambda message: message.text.startswith('/text'))
async def get_texts(message: types.Message):
    stroke = message.text.split(' ')

    numb = stroke[1]
    vk_group_id = stroke[-1].split('/')[3]

    if numb.isdigit():
        await message.answer(f"Получение {numb} текстов из {vk_group_id}")

        posts = GetVK(vk_group_id, int(numb))
        texts = posts.get_texts()

        for text in texts:
            await message.answer(text)
    else:
        await message.reply('Не корректно, пример:\n/photo 34')


@dp.message_handler(lambda message: message.text.startswith('/video'))
async def get_videos(message: types.Message):
    stroke = message.text.split(' ')
    numb = stroke[1]
    vk_group_id = stroke[-1].split('/')[3]

    if numb.isdigit():
        await message.answer(f"Получение {numb} видео из {vk_group_id}")

        posts = GetVK(vk_group_id, int(numb))
        videos = posts.get_videos()

        for video in videos:
            await message.answer(video)
    else:
        await message.reply('Не корректно, пример:\n/photo 34')
