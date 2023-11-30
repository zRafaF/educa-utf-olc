# Copyright (c) 2023 Rafael F.M. & Reinaldo
#
# This software is released under the MIT License.
# https://opensource.org/licenses/MIT

# Create FastAPI app
from fastapi import FastAPI, responses, Request
import httpx
from .scheduler import app_rocketry
from . import algorithms_olc
from pocketbase_api.core import pb_api

app_fastapi = FastAPI()

session = app_rocketry.session


@app_fastapi.get("/running-tasks")
async def get_tasks():
    """
    Endpoint para obter as tarefas em execução do Rocketry
    """
    return session.tasks


@app_fastapi.get("/")
async def read_root(request: Request):
    """
    Endpoint de saúde da API
    """

    response = await pb_api.health()
    if isinstance(response, httpx.Response):
        return {
            "message": "Hello EducaUTF-OLC!",
            "pb_health": {
                "code": response.status_code,
                "message": response.json()["message"],
            },
            "root_path": request.scope.get("root_path"),
        }
    return {
        "message": "Hello EducaUTF-OLC!",
        "pb_health": {
            "code": "502",
            "message": "unable to contact PB API",
        },
        "root_path": request.scope.get("root_path"),
    }


@app_fastapi.get("/trending-articles")
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
