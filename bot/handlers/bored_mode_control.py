from aiogram import Dispatcher, types
from aiogram.dispatcher import FSMContext

from bot.services.database.commands.mode_task import all_tasks, is_in_db, add_task
from bot.states.AddModeTaskState import AddTask


async def command_add_task_handler(message: types.Message):
    await AddTask.enterTask.set()
    await message.answer(text=f'Введите задание:')


async def get_task_handler(message: types.Message, state: FSMContext):
    task = message.text
    if is_in_db(task):
        await message.answer(f'Такое задание уже хранится в базе данных! Попробуй другое')
    else:
        add_task(task)
        await state.finish()
        await message.answer("Задача успешно добавлена✨")


async def command_tasks_handler(message: types.Message):
    await message.answer('✨Все интересные задачи✨:')
    for task in all_tasks():
        await message.answer(f'· <i>{str(task)}</i>')


def register_tasks_control(dp: Dispatcher):
    dp.register_message_handler(command_add_task_handler, commands=['add_task'], state='*')
    dp.register_message_handler(get_task_handler, state=AddTask.enterTask)
    dp.register_message_handler(command_tasks_handler, commands=['tasks'], state='*')
