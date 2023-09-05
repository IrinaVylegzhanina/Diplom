# Ирина Вылегжанина, 8-я когорта — Финальный проект. Инженер по тестированию плюс


from sender_stand_request import post_create_order, get_order_by_number


def test_create_order_and_get_track():
    response = post_create_order()
    track = response.json()["track"]
    response = get_order_by_number(track)
    assert(response.status_code == 200)
