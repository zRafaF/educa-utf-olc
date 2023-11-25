# Copyright (c) 2023 Rafael F.M. & Reinaldo
#
# This software is released under the MIT License.
# https://opensource.org/licenses/MIT
import uvicorn
from . import scheduler


class Server(uvicorn.Server):
    """
    Servidor uvicorn customizado

    O servidor Uvicorn sobrescreve a função de desligamento para incluir o Rocketry.
    """

    def handle_exit(self, sig: int, frame) -> None:
        scheduler.app_rocketry.session.shut_down()
        return super().handle_exit(sig, frame)
