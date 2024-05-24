# заголовки для HTTP-запроса, указывающие на то, что тело запроса будет в формате JSON
headers = {
    "Content-Type": "application/json"
}

# данные для создания заказа
order_body = {
    "firstName": "Кролик",
    "lastName": "Белый",
    "address": "Нора",
    "metroStation": 1,
    "phone": "+7 999 100 11 22",
    "rentTime": 5,
    "deliveryDate": "2024-05-31",
    "comment": "Свободу передвижения кролям!",
    "color": [
        "GREY"
    ]
}
