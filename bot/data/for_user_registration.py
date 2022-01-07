from sqlalchemy.orm import sessionmaker
from bot.data.db import User, List_db, engine, Task
from datetime import datetime


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

def is_lists_in_db():
    session = sessionmaker(bind=engine)
    s = session()
    if s.query(List_db).first():
        return False
    else:
        return True


def is_task_in_list(id):
    session = sessionmaker(bind=engine)
    s = session()
    if s.query(Task).filter(Task.list_id==id).first():
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


def add_task(list_id, text, disc, date, time):
    session = sessionmaker(bind=engine)
    s = session()
    temp_task = Task(list_id=list_id, title=text, description = disc, complation_date = date, complation_time = time)
    s.add(temp_task)
    s.commit()


def show_all_tasks(list_id):
    session = sessionmaker(bind=engine)
    s = session()
    list_of_tasks = []
    for temp in s.query(Task).filter(Task.list_id == list_id).all():
        if temp.iscomplete == True:
            list_of_tasks.append("✅ "+temp.title + ":\n" + temp.description+f"\nДата: {temp.complation_date}"
                                                                            f"\nВремя: {temp.complation_time}")
        else:
            list_of_tasks.append(temp.title+":\n"+temp.description+f"\nДата: {temp.complation_date}"
                                                                            f"\nВремя: {temp.complation_time}")
    return list_of_tasks


def all_tasks():
    session = sessionmaker(bind=engine)
    s = session()
    dict = {}
    for title in s.query(Task):
        dict[title.title]=str(title.task_id)
    return dict


def complete_task(id):
    session = sessionmaker(bind=engine)
    s = session()
    s.query(Task).filter(Task.task_id == id).update({"iscomplete":True})
    s.commit()


def edit_title(id, text):
    session = sessionmaker(bind=engine)
    s = session()
    s.query(Task).filter(Task.task_id == id).update({"title": text})
    s.commit()


def edit_disc(id, text):
    session = sessionmaker(bind=engine)
    s = session()
    s.query(Task).filter(Task.task_id == id).update({"description": text})
    s.commit()


def return_name_of_list(id):
    session = sessionmaker(bind=engine)
    s = session()
    temp = str
    for i in s.query(List_db).filter(List_db.list_id == id).all():
        temp = i.title
    return temp


def delete_task(id):
    session = sessionmaker(bind=engine)
    s = session()
    s.query(Task).filter(Task.task_id == id).delete()
    s.commit()

def show_today_deals():
    session = sessionmaker(bind=engine)
    s = session()
    list_of_deals = []
    for temp in s.query(Task).filter(Task.complation_date == datetime.now().date()).all():
        if temp.iscomplete == True:
            list_of_deals.append("✅ " + temp.title + ":\n" + temp.description + f"\nДата: {temp.complation_date}"
                                                                                f"\nВремя: {temp.complation_time}")
        else:
            list_of_deals.append(temp.title + ":\n" + temp.description + f"\nДата: {temp.complation_date}"
                                                               f"\nВремя: {temp.complation_time}")
    if list_of_deals==[]:
        list_of_deals.append("ОТДЫХАТЬ!\nДел на сегодня нет!!!!")
    return list_of_deals