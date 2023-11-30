# Copyright (c) 2023 Rafael F.M. & Reinaldo
# 
# This software is released under the MIT License.
# https://opensource.org/licenses/MIT

from pocketbase_api import pb_api
from pocketbase_api import helpers as pb_helpers
import asyncio
import uvicorn
from datetime import datetime, timedelta

class AlgorithmsOLC:
    """
    Classe que contém os algoritmos do OLC
    """
    def __init__(self):
        self.__trending_articles = [] #Lista de artigos que estão em alta no máximo 50
        
    async def calculate_score(self):
        """
        Calcula o score de cada artigo e atualiza a lista de artigos em alta
        """
        articles_stats_list = await pb_api.get_list_of_articles_stats_records_by_age(500, 300)
        articles_instances = pb_helpers.get_record_list_from_response(articles_stats_list)
        
        # print(articles_instances)
        scores= []
        for i in articles_instances:
            created:str = i.get("created", '0000-00-00 00:00:00.000Z') # 2023-09-15 16:50:07.282000
            latest_views:int = i.get("latest_views", 0)
            likes:int = i.get("likes", 0)
            
            converted_time = datetime.strptime(created, "%Y-%m-%d %H:%M:%S.%fZ")
            
            # calculates the number of days since created counting from today
            age = (datetime.today() - converted_time).days

            # float division
            score = (float(latest_views)/float(age))+0.4*likes
            scores.append((score, i))


        #sort values by the score
        sorted_values_by_score = sorted(scores, key=lambda tup: tup[0], reverse=True)
        
        print(f'sorted scores: {[score for score, _ in sorted_values_by_score]}')  # Print only the scores
        
        self.__trending_articles = [item[1] for item in sorted_values_by_score[:50]]

    def get_trending_articles(self):
        return self.__trending_articles

alg_olc = AlgorithmsOLC()

#Hacker News algoritmo de score 
# Score = (P-1) / (T+2)^G
# where,
# P = points of an item (and -1 is to negate submitters vote)
# T = time since submission (in hours)
# G = Gravity, defaults to 1.8 in news