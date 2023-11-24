import schedule
import time
from argparse import ArgumentParser
from pocketbase_api import pb_api
from pocketbase_api import helpers as pb_helpers
import asyncio

PB_URL = "https://educautf.td.utfpr.edu.br/db/api"

parser = ArgumentParser()
parser.add_argument(
    "--http",
    help="Specify a URL with the format 'host:port'\nExample: http://127.0.0.1:8090 or https://educautf.td.utfpr.edu.br/db",
)
args = parser.parse_args()

if args.http:
    PB_URL = args.http


async def main():
    # Inicializando a comunicação com o banco
    pb_api.set_base_url(PB_URL)
    h = await pb_api.get_list_of_articles_records(5)
    article_list = pb_helpers.get_record_list_from_response(h)
    for i in article_list:
        print(i.get("title"))


if __name__ == "__main__":
    asyncio.run(main())
