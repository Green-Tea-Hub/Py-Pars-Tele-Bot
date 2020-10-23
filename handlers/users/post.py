from aiogram import types
from loader import dp

from utils.vk_api import PostVK


@dp.message_handler(commands=["post"])
async def take_me_photo(message: types.Message):
    text = [
        '/vkpost message',
    ]
    await message.answer('\n'.join(text))


@dp.message_handler(lambda message: message.text.startswith('/vkpost'))
async def get_photos(message: types.Message):
    text = message.text[8:]

    group = PostVK("199593124")
    post = group.postMedia(text)
    await message.answer(post)
