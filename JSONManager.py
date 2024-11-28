from typing import Dict, List
import json

#Путь к JSON-файлу
LIBRARY_PATH = "tasks.json"

def getAllTasks() -> List[Dict[str, str]]:
    
    #Проверка существования JSON-файла и создание оного, в случае отсутствия
    checkFile()

    #Считывание JSON-файла
    with open(LIBRARY_PATH, 'r') as file:
        tasks: List[Dict[str, str]] = json.load(file)

    return tasks

def updateFile(tasks: List[Dict[str, str]]) -> None:

    #Запись в JSON-файл
    with open(LIBRARY_PATH, 'w') as file:
        json.dump(tasks, file)

def get_tasks_quantity() -> int:
    return len(getAllTasks())

def checkFile() -> None:
    from os.path import isfile
    if not isfile(LIBRARY_PATH):
        with open(LIBRARY_PATH, 'w') as file:
            file.write('[]')