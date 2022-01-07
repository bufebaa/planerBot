from aiogram.dispatcher.filters.state import StatesGroup, State


class DeleteTask(StatesGroup):
    chooseTastToDelete = State()