# Copyright (c) 2023 Rafael F.M. & Reinaldo
#
# This software is released under the MIT License.
# https://opensource.org/licenses/MIT

from rocketry import Rocketry
from rocketry.conds import every
from .algorithms_olc import alg_olc

app_rocketry = Rocketry()


@app_rocketry.task(every("30 seconds"), execution="async")
async def do_things():
    """
    Tarefa de teste
    """
    print("Scheduler health check")

@app_rocketry.task(every("6 hours"))
def update_trending_articles():
    """
    Tarefa para atualizar os artigos em ascensão
    """
    alg_olc.calculate_score()
    print("Updating trending articles")