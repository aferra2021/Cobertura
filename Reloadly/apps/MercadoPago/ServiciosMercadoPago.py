import requests
from .models import ClienteMercadoPago

def CrearClienteAPI():
    url = "https://api.mercadopago.com/v1/customers?access_token=TEST-3968442574725364-052821-0a162b8a21c4dbd43f48933d227339ce-468607165"
    headers = {}
    payload = {
        "email": "bsqqrqqwqwwssqqworqedw@gmail.com",
        "first_name": "Bwqqqqqswqsqsrrudweqce",
        "last_name": "Wwawqqqqqssqsyqrwedsqe",
        "phone": {
            "area_code": "023",
            "number": "12129195"
        },
        "identification": {
            "type": "DNI",
            "number": "11141050"
        },
        "address": {
            "zip_code": "SG1 2AX",
            "street_name": "Old Knebworth Ln"
        },
        "description": "Lorem Ipsum"
    }
    response = requests.request("POST", url, headers=headers, json=payload)
    #creo el modelo de clienteMercadoPago
    response_json = response.json()
    return response_json

#payload
"""
payload = {
        "email": "bsqrqwwwoq@gmail.com",
        "first_name": "Bqwqsruqce",
        "last_name": "Wawqsyqsqe",
        "phone": {
            "area_code": "023",
            "number": "12025198"
        },
        "identification": {
            "type": "DNI",
            "number": "12041190"
        },
        "address": {
            "zip_code": "SG1 2AX",
            "street_name": "Old Knebworth Ln"
        },
        "description": "Lorem Ipsum"
    }"""

def ObtenerCliente(id):
#'https://api.mercadopago.com/v1/customers/000000001-sT93QZFAsfxU9P5?access_token=ACCESS_TOKEN_ENV'
    id='604240754-gVHd0nFtLL4vH7'
    url = "https://api.mercadopago.com/v1/customers/" +id+ "?access_token=TEST-3968442574725364-052821-0a162b8a21c4dbd43f48933d227339ce-468607165"
    headers = {}
    response = requests.request("GET", url, headers=headers)
    print(response.text.encode('utf8'))
    return response


