from sqlalchemy.orm import sessionmaker
from bot.database.db import User, engine


def create_session():
    session = sessionmaker(bind=engine)
    return session()


async def add_user(user_id, credentials):
    s = create_session()
    temp_user = User(user_id=user_id, credentials=credentials)
    s.add(temp_user)
    s.commit()


def is_not_in_db(user_id):
    s = create_session()
    if s.query(User).filter(User.user_id == user_id).first():
        return False
    else:
        return True


def find_user(user_id):
    s = create_session()
    return s.query(User).filter(User.user_id == user_id)


def update_user(user_id, credentials, time_zone):
    s = create_session()
    user = find_user(user_id)
    user.credentials = credentials
    user.time_zone = time_zone
    s.commit()


def delete_user(user_id):
    s = create_session()
    s.query(User).filter(User.user_id == user_id).delete()
    s.commit()
