from aiogram.dispatcher.filters.state import StatesGroup, State


class Authorization(StatesGroup):
    enterCode = State()
