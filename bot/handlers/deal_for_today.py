from aiogram import types, Dispatcher
from bot.data import for_user_registration


async def show_today_deals(callback : types.CallbackQuery):
    await callback.message.answer("Дела на сегодня: ")
    for i in for_user_registration.show_today_deals():
        await callback.message.answer(str(i))


def register_show_today_tasks_handler(dp: Dispatcher):
    dp.register_callback_query_handler(show_today_deals, text="tasks_for_day")
