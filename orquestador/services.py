import requests

# URLs de los microservicios (ajusta según sea necesario)
MICROSERVICE_1_URL = 'http://microservice1:8081/api/estudiantes'
MICROSERVICE_2_URL = 'http://microservice2:8082/api/empleos'
MICROSERVICE_3_URL = 'http://microservice3:8083/api/empresas'

def call_microservices():
    # Hacer llamadas a los microservicios
    response1 = requests.get(MICROSERVICE_1_URL)
    data1 = response1.json()

    response2 = requests.get(MICROSERVICE_2_URL)
    data2 = response2.json()

    response3 = requests.get(MICROSERVICE_3_URL)
    data3 = response3.json()

    # Combinar las respuestas de los microservicios
    combined_response = {
        'estudiantes': data1,
        'empleos': data2,
        'pagos': data3
    }

    return combined_response
