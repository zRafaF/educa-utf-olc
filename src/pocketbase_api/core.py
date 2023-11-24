# Copyright (c) 2023 Rafael F.M. & Reinaldo
# 
# This software is released under the MIT License.
# https://opensource.org/licenses/MIT

import httpx

class PocketBase_API:
    """
    Classe de abstração do Backend utilizando [PocketBase](https://pocketbase.io/docs/).

    Oferece uma implementação assíncrona do SDK fornecido (não oficial) em <https://github.com/vaphes/pocketbase>

    A lista de tipos e relações pode ser encontrada em <https://github.com/zRafaF/educa-utf/blob/main/app/types/pocketbase-types.ts>
    """
    def __init__(self, pb_url: str = "http://127.0.0.1:8090"):
        self.__pb_url = pb_url
        self.client = httpx.AsyncClient()
    
    def set_base_url(self, url:str):
        """
        Altera a URL base da API do PocketBase
        """

        self.__pb_url = url

    def build_url(self, path: str)->str:
        """
        Função auxiliar para construir a URL completa para a API do PocketBase
        """
        return f'{self.__pb_url}/{path}'

    async def health(self):
        """
        Retorna o status de saúde da API do PocketBase
        """
        return await self.client.get(self.build_url("health"))

    async def get_list_of_articles_records(self, num_of_records: int = 10)->httpx.Response:
        """
        Retorna uma lista de artigos do PocketBase

        Args:
            num_of_records (int, optional): Número de registros a serem retornados. Defaults to 10.
        
        Returns:
            httpx.Response: Resposta da requisição HTTP
        """

        return await self.client.get(self.build_url("collections/articles/records"), params={'page': "1", 'perPage': num_of_records})

