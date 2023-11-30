# Copyright (c) 2023 Rafael F.M. & Reinaldo
#
# This software is released under the MIT License.
# https://opensource.org/licenses/MIT

from typing import List, Dict
import httpx
from . import types
from datetime import datetime, timedelta

"""
Article_stats_dict

{
"id": "RECORD_ID",
"collectionId": "yj5hrb87l3zixoo",
"collectionName": "articles_stats",
"title": "test",
"description": "test",
"user": "RELATION_RECORD_ID",
"author_name": "test",
"author_username": "test",
"author_avatar": "filename.jpg",
"document": "filename.jpg",
"tags": [
"RELATION_RECORD_ID"
],
"visibility": "public",
"likes": 123,
"views": 123,
"latest_views": 123
}

"""

def get_record_list_from_response(response: httpx.Response | httpx.HTTPError) -> List[Dict]:
    """
    Retorna a lista de Artigos da resposta como uma Lista de dicionários.

    Args:
        response (httpx.Response): Resposta da requisição HTTP.

    Returns:
        List[Dict]: Lista de dicionários representando os Artigos.
    """
    if(isinstance(response, httpx.Response)):
        data = response.json()
        return data.get("items", [])
    return []

def calculate_date_since_today(start_date: datetime = datetime.today(), number_of_days: int = 30)->str:
    """
    Calcula uma data no formato YYYY-MM-DD de acordo com o número de dias passados.
    
    Args:
        start_date (datetime, optional): Data inicial. Defaults to datetime.today().
        number_of_days (int, optional): Número de dias a serem subtraídos. Defaults to 30.
    
    Returns:
        str: Data no formato YYYY-MM-DD
    """
    since = start_date - timedelta(days=number_of_days)
    return since.strftime("%Y-%m-%d")