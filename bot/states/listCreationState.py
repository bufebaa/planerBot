from aiogram.dispatcher.filters.state import StatesGroup, State


class ListCreation(StatesGroup):
    name = State()

