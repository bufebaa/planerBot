from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from bot.data import for_user_registration
from aiogram.utils.callback_data import CallbackData
from aiogram import types



#Buttons, menu for MainMenu
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

list_cb = CallbackData('list', 'action')


listMenu = InlineKeyboardMarkup(row_width=1)
show_deals = InlineKeyboardButton(text = "Посмотреть все задачи", callback_data=list_cb.new(action = "show_deals"))
add_deals = InlineKeyboardButton(text = "Добавить задачу", callback_data=list_cb.new(action = "add_deals"))
do_deals = InlineKeyboardButton(text = "Сделать задачу", callback_data=list_cb.new(action = "do_deals"))
edit_deal = InlineKeyboardButton(text = "Редактировать задачу", callback_data=list_cb.new(action = "edit_deal"))
delete_deal = InlineKeyboardButton(text = "Удалить задачу", callback_data=list_cb.new(action = "delete_deal"))
delete_list = InlineKeyboardButton(text = "Завершить работу со списком", callback_data=list_cb.new(action = "exit_list"))
listMenu.add(show_deals, add_deals, do_deals, edit_deal, delete_deal, delete_list)

def create_list_of_lists():
    keyboard = InlineKeyboardMarkup()
    keyboard.row_width = 1
    for key, values in for_user_registration.all_lists().items():
        keyboard.add(InlineKeyboardButton(text = key, callback_data=values))
    return keyboard



# def create_list_of_lists():
#     keyboard = types.ReplyKeyboardMarkup()
#     keyboard.row_width = 1
#     for key, values in for_user_registration.all_lists().items():
#         keyboard.add(types.KeyboardButton(text = key))
#     return keyboard

# ListMenu = types.ReplyKeyboardMarkup(row_width=1)
# show_deals = types.KeyboardButton(text = "Посмотреть все задачи", callback_data= "show_deals")
# add_deals = types.KeyboardButton(text = "Добавить задачу", callback_data= "add_deals")
# do_deals = types.KeyboardButton(text = "Сделать задачу", callback_data= "do_deals")
# edit_deal = types.KeyboardButton(text = "Редактировать задачу", callback_data= "edit_deal")
# delete_deal = types.KeyboardButton(text = "Удалить задачу", callback_data= "delete_deal")
# delete_list = types.KeyboardButton(text = "Удалить список дел", callback_data= "delete_list")
# ListMenu.add(show_deals, add_deals, do_deals, edit_deal, delete_deal, delete_list)
