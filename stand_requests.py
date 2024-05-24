# Импортируем модуль requests, который предназначен для отправки HTTP-запросов
import requests
# Импортируем модуль configuration с настройками подключения и путями к документации
import configuration
# Импортируем модуль data с данными для подстановки в тест-кейсы
import data

#######################################
# функция для создания запроса
def post_new_order(body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_ORDER_PATH,
                         json=body,  # Тело запроса в формате JSON
                         headers=data.headers)  # Использование заголовков из файла data.py

# функция запроса на получение заказа по треку
def get_order_by_track(track):
    return requests.get(configuration.URL_SERVICE + configuration.GET_ORDER_BY_TRACK_PATH \
                        + "?t=" + str(track), # передаем в URL значение трека созданного заказа
                        headers=data.headers) # Использование заголовков из файла data.py
