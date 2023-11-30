# Copyright (c) 2023 Rafael F.M. & Reinaldo
#
# This software is released under the MIT License.
# https://opensource.org/licenses/MIT

from pocketbase_api.core import pb_api
from pocketbase_api import helpers as pb_helpers
import httpx
from datetime import datetime

RESPONSE_SIZE = 10

DEFAULT_NUMBER_OF_ARTICLES_FOR_SCORING = 500


class AlgorithmsOLC:
    """
    Classe que contém os algoritmos do OLC
    """

    def __init__(self):
        self.__trending_articles = []  # Lista de artigos que estão em alta no máximo 50

    async def fetch_article_list(
        self, min_articles: int = 10, age_in_days: int = 7
    ) -> httpx.Response | httpx.HTTPError:
        """
        Fetches a list of articles from the database to calculate the score, if the number of articles is less than `min_articles` then it returns a fallback list of articles.

        Args:
            min_articles (int, optional): Minimum number of articles in the response. Defaults to 10.
            age_in_days (int, optional): Maximum age of the articles in the response. Defaults to 7.

        Returns:
            httpx.Response | httpx.HTTPError: Response from the API
        """
        articles_list = await pb_api.get_list_of_articles_stats_records_by_age(
            DEFAULT_NUMBER_OF_ARTICLES_FOR_SCORING, age_in_days
        )
        if isinstance(articles_list, httpx.Response):
            number_of_records = articles_list.json().get("totalItems", 0)
            print(f"Found: {number_of_records} articles")
            if number_of_records >= min_articles:
                return articles_list

        print("Minimum number of articles not found, fetching fallback list...")

        fallback_articles_list = await pb_api.get_list_of_articles_stats_records(
            page=1, num_of_records=10, sort="-created"
        )
        return fallback_articles_list

    async def update_trending_articles(self):
        """
        Atualiza a lista de artigos em alta
        """
        min_article_age = 30

        articles_stats_list = await self.fetch_article_list(
            RESPONSE_SIZE, min_article_age
        )

        self.calculate_score(articles_stats_list)

    def calculate_score(
        self,
        articles_stats_list: httpx.Response | httpx.HTTPError,
        date_for_calculation: datetime = datetime.today(),
    ):
        """
        Calcula o score de cada artigo e atualiza a lista de artigos em alta, ordenando-os pelo score

        Args:
            articles_stats_list (httpx.Response | httpx.HTTPError): Lista de artigos
            date_for_calculation (datetime, optional): Data para calcular o score. Defaults to datetime.today().
        """

        articles_instances = pb_helpers.get_record_list_from_response(
            articles_stats_list
        )

        scores = []
        for i in articles_instances:
            created: str = i.get("created", "0000-00-00 00:00:00.000Z")
            latest_views: int = i.get("latest_views", 0)
            likes: int = i.get("likes", 0)

            converted_time = datetime.strptime(created, "%Y-%m-%d %H:%M:%S.%fZ")

            # calculates the number of days since created counting from today
            age = (date_for_calculation - converted_time).days

            score = (float(latest_views) / float(age)) + 0.4 * likes
            scores.append((score, i))

        # sort values by the score
        sorted_values_by_score = sorted(scores, key=lambda tup: tup[0], reverse=True)

        print(
            f"sorted scores: {[score for score, _ in sorted_values_by_score]}"
        )  # Print only the scores

        self.__trending_articles = [item[1] for item in sorted_values_by_score[:50]]
        return self.__trending_articles

    def get_trending_articles(self):
        return self.__trending_articles


alg_olc = AlgorithmsOLC()
