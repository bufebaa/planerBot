from aiogram.dispatcher.filters.state import StatesGroup, State


class TaskCreation(StatesGroup):
    list_id = int
    title = str
    disc = str
    date = None
    get_description = State()
    get_date = State()
    get_time = State()


