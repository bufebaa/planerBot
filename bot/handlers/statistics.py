from aiogram import Dispatcher, types

from bot.services.database.commands.task import count_completed_tasks, count_all_tasks


async def command_statistics_handler(message: types.Message):

    await message.answer(text=f'✨Ваша статистика✨:')
    await message.answer(text=get_statistics(user_id=message.from_user.id))


def get_statistics(user_id):
    completed = count_completed_tasks(user_id)
    every = count_all_tasks(user_id)
    if not completed or not every:
        return f'За этот месяц не выполнено ни одной задачи! Старайтесь лучше :)\n'
    percent = completed / every * 100
    return f'За этот месяц выполнено: {completed} заданий\n' \
           f'Это {percent}% от общего количества ваших задач'


def register_statistics_command(dp: Dispatcher):
    dp.register_message_handler(command_statistics_handler, commands=['statistics'], state='*')
