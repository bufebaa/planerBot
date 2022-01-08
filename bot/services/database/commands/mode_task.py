import json
from random import randrange

from sqlalchemy.orm import sessionmaker

from bot.services.database.db import engine, ModeTask


def create_session():
    session = sessionmaker(bind=engine)
    return session()


def add_task(task):
    s = create_session()
    temp_task = ModeTask(task=task)
    s.add(temp_task)
    s.commit()


def is_in_db(task):
    s = create_session()
    return True if s.query(ModeTask).filter(ModeTask.task == task).first() else False


def all_tasks():
    s = create_session()
    tasks = {}
    for task in s.query(ModeTask).all():
        tasks[task.task] = str(task.task)
    return tasks


def random_task():
    s = create_session()
    num_of_tasks = s.query(ModeTask).count()
    return s.query(ModeTask).filter(ModeTask.task_id == randrange(1, num_of_tasks)).first().task


def load_example_data():
    file = open('bot/resources/example_data.json', encoding='utf-8')
    data = json.load(file)
    for task in data['tasks']:
        add_task(task)

