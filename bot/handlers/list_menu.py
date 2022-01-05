import re

from aiogram import types, Dispatcher
from aiogram.dispatcher import FSMContext
from bot.data import for_user_registration
from bot.states import ListCreation
from bot.keyboards import inline

async def open_list_menu(callback : types.CallbackQuery):
    get = callback.data
    await callback.message.answer(get)

def register_open_list_menu(dp: Dispatcher):
    dp.register_callback_query_handler(open_list_menu, text = None)