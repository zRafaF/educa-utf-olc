# Copyright (c) 2023 Rafael F.M. & Reinaldo
#
# This software is released under the MIT License.
# https://opensource.org/licenses/MIT

import httpx
from src.pocketbase_api.core import PocketBase_API
import pytest
from pytest_httpserver import HTTPServer
from src.pocketbase_api import helpers as pb_helpers
from datetime import datetime


@pytest.fixture
def pb_api(httpserver: HTTPServer):
    return PocketBase_API(httpserver.url_for(""), 0.3)


def test_url_builder(pb_api: PocketBase_API, httpserver: HTTPServer):
    assert pb_api.build_url("health") == httpserver.url_for("health")


async def test_health(pb_api: PocketBase_API, httpserver: HTTPServer):
    httpserver.expect_request("/health").respond_with_json(
        {"code": 200, "message": "API is healthy.", "data": {"canBackup": True}}
    )
    request = await pb_api.health()
    assert request.json()["message"] == "API is healthy."


def test_get_record_list_from_response(pb_api: PocketBase_API):
    # mock data
    data = {
        "items": [
            {
                "id": "abcde",
                "collectionId": "yj5hrb87l3zixoo",
                "collectionName": "articles_stats",
                "title": "test",
                "description": "test",
                "user": "RELATION_RECORD_ID",
                "author_name": "test",
                "author_username": "test",
                "author_avatar": "filename.jpg",
                "document": "filename.jpg",
                "tags": ["RELATION_RECORD_ID"],
                "visibility": "public",
                "likes": 123,
                "views": 123,
                "latest_views": 123,
            },
        ],
        "page": 1,
        "perPage": 1,
        "totalPages": 1,
        "totalItems": 1,
    }

    response = httpx.Response(json=data, status_code=200)
    assert (
        pb_helpers.get_record_list_from_response(response)[0]["id"]
        == data["items"][0]["id"]
    )

    response2 = httpx.HTTPError("Error")
    assert pb_helpers.get_record_list_from_response(response2) == []


def test_calculate_date_since_today():
    date = datetime.strptime("2021-10-01", "%Y-%m-%d")
    assert pb_helpers.calculate_date_since_today(date, -20) == "2021-10-21"
    assert pb_helpers.calculate_date_since_today(date, 20) == "2021-09-11"
    assert pb_helpers.calculate_date_since_today(date, 0) == "2021-10-01"
    assert pb_helpers.calculate_date_since_today(date, 360) == "2020-10-06"
    assert pb_helpers.calculate_date_since_today(date, -1) == "2021-10-02"
    assert pb_helpers.calculate_date_since_today(date, 9999) == "1994-05-17"
