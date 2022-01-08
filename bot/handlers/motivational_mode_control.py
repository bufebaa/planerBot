from aiogram import Dispatcher, types
from aiogram.dispatcher import FSMContext

from bot.services.database.commands.quote import is_in_db, add_quote, all_quotes, random_quote
from bot.states.AddQuoteState import AddQuote


async def command_add_quote_handler(message: types.Message):
    await AddQuote.enterQuote.set()
    await message.answer(text=f'Введите цитату:')


async def get_quote_handler(message: types.Message, state: FSMContext):
    quote = message.text
    if is_in_db(quote):
        await message.answer(f'Такая цитата уже хранится в базе данных! Попробуй другую')
    else:
        add_quote(quote)
        await state.finish()
        await message.answer("Цитата успешно добавлена✨")


async def command_quotes_handler(message: types.Message):
    await message.answer('✨Все мотивационные цитаты✨:')
    for quote in all_quotes():
        await message.answer(f'<i>"{str(quote)}"</i>')


async def random_quote_handler(message: types.Message):
    await message.answer('✨Мотивационная цитата✨:')
    await message.answer(f'<i>"{str(random_quote())}"</i>')


def register_quotes_control(dp: Dispatcher):
    dp.register_message_handler(command_add_quote_handler, commands=['add_quote'], state='*')
    dp.register_message_handler(get_quote_handler, state=AddQuote.enterQuote)
    dp.register_message_handler(command_quotes_handler, commands=['quotes'], state='*')
    dp.register_message_handler(random_quote_handler, commands=['rand_quote'], state='*')
