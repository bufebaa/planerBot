import logging

from googleapiclient.errors import HttpError

from bot.services.database.commands.list import get_title_of_list
from google_core.default_methods import get_service

logger = logging.getLogger(__name__)


def is_in_lists(user_id, title):
    service = get_service(user_id)
    try:
        lists = service.tasklists().list().execute().get('items', [])
        return any(title == tasklist['title'] for tasklist in lists)
    except HttpError as err:
        logger.error(err, user_id=user_id)


def create_list(user_id, title):
    if is_in_lists(user_id, title):
        return 'ALREADY EXIST'
    service = get_service(user_id)
    try:
        service.tasklists().insert(body={'title': title}).execute()
        return 'SUCCESS'
    except HttpError as err:
        logger.error(err, user_id=user_id)
    return 'ERROR'


def delete_list(user_id, title):
    if not is_in_lists(user_id, title):
        return 'NOT EXIST'
    service = get_service(user_id)
    try:
        service.tasklists().delete(tasklist=get_list_id(user_id, title)).execute()
        return 'SUCCESS'
    except HttpError as err:
        logger.error(err, user_id=user_id)
    return 'ERROR'


def get_list_id(user_id, title):
    service = get_service(user_id)
    try:
        lists = service.tasklists().list().execute().get('items', [])
        for tasklist in lists:
            if title == tasklist['title']:
                return tasklist['id']
    except HttpError as err:
        logger.error(err, user_id=user_id)


def get_list_id_by_id(user_id, list_id):
    return get_list_id(user_id, get_title_of_list(list_id))
