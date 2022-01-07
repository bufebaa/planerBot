from sqlalchemy.orm import sessionmaker
from bot.database.db import List_db, engine, Task


def create_session():
    session = sessionmaker(bind=engine)
    return session()


async def add_list(user_id, title):
    s = create_session()
    temp_list = List_db(user_id=user_id, title=title)
    s.add(temp_list)
    s.commit()


def all_lists(user_id):
    s = create_session()
    lists = {}
    for title in s.query(List_db).filter(List_db.user_id == user_id).all():
        lists[title.title] = str(title.list_id)
    return lists


def is_no_lists_in_db(user_id):
    s = create_session()
    if s.query(List_db).filter(List_db.user_id == user_id).first():
        return False
    else:
        return True


def is_not_list_in_db(title):
    s = create_session()
    if s.query(List_db).filter(List_db.title == title).first():
        return False
    else:
        return True


def get_title_of_list(user_id):
    s = create_session()
    temp = str
    for i in s.query(List_db).filter(List_db.list_id == user_id).all():
        temp = i.title
    return temp


def is_not_tasks_in_list(list_id):
    s = create_session()
    if s.query(Task).filter(Task.list_id == list_id).first():
        return False
    else:
        return True
