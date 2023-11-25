# Copyright (c) 2023 Rafael F.M. & Reinaldo
#
# This software is released under the MIT License.
# https://opensource.org/licenses/MIT

# Create FastAPI app
from fastapi import FastAPI
from .scheduler import app_rocketry

app_fastapi = FastAPI()

session = app_rocketry.session


@app_fastapi.get("/running-tasks")
async def get_tasks():
    """
    Endpoint para obter as tarefas em execução do Rocketry
    """
    return session.tasks


@app_fastapi.get("/")
def read_root():
    return {"message": "Hello EducaUTF-OLC!"}
