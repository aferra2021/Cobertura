from apps.ServiciosDing.Servicios import SendTransfer
import random
def recargasNauta(nauta):
    json = {'SkuCode': 'EL ESKUDCODE DE NAUTA', 'SendValue': '', 'SendCurrencyIso': 'USD', 'AccountNumber': '',
            'DistributorRef': '', 'Settings': '', 'ValidateOnly': 'True'}
    jsonCubacel = []
    for trans in nauta:
        SendValue = trans.SendValue
        AccountNumber = trans.accountNumber
        json['SendValue'] = SendValue
        json['AccountNumber'] = AccountNumber
        json['DistributorRef'] = random
        jsonCubacel.append(SendTransfer(json))
    return jsonCubacel
