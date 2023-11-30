from argparse import ArgumentParser
from pocketbase_api.core import pb_api
from pocketbase_api import helpers as pb_helpers
import asyncio
import uvicorn
from olc_server import scheduler, api, core as olc_core
import httpx


parser = ArgumentParser()
parser.add_argument(
    "--pb_url",
    default="https://educautf.td.utfpr.edu.br/db/api",
    help="Specify a URL with the format 'host:port'\nExample: http://127.0.0.1:8090 or https://educautf.td.utfpr.edu.br/db/api",
)
parser.add_argument(
    "--host", default="127.0.0.1", help="Specify the host to run FastAPI app"
)
parser.add_argument(
    "--port", type=int, default=8000, help="Specify the port to run FastAPI app"
)
parser.add_argument(
    "--root_path",
    default="/olc-api",
    help="Specify the root path to run FastAPI app",
)
args = parser.parse_args()


async def main():
    # Inicializando a comunicação com o banco
    pb_api.set_base_url(args.pb_url)

    server = olc_core.OLCServer(
        config=uvicorn.Config(
            api.app_fastapi,
            workers=1,
            loop="asyncio",
            host=args.host,
            port=args.port,
            root_path=args.root_path,
        )
    )

    api_server = asyncio.create_task(server.serve())
    sched = asyncio.create_task(scheduler.app_rocketry.serve())

    await asyncio.wait([sched, api_server])


if __name__ == "__main__":
    asyncio.run(main())
