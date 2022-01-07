from bot.keyboards.callendar import DialogCalendar
from aiogram import types, Dispatcher
from aiogram.dispatcher import FSMContext
from bot.data import for_user_registration
from bot.states import ListCreation, TaskCreation,CompleteState,EditTask, DeleteTask
from bot.keyboards import inline
from bot.keyboards.inline import list_cb, task_cb


async def open_list_menu(callback : types.CallbackQuery, state : FSMContext):
    data = callback.data
    await state.update_data(list_id = int(data))
    await callback.message.answer("✨Меню списка: ", reply_markup=inline.listMenu)
    await ListCreation.next()
    TaskCreation.list_id = int(data)


async def action_with_menu(callback : types.CallbackQuery,callback_data: dict, state : FSMContext):
    action = callback_data['action']

    if "add_deals" == action:
        await callback.message.answer("Введите название задачи: ")
        await ListCreation.get_name.set()

    elif "show_deals" == action:
        await callback.message.answer(f"✨Задачи списка {for_user_registration.return_name_of_list(TaskCreation.list_id)}✨:", parse_mode='Markdown')
        for i in for_user_registration.show_all_tasks(TaskCreation.list_id):
            await callback.message.answer(str(i))
        await callback.message.answer("✨Меню списка: ", reply_markup=inline.listMenu)

    elif "do_deals" == action:
        await callback.message.answer("Выберите задачу, которую вы выполнили: ", reply_markup=inline.create_list_of_tasks())
        await state.finish()
        await CompleteState.choose.set()

    elif "edit_deal" == action:
        await callback.message.answer("Выберите задачу, которую вы хотите отредактировать: ",
                                      reply_markup=inline.create_list_of_tasks())
        await state.finish()
        await EditTask.choice1.set()

    elif "delete_deal" == action:
        await callback.message.answer("Выберите задачу, которую вы хотите удалить: ",
                                      reply_markup=inline.create_list_of_tasks())
        await state.finish()
        await DeleteTask.chooseTastToDelete.set()

    elif "exit_list" == action:
        await state.finish()
        await callback.message.answer("✨Главное меню✨: ", reply_markup=inline.menu)


#Work with states for task adding:
async def get_task_title (message: types.Message,state : FSMContext):
    TaskCreation.title = message.text
    await message.answer("Введите описание задачи: ")
    await state.finish()
    await TaskCreation.get_description.set()

async def get_task_discription (message: types.Message,state : FSMContext):
    TaskCreation.disc = message.text
    await message.answer("Введите дату задачи: ",reply_markup=await DialogCalendar().start_calendar())
    await TaskCreation.get_date.set()



#In order to complete Task
async def complete_task(callback : types.CallbackQuery, state : FSMContext):
    data = callback.data
    for_user_registration.complete_task(data)
    await callback.message.answer("Сделано!!!", reply_markup=inline.listMenu )
    await state.finish()
    await ListCreation.actionwithmenu.set()


#In order to edit Task
async def edit_task(callback : types.CallbackQuery, state : FSMContext):
    data = callback.data
    EditTask.id_task = data
    await callback.message.answer("Выберите что вы хотите редактировать: ", reply_markup=inline.editingTaskMenu)
    await EditTask.choice2.set()


async def editing(callback : types.CallbackQuery,callback_data: dict, state : FSMContext):
    action = callback_data['action']

    if "edit_title" == action:
        await callback.message.answer("Введите новое название)")
        await EditTask.titleEditing.set()

    elif "edit_disc" == action:
        await callback.message.answer("Введите новое описание)")
        await EditTask.discEditing.set()


async def edit_title(message: types.Message,state : FSMContext):
    for_user_registration.edit_title(EditTask.id_task, message.text)
    await message.answer("Отредактировано!!!", reply_markup=inline.listMenu)
    await state.finish()
    await ListCreation.actionwithmenu.set()


async def edit_disc(message: types.Message,state : FSMContext):
    for_user_registration.edit_disc(EditTask.id_task, message.text)
    await message.answer("Отредактировано!!!", reply_markup=inline.listMenu)
    await state.finish()
    await ListCreation.actionwithmenu.set()

#In order to delete task

async def delete_task(callback : types.CallbackQuery, state : FSMContext):
    data = callback.data
    for_user_registration.delete_task(data)
    await callback.message.answer("Задача была успешно удалена !)", reply_markup=inline.listMenu)
    await state.finish()
    await ListCreation.actionwithmenu.set()


def register_open_list_menu(dp: Dispatcher):
    dp.register_callback_query_handler(open_list_menu, text = None, state=ListCreation.showlists)

    dp.register_callback_query_handler(action_with_menu, list_cb.filter(action = "add_deals"), state=ListCreation.actionwithmenu)
    dp.register_callback_query_handler(action_with_menu, list_cb.filter(action = "show_deals"), state=ListCreation.actionwithmenu)
    dp.register_callback_query_handler(action_with_menu, list_cb.filter(action = "exit_list"), state=ListCreation.actionwithmenu)
    dp.register_callback_query_handler(action_with_menu, list_cb.filter(action = "do_deals"), state=ListCreation.actionwithmenu)
    dp.register_callback_query_handler(action_with_menu, list_cb.filter(action = "edit_deal"), state=ListCreation.actionwithmenu)
    dp.register_callback_query_handler(action_with_menu, list_cb.filter(action = "delete_deal"), state=ListCreation.actionwithmenu)



    dp.register_message_handler(get_task_title, state=ListCreation.get_name)
    dp.register_message_handler(get_task_discription, state=TaskCreation.get_description)

    dp.register_callback_query_handler(complete_task, text = None, state=CompleteState.choose)

    dp.register_callback_query_handler(edit_task,text = None, state=EditTask.choice1)
    dp.register_callback_query_handler(editing,task_cb.filter(action = "edit_title"), state=EditTask.choice2)
    dp.register_callback_query_handler(editing,task_cb.filter(action = "edit_disc"), state=EditTask.choice2)
    dp.register_message_handler(edit_title, state=EditTask.titleEditing)
    dp.register_message_handler(edit_disc, state=EditTask.discEditing)

    dp.register_callback_query_handler(delete_task, text = None, state=DeleteTask.chooseTastToDelete)

