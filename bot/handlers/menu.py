from aiogram import types, Dispatcher
import bot.keyboards.inline as nav


async def command_menu_handler(message: types.Message):
    await message.answer("Главное меню:", reply_markup=nav.menu)


def register_menu_handler(dp: Dispatcher):
    dp.register_message_handler(command_menu_handler, commands='menu')
