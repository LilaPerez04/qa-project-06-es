import sender_stand_request
import data
# import pytest
# import json


def positive_assert(kit_body):
    # El cuerpo de la solicitud actualizada se guarda en la variable kit
    kit = sender_stand_request.post_new_client_kit(kit_body)
    # Comprueba si el código de estado es 201
    assert kit.status_code == 201
    # Necesitas otro assert para comprobar que el name que se esté guardando sea el mismo que mandas
    assert kit.json()["name"] == kit_body["name"]


def negative_assert(kit_body):
    # El cuerpo de la solicitud actualizada se guarda en la variable user_body
    kit = sender_stand_request.post_new_client_kit(kit_body)
    # Comprueba si el código de estado es 201
    assert kit.status_code == 400


# Comprueba el número mínimo de caracteres permitidos: 1
def test_min_character():
    kit_body = data.kit_body.kit_body1
    positive_assert(kit_body)


# Comprueba el número máximo de caracteres permitidos: 511
def test_max_character():
    kit_body = data.kit_body.kit_body2
    positive_assert(kit_body)


# Comprueba el número por debajo de los caracteres permitidos: 0
def test_zero_character():
    kit_body = data.kit_body.kit_body3
    negative_assert(kit_body)


# Comprueba el número por encima de los caracteres permitidos: 512
def test_over_character():
    kit_body = data.kit_body.kit_body4
    negative_assert(kit_body)


# Comprueba los caracteres especiales
def test_special_character():
    kit_body = data.kit_body.kit_body5
    positive_assert(kit_body)


# Comprueba los espacios entre caracteres
def test_space_between_character():
    kit_body = data.kit_body.kit_body6
    positive_assert(kit_body)


# Comprueba los números entre caracteres
def test_numbers():
    kit_body = data.kit_body.kit_body7
    positive_assert(kit_body)


# Comprueba cuando el parámetro no se pasa en la solicitud
def test_no_parameters():
    kit_body = data.kit_body.kit_body8
    negative_assert(kit_body)


# Comprueba cuando se pasa un tipo diferente de parámetro en la solicitud
def test_different_kind_of_character():
    kit_body = data.kit_body.kit_body9
    negative_assert(kit_body)
