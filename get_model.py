# Arda Mavi
# Импорт необходимых библиотек для создания и сохранения модели
import os
from keras.models import Model
from keras.optimizers import Adadelta
from keras.layers import Input, Conv2D, Activation, MaxPooling2D, Flatten, Dense, Dropout

def save_model(model):
    #Сохраняет модель и её веса в файлы.
    # Проверяем, существует ли директория для сохранения модели, если нет - создаем
    if not os.path.exists('Data/Model/'):
        os.makedirs('Data/Model/')
    
    # Сериализация структуры модели в формат JSON
    model_json = model.to_json()
    # Сохранение структуры модели в файл
    with open("Data/Model/model.json", "w") as model_file:
        model_file.write(model_json)

    # Сериализация весов модели в файл формата HDF5
    model.save_weights("Data/Model/weights.h5")
    print('Model and weights saved')
    return

def get_model():
    #Создает и компилирует нейронную сеть для обработки изображений.
    # Определение входного слоя с заданной формой изображений
    inputs = Input(shape=(150, 150, 3))

    # Первый свёрточный слой
    conv_1 = Conv2D(32, (3, 3), strides=(1, 1))(inputs)  # Применяет 32 фильтра размером 3x3
    act_1 = Activation('relu')(conv_1)  # Функция активации ReLU

    # Второй свёрточный слой
    conv_2 = Conv2D(64, (3, 3), strides=(1, 1))(act_1)  # Применяет 64 фильтра размером 3x3
    act_2 = Activation('relu')(conv_2)  # Функция активации ReLU

    # Третий свёрточный слой
    conv_3 = Conv2D(64, (3, 3), strides=(1, 1))(act_2)  # Применяет 64 фильтра размером 3x3
    act_3 = Activation('relu')(conv_3)  # Функция активации ReLU

    # Первый слой подвыборки (максимальная подвыборка)
    pooling_1 = MaxPooling2D(pool_size=(2, 2), strides=(2, 2))(act_3)  # Снижает размеры изображения вдвое

    # Четвёртый свёрточный слой
    conv_4 = Conv2D(128, (3, 3), strides=(1, 1))(pooling_1)  # Применяет 128 фильтров размером 3x3
    act_4 = Activation('relu')(conv_4)  # Функция активации ReLU

    # Второй слой подвыборки
    pooling_2 = MaxPooling2D(pool_size=(2, 2), strides=(2, 2))(act_4)  # Снижает размеры изображения вдвое

    # Преобразование многомерного массива в одномерный
    flat_1 = Flatten()(pooling_2)  # Сплющивание выходов предыдущего слоя

    # Полносвязный слой
    fc = Dense(1280)(flat_1)  # Вход в полносвязный слой с 1280 нейронами
    fc = Activation('relu')(fc)  # Функция активации ReLU
    fc = Dropout(0.5)(fc)  # Удаление 50% нейронов для предотвращения переобучения
    fc = Dense(4)(fc)  # Полносвязный слой с 4 нейронами для классификации на 4 категории

    # Выходной слой с сигмоидной активацией
    outputs = Activation('sigmoid')(fc)  # Функция активации для многоклассовой классификации

    # Создание модели с заданными входами и выходами
    model = Model(inputs=inputs, outputs=outputs)

    # Компиляция модели с выбором функции потерь и оптимизатора
    model.compile(loss='categorical_crossentropy', optimizer='adadelta', metrics=['accuracy'])

    return model  # Возвращает созданную и скомпилированную модель

# Запуск программы
if __name__ == '__main__':
    save_model(get_model())
