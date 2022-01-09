from aiogram import types, Dispatcher

from bot.keyboards.inline import bored_mode_menu
from bot.services.database.commands.mode_task import random_task


async def bored_mode_handler(callback: types.CallbackQuery):
    await callback.answer()
    await callback.message.answer('Попробуй выполнить это задание!')
    await send_task(callback)


async def another_task_handler(callback: types.CallbackQuery):
    await callback.answer()
    await send_task(callback)


async def send_task(callback: types.CallbackQuery):
    await callback.message.answer('✨Задание✨:')
    await callback.message.answer(f'· <i>{str(random_task())}</i>', reply_markup=bored_mode_menu)


def register_bored_mode_handler(dp: Dispatcher):
    dp.register_callback_query_handler(bored_mode_handler, text="bored_mode")
    dp.register_callback_query_handler(another_task_handler, text="another_task")
