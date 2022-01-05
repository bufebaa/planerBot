from aiogram.types import ReplyKeyboardMarkup

main_menu = 'Создать список'
calendar = 'Добавить задачу'
tasks_for_day = 'Просмотреть все задачи на сегодня'
motivation_mode= 'Режим мотивационных цитат'
sad_mode = 'Режим "мне грустно"'
bored_mode = 'Режим "мне скучно"'

menu = ReplyKeyboardMarkup(resize_keyboard=True)
menu.add(create_list, add_task)
menu.add(lists)
menu.add(tasks_for_day)
menu.add(motivation_mode)
menu.add(sad_mode, bored_mode)
