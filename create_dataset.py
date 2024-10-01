# Arda Mavi
# Импортирование необходимых библиотек
import os
import sys
import platform
import numpy as np
from time import sleep
from PIL import ImageGrab
from game_control import *
from predict import predict
from scipy.misc import imresize
from game_control import get_id
from get_dataset import save_img
from multiprocessing import Process
from keras.models import model_from_json
from pynput.mouse import Listener as mouse_listener
from pynput.keyboard import Listener as key_listener

# Функция для захвата скриншота экрана и предобработки изображения
def get_screenshot():
    img = ImageGrab.grab()  # Захват изображения с экрана
    img = np.array(img)[:, :, :3]  # Получение первых трех каналов изображения (RGB)
    img = imresize(img, (150, 150, 3)).astype('float32') / 255.  # Изменение размера и нормализация
    return img  # Возвращение обработанного изображения

# Функция для сохранения события клавиатуры с текущим скриншотом
def save_event_keyboard(data_path, event, key):
    key = get_id(key)  # Получение ID клавиши
    # Формирование пути для сохранения изображения с указанием события и клавиши
    data_path = data_path + '/-1,-1,{0},{1}'.format(event, key)
    screenshot = get_screenshot()  # Получение скриншота
    save_img(data_path, screenshot)  # Сохранение скриншота
    return

# Функция для сохранения события мыши с текущим скриншотом
def save_event_mouse(data_path, x, y):
    # Формирование пути для сохранения изображения с указанием координат мыши
    data_path = data_path + '/{0},{1},0,0'.format(x, y)
    screenshot = get_screenshot()  # Получение скриншота
    save_img(data_path, screenshot)  # Сохранение скриншота
    return

# Функция для прослушивания событий мыши
def listen_mouse():
    data_path = 'Data/Train_Data/Mouse'  # Указание пути к папке для сохранения данных
    if not os.path.exists(data_path):
        os.makedirs(data_path)  # Создание папки, если она не существует

    # Функция для обработки кликов мыши
    def on_click(x, y, button, pressed):
        save_event_mouse(data_path, x, y)  # Сохранение события клика мыши

    # Пустые функции для события прокрутки и движения мыши
    def on_scroll(x, y, dx, dy):
        pass
    
    def on_move(x, y):
        pass

    # Запуск слушатель мыши
    with mouse_listener(on_move=on_move, on_click=on_click, on_scroll=on_scroll) as listener:
        listener.join()  # Ожидание завершения слушателя

# Функция для прослушивания событий клавиатуры
def listen_keyboard():
    data_path = 'Data/Train_Data/Keyboard'  # Указание пути к папке для сохранения данных
    if not os.path.exists(data_path):
        os.makedirs(data_path)  # Создание папки, если она не существует

    # Функция для обработки нажатия клавиши
    def on_press(key):
        save_event_keyboard(data_path, 1, key)  # Сохранение события нажатия клавиши

    # Функция для обработки отпускания клавиши
    def on_release(key):
        save_event_keyboard(data_path, 2, key)  # Сохранение события отпускания клавиши

    # Запуск слушателя клавиатуры
    with key_listener(on_press=on_press, on_release=on_release) as listener:
        listener.join()  # Ожидание завершения слушателя

# Главная функция программы
def main():
    dataset_path = 'Data/Train_Data/'  # Указание пути к папке для хранения набора данных
    if not os.path.exists(dataset_path):
        os.makedirs(dataset_path)  # Создание папки, если она не существует

    # Запуск прослушивания мыши в новом процессе
    Process(target=listen_mouse, args=()).start()  
    listen_keyboard()  # Запуск прослушивания клавиатуры
    return

# Запуск программы
if __name__ == '__main__':
    main()
