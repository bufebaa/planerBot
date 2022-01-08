import pickle
import logging

from google_auth_oauthlib.flow import Flow
from googleapiclient.discovery import build

from bot.config import load_config
from bot.services.database import find_user


logger = logging.getLogger(__name__)


def get_flow():

    config = load_config(".env")
    scopes = config.google.scopes
    client_secret = config.google.client_secret
    redirect_url = config.google.redirect_url

    flow = Flow.from_client_secrets_file(
        client_secret,
        scopes=scopes,
        redirect_uri=redirect_url)

    return flow


def get_credentials(user_id):
    try:
        credentials = pickle.loads(find_user(user_id).get('credentials'))

    except TypeError:
        logger.error(TypeError, user_id=user_id)
        credentials = None

    return credentials


def get_service(user_id, credentials=None):

    credentials = credentials or get_credentials(user_id)
    config = load_config(".env")
    service = config.google.api_service
    version = config.google.api_version
    try:
        service = build(service, version, credentials=credentials)
    except AttributeError:
        logger.error(AttributeError, user_id=user_id)
        return None

    return service
