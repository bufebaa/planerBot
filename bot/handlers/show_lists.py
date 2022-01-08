from aiogram import types, Dispatcher
from bot.services.database.commands.list import is_no_lists_in_db
from bot.keyboards import inline
from bot.states import ListCreation
from bot.keyboards.inline import menu


async def show_lists(callback: types.CallbackQuery):
    await callback.answer()
    if not is_no_lists_in_db(callback.from_user.id):
        await callback.message.answer("Выберите список для работы с ним: ",
                                      reply_markup=inline.create_list_of_lists(callback.from_user.id))
        await ListCreation.showlists.set()
    else:
        await callback.message.answer("У вас нет текущих списков дел! Сначала создайте его :)", reply_markup=menu)


def register_show_list_handler(dp: Dispatcher):
    dp.register_callback_query_handler(show_lists, text="lists")
