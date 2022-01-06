from aiogram.dispatcher.filters.state import StatesGroup, State


class TaskCreation(StatesGroup):
    list_id = int
    title = str
    get_description = State()


