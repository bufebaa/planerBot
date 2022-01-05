from aiogram import types, Dispatcher

from bot.keyboards.inline import menu


async def command_start_handler(message: types.Message):
    await message.answer(text=f'<b>Вас приветствует бот-планер!</b> ✨\n'
                         f'Что вы можете сделать с помощью этого бота:\n\n'
                         f'· создавать разнообразные списки дел\n\n'
                         f'· планировать свои задачи\n\n'
                         f'· получать напоминания о дедлайнах\n\n'
                         f'· добавлять задачи в гугл календарь\n\n'
                         f'· отслеживать свои успехи и получать статистику\n\n'
                         f'· получать заряд мотивации с помощью режима мотивационных цитат\n\n'
                         f'· получать поддержку с помощью режима “мне грустно”\n\n'
                         f'· вносить разнообразие в свои будни с помощью режима “мне скучно”\n\n', reply_markup=menu)


def register_start_command(dp: Dispatcher):
    dp.register_message_handler(command_start_handler, commands=['start'])
