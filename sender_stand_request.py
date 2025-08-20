import requests
import configuration


def create_order(order_body):
    return requests.post(
        configuration.URL_SERVICE + configuration.CREATE_ORDER,
        json=order_body
    )


def get_order(track_number):
    return requests.get(
        configuration.URL_SERVICE +
        configuration.GET_ORDER + "?t=" + str(track_number)
    )
