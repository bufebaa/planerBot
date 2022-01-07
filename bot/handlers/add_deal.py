from aiogram import types, Dispatcher
from aiogram.dispatcher import FSMContext
from bot.database.commands.list import is_no_lists_in_db
from bot.keyboards import inline
from bot.keyboards.calendar import DialogCalendar
from bot.states import AddDeal, TaskCreation
from bot.keyboards.inline import menu


async def add_deal(callback: types.CallbackQuery):
    await callback.answer()
    if not is_no_lists_in_db(callback.from_user.id):
        await callback.message.answer("Выберите список в который вы хотите добавить задачу: ",
                                      reply_markup=inline.create_list_of_lists(callback.from_user.id))
        await AddDeal.chooseList.set()
    else:
        await callback.message.answer("У вас нет текущих списков дел)\nСначала создайте его", reply_markup=menu)


async def choose_list(callback: types.CallbackQuery, state: FSMContext):
    await callback.answer()
    data = callback.data
    TaskCreation.list_id = data
    await callback.message.answer("Введите название задачи: ")
    await AddDeal.get_title.set()


async def get_task_title(message: types.Message, state: FSMContext):
    TaskCreation.title = message.text
    await message.answer("Введите описание задачи: ")
    await AddDeal.get_disc.set()


async def get_task_description(message: types.Message, state: FSMContext):
    TaskCreation.disc = message.text
    await message.answer("Введите дату задачи: ", reply_markup=await DialogCalendar().start_calendar())
    await state.finish()
    await TaskCreation.get_date.set()


def register_adding_task_handler(dp: Dispatcher):
    dp.register_callback_query_handler(add_deal, text="add_task")
    dp.register_callback_query_handler(choose_list, text=None, state=AddDeal.chooseList)
    dp.register_message_handler(get_task_title, state=AddDeal.get_title)
    dp.register_message_handler(get_task_description, state=AddDeal.get_disc)
