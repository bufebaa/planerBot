from aiogram import types, Dispatcher
from bot.keyboards import inline


async def show_lists(callback : types.CallbackQuery):
    await callback.message.answer("Все списки дел: ", reply_markup=inline.create_list_of_lists())



def register_show_list_handler(dp: Dispatcher):
    dp.register_callback_query_handler(show_lists, text="lists")
