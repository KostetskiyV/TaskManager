from typing import List
from InputManager import menuInput

def showMenu() -> None:
    #Список функций программы
    menu: List[str] = ["1. Просмотр задач", "2. Добавление задачи", "3. Изменить задачу", "4. Удалить задачу", "5. Поиск задачи", "0. Выход"]
    print()
    for option in menu:
        print(option)


#Отображение меню
showMenu()
while menuInput():
    #Отображение меню
    showMenu()