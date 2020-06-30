#aki se construyen los servicios de q tienen q ver con las recargas a cubacel
from apps.ServiciosDing.Servicios import SendTransfer
from django.shortcuts import render,redirect
from django.http import HttpResponse


#aki trabajo las excepciones y trabajo con el json devuelto
def recargaCubacel(cubacel):
    json={'SkuCode':'3CCUCU80037','SendValue':'','SendCurrencyIso':'USD','AccountNumber':'','DistributorRef':'','Settings':'','ValidateOnly':'True'}
    jsonCubacel=[]
    for trans in cubacel:
        SendValue=trans.SendValue
        AccountNumber=trans.accountNumber
        json['SendValue']=SendValue
        json['AccountNumber']=AccountNumber
        json['DistributorRef']=trans.id
        jsonCubacel.append(SendTransfer(json))
    return jsonCubacel


