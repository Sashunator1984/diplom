# Александр Кудинов, 33 qa-plus. Финальный проект

import sender_stand_request
import data


def test_create_and_check_order():
    response = sender_stand_request.create_order(data.order_body)
    track = response.json()["track"]
    order_response = sender_stand_request.get_order(track)
    assert order_response.status_code == 200
