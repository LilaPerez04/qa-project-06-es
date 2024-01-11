import sender_stand_request
import data
import pytest
# import json


def positive_assert(kit_body):
    # El cuerpo de la solicitud actualizada se guarda en la variable user_body
    kit = sender_stand_request.post_new_client_kit(kit_body)
    # Comprueba si el código de estado es 201
    assert kit.status_code == 201
    # Necesitas otro assert para comprobar que el name que se esté guardando sea el mismo que mandas
    assert kit.json()["name"] == kit_body["name"]


def test1():
    kit_body = data.kit_body.kit_body1
    positive_assert(kit_body)


def test2():
    kit_body = data.kit_body.kit_body2
    positive_assert(kit_body)


def test5():
    kit_body = data.kit_body.kit_body5
    positive_assert(kit_body)


def test6():
    kit_body = data.kit_body.kit_body6
    positive_assert(kit_body)


def test7():
    kit_body = data.kit_body.kit_body7
    positive_assert(kit_body)


def negative_assert(kit_body):
    # El cuerpo de la solicitud actualizada se guarda en la variable user_body
    kit = sender_stand_request.post_new_client_kit(kit_body)
    # Comprueba si el código de estado es 201
    assert kit.status_code == 400
    # Necesitas otro assert para comprobar que el name que se esté guardando sea el mismo que mandas
    assert kit.json()["name"] == kit_body["name"]


def test3():
    kit_body = data.kit_body.kit_body3
    positive_assert(kit_body)


def test4():
    kit_body = data.kit_body.kit_body4
    positive_assert(kit_body)


def test8():
    kit_body = data.kit_body.kit_body8
    positive_assert(kit_body)


def test9():
    kit_body = data.kit_body.kit_body9
    positive_assert(kit_body)
