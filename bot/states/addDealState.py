from aiogram.dispatcher.filters.state import StatesGroup, State


class AddDeal(StatesGroup):
    chooseList =State()
    get_title = State()
    get_disc = State()