from aiogram import types, Dispatcher
from bot.keyboards import inline
from bot.states import ListCreation
from bot.data import for_user_registration
from bot.keyboards.inline import menu


async def show_lists(callback : types.CallbackQuery):
    if for_user_registration.is_lists_in_db() == False:
        await callback.message.answer("Выберите список для работы с ним: ")
        await callback.message.answer("Все списки дел: ", reply_markup=inline.create_list_of_lists())
        await ListCreation.showlists.set()
    else:
        await callback.message.answer("У вас нет текущих списков дел)\nСначала создайте его", reply_markup=menu)


def register_show_list_handler(dp: Dispatcher):
    dp.register_callback_query_handler(show_lists, text="lists")
