from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

create_list = InlineKeyboardButton(text='Создать список', callback_data='create_list')
add_task = InlineKeyboardButton(text='Добавить задачу', callback_data='add_task')
lists = InlineKeyboardButton(text='Просмотреть текущие списки задач', callback_data='lists')
tasks_for_day = InlineKeyboardButton(text='Просмотреть все задачи на сегодня', callback_data='tasks_for_day')
motivation_mode = InlineKeyboardButton(text='Режим мотивационных цитат', callback_data='motivation_mode')
sad_mode = InlineKeyboardButton(text='Режим "мне грустно"', callback_data='sad_mode')
bored_mode = InlineKeyboardButton(text='Режим "мне скучно"', callback_data='bored_mode')

menu = InlineKeyboardMarkup()
menu.add(create_list, add_task)
menu.add(lists)
menu.add(tasks_for_day)
menu.add(motivation_mode)
menu.add(sad_mode, bored_mode)

