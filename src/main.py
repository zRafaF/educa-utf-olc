from argparse import ArgumentParser
from pocketbase_api import pb_api
from pocketbase_api import helpers as pb_helpers
import asyncio
import uvicorn
from olc_server import scheduler, api, Server


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
args = parser.parse_args()


async def main():
    # Inicializando a comunicação com o banco
    pb_api.set_base_url(args.pb_url)
    h = await pb_api.get_list_of_articles_records(5)
    if(h.status_code == 200):
        article_list = pb_helpers.get_record_list_from_response(h)
        for i in article_list:
            print(i.get("title"))

    server = Server(
        config=uvicorn.Config(
            api.app_fastapi, workers=1, loop="asyncio", host=args.host, port=args.port
        )
    )
    api_server = asyncio.create_task(server.serve())
    sched = asyncio.create_task(scheduler.app_rocketry.serve())

    await asyncio.wait([sched, api_server])


if __name__ == "__main__":
    asyncio.run(main())
