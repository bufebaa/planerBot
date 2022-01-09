from sqlalchemy.orm import sessionmaker
from bot.services.database.db import User, engine


def create_session():
    session = sessionmaker(bind=engine)
    return session()


def add_user(user_id, credentials):
    s = create_session()
    temp_user = User(user_id=user_id, credentials=credentials)
    s.add(temp_user)
    s.commit()


def start_add_user(user_id):
    s = create_session()
    temp_user = User(user_id=user_id)
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
    return s.query(User).filter(User.user_id == user_id).first()


def update_credentials(user_id, credentials):
    s = create_session()
    s.query(User).filter(User.user_id == user_id).update({"credentials": credentials})
    s.commit()


def delete_user(user_id):
    s = create_session()
    s.query(User).filter(User.user_id == user_id).delete()
    s.commit()


def switch_mode(user_id):
    s = create_session()
    user = s.query(User).filter(User.user_id == user_id)
    if user.first().is_mode_on:
        user.update({"is_mode_on": False})
    else:
        user.update({"is_mode_on": True})
    s.commit()


def authorized(user_id):
    s = create_session()
    user = s.query(User).filter(User.user_id == user_id)
    user.update({"is_google_synchronized": True})
    s.commit()


def switch_google_sync(user_id):
    s = create_session()
    user = s.query(User).filter(User.user_id == user_id)
    if user.first().is_mode_on:
        user.update({"is_google_synchronized": False})
    else:
        user.update({"is_google_synchronized": True})
    s.commit()


def logout_user(user_id):
    s = create_session()
    user = s.query(User).filter(User.user_id == user_id)
    user.update({"is_google_synchronized": False})
    s.query(User).filter(User.user_id == user_id).update({"credentials": None})

