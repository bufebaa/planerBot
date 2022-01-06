from sqlalchemy.orm import sessionmaker
from bot.data.db import User, List_db, engine, Task
from sqlalchemy import create_engine, select, Table, Column, Integer, String, MetaData, ForeignKey
meta = MetaData()


async def add_user(id, e_mail):
    session = sessionmaker(bind=engine)
    s = session()
    temp_user = User(user_id = id, e_mail = e_mail)
    s.add(temp_user)
    s.commit()


async def add_list(id, title):
    session = sessionmaker(bind=engine)
    s = session()
    temp_list = List_db(user_id=id, title=title)
    s.add(temp_list)
    s.commit()


def all_lists():
    session = sessionmaker(bind=engine)
    s = session()
    dict = {}
    for title in s.query(List_db):
        dict[title.title]=str(title.list_id)
    return dict


def is_in_db(id):
    session = sessionmaker(bind=engine)
    s = session()
    if s.query(User).filter(User.user_id == id).first():
        return False
    else:
        return True


def is_list_in_db(name):
    session = sessionmaker(bind=engine)
    s = session()
    if s.query(List_db).filter(List_db.title == name).first():
        return False
    else:
        return True


def add_task(list_id, text, disc):
    session = sessionmaker(bind=engine)
    s = session()
    temp_task = Task(list_id=list_id, title=text, description = disc)
    s.add(temp_task)
    s.commit()

def show_all_tasks(list_id):
    session = sessionmaker(bind=engine)
    s = session()
    list_of_tasks = []
    for temp in s.query(Task).filter(Task.list_id == list_id).all():
        list_of_tasks.append(temp.title+":\n"+temp.description)
    return list_of_tasks

