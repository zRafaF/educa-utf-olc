# Copyright (c) 2023 Rafael F.M. & Reinaldo
#
# This software is released under the MIT License.
# https://opensource.org/licenses/MIT

from datetime import datetime
from src.olc_server import api as olc_api, algorithms_olc
import httpx
import pytest
from fastapi.testclient import TestClient
from .test_mock import mock_articles_stats_response, mock_trending_response


@pytest.fixture
def fastapi_client():
    return TestClient(olc_api.app_fastapi)


@pytest.fixture
def alg_olc():
    return algorithms_olc.AlgorithmsOLC()


def test_trending_articles(fastapi_client):
    response = fastapi_client.get("/trending-articles")
    assert response.status_code == 200
    assert response.json() == {
        "page": 1,
        "perPage": algorithms_olc.RESPONSE_SIZE,
        "totalPages": 1,
        "totalItems": 0,
        "items": [],
    }


def test_calculate_score(mock_articles_stats_response, mock_trending_response, alg_olc):
    date = datetime.strptime("2023-10-01", "%Y-%m-%d")
    sorted = alg_olc.calculate_score(mock_articles_stats_response, date)
    assert sorted == mock_trending_response.json()["items"]
