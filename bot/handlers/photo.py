from aiogram import types, Dispatcher


async def get_photo(message: types.Message):
    await message.answer(message.photo[0].file_id)


def register_photo_handler(dp: Dispatcher):
    dp.register_message_handler(get_photo, content_types=['photo'])
