#aki se realizaran todas las llamadas a la api
import requests
from requests.exceptions import ConnectionError
from django.http import HttpResponse,Http404
from django.shortcuts import render
#en este archivo estan los metodos de ding es decir de las distintas aplicaciones se llaman los metodos de aki
def SendTransfer(json):
	urlTest="https://api.dingconnect.com/api/V1/SendTransfer"
	headers={'api_key':'K9CHHAmuNEH6MR6XhcPhX8','Cache-Control':'no-cache','Content-Type':'application/json'}
	session = requests.session()
	try:
		responseTest=session.post(urlTest,headers=headers,json=json)
		results = responseTest.json()
		return results
	except ConnectionError as e:
		return e

"""
def SendTransfer2(json):
    url='http://api.dingconnect.com/api/V1/SendTransfer'
    headers={'api_key':'K9CHHAmuNEH6MR6XhcPhX8','Cache-Control':'no-cache','Content-Type':'applications/json'}

    try:
        session=requests.session()
        response=requests.post(url,headers=headers,json={'SkuCode':'3CCUCU80037','SendValue':'20.0','SendCurrencyIso':'USD','AccountNumber':'5354393413','DistributorRef':'1','ValidateOnly':'true'})
        result=response.json()
        print(result)
        return result
    except ConnectionError as e:
        return result

#aki va el metodo q se encarga de crear el json
def CarritoJson():
    carrito={
        'compras':[
        #cada elemento de la lista compra sera un diciionario de tipo compra
        ]
    }
    compra={
        'tipo':'',
        'accountNumber':'',
        'sendValue':''
    }
    json={
        'carrito':carrito,
        'compra':compra
    }
    return json

"""

"""    SkuCode='3CCUCU80037'
    SendValue='20.0'
    SendCurrencyIso='USD'
    AccountNumber='54393413'
    DistributorRef='1'
    Name='Test'
    Value='20.0'
    Settings=[{'Name':Name,'Value':Value}]
    ValidateOnly='true'
    parametros={'SkuCode':SkuCode,'SendValue':SendValue,'SendCurrencyIso':SendCurrencyIso,'AccountNumber':AccountNumber,
                'DistributorRef':DistributorRef,'Settings':Settings,'ValidateOnly':ValidateOnly}"""
