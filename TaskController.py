from typing import Dict, List
import JSONManager

def showTasksAsTable(tasks: List[Dict[str, str]]) -> None:
    print()
    #Получение максимальной длины каждого столбца таблицы, для красивого отображения списка задач
    max_id_len: int = max(len(str(tasks[-1]["id"])), 2)
    max_title_len: int = 8
    max_description_len: int = 8
    max_category_len: int = 9
    max_due_date_len: int = 4
    max_priority_len: int = 9
    for task in tasks:
        title_len: int = len(task["title"])
        description_len: int = len(task["description"])
        category_len: int = len(task["category"])
        due_date_len: int = len(task["due_date"])
        priority_len: int = len(task["priority"])
        max_title_len = max(title_len, max_title_len)
        max_description_len = max(description_len, max_description_len)
        max_category_len = max(category_len, max_category_len)
        max_due_date_len = max(due_date_len, max_due_date_len)
        max_priority_len = max(priority_len, max_priority_len)

    #Составление заголовка таблицы
    table_header: str = "id" + " "*(max_id_len+1-2) + "| Название" + " "*(max_title_len+1-8) + "| Описание" + " "*(max_description_len+1-8) + "| Категория" + " "*(max_category_len+1-9) + "| Срок" + " "*(max_due_date_len+1-4) + "| Приоритет" + " "*(max_priority_len+1-9) + "| Статус выполнения"
    print(table_header)
    print("-"* (len(table_header)))
    #Отображение задач
    for task in tasks:
        task_id: str = str(task["id"])
        title: str = task["title"]
        description: str = str(task["description"])
        category: str = str(task["category"])
        due_date: str = str(task["due_date"])
        priority: str = str(task["priority"])
        status: str = task["status"]
        row: str = task_id + " "*(max_id_len+1-len(task_id)) + "| " + title + " "*(max_title_len+1-len(title)) + "| " + description + " "*(max_description_len+1-len(description)) + "| " + category + " "*(max_category_len+1-len(category)) + "| " + due_date + " "*(max_due_date_len+1-len(due_date)) + "| " + priority + " "*(max_priority_len+1-len(priority)) + "| " + status
        print(row)

def showAllTasks() -> None:

    #Получение всех задач
    tasks: List[Dict[str, str]] = JSONManager.getAllTasks()

    #Проверка, на случай если задач не загружено
    if len(tasks) == 0:
        print("Не загружено ни одной задачи")
        return

    #Отображение задач в таблице
    showTasksAsTable(tasks)

def addTask(title: str, description: str, category: str, due_date: str, priority: str) -> None:
    task_id: int = JSONManager.get_tasks_quantity() + 1
    status: str = "не выполнена"

    #Получение всех задач
    tasks: List[Dict[str, str, int]] = JSONManager.getAllTasks()
    #Присваивание значений
    new_task: Dict[str, str] = {"id": task_id, "title": title, "description": description, "category": category, "due_date": due_date, "priority": priority, "status": status}
    #Добавление задачи
    tasks.append(new_task)
    JSONManager.updateFile(tasks)

def redactTask(task_id: int, redacted_field: str, new_value: str) -> None:
    
    #Получение всех задач
    tasks: List[Dict[str, str, int]] = JSONManager.getAllTasks()
    #Присваивание нового значения
    tasks[task_id-1][redacted_field] = new_value

    JSONManager.updateFile(tasks)

def removeTaskById(task_id: int) -> None:
    #Получение всех задач
    tasks: List[Dict[str, str]] = JSONManager.getAllTasks()
    #Удаление задачи из списка по id
    del tasks[task_id-1]
    for i in range(task_id-1, JSONManager.get_tasks_quantity() - 1):
        tasks[i]["id"] -= 1
    #Обновление списка задач
    JSONManager.updateFile(tasks)

def removeTaskByCategory(category: str) -> None:
    #Получение всех задач
    tasks: List[Dict[str, str]] = JSONManager.getAllTasks()

    new_tasks: List[Dict[str, str]] = []
    tasks_count = 0
    #Добавление в список задач, не соответствующих указанной категории
    for task in tasks:
        if task["category"] != category:
            new_tasks.append(task)
            tasks_count += 1
            new_tasks[tasks_count-1]["id"] = tasks_count

    if tasks_count == JSONManager.get_tasks_quantity():
        print("Не найдено задач этой категории")
    else:
        print("Задачи удалены")

    #Обновление списка задач
    JSONManager.updateFile(new_tasks)

def getTasksByKey(key: str) -> List[Dict[str, str]]:
    key_words = key.split()

    #Получение всех задач
    tasks: List[Dict[str, str]] = JSONManager.getAllTasks()

    found_tasks: List[Dict[str, str]] = []

    #Добавление в список задач с подходящими названиями
    for task in tasks:
        for key_word in key_words:
            title_words = task["title"].split()

            for title_word in title_words:
                if title_word == key_word:
                    found_tasks.append(task)
                    break
            else:
                continue
            break

    #Проверка на случай, если задач не найдено
    if len(found_tasks) == 0:
        print("Задач не найдено")
        return []

    #Отображение задач в таблице
    showTasksAsTable(found_tasks)
    return found_tasks

def getTasksByField(field: str, value: str) -> List[Dict[str, str]]:

    #Получение всех задач
    tasks: List[Dict[str, str]] = JSONManager.getAllTasks()

    found_tasks: List[Dict[str, str]] = []
    #Добавление в список задач, с соответствующим значением поля поиска
    for task in tasks:
        if task[field] == value:
            found_tasks.append(task)

    #Проверка на случай, если задач не найдено
    if len(found_tasks) == 0:
        print("Задач не найдено")
        return []

    #Отображение задач в таблице
    showTasksAsTable(found_tasks)
    return found_tasks