from aiogram import types, Dispatcher
from bot.keyboards import inline
from bot.states import ListCreation


async def show_lists(callback : types.CallbackQuery):
    await callback.message.answer("Выберите список для работы с ним: ")
    await callback.message.answer("Все списки дел: ", reply_markup=inline.create_list_of_lists())
    await ListCreation.showlists.set()



def register_show_list_handler(dp: Dispatcher):
    dp.register_callback_query_handler(show_lists, text="lists")
