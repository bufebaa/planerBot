import asyncio
import logging
from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage

from bot.config import load_config
from bot.handlers.authorize import register_authorize_handler
from bot.handlers.bored_mode import register_bored_mode_handler
from bot.handlers.bored_mode_control import register_tasks_control
from bot.handlers.help import register_help_command
from bot.handlers.logout import register_logout_handler
from bot.handlers.motivational_mode import register_motivational_mode_handler
from bot.handlers.motivational_mode_control import register_quotes_control
from bot.handlers.photo import register_photo_handler
from bot.handlers.start import register_start_command
from bot.handlers.menu import register_menu_handler
from bot.handlers.create_list import register_list_handler
from bot.handlers.show_lists import register_show_list_handler
from bot.handlers.list_menu import register_open_list_menu
from bot.handlers.add_deal import register_adding_task_handler
from bot.handlers.statistics import register_statistics_command
from bot.misc.default_commands import set_default_commands
from bot.handlers.calendar import register_test_handler
from bot.handlers.deal_for_today import register_show_today_tasks_handler
from bot.handlers.get_time import register_get_time
from bot.misc.scheduler import start
from bot.services.database.commands import quote, mode_task
from flask_core.program import app

logger = logging.getLogger(__name__)


def register_all_handlers(dp):
    register_start_command(dp)
    register_help_command(dp)
    register_menu_handler(dp)
    register_statistics_command(dp)
    register_quotes_control(dp)
    register_tasks_control(dp)
    register_authorize_handler(dp)
    register_logout_handler(dp)
    register_list_handler(dp)
    register_show_list_handler(dp)
    register_open_list_menu(dp)
    register_adding_task_handler(dp)
    register_test_handler(dp)
    register_get_time(dp)
    register_show_today_tasks_handler(dp)
    register_motivational_mode_handler(dp)
    register_bored_mode_handler(dp)
    register_photo_handler(dp)


def load_example_data():
    quote.load_example_data()
    mode_task.load_example_data()


async def main():
    logging.basicConfig(
        level=logging.INFO,
        format=u'%(filename)s:%(lineno)d #%(levelname)-8s [%(asctime)s] - %(name)s - %(message)s',
    )
    logger.info("Starting bot")
    config = load_config(".env")

    storage = MemoryStorage()
    bot = Bot(token=config.bot.token, parse_mode='HTML')
    dp = Dispatcher(bot, storage=storage)

    bot['config'] = config

    register_all_handlers(dp)
    await set_default_commands(dp)
    load_example_data()

    try:
        start()
        await dp.start_polling()
    finally:
        await dp.storage.close()
        await dp.storage.wait_closed()
        await bot.session.close()


if __name__ == '__main__':
    try:
        asyncio.run(main())
    except (KeyboardInterrupt, SystemExit):
        logger.error("Bot stopped!")
