import logging
import pickle

from bot.services.database.commands.user import add_user, update_credentials, delete_user, \
    is_not_in_db, authorized
from google_core.default_methods import get_flow

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


def save_user(user_id, credentials):
    if is_not_in_db(user_id):
        add_user(user_id, credentials)
    else:
        update_credentials(user_id, credentials)
    authorized(user_id)


def user_logout(user_id):
    delete_user(user_id)
