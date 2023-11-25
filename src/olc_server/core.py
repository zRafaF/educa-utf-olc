# Copyright (c) 2023 Rafael F.M. & Reinaldo
#
# This software is released under the MIT License.
# https://opensource.org/licenses/MIT

# Create FastAPI app
from fastapi import FastAPI
from .scheduler import app_rocketry
from pocketbase_api import pb_api

app_fastapi = FastAPI()

session = app_rocketry.session


@app_fastapi.get("/running-tasks")
async def get_tasks():
    """
    Endpoint para obter as tarefas em execução do Rocketry
    """
    return session.tasks


@app_fastapi.get("/")
async def read_root():
    pb_health = await pb_api.health()
    return {"message": "Hello EducaUTF-OLC!", "pb_health": {
        "code": pb_health.status_code,
        # only return message if status_code is 200
        "message": pb_health.json()["message"] if pb_health.status_code == 200 else "unable to contact PB API"
    }}
