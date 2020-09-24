#aki se construyen los servicios de q tienen q ver con las recargas a cubacel
from apps.ServiciosDing.Servicios import SendTransfer
from apps.Usuarios.models import TranferenciaGeneral,Contacto
from django.shortcuts import render,redirect
from django.http import HttpResponse


#aki trabajo las excepciones y trabajo con el json devuelto
def recargaCubacel(cubacel):
    json={'SkuCode':'3CCUCU80037','SendValue':'','SendCurrencyIso':'USD','AccountNumber':'',
          'DistributorRef':'','Settings':'','ValidateOnly':'True'}
    jsonCubacel=[]
    for trans in cubacel:
        for c in range(trans.cant):
            # la cobro y despues la realizo una por una
            SendValue=int(trans.SendValue)/trans.cant
            AccountNumber=trans.accountNumber
            contacto =trans.contacto
            TransGeneral = TranferenciaGeneral(tipo=trans.tipo, Descripcion=trans.Descripcion, fecha=trans.fecha,cliente=trans.cliente, SendValue=SendValue, contacto=contacto)
            TransGeneral.save()
            json['SendValue']=SendValue
            json['AccountNumber']=AccountNumber
            json['DistributorRef']=TransGeneral.id
            respons=SendTransfer(json,0)
            if respons['ResultCode'] == 5:  # en realidad debe ser 2 no 5
                TransGeneral.save()
            #id=respons['TransferRecord']['TransferId']#['TransferRef'] esto es para cuando la cuenta tiene dinero
            #TransGeneral(TransferRef=id)
                jsonCubacel.append(respons)
                trans.delete()
                #aki hacer el pago de esta y asi sucesivamente
            else:
                return respons
    return jsonCubacel

def PaquetesDatosCubacel(paquetes):
    jsonPaquetes=[]
    jsonTo600MB = {'SkuCode': '1HCUCU4205', 'SendValue': '7', 'SendCurrencyIso': 'USD', 'AccountNumber': '',
                   'DistributorRef': '', 'Settings': '', 'ValidateOnly': 'True'}
    jsonTo600MBLTE = {'SkuCode': '1HCUCU8082', 'SendValue': '7', 'SendCurrencyIso': 'USD', 'AccountNumber': '',
            'DistributorRef': '', 'Settings': '', 'ValidateOnly': 'True'}
    jsonTo1GB = {'SkuCode': '1HCUCU68614', 'SendValue': '10', 'SendCurrencyIso': 'USD', 'AccountNumber': '',
            'DistributorRef': '', 'Settings': '', 'ValidateOnly': 'True'}
    jsonTo1GBLTE = {'SkuCode': '1HCUCU53855', 'SendValue': '10', 'SendCurrencyIso': 'USD', 'AccountNumber': '',
            'DistributorRef': '', 'Settings': '', 'ValidateOnly': 'True'}
    jsonTo25GB = {'SkuCode': '1HCUCU26597', 'SendValue': '20', 'SendCurrencyIso': 'USD', 'AccountNumber': '',
            'DistributorRef': '', 'Settings': '', 'ValidateOnly': 'True'}
    jsonTo4GB = {'SkuCode': '1HCUCU52016', 'SendValue': '30', 'SendCurrencyIso': 'USD', 'AccountNumber': '',
            'DistributorRef': '', 'Settings': '', 'ValidateOnly': 'True'}
    for trans in paquetes:
        SendValue=0
        if trans.cant==1:
            # la cobro y despues la realizo una por una
            jsonTo600MB['AccountNumber'] = trans.accountNumber
            jsonTo600MB['DistributorRef'] = trans.id
            SendValue=jsonTo600MB['SendValue']
            respons = SendTransfer(jsonTo600MB,0)
            jsonPaquetes.append(respons)
        elif trans.cant==2:
            jsonTo600MBLTE['AccountNumber'] = trans.accountNumber
            jsonTo600MBLTE['DistributorRef'] = trans.id
            SendValue=jsonTo600MBLTE['SendValue']
            respons = SendTransfer(jsonTo600MBLTE,0)
            jsonPaquetes.append(respons)
        elif trans.cant==3:
            jsonTo1GB['AccountNumber'] = trans.accountNumber
            jsonTo1GB['DistributorRef'] = trans.id
            SendValue=jsonTo1GB['SendValue']
            respons = SendTransfer(jsonTo1GB,0)
            jsonPaquetes.append(respons)
        elif trans.cant==4:
            jsonTo1GBLTE['AccountNumber'] = trans.accountNumber
            jsonTo1GBLTE['DistributorRef'] = trans.id
            SendValue=jsonTo1GBLTE['SendValue']
            respons = SendTransfer(jsonTo1GBLTE,0)
            jsonPaquetes.append(respons)
        elif trans.cant==5:
            jsonTo25GB['AccountNumber'] = trans.accountNumber
            jsonTo25GB['DistributorRef'] = trans.id
            SendValue=jsonTo25GB['SendValue']
            respons = SendTransfer(jsonTo25GB,0)
            jsonPaquetes.append(respons)
        elif trans.cant==6:
            jsonTo4GB['AccountNumber'] = trans.accountNumber
            jsonTo4GB['DistributorRef'] = trans.id
            SendValue=jsonTo4GB['SendValue']
            respons = SendTransfer(jsonTo4GB,0)
            jsonPaquetes.append(respons)
        if respons!='error':
            contacto =trans.contacto
            TransGeneral = TranferenciaGeneral(tipo=trans.tipo, Descripcion=trans.Descripcion, fecha=trans.fecha,cliente=trans.cliente, SendValue=SendValue, contacto=contacto)
            TransGeneral.save()
            trans.delete()
            return jsonPaquetes
        else:
            return respons
