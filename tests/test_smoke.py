import pytest
import configparser

from datetime import datetime

from utils import get_today_date_string, request_with_retries, check_valid_url

# define configparser object
config = configparser.ConfigParser()
config.read("/DE_TEST/configs/cfgs.ini")
token  = config.get('football_api','token')


def test_get_today_date_string():
    assert get_today_date_string() == datetime.today().strftime('%Y%m%d')


@pytest.mark.parametrize(
    "url,token",
    [
        ("https://api.football-data.org/v4/competitions",{"X-Auth-Token":token}),
        ("https://api.football-data.org/v4/competitions/ELC/standings", {"X-Auth-Token":token})
    ]
)
def test_request_with_retries(url, token):
    assert request_with_retries(url, token).status_code == 200



@pytest.mark.parametrize( "url", ["https://api.football-data.org/v4/competitions"])
def test_check_valid_url(url):
    assert check_valid_url(url) == True

