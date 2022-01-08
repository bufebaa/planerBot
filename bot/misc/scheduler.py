from datetime import datetime, timedelta

from aiogram import Dispatcher
from apscheduler.schedulers.asyncio import AsyncIOScheduler

from bot.services.database.commands.quote import random_quote
from bot.services.database.commands.task import get_task

scheduler = AsyncIOScheduler()


def start():
    scheduler.start()


# TEST REMINDERS


async def send_task_reminder(dp: Dispatcher, task_id):
    task = get_task(task_id)
    user = task.user_id
    time_left = datetime.combine(task.completion_date, task.completion_time) - datetime.now()
    message = f'✨Напоминание✨\n' \
              f'Задача: "{task.title}"\n' \
              f'До дедлайна осталось: {time_format(time_left, "{hours} дней, {hours} часов и {minutes} минут")}\n' \
              f'Поторопитесь!'
    await dp.bot.send_message(user, message)


def time_format(delta, fmt):
    d = {"days": delta.days}
    d["hours"], rem = divmod(delta.seconds, 3600)
    d["minutes"], d["seconds"] = divmod(rem, 60)
    return fmt.format(**d)


def add_task_reminders(dp: Dispatcher, task_id):
    task = get_task(task_id)
    run_date = datetime.combine(task.completion_date, task.completion_time)
    day_before_date = run_date - timedelta(days=1)
    hour_before_date = run_date - timedelta(hours=1)
    minute_before_date = run_date - timedelta(minutes=1)
    scheduler.add_job(send_task_reminder, "date", run_date=day_before_date, args=(dp, task_id),
                      id='task'+str(task_id)+'day')
    scheduler.add_job(send_task_reminder, "date", run_date=hour_before_date, args=(dp, task_id),
                      id='task'+str(task_id)+'hour')
    scheduler.add_job(send_task_reminder, "date", run_date=minute_before_date, args=(dp, task_id),
                      id='task'+str(task_id)+'minute')


def add_test_reminder(dp: Dispatcher, task_id):
    seconds_after_date = datetime.now() + timedelta(seconds=15)
    scheduler.add_job(send_task_reminder, "date", run_date=seconds_after_date, args=(dp, task_id),
                      id=str(task_id)+'test_reminder')


def del_task_reminders(task_id):
    scheduler.remove_job(job_id='task'+str(task_id)+'day')
    scheduler.remove_job(job_id='task'+str(task_id)+'hour')
    scheduler.remove_job(job_id='task'+str(task_id)+'minute')


# MOTIVATIONAL MODE


async def send_motivational_quote(dp: Dispatcher, user_id):
    await dp.bot.send_message(user_id, '✨Мотивационная цитата✨:')
    await dp.bot.send_message(user_id, f'<i>"{str(random_quote())}"</i>')


def motivational_mode_on(dp: Dispatcher, user_id):
    scheduler.add_job(send_motivational_quote, "cron", hour=12, args=(dp, user_id),
                      id=str(user_id)+'mode')


def motivational_mode_off(user_id):
    scheduler.remove_job(job_id=str(user_id)+'mode')


def test_motivational_mode(dp: Dispatcher, user_id):
    seconds_after_date = datetime.now() + timedelta(seconds=15)
    scheduler.add_job(send_motivational_quote, "date", run_date=seconds_after_date, args=(dp, user_id),
                      id=str(user_id)+'test_mode')



