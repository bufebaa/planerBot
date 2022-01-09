from aiogram import types, Dispatcher

from bot.config import load_config
from bot.misc.default_commands import set_admin_commands
from bot.services.database.commands.user import is_not_in_db, add_user, start_add_user
from bot.keyboards.inline import menu, start_menu


async def command_start_handler(message: types.Message):
    config = load_config('.env')

    dp = Dispatcher.get_current()
    if message.from_user.id in config.bot.admin_ids:
        await set_admin_commands(dp)

    await message.answer(text=f'<b>Вас приветствует бот-планер!</b> ✨\n'
                         f'Что вы можете сделать с помощью этого бота:\n\n'
                         f'· создавать разнообразные списки дел\n\n'
                         f'· планировать свои задачи\n\n'
                         f'· получать напоминания о дедлайнах\n\n'
                         f'· добавлять задачи в гугл календарь\n\n'
                         f'· отслеживать свои успехи и получать статистику\n\n'
                         f'· получать заряд мотивации с помощью режима мотивационных цитат\n\n'
                         f'· вносить разнообразие в свои будни с помощью режима “мне скучно”\n\n')

    if is_not_in_db(message.from_user.id):
        await message.answer(text="Вы желаете синхронизировать задачи с вашим google календарём?",
                             reply_markup=start_menu)
    else:
        await message.answer("✨Главное меню✨: ", reply_markup=menu)


async def start_without_google_handler(callback: types.CallbackQuery):
    await callback.answer()
    start_add_user(callback.from_user.id)
    await callback.message.answer("✨Главное меню✨: ", reply_markup=menu)


def register_start_command(dp: Dispatcher):
    dp.register_message_handler(command_start_handler, commands=['start'], state='*')
    dp.register_callback_query_handler(start_without_google_handler, text='start_add_user')

