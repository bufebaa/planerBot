from aiogram import types, Dispatcher
from aiogram.dispatcher import FSMContext
from bot.data import for_user_registration
from bot.keyboards import inline
from bot.states import AddDeal
from bot.keyboards.inline import menu



async def add_deal(callback : types.CallbackQuery):
    if for_user_registration.is_lists_in_db() == False:
        await callback.message.answer("Выберите список в который вы хотите добавить задачу: ",
                                  reply_markup=inline.create_list_of_lists())
        await AddDeal.chooseList.set()
    else:
        await callback.message.answer("У вас нет текущих списков дел)\nСначала создайте его", reply_markup=menu)


async def choose_list(callback : types.CallbackQuery, state : FSMContext):
    data = callback.data
    AddDeal.list_id = data
    await callback.message.answer("Введите название задачи: ")
    await AddDeal.get_title.set()


async def get_task_title (message: types.Message,state : FSMContext):
    AddDeal.title = message.text
    await message.answer("Введите описание задачи: ")
    await AddDeal.get_disc.set()


async def get_task_discription (message: types.Message,state : FSMContext):
    for_user_registration.add_task(AddDeal.list_id, AddDeal.title, message.text)
    await message.answer("Задача успешно добавлена ", reply_markup=inline.menu)
    await state.finish()


def register_adding_task_handler(dp: Dispatcher):
    dp.register_callback_query_handler(add_deal, text="add_task")
    dp.register_callback_query_handler(choose_list, text=None, state=AddDeal.chooseList)
    dp.register_message_handler(get_task_title, state=AddDeal.get_title)
    dp.register_message_handler(get_task_discription, state=AddDeal.get_disc)





