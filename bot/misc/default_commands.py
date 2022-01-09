from aiogram import types


async def set_default_commands(dp):
    await dp.bot.set_my_commands(
        [
            types.BotCommand("start", "Запустить бот"),
            types.BotCommand("help", "Вывести основную информацию о боте"),
            types.BotCommand("menu", "Открыть главное меню"),
            types.BotCommand("statistics", "Показать статистику выполненных заданий"),
            types.BotCommand("authorize", "Авторизоваться в google_core tasks"),
            types.BotCommand("logout", "Остановить синхронизацию с google_core tasks")
        ]
    )


async def set_admin_commands(dp):
    await dp.bot.set_my_commands(
        [
            types.BotCommand("start", "Запустить бот"),
            types.BotCommand("help", "Вывести основную информацию о боте"),
            types.BotCommand("menu", "Открыть главное меню"),
            types.BotCommand("statistics", "Показать статистику выполненных заданий"),
            types.BotCommand("authorize", "Авторизоваться в google_core tasks"),
            types.BotCommand("logout", "Остановить синхронизацию с google_core tasks"),
            types.BotCommand("add_quote", "Добавить цитаты"),
            types.BotCommand("quotes", "Показать все мотивационные цитаты"),
            types.BotCommand("add_task", "Добавить задание для режима 'мне скучно'"),
            types.BotCommand("tasks", "Показать все задания"),
        ]
    )