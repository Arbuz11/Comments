# Arda Mavi
# Импорт необходимых библиотек и файлов
import os
import numpy
from get_dataset import get_dataset
from get_model import get_model, save_model
from keras.callbacks import ModelCheckpoint, TensorBoard

# Определение гиперпараметров обучения
epochs = 100 # Количество эпох для обучения модели
batch_size = 5 # Размер батча для обучения

# Обучает модель на заданном наборе данных
# model: Обучаемая модель Keras
# X: Обучающий набор данных (входные признаки)
# X_test: Тестовый набор данных (входные признаки)
# Y: Обучающие метки (выходные классы)
# Y_test: Тестовые метки (выходные классы)
def train_model(model, X, X_test, Y, Y_test):
    checkpoints = [] # Список для хранения колбеков

    # Проверка существования директории для чекпоинтов; если нет, создание директории
    if not os.path.exists('Data/Checkpoints/'):
        os.makedirs('Data/Checkpoints/')

    # Добавление чекпоинта для сохранения лучших весов модели на основе валидационной потери
    checkpoints.append(ModelCheckpoint('Data/Checkpoints/best_weights.h5', monitor='val_loss', verbose=0, save_best_only=True, save_weights_only=True, mode='auto', period=1))
    # Добавление колбека TensorBoard для визуализации процесса обучения
    checkpoints.append(TensorBoard(log_dir='Data/Checkpoints/./logs', histogram_freq=0, write_graph=True, write_images=False, embeddings_freq=0, embeddings_layer_names=None, embeddings_metadata=None))

    # Обучение модели с использованием заданных данных, батча, количества эпох и колбеков
    model.fit(X, Y, batch_size=batch_size, epochs=epochs, validation_data=(X_test, Y_test), shuffle=True, callbacks=checkpoints)

    # Возвращает обученную модель
    return model

# Главная функция, которая управляет процессом обучения
def main():
    # Получение тренировочного и тестового наборов данных
    X, X_test, Y, Y_test = get_dataset()
    # Получение модели для обучения
    model = get_model()
    # Обучение модели и получение обученной модели
    model = train_model(model, X, X_test, Y, Y_test)
    # Сохранение обученной модели на диск
    save_model(model)
    # Возвращает обученную модель
    return model

# Запуск программы
if __name__ == '__main__':
    main()
