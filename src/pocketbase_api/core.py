# Copyright (c) 2023 Rafael F.M. & Reinaldo
#
# This software is released under the MIT License.
# https://opensource.org/licenses/MIT

import httpx
from . import helpers as pb_helpers


class PocketBase_API:
    """
    Classe de abstração do Backend utilizando [PocketBase](https://pocketbase.io/docs/).

    Oferece uma implementação assíncrona do SDK fornecido (não oficial) em <https://github.com/vaphes/pocketbase>

    A lista de tipos e relações pode ser encontrada em <https://github.com/zRafaF/educa-utf/blob/main/app/types/pocketbase-types.ts>
    """

    def __init__(self, pb_url: str = "http://127.0.0.1:8090", timeout: float = 5.0):
        """
        Construtor da classe PocketBase_API.

        Args:
            pb_url (str, optional): URL base da API do PocketBase. Defaults to "http://127.0.0.1:8090".
            timeout (float, optional): Tempo máximo de espera para uma resposta da API do PocketBase. Defaults to 5.0.
        """

        self.__pb_url = pb_url
        self.__timeout = timeout
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

    async def health(self) -> httpx.Response | httpx.HTTPError:
        """
        Retorna o status de saúde da API do PocketBase

        Returns:
            httpx.Response: Resposta da requisição HTTP

        """
        try:
            response = await self.client.get(
                self.build_url("/health"), timeout=self.__timeout
            )
            response.raise_for_status()
            return response
        except httpx.HTTPError as exc:
            print(f"HTTP Exception for {exc.request.url} - {exc}")
            return exc

    async def get_list_of_articles_stats_records(
        self, page: int = 1, num_of_records: int = 10, filter: str = "", sort: str = ""
    ) -> httpx.Response | httpx.HTTPError:
        """
        Retorna uma lista de artigos do PocketBase


        Args:
            page (int, optional): Página a ser retornada. Defaults to 1.
            num_of_records (int, optional): Número de registros a serem retornados. Defaults to 10.
            filter (str, optional): Filtro a ser aplicado. Defaults to "".
            sort (str, optional): Ordenação a ser aplicada. Defaults to "".

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
        params = {}

        params["page"] = page
        params["perPage"] = num_of_records
        if filter != "":
            params["filter"] = filter

        if sort != "":
            params["sort"] = sort

        try:
            response = await self.client.get(
                self.build_url("/collections/articles_stats/records"),
                params=params,
                timeout=self.__timeout,
            )

            response.raise_for_status()
            return response
        except httpx.HTTPError as exc:
            print(f"HTTP Exception for {exc.request.url} - {exc}")
            return exc

    async def get_list_of_articles_stats_records_by_age(
        self, num_of_records: int = 10, age_in_days: int = 7
    ) -> httpx.Response | httpx.HTTPError:
        """
        Retorna uma lista de artigos do PocketBase com idade menor ou igual a `age_in_days` dias. Ordenado por `created` em ordem decrescente.

        args:
            num_of_records (int, optional): Número de registros a serem retornados.
            age_in_days (int, optional): Idade máxima dos registros em dias.
        Returns:
            httpx.Response: Resposta da requisição HTTP
        """

        filter_date = pb_helpers.calculate_date_since_today(number_of_days=age_in_days)

        return await self.get_list_of_articles_stats_records(
            num_of_records=num_of_records,
            filter=f'created>="{filter_date}"',
            sort="-created",
        )
