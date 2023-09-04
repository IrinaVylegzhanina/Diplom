import requests
import configuration
import data


def post_create_order():
    return requests.post(
        configuration.URL_SERVICE + configuration.CREATE_ORDER_PATH,
        json={
            "firstName": "Лев",
            "lastName": "Левицкий",
            "address": "Лесная, 1",
            "metroStation": 15,
            "phone": "+7 800 555 35 35",
            "rentTime": 8,
            "deliveryDate": "2023-09-10",
            "comment": "Держатель для гривы",
            "color": [
                "BLACK"
            ]
        },
        headers=data.headers
    )


def get_order_by_number(track):
    return requests.get(configuration.URL_SERVICE + configuration.GET_ORDER_BY_NUMBER_PATH,
                        params={"t": track}
                        )


#print(post_create_order().json())


response = post_create_order()
track = response.json()["track"]

response = get_order_by_number(track)

print(response.status_code)

