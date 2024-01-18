import requests
import configuration
import data
# import json


def post_new_user(body):
    headers = {
        "Content-Type": "application/json"
    }
    # inserta la dirección URL completa
    response = requests.post(configuration.URL_SERVICE + configuration.CREATE_USER_PATH,
                             json=body,  # inserta el cuerpo de solicitud
                             headers=headers)  # inserta los encabezados
    response_token = response.json()["authToken"]  # guarda el token de autenticación en una variable
    return response_token


# auth_token = post_new_user(data.user_body)
# print(auth_token)


def post_new_client_kit(body):
    # insert the full URL
    token = post_new_user(data.user_body)
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {token}"
    }
    response_kit = requests.post(configuration.URL_SERVICE + configuration.KITS_PATH,
                                 json=body,
                                 headers=headers)  # insert the headers
#    kit_response = response_kit.json()["name"]
    return response_kit


# response, new_kit = post_new_kit(data.kit_bd)
# print(new_kit)
