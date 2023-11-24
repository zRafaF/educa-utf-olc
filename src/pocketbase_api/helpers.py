# Copyright (c) 2023 Rafael F.M. & Reinaldo
# 
# This software is released under the MIT License.
# https://opensource.org/licenses/MIT

from typing import List, Dict
import httpx
from . import types



def get_record_list_from_response(response: httpx.Response) -> List[any]:
    """
    Parse the response from get_list_of_articles_records function and return a list of ArticlesResponse objects.
    """
    data = response.json()

    return data.get("items", [])
