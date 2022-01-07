from aiogram.dispatcher.filters.state import StatesGroup, State


class CompleteState(StatesGroup):
    choose = State()

