from aiogram import types, Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from bot.keyboards.inline import menu
from bot.services.database.commands.user import is_not_in_db, find_user
from bot.states.AuthState import Authorization
from google_core.user import get_authorisation_url, fetch_token


async def authorize_handler(callback: types.CallbackQuery):
    await callback.answer()
    menu = create_url_menu(get_authorisation_url())
    await callback.message.answer('Пожалуйста, следуйте инструкциям по этому URL-адресу '
                                  'и скопируйте нам код, который показан на фотографии ниже, '
                                  'чтобы мы имели возможность добавлять задачи в ваш google календарь✨',
                                  reply_markup=menu)
    dp = Dispatcher.get_current()
    await dp.bot.send_photo(callback.from_user.id,
                            photo='AgACAgIAAxkBAAIKbWHZ-DpjL4msQ763XYuYkVRy03SNAAO7MRsd2NFKY7esTjz9UV4BAAMCAANzAAMjBA')
    await Authorization.enterCode.set()


def create_url_menu(url):
    url_menu = InlineKeyboardMarkup()
    button = InlineKeyboardButton('Перейти', url=url)
    url_menu.add(button)
    return url_menu


async def authorize_command_handler(message: types.Message):
    user_id = message.from_user.id
    if not is_not_in_db(user_id):
        if find_user(user_id).is_google_synchronized:
            await message.answer('Вы уже авторизованы✨')
            return
    menu = create_url_menu(get_authorisation_url())
    await message.answer('Пожалуйста, следуйте инструкциям по этому URL-адресу '
                         'и скопируйте нам код, который показан на фотографии ниже, '
                         'чтобы мы имели возможность добавлять задачи в ваш google календарь✨',
                         reply_markup=menu)
    dp = Dispatcher.get_current()
    await dp.bot.send_photo(message.from_user.id,
                            photo='AgACAgIAAxkBAAIKbWHZ-DpjL4msQ763XYuYkVRy03SNAAO7MRsd2NFKY7esTjz9UV4BAAMCAANzAAMjBA')
    await Authorization.enterCode.set()


async def fetch_code(message: types.Message, state: FSMContext):
    user = message.from_user.id
    code = message.text
    if fetch_token(user, code):
        await message.answer('Авторизация в гугл прошла успешно✨\n'
                             'Теперь все ваши задачи и списки будут добавляться в ваш календарь. '
                             'Чтобы отключить функцию, нажмите /logout', reply_markup=menu)
    else:
        await message.answer('К сожалению, что-то пошло не так. Чтобы попробовать снова, нажмите /authorization')
    await state.finish()


def register_authorize_handler(dp: Dispatcher):
    dp.register_callback_query_handler(authorize_handler, text="authorize")
    dp.register_message_handler(authorize_command_handler, commands="authorize", state='*')
    dp.register_message_handler(fetch_code, state=Authorization.enterCode)
