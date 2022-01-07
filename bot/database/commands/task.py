from sqlalchemy.orm import sessionmaker
from bot.database.db import engine, Task
from datetime import datetime


def create_session():
    session = sessionmaker(bind=engine)
    return session()


def add_task(user_id, list_id, text, desc, date, time):
    s = create_session()
    temp_task = Task(user_id=user_id, list_id=list_id, title=text, description=desc,
                     completion_date=date, completion_time=time)
    s.add(temp_task)
    s.commit()


def all_tasks_in_list(list_id):
    s = create_session()
    list_of_tasks = []
    for temp in s.query(Task).filter(Task.list_id == list_id).all():
        if temp.iscomplete:
            list_of_tasks.append("✅ " + temp.title + ":\n" + temp.description + f"\nДата: {temp.completion_date}"
                                                                                f"\nВремя: {temp.completion_time}")
        else:
            list_of_tasks.append(temp.title + ":\n" + temp.description + f"\nДата: {temp.completion_date}"
                                                                         f"\nВремя: {temp.completion_time}")
    return list_of_tasks


def all_tasks(user_id):
    s = create_session()
    tasks = {}
    for title in s.query(Task).filter(Task.user_id == user_id).all():
        tasks[title.title] = str(title.task_id)
    return tasks


def complete_task(task_id):
    s = create_session()
    s.query(Task).filter(Task.task_id == task_id).update({"iscomplete": True})
    s.commit()


def edit_title(task_id, text):
    s = create_session()
    s.query(Task).filter(Task.task_id == task_id).update({"title": text})
    s.commit()


def edit_desc(task_id, text):
    s = create_session()
    s.query(Task).filter(Task.task_id == task_id).update({"description": text})
    s.commit()


def delete_task(task_id):
    s = create_session()
    s.query(Task).filter(Task.task_id == task_id).delete()
    s.commit()


def get_today_deals(user_id):
    s = create_session()
    list_of_deals = []
    for temp in s.query(Task).filter(Task.user_id == user_id, Task.completion_date == datetime.now().date()).all():
        if temp.iscomplete:
            list_of_deals.append("✅ " + temp.title + ":\n" + temp.description + f"\nДата: {temp.completion_date}"
                                                                                f"\nВремя: {temp.completion_time}")
        else:
            list_of_deals.append(temp.title + ":\n" + temp.description + f"\nДата: {temp.completion_date}"
                                                                         f"\nВремя: {temp.completion_time}")
    if not list_of_deals:
        list_of_deals.append("ОТДЫХАТЬ!\nДел на сегодня нет!!!!")
    return list_of_deals
