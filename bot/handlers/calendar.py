from aiogram import Dispatcher
from aiogram.dispatcher import FSMContext
from bot.keyboards.calendar import DialogCalendar
from bot.states import TaskCreation
from aiogram.types import CallbackQuery
from aiogram_calendar import dialog_cal_callback, DialogCalendar


async def process_simple_calendar(callback_query: CallbackQuery, callback_data: dict, state: FSMContext):
    selected, date = await DialogCalendar().process_selection(callback_query, callback_data)
    if selected:
        await callback_query.message.answer(f'Вы выбрали {date.strftime("%d/%m/%Y")}')
        TaskCreation.date = date
        await callback_query.message.answer("Введите время (пример: <code>15:30</code>).")
        await TaskCreation.get_time.set()


def register_test_handler(dp: Dispatcher):
    # dp.register_callback_query_handler(command_date, text=None, state=TaskCreation.get_date)
    dp.register_callback_query_handler(process_simple_calendar, dialog_cal_callback.filter(),
                                       state=TaskCreation.get_date)
