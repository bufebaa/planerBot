from aiogram import types, Dispatcher

from bot.keyboards.inline import menu


async def command_menu_handler(message: types.Message):
    await message.answer("✨Главное меню✨: ", reply_markup=menu)


async def menu_handler(callback: types.CallbackQuery):
    await callback.answer()
    await callback.message.answer("✨Главное меню✨: ", reply_markup=menu)


def register_menu_handler(dp: Dispatcher):
    dp.register_message_handler(command_menu_handler, commands='menu', state='*')
    dp.register_callback_query_handler(menu_handler, text='menu')
