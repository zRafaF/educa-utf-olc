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
        """
        Construtor da classe PocketBase_API.

        Args:
            pb_url (str, optional): URL base da API do PocketBase. Defaults to "http://127.0.0.1:8090".
        """

        self.__pb_url = pb_url
        self.client = httpx.AsyncClient()

    def set_base_url(self, url: str):
        """
        Altera a URL base da API do PocketBase

        Args:
            url (str): Nova URL base para a API do PocketBase.
        """

        self.__pb_url = url

    def build_url(self, path: str) -> str:
        """
        Função auxiliar para construir a URL completa para a API do PocketBase.

        Concatena o `path` ao url base da API do PocketBase.

        Args:
            path str: Caminho novo.

        Returns:
            srt: url construída.

        """
        return f"{self.__pb_url}{path}"

    async def health(self) -> httpx.Response:
        """
        Retorna o status de saúde da API do PocketBase

        Returns:
            httpx.Response: Resposta da requisição HTTP

        """
        return await self.client.get(self.build_url("/health"))

    async def get_list_of_articles_records(
        self, num_of_records: int = 10
    ) -> httpx.Response:
        """
        Retorna uma lista de artigos do PocketBase


        Args:
            num_of_records (int, optional): Número de registros a serem retornados.

        Returns:
            httpx.Response: Resposta da requisição HTTP

        Exemplo:
            ```python
            import asyncio
            from pocketbase_api import pb_api
            from pocketbase_api import helpers as pb_helpers

            PB_URL = "https://educautf.td.utfpr.edu.br/db/api"

            async def main():
                # Inicializando a comunicação com o banco
                pb_api.set_base_url(PB_URL)
                h = await pb_api.get_list_of_articles_records(5)
                article_list = pb_helpers.get_record_list_from_response(h)
                for i in article_list:
                    print(i.get("title"))

            if __name__ == "__main__":
                asyncio.run(main())
            ```
        """

        return await self.client.get(
            self.build_url("/collections/articles/records"),
            params={"page": "1", "perPage": num_of_records},
        )
