import logging

from googleapiclient.errors import HttpError

from google.default_methods import get_service

logger = logging.getLogger(__name__)


def create_list(user_id, title):

    service = get_service(user_id)

    try:
        new_list = service.tasklists().insert(
            body={'title': title}
        ).execute()
        return 'CREATED'

    except HttpError as err:
        logger.error(err, user_id=user_id)
        if err.resp.status == 404:
            pass

    return 'MISTAKE'


def is_in_tasklists(user_id, title):
    service = get_service(user_id)

    try:
        results = service.tasklists().list().execute().get('items', [])
        return title in results.get('title')

    except HttpError as err:
        logger.error(err, user_id=user_id)
        if err.resp.status == 404:
            pass

    return False


def add_task(user_id, task_list, title, description, date):
    pass


# def add_event(user_id, description, start, end, service=None, attendees=None, location=None):
#     """Try to add event;
#     Input:
#         user_id - as it is in our database;
#         description - string - main message for the event; first 50 symbols will be set as a title;
#         start, end - datetime.datetime/ datetime.date - start and end time for an event
#         service - Google Calendar service if already known
#         attendees - [list of emails] - who will be invited to an event
#         location - string - location for an event
#     Output:
#         ['CREATED', 'MISTAKE']
#     """
#
#     settings = get_user_settings(user_id)
#
#     credentials = settings.get('credentials')
#     time_zone = settings.get('time_zone')
#     calendar_id = settings.get('calendar_id')
#
#     if not calendar_id:
#         set_calendar_to_primary(user_id)
#
#     credentials = pickle.loads(credentials)
#
#     start_formatted, end_formatted = get_formatted_start_end_time(start, end, time_zone)
#
#     event = {
#         'start': start_formatted,
#         'end': end_formatted,
#         'summary': description[:50],
#         'description': description,
#         'location': location,
#         'attendees': [{'email': email} for email in attendees] if attendees else None
#     }
#
#     service = service or get_calendar_service(user_id, credentials)
#
#     try:
#         service.events().insert(calendarId=calendar_id, body=event, sendNotifications=True).execute()
#         return 'CREATED'
#
#     except HttpError as err:
#         logger.error(err, user_id=user_id)
#
#         if err.resp.status == 404:
#             pass
#
#     return 'MISTAKE'
