# -*- coding: utf-8 -*-

# Данные для создания заказа
order_body = {
    "firstName": "Сергей",           # Только русские буквы, длина 2-15
    "lastName": "Егоров",            # Только русские буквы, длина 2-15
    "address": "Москва, ул. Ленина, 10, кв. 5",  # Русские буквы, цифры, точка, запятая
    "metroStation": 4,               # ID станции метро (число)
    "phone": "+79001234567",         # Цифры и знак "+", 12 символов
    "rentTime": 5,                   # Число от 1 до 7
    "deliveryDate": "2026-08-20",    # Дата в формате YYYY-MM-DD
    "comment": "Доставить до подъезда",  # Русские буквы, длина до 24
    "color": [
        "BLACK"                       # Чёрный жемчуг
    ]
}

# Альтернативные данные для тестов (без указания цвета)
order_body_without_color = {
    "firstName": "Сергей",
    "lastName": "Егоров",
    "address": "Москва, ул. Ленина, 10, кв. 5",
    "metroStation": 4,
    "phone": "+79001234567",
    "rentTime": 5,
    "deliveryDate": "2026-08-20",
    "comment": "Доставить до подъезда"
}

# Минимальный набор данных
order_body_minimal = {
    "firstName": "Сергей",
    "lastName": "Егоров",
    "address": "Москва, ул. Ленина, 10",
    "metroStation": 2,
    "phone": "+79001234567",
    "rentTime": 3,
    "deliveryDate": "2026-08-21"
}

# С обоими цветами
order_body_both_colors = {
    "firstName": "Сергей",
    "lastName": "Егоров",
    "address": "Москва, ул. Ленина, 10, кв. 5",
    "metroStation": 4,
    "phone": "+79001234567",
    "rentTime": 5,
    "deliveryDate": "2026-08-20",
    "comment": "Доставить до подъезда",
    "color": ["BLACK", "GREY"]    # Чёрный жемчуг + серая безысходность
}

# С другим адресом и телефоном (для разных тестов)
order_body_alternative = {
    "firstName": "Сергей",
    "lastName": "Егоров",
    "address": "Санкт-Петербург, Невский пр., 20",
    "metroStation": 10,
    "phone": "+79876543210",
    "rentTime": 7,
    "deliveryDate": "2026-08-22",
    "comment": "Позвонить за час",
    "color": ["GREY"]
}