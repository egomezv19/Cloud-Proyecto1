import httpx


MS1_URL_ESTUDIANTES = 'http://microservicio1:8080/estudiantes'
MS2_URL_EMPRESAS = 'http://microservicio2:8080/empresas'
MS2_URL_PROGRAMAS = 'http://microservicio2:8080/programas'
MS3_URL_PAGOS = 'http://microservicio3:8080/pagos'


async def get_estudiantes():
    async with httpx.AsyncClient() as client:
        response = await client.get(MS1_URL_ESTUDIANTES)
        if response.status_code != 200:
            raise Exception("Error al obtener estudiantes desde MS1")
        return response.json()

async def get_empresas():
    async with httpx.AsyncClient() as client:
        response = await client.get(MS2_URL_EMPRESAS)
        if response.status_code != 200:
            raise Exception("Error al obtener empresas desde MS2")
        return response.json()


async def get_programas():
    async with httpx.AsyncClient() as client:
        response = await client.get(MS2_URL_PROGRAMAS)
        if response.status_code != 200:
            raise Exception("Error al obtener programas desde MS2 invocando a MS1")
        return response.json()


async def get_pagos():
    async with httpx.AsyncClient() as client:
        response = await client.get(MS3_URL_PAGOS)
        if response.status_code != 200:
            raise Exception("Error al obtener pagos desde MS3")
        return response.json()
