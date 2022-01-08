from aiogram import Dispatcher, types


async def command_help_handler(message: types.Message):
    msg = f'<i>С помощью данного бота вы сможете грамотно планировать свои дни.</i> '
    await message.answer(text=f'✨О боте✨:')
    await message.answer(msg)


def register_help_command(dp: Dispatcher):
    dp.register_message_handler(command_help_handler, commands=['help'], state='*')
