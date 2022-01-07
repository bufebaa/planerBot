import logging
import pickle

from bot.database import commands
from google.default_methods import get_flow

logger = logging.getLogger(__name__)


def get_authorisation_url():

    flow = get_flow()
    auth_url, _ = flow.authorization_url(prompt='consent')
    return auth_url


def fetch_token(user_id, code):

    flow = get_flow()
    try:
        flow.fetch_token(code=code)
        credentials = flow.credentials
        save_user(user_id, credentials=pickle.dumps(credentials))
        return True
    except Exception as e:
        logger.exception(e, user_id=user_id, code=code)
        return False


def get_user_settings(user_id):
    return commands.find_user(user_id)


def save_user(user_id, credentials):
    commands.add_user(user_id, credentials)


def save_settings(user_id, credentials):
    commands.update_user(user_id, credentials)


def delete_user(user_id):
    return commands.delete_user(user_id)
