from aiogram import types, Dispatcher

from bot.services.database.commands.user import find_user, logout_user, is_not_in_db


async def logout_command_handler(message: types.Message):
    user_id = message.from_user.id
    if is_not_in_db(user_id) or not find_user(user_id).is_google_synchronized:
        await message.answer('Невозможно остановить синхронизацию, так как вы не авторизованы✨')
    else:
        logout_user(user_id)
        await message.answer('Синхронизация была успешно остановлена✨')


def register_logout_handler(dp: Dispatcher):
    dp.register_message_handler(logout_command_handler, commands="logout", state='*')
