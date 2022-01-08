from aiogram.dispatcher.filters.state import StatesGroup, State


class AddTask(StatesGroup):
    enterTask = State()
