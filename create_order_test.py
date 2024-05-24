# Алла Сафонова, 16-я когорта, Финальный проект, Инженер по тестированию плюс

# Импортируем модуль sender_stand_request, содержащий функции для отправки HTTP-запросов к API.
import stand_requests

# Импортируем модуль data, в котором определены данные, необходимые для HTTP-запросов.
import data

#######################################
# функция создания нового заказа и возвращения его трека
def get_order_track():
    # В переменную order_response сохраняется результат запроса на создание заказа с телом из файла data.py:
    order_response = stand_requests.post_new_order(data.order_body)

    # Проверяется, что код ответа равен 201
    assert order_response.status_code == 201
    # Проверяется, что в ответе есть поле track и оно не пустое
    order_track = order_response.json()["track"]
    assert order_track != ""
    # возвращаем номер трека
    return order_track


def positive_assert():
    # в переменную order_track сохраняется номер трека созданного заказа
    order_track = get_order_track()
    # в переменную order_response сохраняется ответ на запрос заказа по его номеру
    order_response = stand_requests.get_order_by_track(order_track)
    print(order_response)

    # проверяется, что код ответа равен 200
    assert order_response.status_code == 200


########################################
def test_success_create_order():
    positive_assert()
