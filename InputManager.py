from datetime import datetime, date as dt
from typing import List, Union
from TaskController import showAllTasks, getTasksByKey, getTasksByField, addTask, removeTaskById, removeTaskByCategory, redactTask
from JSONManager import get_tasks_quantity

def checkDate(inp_date: str) -> bool:
    try:
        date = dt.fromisoformat(inp_date)
    except ValueError:
        print("Неверный формат или не существующая дата")
        return False
    if date < datetime.now().date():
        print("Введена прошедшая дата")
        return False
    return True

def showTasksInput() -> None:
    category = input("Введите категорию задач для отображения или не вводите ничего, чтобы отобразить все задачи: ")
    if len(category) == 0:
        showAllTasks()
    else:
        getTasksByField("category", category)

def addTaskInput() -> None:
    title: str = input("Введите название: ")
    #Проверка ввода на пустоту
    if len(title) == 0:
        print("Пустой ввод")
        return
    description: str = input("Введите описание: ")
    category: str = input("Введите категорию задачи: ")
    if len(category) == 0:
        print("Пустой ввод")
        return
    due_date: str = input("Введите срок выполнения (в формате ГГГГ-ММ-ДД): ")
    if not checkDate(due_date):
        return
    priority: str = input("Введите приоритет (низкий/средний/высокий): ")
    if priority != "низкий" and priority != "средний" and priority != "высокий":
        print("Некорректный ввод")
        return

    addTask(title, description, category, due_date, priority)

def findTaskMenu() -> None:

    menu: List[str] = ['Введите "1" для поиска по ключевым словам в названии', 'Введите "2" для поиска по категории', 'Введите "3", чтобы найти все выполненные задачи', 'Введите "4", чтобы найти все не выполненные задачи', 'Введите "0", чтобы выйти из режима поиска']
    for punct in menu:
        print(punct)

    inp: str = input()
    if inp == "1":
        key: str = input("Введите ключевое(-ые) слово(-а) для поиска: ")
        while len(key) == 0:
            print("Пустой ввод")
            key: str = input("Введите ключевое(-ые) слово(-а) для поиска: ")
        getTasksByKey(key)
    elif inp == "2":
        category: str = input("Введите категорию: ")
        while len(category) == 0:
            print("Пустой ввод")
            category: str = input("Введите категорию: ")
        getTasksByField("category", category)
    elif inp == "3":
        getTasksByField("status", "выполнена")
    elif inp == "4":
        getTasksByField("status", "не выполнена")
    elif inp == "0":
        pass
    else:
        print("Некорректный ввод.")

def removeTaskInput() -> None:
    #Получение количества задач
    tasks_quantity: int = get_tasks_quantity()
    #Проверка наличия хотя бы одной задачи в базе
    if tasks_quantity == 0:
        print("Нет задач для удаления")
        return

    key: str = input(f"Введите id задачи (1-{get_tasks_quantity()}) или категорию: ")
    #Проверка введённого id
    if not key.isdigit():
        #Удаление задач по категории
        removeTaskByCategory(key)
        return
    task_id: int = int(key)
    if task_id <= 0 or task_id > get_tasks_quantity():
        #Удаление задач по категории
        print("Введён не существующий id")
        return

    #Удаление задачи по id
    removeTaskById(task_id)

def redactMenu(task_id: int) -> None:
    menu: List[str] = ['Введите "1", чтобы изменить название задачи', 'Введите "2", чтобы изменить описание задачи', 'Введите "3", чтобы поменять категорию задачи', 'Введите "4", чтобы изменить срок выполнения задачи', 'Введите "5", чтобы изменить приоритет задачи', 'Введите "6", чтобы отметить задачу как выполненную', 'Введите "0", чтобы выйти из режима редактирования']
    for punct in menu:
        print(punct)

    inp: str = input()
    if inp == "1":
        #Изменение названия

        new_title: str = input("Введите новое название: ")
        #Проверка ввода на пустоту
        while len(new_title) == 0:
            print("Пустой ввод")
            new_title: str = input("Введите новое название: ")
        redactTask(task_id, "title", new_title)
    elif inp == "2":
        #Изменение описания

        new_description: str = input("Введите новое описание: ")
        redactTask(task_id, "description", new_description)
    elif inp == "3":
        #Изменение категории

        new_category: str = input("Введите категорию: ")
        #Проверка ввода на пустоту
        while len(new_category) == 0:
            print("Пустой ввод")
            new_title: str = input("Введите категорию: ")
        redactTask(task_id, "category", new_category)
    elif inp == "4":
        #Изменение срока выполнения

        new_due_date: str = input("Введите новый срок выполнения (в формате ГГГГ-ММ-ДД): ")
        while not checkDate(new_due_date):
            new_due_date: str = input("Введите новый срок выполнения (в формате ГГГГ-ММ-ДД): ")
        redactTask(task_id, "due_date", new_due_date)
    elif inp == "5":
        #Изменение приоритета

        new_priority: str = input("Введите новый приоритет (низкий/средний/высокий): ")
        while new_priority != "низкий" and new_priority != "средний" and new_priority != "высокий":
            print("Некорректный ввод")
            new_priority: str = input("Введите новый приоритет (низкий/средний/высокий): ")
        redactTask(task_id, "priority", new_priority)
    elif inp == "6":
        #Отметка выполнения

        redactTask(task_id, "status", "выполнена")
    elif inp == "0":
        pass
    else:
        print("Некорректный ввод.")

def redactTaskInput() -> None:
    #Получение количества задач
    tasks_quantity: int = get_tasks_quantity()
    #Проверка наличия хотя бы одной задачи в базе
    if tasks_quantity == 0:
        print("Нет задач для редактирования")
        return

    task_id: Union[str, int] = input(f"Введите id задачи (1-{tasks_quantity}): ")
    #Проверка введённого id
    if not task_id.isdigit():
        print("Некорректный ввод.")
        return
    task_id = int(task_id)
    if task_id <= 0 or task_id > tasks_quantity:
        print("Введён несуществующий id.")
        return

    #Переход в меню редактирования
    redactMenu(task_id)

def menuInput() -> bool:
    inp: str = input()
    if inp == "1":
        showTasksInput()
    elif inp == "2":
        addTaskInput()
    elif inp == "3":
        redactTaskInput()
    elif inp == "4":
        removeTaskInput()
    elif inp == "5":
        findTaskMenu()
    elif inp == "0":
        return False
    else:
        print("Некорректный ввод.")
    return True