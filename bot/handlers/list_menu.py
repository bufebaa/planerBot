import re
from bot.states.listCreationState import ListCreation
from aiogram import types, Dispatcher
from aiogram.dispatcher import FSMContext
from bot.data import for_user_registration
from bot.states import ListCreation, TaskCreation
from bot.keyboards import inline
from bot.keyboards.inline import list_cb


async def open_list_menu(callback : types.CallbackQuery, state : FSMContext):
    data = callback.data
    await state.update_data(list_id = int(data))
    await callback.message.answer(data)
    await callback.message.answer("Меню списка: ", reply_markup=inline.listMenu)
    await ListCreation.next()
    TaskCreation.list_id = int(data)


async def action_with_menu(callback : types.CallbackQuery,callback_data: dict, state : FSMContext):
    action = None
    action = callback_data['action']

    if "add_deals" == action:
        await callback.message.answer("Введите название задачи: ")
        await ListCreation.get_name.set()

    elif "show_deals" == action:
        for i in for_user_registration.show_all_tasks(TaskCreation.list_id):
            await callback.message.answer(str(i))




#Work with states for task adding:
async def get_task_title (message: types.Message,state : FSMContext):
    TaskCreation.title = message.text
    await message.answer("Введите описание задачи: ")
    await state.finish()
    await TaskCreation.get_description.set()

async def get_task_discription (message: types.Message,state : FSMContext):
    for_user_registration.add_task(TaskCreation.list_id, TaskCreation.title, message.text)
    await message.answer("Задача успешно добавлена ", reply_markup=inline.listMenu)
    await state.finish()
    await ListCreation.actionwithmenu.set()


def register_open_list_menu(dp: Dispatcher):
    dp.register_callback_query_handler(open_list_menu, text = None, state=ListCreation.showlists)
    dp.register_callback_query_handler(action_with_menu, list_cb.filter(action = "add_deals"), state=ListCreation.actionwithmenu)
    dp.register_callback_query_handler(action_with_menu, list_cb.filter(action = "show_deals"), state=ListCreation.actionwithmenu)
    dp.register_message_handler(get_task_title, state=ListCreation.get_name)
    dp.register_message_handler(get_task_discription, state=TaskCreation.get_description)