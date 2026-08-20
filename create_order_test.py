# Егоров Сергей 46 когорта диплом автотесты самокат

import pytest
import sender_stand_request
import data

class TestCreateOrder:
    
    def test_create_order_and_get_by_track(self):
        """
        Тест-сценарий:
        1. Создать заказ с данными Сергея Егорова
        2. Сохранить номер трека заказа
        3. Выполнить запрос на получение заказа по треку
        4. Проверить, что код ответа равен 200
        """
        print("\n" + "="*60)
        print("ТЕСТ: Создание заказа и получение по трек-номеру")
        print("="*60)
        
        # ШАГ 1: Создание заказа
        print("\nШаг 1: Создание заказа...")
        create_response = sender_stand_request.create_order(data.order_body)
        
        # Проверяем, что заказ создан успешно (код 201)
        assert create_response.status_code == 201, \
            f"Ошибка: ожидался код 201, получен {create_response.status_code}"
        print(f"   Заказ создан, код ответа: {create_response.status_code}")
        
        # ШАГ 2: Сохранить номер трека заказа
        print("\nШаг 2: Сохранение трек-номера...")
        track_number = sender_stand_request.get_track_from_response(create_response)
        assert track_number is not None, "Трек-номер не найден в ответе"
        print(f"   Трек-номер сохранен: {track_number}")
        
        # ШАГ 3: Запрос на получение заказа по треку
        print("\nШаг 3: Получение заказа по трек-номеру...")
        get_response = sender_stand_request.get_order_by_track(track_number)
        
        # ШАГ 4: Проверка, что код ответа равен 200
        print("\nШаг 4: Проверка кода ответа...")
        assert get_response.status_code == 200, \
            f"Ошибка: ожидался код 200, получен {get_response.status_code}"
        print(f"   Код ответа: {get_response.status_code}")
        
        # ДОПОЛНИТЕЛЬНЫЕ ПРОВЕРКИ
        print("\nДополнительные проверки данных заказа:")
        
        order_data = get_response.json()
        
        # Проверяем структуру ответа
        assert "order" in order_data, "В ответе отсутствует поле 'order'"
        print("   Поле 'order' присутствует")
        
        # Проверяем, что трек-номер совпадает
        assert order_data["order"]["track"] == track_number, \
            f"Трек-номер не совпадает: ожидался {track_number}, получен {order_data['order']['track']}"
        print(f"   Трек-номер совпадает: {track_number}")
        
        # Проверяем, что данные заказа корректны
        assert order_data["order"]["firstName"] == "Сергей", \
            f"Имя не совпадает: ожидалось 'Сергей', получено '{order_data['order']['firstName']}'"
        print(f"   Имя: {order_data['order']['firstName']}")
        
        assert order_data["order"]["lastName"] == "Егоров", \
            f"Фамилия не совпадает: ожидалась 'Егоров', получена '{order_data['order']['lastName']}'"
        print(f"   Фамилия: {order_data['order']['lastName']}")
        
        assert order_data["order"]["address"] == "Москва, ул. Ленина, 10, кв. 5", \
            "Адрес не совпадает"
        print(f"   Адрес: {order_data['order']['address']}")
        
        # Проверяем телефон
        assert order_data["order"]["phone"] == "+79001234567", \
            f"Телефон не совпадает: ожидался '+79001234567', получен '{order_data['order']['phone']}'"
        print(f"   Телефон: {order_data['order']['phone']}")
        
        # Проверяем статус (0 - активный заказ)
        assert order_data["order"]["status"] == 0, \
            f"Статус заказа: ожидался 0 (активный), получен {order_data['order']['status']}"
        print(f"   Статус: {order_data['order']['status']} (активный)")
        
        # ИТОГОВЫЙ ВЫВОД
        print("\n" + "="*60)
        print("ТЕСТ УСПЕШНО ПРОЙДЕН")
        print("="*60)
        print("ИНФОРМАЦИЯ О ЗАКАЗЕ:")
        print(f"   - ID заказа: {order_data['order']['id']}")
        print(f"   - Клиент: {order_data['order']['firstName']} {order_data['order']['lastName']}")
        print(f"   - Адрес: {order_data['order']['address']}")
        print(f"   - Станция метро: {order_data['order']['metroStation']}")
        print(f"   - Телефон: {order_data['order']['phone']}")
        print(f"   - Срок аренды: {order_data['order']['rentTime']} дней")
        print(f"   - Дата доставки: {order_data['order']['deliveryDate']}")
        print(f"   - Трек-номер: {order_data['order']['track']}")
        print(f"   - Статус: {order_data['order']['status']} (активный)")
        print("="*60)
    
    def test_create_order_without_color(self):
        """Тест: создание заказа без указания цвета"""
        print("\n" + "="*60)
        print("ТЕСТ: Создание заказа без указания цвета")
        print("="*60)
        
        create_response = sender_stand_request.create_order(data.order_body_without_color)
        assert create_response.status_code == 201, \
            f"Ошибка: ожидался код 201, получен {create_response.status_code}"
        
        track_number = sender_stand_request.get_track_from_response(create_response)
        assert track_number is not None, "Трек-номер не найден в ответе"
        print(f"Заказ создан, трек-номер: {track_number}")
        
        get_response = sender_stand_request.get_order_by_track(track_number)
        assert get_response.status_code == 200, \
            f"Ошибка: ожидался код 200, получен {get_response.status_code}"
        
        order_data = get_response.json()
        assert "order" in order_data, "В ответе отсутствует поле 'order'"
        assert order_data["order"]["track"] == track_number, "Трек-номер не совпадает"
        
        print("Тест пройден: заказ создан без указания цвета")
        print("="*60)
    
    def test_create_order_minimal(self):
        """Тест: создание заказа с минимальными данными"""
        print("\n" + "="*60)
        print("ТЕСТ: Создание заказа с минимальными данными")
        print("="*60)
        
        create_response = sender_stand_request.create_order(data.order_body_minimal)
        assert create_response.status_code == 201, \
            f"Ошибка: ожидался код 201, получен {create_response.status_code}"
        
        track_number = sender_stand_request.get_track_from_response(create_response)
        assert track_number is not None, "Трек-номер не найден в ответе"
        print(f"Заказ создан, трек-номер: {track_number}")
        
        get_response = sender_stand_request.get_order_by_track(track_number)
        assert get_response.status_code == 200, \
            f"Ошибка: ожидался код 200, получен {get_response.status_code}"
        
        order_data = get_response.json()
        assert "order" in order_data, "В ответе отсутствует поле 'order'"
        assert order_data["order"]["track"] == track_number, "Трек-номер не совпадает"
        
        # Проверяем минимальные данные
        assert order_data["order"]["firstName"] == "Сергей", "Имя не совпадает"
        assert order_data["order"]["lastName"] == "Егоров", "Фамилия не совпадает"
        assert order_data["order"]["address"] == "Москва, ул. Ленина, 10", "Адрес не совпадает"
        
        print("Тест пройден: заказ создан с минимальными данными")
        print("="*60)
    
    def test_create_order_with_both_colors(self):
        """Тест: создание заказа с двумя цветами"""
        print("\n" + "="*60)
        print("ТЕСТ: Создание заказа с двумя цветами")
        print("="*60)
        
        create_response = sender_stand_request.create_order(data.order_body_both_colors)
        assert create_response.status_code == 201, \
            f"Ошибка: ожидался код 201, получен {create_response.status_code}"
        
        track_number = sender_stand_request.get_track_from_response(create_response)
        assert track_number is not None, "Трек-номер не найден в ответе"
        print(f"Заказ создан, трек-номер: {track_number}")
        
        get_response = sender_stand_request.get_order_by_track(track_number)
        assert get_response.status_code == 200, \
            f"Ошибка: ожидался код 200, получен {get_response.status_code}"
        
        order_data = get_response.json()
        assert "order" in order_data, "В ответе отсутствует поле 'order'"
        assert order_data["order"]["track"] == track_number, "Трек-номер не совпадает"
        assert order_data["order"]["color"] == ["BLACK", "GREY"], \
            f"Цвета не совпадают: ожидались ['BLACK', 'GREY'], получены {order_data['order']['color']}"
        
        print("Тест пройден: заказ создан с двумя цветами")
        print("="*60)
    
    def test_create_order_with_grey_color(self):
        """Тест: создание заказа с серым цветом"""
        print("\n" + "="*60)
        print("ТЕСТ: Создание заказа с серым цветом")
        print("="*60)
        
        test_data = data.order_body.copy()
        test_data["color"] = ["GREY"]
        
        create_response = sender_stand_request.create_order(test_data)
        assert create_response.status_code == 201, \
            f"Ошибка: ожидался код 201, получен {create_response.status_code}"
        
        track_number = sender_stand_request.get_track_from_response(create_response)
        assert track_number is not None, "Трек-номер не найден в ответе"
        print(f"Заказ создан, трек-номер: {track_number}")
        
        get_response = sender_stand_request.get_order_by_track(track_number)
        assert get_response.status_code == 200, \
            f"Ошибка: ожидался код 200, получен {get_response.status_code}"
        
        order_data = get_response.json()
        assert order_data["order"]["color"] == ["GREY"], \
            f"Цвет не совпадает: ожидался ['GREY'], получен {order_data['order']['color']}"
        
        print("Тест пройден: заказ создан с серым цветом")
        print("="*60)
    
    def test_create_order_with_long_comment(self):
        """Тест: создание заказа с длинным комментарием (максимум 24 символа)"""
        print("\n" + "="*60)
        print("ТЕСТ: Создание заказа с длинным комментарием")
        print("="*60)
        
        test_data = data.order_body.copy()
        test_data["comment"] = "Доставить строго до двери"
        
        create_response = sender_stand_request.create_order(test_data)
        assert create_response.status_code == 201, \
            f"Ошибка: ожидался код 201, получен {create_response.status_code}"
        
        track_number = sender_stand_request.get_track_from_response(create_response)
        assert track_number is not None, "Трек-номер не найден в ответе"
        print(f"Заказ создан, трек-номер: {track_number}")
        
        get_response = sender_stand_request.get_order_by_track(track_number)
        assert get_response.status_code == 200, \
            f"Ошибка: ожидался код 200, получен {get_response.status_code}"
        
        order_data = get_response.json()
        assert order_data["order"]["comment"] == "Доставить строго до двери", \
            f"Комментарий не совпадает: ожидался 'Доставить строго до двери', получен {order_data['order']['comment']}"
        
        print("Тест пройден: заказ создан с длинным комментарием")
        print("="*60)
    
    def test_create_order_different_rent_time(self):
        """Тест: создание заказа с разным сроком аренды (1 и 7 дней)"""
        print("\n" + "="*60)
        print("ТЕСТ: Создание заказа с разным сроком аренды")
        print("="*60)
        
        # Тест с минимальным сроком аренды (1 день)
        test_data = data.order_body.copy()
        test_data["rentTime"] = 1
        
        create_response = sender_stand_request.create_order(test_data)
        assert create_response.status_code == 201, \
            f"Ошибка: ожидался код 201, получен {create_response.status_code}"
        
        track_number = sender_stand_request.get_track_from_response(create_response)
        get_response = sender_stand_request.get_order_by_track(track_number)
        assert get_response.status_code == 200
        assert get_response.json()["order"]["rentTime"] == 1, "Срок аренды должен быть 1 день"
        print("   Срок аренды 1 день - успешно")
        
        # Тест с максимальным сроком аренды (7 дней)
        test_data = data.order_body.copy()
        test_data["rentTime"] = 7
        
        create_response = sender_stand_request.create_order(test_data)
        assert create_response.status_code == 201, \
            f"Ошибка: ожидался код 201, получен {create_response.status_code}"
        
        track_number = sender_stand_request.get_track_from_response(create_response)
        get_response = sender_stand_request.get_order_by_track(track_number)
        assert get_response.status_code == 200
        assert get_response.json()["order"]["rentTime"] == 7, "Срок аренды должен быть 7 дней"
        print("   Срок аренды 7 дней - успешно")
        
        print("Тест пройден: заказы созданы с разным сроком аренды")
        print("="*60)