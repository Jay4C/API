import unittest
import requests


class UnitTestsCoindesk(unittest.TestCase):
    def test_get_the_current_price(self):
        print('test_get_the_current_price')

        url = "https://api.coindesk.com/v1/bpi/currentprice.json"

        headers = {
            'accept': "application/json",
            'content-type': "application/json"
        }

        response = requests.request("GET", url, headers=headers)

        print(response.text)

    def test_get_the_current_price_in_any_currency(self):
        print('test_get_the_current_price')

        currency = "CNY"

        url = "https://api.coindesk.com/v1/bpi/currentprice/" + currency + ".json"

        headers = {
            'accept': "application/json",
            'content-type': "application/json"
        }

        response = requests.request("GET", url, headers=headers)

        print(response.text)

    def test_get_the_historical_price(self):
        print('test_get_the_historical_price')

        url = "https://api.coindesk.com/v1/bpi/historical/close.json"

        headers = {
            'accept': "application/json",
            'content-type': "application/json"
        }

        response = requests.request("GET", url, headers=headers)

        print(response.text)

    def test_get_the_historical_price_for_a_specific_period(self):
        print('test_get_the_historical_price_for_a_specific_period')

        start = "2013-09-01"

        end = "2013-09-05"

        url = "https://api.coindesk.com/v1/bpi/historical/close.json?start=" + start + "&end=" + end

        headers = {
            'accept': "application/json",
            'content-type': "application/json"
        }

        response = requests.request("GET", url, headers=headers)

        print(response.text)


if __name__ == '__main__':
    unittest.main()
