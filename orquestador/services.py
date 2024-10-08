import httpx

# URLs de los microservicios
MS2_URL_EMPRESAS = 'http://microservicio2:8080/empresas'
MS2_URL_EMPLEOS = 'http://microservicio2:8080/empleos'  
MS2_URL_PAGOS = 'http://microservicio2:8080/pagos'
MS3_URL_ALOJAMIENTOS = 'http://mongodb:8080/alojamientos'  


async def get_empresas():
    async with httpx.AsyncClient() as client:
        response = await client.get(MS2_URL_EMPRESAS)
        if response.status_code != 200:
            raise Exception("Error al obtener empresas desde MS2")
        return response.json()


async def get_empleos():
    async with httpx.AsyncClient() as client:
        response = await client.get(MS2_URL_EMPLEOS)
        if response.status_code != 200:
            raise Exception("Error al obtener empleos desde MS2")
        return response.json()


async def get_pagos():
    async with httpx.AsyncClient() as client:
        response = await client.get(MS2_URL_PAGOS)
        if response.status_code != 200:
            raise Exception("Error al obtener pagos desde MS2")
        return response.json()


async def get_alojamientos():
    async with httpx.AsyncClient() as client:
        response = await client.get(MS3_URL_ALOJAMIENTOS)
        if response.status_code != 200:
            raise Exception("Error al obtener alojamientos desde MS3")
        return response.json()
