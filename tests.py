import TaskController, JSONManager
import os

def test_addTask():
    
    try:
        os.remove(JSONManager.LIBRARY_PATH)
    except:
        pass

    test_data = [{"id": 1, "title": "Закончить приложение", "description": "Написать тесты", "category": "Работа", "due_date": "2024-12-03", "priority": "высокий", "status": "не выполнена"},
                 {"id": 2, "title": "Написать лабораторную", "description": "", "category": "Учёба", "due_date": "2024-12-02", "priority": "средний", "status": "не выполнена"},
                 {"id": 3, "title": "Сходить на тренировку", "description": "", "category": "Спорт", "due_date": "2024-12-05", "priority": "средний", "status": "не выполнена"},
                 {"id": 4, "title": "Сделать индивидуальное задание", "description": "", "category": "Учёба", "due_date": "2024-12-15", "priority": "высокий", "status": "не выполнена"}]

    for task in test_data:
        TaskController.addTask(task["title"], task["description"], task["category"], task["due_date"], task["priority"])

    data = JSONManager.getAllTasks()

    assert len(data) == len(test_data)
    for i in range(len(data)):
        assert data[i] == test_data[i]

def test_getTaskByField():
    test_data = [{"id": 2, "title": "Написать лабораторную", "description": "", "category": "Учёба", "due_date": "2024-12-02", "priority": "средний", "status": "не выполнена"},
                 {"id": 3, "title": "Сходить на тренировку", "description": "", "category": "Спорт", "due_date": "2024-12-05", "priority": "средний", "status": "не выполнена"},
                 {"id": 4, "title": "Сделать индивидуальное задание", "description": "", "category": "Учёба", "due_date": "2024-12-15", "priority": "высокий", "status": "не выполнена"}]

    data = TaskController.getTasksByField("description", "")

    assert len(data) == len(test_data)
    for i in range(len(data)):
        assert data[i] == test_data[i]

    test_data = [{"id": 2, "title": "Написать лабораторную", "description": "", "category": "Учёба", "due_date": "2024-12-02", "priority": "средний", "status": "не выполнена"},
                 {"id": 4, "title": "Сделать индивидуальное задание", "description": "", "category": "Учёба", "due_date": "2024-12-15", "priority": "высокий", "status": "не выполнена"}]

    data = TaskController.getTasksByField("category", "Учёба")

    assert len(data) == len(test_data)
    for i in range(len(data)):
        assert data[i] == test_data[i]

    test_data = [{"id": 1, "title": "Закончить приложение", "description": "Написать тесты", "category": "Работа", "due_date": "2024-12-03", "priority": "высокий", "status": "не выполнена"}]

    data = TaskController.getTasksByField("category", "Работа")

    assert len(data) == len(test_data)
    for i in range(len(data)):
        assert data[i] == test_data[i]
        
    test_data = [{"id": 1, "title": "Закончить приложение", "description": "Написать тесты", "category": "Работа", "due_date": "2024-12-03", "priority": "высокий", "status": "не выполнена"},
                 {"id": 2, "title": "Написать лабораторную", "description": "", "category": "Учёба", "due_date": "2024-12-02", "priority": "средний", "status": "не выполнена"},
                 {"id": 3, "title": "Сходить на тренировку", "description": "", "category": "Спорт", "due_date": "2024-12-05", "priority": "средний", "status": "не выполнена"},
                 {"id": 4, "title": "Сделать индивидуальное задание", "description": "", "category": "Учёба", "due_date": "2024-12-15", "priority": "высокий", "status": "не выполнена"}]

    data = TaskController.getTasksByField("status", "не выполнена")

    assert len(data) == len(test_data)
    for i in range(len(data)):
        assert data[i] == test_data[i]

    test_data = []

    data = TaskController.getTasksByField("status", "выполнена")

    assert len(data) == len(test_data)
    for i in range(len(data)):
        assert data[i] == test_data[i]

