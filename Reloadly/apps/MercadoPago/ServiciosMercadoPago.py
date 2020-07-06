import requests



def CrearCliente():
    url = "https://api.mercadopago.com/v1/customers?access_token=TEST-3968442574725364-052821-0a162b8a21c4dbd43f48933d227339ce-468607165"
    payload = {
        "email": "bruno@gmail.com",
        "first_name": "Bruce",
        "last_name": "Wayne",
        "phone": {
            "area_code": "023",
            "number": "12345678"
        },
        "identification": {
            "type": "DNI",
            "number": "12345678"
        },
        "address": {
            "zip_code": "SG1 2AX",
            "street_name": "Old Knebworth Ln"
        },
        "description": "Lorem Ipsum"
    }
    headers = {}
    response = requests.request("POST", url, headers=headers, json=payload)
    #creo el modelo de clienteMercadoPago

    print(response.text.encode('utf8'))


def ObtenerCliente():
#'https://api.mercadopago.com/v1/customers/000000001-sT93QZFAsfxU9P5?access_token=ACCESS_TOKEN_ENV'
    id='604240754-gVHd0nFtLL4vH7'
    url = "https://api.mercadopago.com/v1/customers/" +id+ "?access_token=TEST-3968442574725364-052821-0a162b8a21c4dbd43f48933d227339ce-468607165"
    headers = {}
    response = requests.request("GET", url, headers=headers)
    print(response.text.encode('utf8'))
    return response


