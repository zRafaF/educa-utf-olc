# Copyright (c) 2023 Rafael F.M. & Reinaldo
#
# This software is released under the MIT License.
# https://opensource.org/licenses/MIT

from http.server import HTTPServer
from src.pocketbase_api import PocketBase_API
import pytest
from pytest_httpserver import HTTPServer


@pytest.fixture
def pb_api(httpserver: HTTPServer):
    return PocketBase_API(httpserver.url_for(""))


def test_url_builder(pb_api: PocketBase_API, httpserver: HTTPServer):
    assert pb_api.build_url("health") == httpserver.url_for("health")


async def test_health(pb_api: PocketBase_API, httpserver: HTTPServer):
    httpserver.expect_request("/health").respond_with_json(
        {"code": 200, "message": "API is healthy.", "data": {"canBackup": True}}
    )
    request = await pb_api.health()
    assert request.json()["message"] == "API is healthy."
