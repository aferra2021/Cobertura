from apps.ServiciosDing.Servicios import SendTransfer
from apps.Usuarios.models import TranferenciaGeneral,Contacto

def recargasNauta(nauta):
    json = {'SkuCode': 'CU_NU_TopUp', 'SendValue': '', 'SendCurrencyIso': 'USD', 'AccountNumber': '',
            'DistributorRef': '', 'Settings': '', 'ValidateOnly': 'True'}
    jsonNauta = []
    c=0
    for trans in nauta:
        #la cobro y despues la realizo una por una
        SendValue = trans.SendValue
        AccountNumber = trans.accountNumber
        contacto = trans.contacto
        TransGeneral = TranferenciaGeneral(tipo=trans.tipo, Descripcion=trans.Descripcion, fecha=trans.fecha,cliente=trans.cliente, SendValue=trans.SendValue, contacto=contacto)
        TransGeneral.save()
        json['SendValue'] = SendValue
        json['AccountNumber'] = AccountNumber
        json['DistributorRef'] = TransGeneral.id
        respons=SendTransfer(json,0)
        #id=respons['TransferRecord']['TransferId']#['TransferRef'] esto es para cuando la cuenta tiene dinero
        #TransGeneral(TransferRef=id)
        if respons['ResultCode']==5:# en realidad debe ser 2 no 5
            TransGeneral.save()
        # id=respons['TransferRecord']['TransferId']#['TransferRef'] esto es para cuando la cuenta tiene dinero
        # TransGeneral(TransferRef=id)
            jsonNauta.append(respons)
            trans.delete()
        else:
            return respons
        c=c+1
    return jsonNauta
