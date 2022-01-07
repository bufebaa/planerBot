from aiogram import types, Dispatcher
from aiogram.dispatcher import FSMContext
from bot.database.commands.user import is_not_in_db, add_user
from bot.states import StartState
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
                         f'· вносить разнообразие в свои будни с помощью режима “мне скучно”\n\n')

    if is_not_in_db(message.from_user.id):
        await message.answer(text="Введите адрес вашей электронной почты для синхронизации с Google Calendar")
        is_not_in_db(message.from_user.id)
        await StartState.e_mail.set()
    else:
        await message.answer("✨Главное меню✨: ", reply_markup=menu)


async def get_email(message: types.Message, state: FSMContext):
    await add_user(message.from_user.id, message.text)
    await message.answer("Ваша почта записана!")
    await message.answer("✨Главное меню✨: ", reply_markup=menu)
    await state.finish()


def register_start_command(dp: Dispatcher):
    dp.register_message_handler(command_start_handler, commands=['start'])
    dp.register_message_handler(get_email, state=StartState.e_mail)

