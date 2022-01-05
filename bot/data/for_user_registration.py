from sqlalchemy import create_engine
from sqlalchemy.exc import NoResultFound
from sqlalchemy.orm import sessionmaker
from typing import List

from bot.data.db import User, List_db
from sqlalchemy import create_engine, select, Table, Column, Integer, String, MetaData, ForeignKey
engine = create_engine('sqlite:///:memory:', echo=True)
meta = MetaData()


async def add_meta():

    user_db = Table('User', meta,
                    Column('user_id', Integer, primary_key=True),
                    Column('e_mail', String(250), nullable=False))
    list_db = Table('List', meta,
                    Column('list_id', Integer, primary_key=True),
                    Column('user_id', Integer, ForeignKey("User.user_id")),
                    Column('title', String(250))
                    )
    meta.create_all(engine)



async def add_user(id, e_mail):

    session = sessionmaker(bind=engine)
    s = session()
    temp_user = User(user_id = id, e_mail = e_mail)
    s.add(temp_user)
    s.commit()
    print(s.query(User).first().e_mail)
    for row in s.query(User, User.user_id).all():
        print("owedrihjoaweihj\n\n\n"+str(row))

async def add_list(id, title):
    session = sessionmaker(bind=engine)
    s = session()
    temp_list = List_db(user_id=id, title=title)
    s.add(temp_list)
    s.commit()
    for row in s.query(List_db, List_db.list_id).all():
        print("LISTiD\n\n\n" + str(row))


def all_lists():
    session = sessionmaker(bind=engine)
    s = session()
    dict = {}
    for title in s.query(List_db):
        dict[title.title]=title.title+str(title.list_id)
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

