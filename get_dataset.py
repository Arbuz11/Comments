# Arda Mavi
# Импорт необходимых библиотек
import os
import numpy as np
from keras.utils import to_categorical
from scipy.misc import imread, imresize, imsave
from sklearn.model_selection import train_test_split

def get_img(data_path):
    #Получает массив изображения из заданного пути.
    img = imread(data_path)
    img = imresize(img, (150, 150, 3))  # Изменение размера изображения до 150x150 пикселей с 3 цветными каналами
    return img

def save_img(img, path):
    #Сохраняет изображение по указанному пути.
    imsave(path, img)
    return

def get_dataset(dataset_path='Data/Train_Data'):
    #Получает набор данных из заданной директории.
    try:
        # Попытка загрузить заранее сохраненные данные
        X = np.load('Data/npy_train_data/X.npy')  # Загружает массив изображений
        Y = np.load('Data/npy_train_data/Y.npy')  # Загружает массив меток
    except:
        # Если файлы не найдены, собираем данные из директории
        labels = os.listdir(dataset_path)
        X = []  # Список для хранения изображений
        Y = []  # Список для хранения меток
        count_categori = [-1, '']  # Для кодирования меток
        for label in labels:
            datas_path = dataset_path + '/' + label  # Путь к категории данных
            for data in os.listdir(datas_path):  # Проход по всем данным в категории
                img = get_img(datas_path + '/' + data)  # Получаем изображение
                X.append(img)  # Добавляем изображение в список
                # Кодирование меток
                if data != count_categori[1]:  # Если метка новая
                    count_categori[0] += 1  # Увеличиваем счетчик категорий
                    count_categori[1] = data.split(',')  # Обновляем метку
                Y.append(count_categori[0])  # Добавляем кодированную метку
        # Создание окончательного набора данных
        X = np.array(X).astype('float32') / 255.  # Нормализация изображений
        Y = np.array(Y).astype('float32')  # Приведение меток к типу float32
        Y = to_categorical(Y, count_categori[0] + 1)  # Преобразование меток в категориальный формат
        # Создание директории для сохранения numpy файлов, если она не существует
        if not os.path.exists('Data/npy_train_data/'):
            os.makedirs('Data/npy_train_data/')
        np.save('Data/npy_train_data/X.npy', X)  # Сохранение массива изображений
        np.save('Data/npy_train_data/Y.npy', Y)  # Сохранение массива меток
    # Разделение данных на обучающую и тестовую выборки
    X, X_test, Y, Y_test = train_test_split(X, Y, test_size=0.1, random_state=42)  # 10% на тестовую выборку
    return X, X_test, Y, Y_test  # Возвращает обучающие и тестовые выборки
