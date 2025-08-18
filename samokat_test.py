import requests
import configuration
import data

def test_create_and_check_order():
    response = requests.post(configuration.URL_SERVICE + configuration.CREATE_ORDER, json=data.order_body)
    track = response.json()["track"]
    order_response = requests.get(configuration.URL_SERVICE + configuration.GET_ORDER + "?t=" + str(track))
    assert order_response.status_code == 200    
