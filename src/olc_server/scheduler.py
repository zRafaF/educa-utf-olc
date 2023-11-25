# Copyright (c) 2023 Rafael F.M. & Reinaldo
#
# This software is released under the MIT License.
# https://opensource.org/licenses/MIT

from rocketry import Rocketry
from rocketry.conds import every

app_rocketry = Rocketry()


@app_rocketry.task(every("2 seconds"))
def do_things():
    print("Doing things")
