from aiogram import types, Dispatcher

from bot.config import load_config
from bot.misc.scheduler import motivational_mode_on, motivational_mode_off, test_motivational_mode
from bot.services.database.commands.user import find_user


async def motivational_mode_handler(callback: types.CallbackQuery):
    await callback.answer()
    user_id = callback.from_user.id
    dp = Dispatcher.get_current()
    if find_user(user_id).is_mode_on:
        await motivational_mode_off(user_id)
        msg = "Режим успешно отключен✨"
    else:
        motivational_mode_on(dp, user_id)
        msg = "Режим успешно включен✨\n" \
              "Цитаты будут отправлятся вам каждое утро. Надеемся, что это сделает вас более мотивированными!"
    await callback.message.answer(msg)

    config = load_config('.env')
    if user_id in config.bot.admin_ids:
        await callback.message.answer("ADMIN MODE")
        await dp.bot.send_sticker(user_id,
                                  sticker='CAACAgQAAxkBAAEDo5th2YZz3cMxS2mnjSmrOXlpWUOb8wACQgAD_-YCK9FHu7tfk9PUIwQ')
        test_motivational_mode(dp, user_id)


def register_motivational_mode_handler(dp: Dispatcher):
    dp.register_callback_query_handler(motivational_mode_handler, text="motivational_mode")
