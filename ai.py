# Arda Mavi
# Файл запуска искусственного интеллекта для компьютерной игры

# Импортирование необходимых библиотек и модулей
import os
import platform
import numpy as np
from time import sleep
from PIL import ImageGrab
from game_control import *
from predict import predict
from keras.models import model_from_json

# Главная функция программы
def main():
    # Загрузка модели искусственного интеллекта из JSON файла
    model_file = open('Data/Model/model.json', 'r')
    model = model_file.read()
    model_file.close()
    
    # Восстановление модели из JSON
    model = model_from_json(model)
    model.load_weights("Data/Model/weights.h5")

    print('AI start now!')

    while 1:  # Бесконечный цикл для постоянного контроля игры
        # Захват скриншота экрана
        screen = ImageGrab.grab()  # Получение текущего изображения с экрана
        # Преобразование изображения в массив NumPy для обработки
        screen = np.array(screen)
        # Преобразование изображения из 4 каналов (RGBA) в 3 канала (RGB)
        
        # Получение действий AI на основе предсказания
        Y = predict(model, screen)  # Получение предсказанных действий от модели

        if Y == [0, 0, 0, 0]:  # Если предсказанное действие: ничего не делать
            continue  # Переход к следующей итерации цикла

        elif Y[0] == -1 and Y[1] == -1:  # Если действия только с клавиатурой
            key = get_key(Y[3])  # Получение кода клавиши из предсказания
            if Y[2] == 1:  # Если нужно нажать клавишу
                press(key)  # Нажатие клавиши
            else:  # Если нужно отпустить клавишу
                release(key)  # Отпускание клавиши

        elif Y[2] == 0 and Y[3] == 0:  # Если действие только мышкой
            click(Y[0], Y[1])  # Клик мышкой в определенной позиции

        else:  # Если действие одновременно с клавиатурой и мышкой
            click(Y[0], Y[1])  # Клик мышкой
            key = get_key(Y[3])  # Получение кода клавиши из предсказания
            if Y[2] == 1:  # Если нужно нажать клавишу
                press(key)  # Нажатие клавиши
            else:  # Если нужно отпустить клавишу
                release(key)  # Отпускание клавиши

# Запуск программы
if __name__ == '__main__':
    main()
