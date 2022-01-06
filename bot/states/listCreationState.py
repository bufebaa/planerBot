from aiogram.dispatcher.filters.state import StatesGroup, State


class ListCreation(StatesGroup):
    name = State()
    showlists = State()
    actionwithmenu = State()

    #get info about task: in order to get back need to state 'actionwithmenu'
    get_name = State()


