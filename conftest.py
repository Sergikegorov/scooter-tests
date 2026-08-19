import pytest
import requests
import sender_stand_request
import data

@pytest.fixture
def created_order_track():
    """Фикстура: создает заказ и возвращает его трек-номер"""
    response = sender_stand_request.create_order(data.order_body)
    assert response.status_code == 201
    track_number = sender_stand_request.get_track_from_response(response)
    return track_number

@pytest.fixture
def created_order_data(created_order_track):
    """Фикстура: возвращает данные заказа по трек-номеру"""
    response = sender_stand_request.get_order_by_track(created_order_track)
    assert response.status_code == 200
    return response.json()