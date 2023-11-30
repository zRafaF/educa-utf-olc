# Copyright (c) 2023 Rafael F.M. & Reinaldo
#
# This software is released under the MIT License.
# https://opensource.org/licenses/MIT

# Create FastAPI app
from fastapi import FastAPI, responses
from .scheduler import app_rocketry
from pocketbase_api import pb_api
from . import algorithms_olc

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
    """
    Endpoint de saúde da API
    """
    pb_health = await pb_api.health()
    return {
        "message": "Hello EducaUTF-OLC!",
        "pb_health": {
            "code": pb_health.status_code,
            # only return message if status_code is 200
            "message": pb_health.json()["message"]
            if pb_health.status_code == 200
            else "unable to contact PB API",
        },
    }


@app_fastapi.get("/trending_articles")
def get_trending_articles():
    """
    Endpoint para obter os artigos em alta

    returns:
        ```json
        {
            "page": 1,
            "perPage": 50,
            "totalPages": 1,
            "totalItems": 50,
            "items": [
                {
                    "id": 1,
                    "title": "Aprendendo a usar o PocketBase",
                    "description": "Aprenda a usar o PocketBase",
                    "content": "Aprenda a usar o PocketBase",
                    "created": "2023-09-15 16:50:07.282000",
                    "updated": "2023-09-15 16:50:07.282000",
                    "author": 1,
                    "likes": 0,
                    "latest_views": 0,
                    "tags": [
                        1,
                        2
                    ]
                },
                ...
            ]
        }
        ```
    """
    articles = algorithms_olc.alg_olc.get_trending_articles()
    return {
        "page": 1,
        "perPage": algorithms_olc.RESPONSE_SIZE,
        "totalPages": 1,
        "totalItems": len(articles),
        "items": articles,
    }


@app_fastapi.get("/olc/", response_class=responses.HTMLResponse)
async def get_olc():
    """
    Easter egg do OLC

    Returns:
        responses.HTMLResponse: HTML
    """
    return """
    <html>
        <head>
            <title>OLC</title>
        </head>
        <body>
            <pre>
⢀⡴⠑⡄⠀⠀⠀⠀⠀⠀⠀⣀⣀⣤⣤⣤⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀ 
⠸⡇⠀⠿⡀⠀⠀⠀⣀⡴⢿⣿⣿⣿⣿⣿⣿⣿⣷⣦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀ 
⠀⠀⠀⠀⠑⢄⣠⠾⠁⣀⣄⡈⠙⣿⣿⣿⣿⣿⣿⣿⣿⣆⠀⠀⠀⠀⠀⠀⠀⠀ 
⠀⠀⠀⠀⢀⡀⠁⠀⠀⠈⠙⠛⠂⠈⣿⣿⣿⣿⣿⠿⡿⢿⣆⠀⠀⠀⠀⠀⠀⠀ 
⠀⠀⠀⢀⡾⣁⣀⠀⠴⠂⠙⣗⡀⠀⢻⣿⣿⠭⢤⣴⣦⣤⣹⠀⠀⠀⢀⢴⣶⣆ 
⠀⠀⢀⣾⣿⣿⣿⣷⣮⣽⣾⣿⣥⣴⣿⣿⡿⢂⠔⢚⡿⢿⣿⣦⣴⣾⠁⠸⣼⡿ 
⠀⢀⡞⠁⠙⠻⠿⠟⠉⠀⠛⢹⣿⣿⣿⣿⣿⣌⢤⣼⣿⣾⣿⡟⠉⠀⠀⠀⠀⠀ 
⠀⣾⣷⣶⠇⠀⠀⣤⣄⣀⡀⠈⠻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀ 
⠀⠉⠈⠉⠀⠀⢦⡈⢻⣿⣿⣿⣶⣶⣶⣶⣤⣽⡹⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀ 
⠀⠀⠀⠀⠀⠀⠀⠉⠲⣽⡻⢿⣿⣿⣿⣿⣿⣿⣷⣜⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀ 
⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⣷⣶⣮⣭⣽⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀ 
⠀⠀⠀⠀⠀⠀⣀⣀⣈⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠇⠀⠀⠀⠀⠀⠀⠀ 
⠀⠀⠀⠀⠀⠀⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠃⠀⠀⠀⠀⠀⠀⠀⠀ 
⠀⠀⠀⠀⠀⠀⠀⠹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀ 
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠛⠻⠿⠿⠿⠿⠛⠉
            </pre>
        </body>
    </html>
    """
