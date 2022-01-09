from aiogram import types, Dispatcher
from aiogram.dispatcher import FSMContext
from bot.services.database.commands.list import add_list
from bot.services.database.commands.user import find_user
from bot.states import ListCreation
from bot.keyboards import inline
from google_core.tasklist import create_list


async def create_deal_list(callback: types.CallbackQuery):
    await callback.answer()
    await callback.message.answer("Как вы хотите назвать этот список?")
    await ListCreation.name.set()


async def get_list_name(message: types.Message, state: FSMContext):
    user_id = message.from_user.id
    title = message.text
    await add_list(user_id, title)
    user = find_user(user_id)
    if user.is_google_synchronized:
        create_list(user_id, title)
    await message.answer("Список был успешно создан")
    await message.answer("Выберите список для работы с ним✨")
    await message.answer("Все списки дел: ", reply_markup=inline.create_list_of_lists(user_id))
    await ListCreation.next()


def register_list_handler(dp: Dispatcher):
    dp.register_callback_query_handler(create_deal_list, text="create_list")
    dp.register_message_handler(get_list_name, state=ListCreation.name)
