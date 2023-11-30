# Copyright (c) 2023 Rafael F.M. & Reinaldo
#
# This software is released under the MIT License.
# https://opensource.org/licenses/MIT

from rocketry import Rocketry
from rocketry.conds import every
from .algorithms_olc import alg_olc

app_rocketry = Rocketry()


@app_rocketry.task(every("240 seconds"))
def check_schedule_health():
    """
    Tarefa para verificar a saúde do scheduler
    """
    print("Scheduler health check")


@app_rocketry.task(every("6 hours"), execution="async")
async def update_trending_articles():
    """
    Tarefa para atualizar os artigos em ascensão
    """
    await alg_olc.update_trending_articles()
    print("Updating trending articles")
