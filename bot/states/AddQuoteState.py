from aiogram.dispatcher.filters.state import StatesGroup, State


class AddQuote(StatesGroup):
    enterQuote = State()
