from aiogram import types, Dispatcher

from bot.config import load_config
from bot.misc.scheduler import add_task_reminders, add_test_reminder
from bot.services.database.commands.task import add_task, get_last_task_id
from bot.keyboards import inline
from bot.states import TaskCreation, ListCreation
from aiogram.dispatcher import FSMContext
from datetime import time


async def get_time(message: types.Message, state: FSMContext):
    try:
        set_time: time = time.fromisoformat(message.text)
    except ValueError:
        return await message.answer("Введено некорректное время :(")
    add_task(message.from_user.id, TaskCreation.list_id, TaskCreation.title, TaskCreation.disc,
             TaskCreation.date, set_time)

    await message.answer("Задача успешно добавлена ✨", reply_markup=inline.listMenu)
    await state.finish()

    config = load_config('.env')
    dp = Dispatcher.get_current()
    task_id = get_last_task_id(message.from_user.id)
    if message.from_user.id in config.bot.admin_ids:
        await message.answer("ADMIN MODE")
        await dp.bot.send_sticker(message.from_user.id,
                                  sticker='CAACAgQAAxkBAAEDo5th2YZz3cMxS2mnjSmrOXlpWUOb8wACQgAD_-YCK9FHu7tfk9PUIwQ')
        add_test_reminder(dp, task_id)
    add_task_reminders(dp, task_id)

    await ListCreation.actionwithmenu.set()


def register_get_time(dp: Dispatcher):
    dp.register_message_handler(get_time, state=TaskCreation.get_time)

