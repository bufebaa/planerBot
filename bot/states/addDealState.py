from aiogram.dispatcher.filters.state import StatesGroup, State


class AddDeal(StatesGroup):
    list_id = int
    title = str
    chooseList =State()
    get_title = State()
    get_disc = State()