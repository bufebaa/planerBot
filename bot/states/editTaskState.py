from aiogram.dispatcher.filters.state import StatesGroup, State


class EditTask(StatesGroup):
    id_task = int
    choice1 = State()
    choice2 = State()
    titleEditing = State()
    discEditing = State()

