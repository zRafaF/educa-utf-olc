# Copyright (c) 2023 Rafael F.M. & Reinaldo
#
# This software is released under the MIT License.
# https://opensource.org/licenses/MIT

from typing import List, Dict
import httpx
from . import types


def get_record_list_from_response(response: httpx.Response) -> List[Dict]:
    """
    Retorna a lista de Artigos da resposta como uma Lista de dicionários.

    Args:
        response (httpx.Response): Resposta da requisição HTTP.

    Returns:
        List[Dict]: Lista de dicionários representando os Artigos.
    """
    if response.status_code == 200:
        data = response.json()
        return data.get("items", [])
    return []
