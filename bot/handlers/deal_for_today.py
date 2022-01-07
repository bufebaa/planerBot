from aiogram import types, Dispatcher
from bot.database.commands.task import get_today_deals


async def show_today_deals(callback: types.CallbackQuery):
    await callback.answer()
    await callback.message.answer("Дела на сегодня: ")
    for i in get_today_deals(callback.from_user.id):
        await callback.message.answer(str(i))


def register_show_today_tasks_handler(dp: Dispatcher):
    dp.register_callback_query_handler(show_today_deals, text="tasks_for_day")
