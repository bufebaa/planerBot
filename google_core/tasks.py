from datetime import datetime
import logging

from googleapiclient.errors import HttpError

from bot.services.database.commands.list import get_title_of_list
from google_core.default_methods import get_service
from google_core.tasklist import get_list_id_by_id, is_in_lists, create_list

logger = logging.getLogger(__name__)


def is_in_list(user_id, list_id, title):
    service = get_service(user_id)
    tasklist = get_list_id_by_id(user_id, list_id)
    try:
        tasks = service.tasks().list(tasklist=tasklist, showCompleted=True).execute().get('items', [])
        return any(title == task['title'] for task in tasks)
    except HttpError as err:
        logger.error(err, user_id=user_id)


def add_task(user_id, list_id, title, description, date, time):
    tasklist = get_title_of_list(list_id)
    if not is_in_lists(user_id, tasklist):
        create_list(user_id, tasklist)
    if is_in_list(user_id, list_id, title):
        return 'ALREADY EXIST'
    tasklist = get_list_id_by_id(user_id, list_id)
    due = convert_to_rfc_datetime(date, time)
    body = construct_request_body(title, description, due)
    service = get_service(user_id)
    try:
        service.tasks().insert(tasklist=tasklist, body=body).execute()
        return 'SUCCESS'
    except HttpError as err:
        logger.error(err, user_id=user_id)
    return 'ERROR'


def construct_request_body(title, notes, due):
    try:
        request_body = {
        'title': title,
        'notes': notes,
        'due': due,
        'status': 'needsAction'
        }
        return request_body
    except Exception:
        return None


def complete_task(user_id, list_id, title):
    tasklist = get_title_of_list(list_id)
    if not is_in_lists(user_id, tasklist):
        return 'NOT EXIST'
    if not is_in_list(user_id, list_id, title):
        return 'NOT EXIST'
    task = get_task(user_id, list_id, title)
    tasklist = get_list_id_by_id(user_id, list_id)
    service = get_service(user_id)
    task['status'] = 'completed'
    try:
        service.tasks().update(tasklist=tasklist, task=task['id'], body=task).execute()
        return 'SUCCESS'
    except HttpError as err:
        logger.error(err, user_id=user_id)
    return 'ERROR'


def delete_task(user_id, list_id, title):
    tasklist = get_title_of_list(list_id)
    if not is_in_lists(user_id, tasklist):
        return 'NOT EXIST'
    if not is_in_list(user_id, list_id, title):
        return 'NOT EXIST'
    task = get_task(user_id, list_id, title)
    tasklist = get_list_id_by_id(user_id, list_id)
    service = get_service(user_id)
    task['deleted'] = True
    try:
        service.tasks().update(tasklist=tasklist, task=task['id'], body=task).execute()
        return 'SUCCESS'
    except HttpError as err:
        logger.error(err, user_id=user_id)
    return 'ERROR'


def get_task(user_id, list_id, title):
    service = get_service(user_id)
    tasklist = get_list_id_by_id(user_id, list_id)
    try:
        tasks = service.tasks().list(tasklist=tasklist, showCompleted=True).execute().get('items', [])
        for task in tasks:
            if title == task['title']:
                return task
    except HttpError as err:
        logger.error(err, user_id=user_id)



def convert_to_rfc_datetime(date, time):
    due = datetime.combine(date, time)
    return due.isoformat() + 'Z'
