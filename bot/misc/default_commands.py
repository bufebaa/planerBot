from aiogram import types


async def set_default_commands(dp):
    await dp.bot.set_my_commands(
        [
            types.BotCommand("start", "Запускает бот"),
            types.BotCommand("help", "Показывает основную информацию о боте")
            # types.BotCommand("menu", "Вызывает главное меню"),
            # types.BotCommand("calendar", "Вызывает меню настроек гугл календаря")
        ]
    )
