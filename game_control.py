# Arda Mavi
# Импорт необходимых классов для работы с мышью и клавиатурой
from pynput.mouse import Button, Controller as Mouse
from pynput.keyboard import Controller as Keyboard

# Функция для получения списка всех клавиш, которые можно использовать
def get_keys():
    return [
'\t', '\n', '\r', ' ', '!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',', '-', '.', '/', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', ':', ';', '<', '=', '>', '?', '@', '[', '\\', ']', '^', '_', '`', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '{', '|', '}', '~', 'accept', 'add', 'alt', 'altleft', 'altright', 'apps', 'backspace', 'browserback', 'browserfavorites', 'browserforward', 
]

# Функция для получения клавиши по её индексу
def get_key(id):
    return get_keys()[id]

# Функция для получения индекса клавиши
def get_id(key):
    return get_keys().index(key)

# Создание объектов контроллеров для клавиатуры и мыши
keyboard = Keyboard()
mouse = Mouse()

# Функции для управления мышью:
def move(x, y):
    #Перемещает курсор мыши в координаты (x, y).
    mouse.position = (x, y)
    return

def scroll(x, y):
    #Скроллит мышь на (x, y) по осям.
    mouse.scroll(x, y)
    return

def click(x, y):
    #Кликает левой кнопкой мыши в указанной точке (x, y).
    mouse.position = (x, y)
    mouse.press(Button.left)
    mouse.release(Button.left)
    return

# Функции для управления клавиатурой:
def press(key):
    #Нажимает указанную клавишу.
    keyboard.press(key)
    return

def release(key):
    #Отпускает указанную клавишу.
    keyboard.release(key)
    return