def test_getTaskByKey():

    key = "Сходить на лабораторную"
    test_data = [{"id": 2, "title": "Написать лабораторную", "description": "", "category": "Учёба", "due_date": "2024-12-02", "priority": "средний", "status": "не выполнена"},
                 {"id": 3, "title": "Сходить на тренировку", "description": "", "category": "Спорт", "due_date": "2024-12-05", "priority": "средний", "status": "не выполнена"}]

    data = TaskController.getTasksByKey(key)

    assert len(data) == len(test_data)
    for i in range(len(data)):
        assert data[i] == test_data[i]

    key = "Написать приложение"
    test_data = [{"id": 1, "title": "Закончить приложение", "description": "Написать тесты", "category": "Работа", "due_date": "2024-12-03", "priority": "высокий", "status": "не выполнена"},
                 {"id": 2, "title": "Написать лабораторную", "description": "", "category": "Учёба", "due_date": "2024-12-02", "priority": "средний", "status": "не выполнена"}]

    data = TaskController.getTasksByKey(key)

    assert len(data) == len(test_data)
    for i in range(len(data)):
        assert data[i] == test_data[i]

    key = "на"
    test_data = [{"id": 3, "title": "Сходить на тренировку", "description": "", "category": "Спорт", "due_date": "2024-12-05", "priority": "средний", "status": "не выполнена"}]

    data = TaskController.getTasksByKey(key)

    assert len(data) == len(test_data)
    for i in range(len(data)):
        assert data[i] == test_data[i]

def test_redactTask():
    
    test_data = [{"id": 1, "title": "Закончить приложение", "description": "Написать тесты", "category": "Работа", "due_date": "2024-12-03", "priority": "высокий", "status": "выполнена"},
                 {"id": 2, "title": "Написать лабораторную", "description": "", "category": "Учёба", "due_date": "2024-12-02", "priority": "средний", "status": "не выполнена"},
                 {"id": 3, "title": "Сходить на физкультуру", "description": "", "category": "Спорт", "due_date": "2024-12-05", "priority": "средний", "status": "не выполнена"},
                 {"id": 4, "title": "Сделать индивидуальное задание", "description": "Предмет: птп", "category": "Учёба", "due_date": "2024-12-15", "priority": "высокий", "status": "не выполнена"}]

    TaskController.redactTask(2, "due_date", "2024-12-01")
    TaskController.redactTask(4, "description", "Предмет: птп")
    TaskController.redactTask(2, "due_date", "2024-12-02")
    TaskController.redactTask(3, "title", "Сходить на физкультуру")
    TaskController.redactTask(1, "status", "выполнена")
    
    data = JSONManager.getAllTasks()

    assert len(data) == len(test_data)
    for i in range(len(data)):
        assert data[i] == test_data[i]

def test_removeTaskById():

    test_data = [{"id": 1, "title": "Закончить приложение", "description": "Написать тесты", "category": "Работа", "due_date": "2024-12-03", "priority": "высокий", "status": "выполнена"},
                 {"id": 2, "title": "Написать лабораторную", "description": "", "category": "Учёба", "due_date": "2024-12-02", "priority": "средний", "status": "не выполнена"},
                 {"id": 3, "title": "Сходить на физкультуру", "description": "", "category": "Спорт", "due_date": "2024-12-05", "priority": "средний", "status": "не выполнена"},
                 {"id": 4, "title": "Сделать индивидуальное задание", "description": "Предмет: птп", "category": "Учёба", "due_date": "2024-12-15", "priority": "высокий", "status": "не выполнена"}]
    
    TaskController.removeTaskById(3)
    del test_data[2]
    test_data[2]["id"] = 3
    data = JSONManager.getAllTasks()

    assert len(data) == len(test_data)
    for i in range(len(data)):
        assert data[i] == test_data[i]

    TaskController.removeTaskById(1)
    del test_data[0]
    test_data[0]["id"] = 1
    test_data[1]["id"] = 2
    data = JSONManager.getAllTasks()

    assert len(data) == len(test_data)
    for i in range(len(data)):
        assert data[i] == test_data[i]

def test_removeTaskByCategory():

    test_data = []

    TaskController.removeTaskByCategory("Учёба")
    data = JSONManager.getAllTasks()

    assert len(data) == len(test_data)
    assert data == test_data