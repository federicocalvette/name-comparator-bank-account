import requests
import settings


def make_request(nro_cbu, bk_code, country_code):

    url = settings.URL

    payload=f'nro_cbu={nro_cbu}&bk_code={bk_code}&country_code={country_code}'
    
    headers = {
    'x-api-key': settings.API_KEY,
    'Content-Type': 'application/x-www-form-urlencoded'
    }

    response = requests.request("POST", url, headers=headers, data=payload)

    if response.status_code == 200:
        response_json = response.json()
        name = response_json['data']['beneficiary_name']
        return name

    elif response.status_code == 404:
        message = "Cuenta credito invalida"
        return message

    elif response.status_code == 503:
        message = "Error de comunicacion con el banco"
        return message

    elif response.status_code == 400:
        message = "Parametros invalidos"
        return message

    else:
        return 'Error'
