import json
import unittest
import requests


# https://freecurrencyapi.net/#features
class UnitTestsFreeCurrencyConversionAPI(unittest.TestCase):
    def test_getting_the_latest_foreign_exchange_rates(self):
        print('test_getting_the_latest_foreign_exchange_rates')

        url = "https://freecurrencyapi.net/api/v1/latest"

        response = requests.request("GET", url)

        print(json.loads(response.text))

    def test_getting_the_latest_foreign_exchange_rates_for_a_specific_base_currency(self):
        print('test_getting_the_latest_foreign_exchange_rates_for_a_specific_base_currency')

        url = "https://freecurrencyapi.net/api/v1/latest?base_currency=GBP"

        response = requests.request("GET", url)

        print(json.loads(response.text))

    def test_getting_the_latest_foreign_exchange_rates_for_a_specific_currency_pair(self):
        print('test_getting_the_latest_foreign_exchange_rates_for_a_specific_currency_pair')

        url = "https://freecurrencyapi.net/api/v1/latest?currency_pair=USD,EUR"

        response = requests.request("GET", url)

        print(json.loads(response.text))

    def test_getting_the_historical_rates_for_a_certain_time_period(self):
        print('test_getting_the_historical_rates_for_a_certain_time_period')

        url = "https://freecurrencyapi.net/api/v1/historic?base_currency=USD&date_from=2019-01-01&date_to=2020-01-01"

        response = requests.request("GET", url)

        print(json.loads(response.text))

    def test_getting_the_historical_rates_for_a_certain_time_period_and_currency_pair(self):
        print('test_getting_the_historical_rates_for_a_certain_time_period_and_currency_pair')

        url = "https://freecurrencyapi.net/api/v1/historic?currency_pair=USD,EUR&date_from=2019-01-01&date_to=2020-01-01"

        response = requests.request("GET", url)

        print(json.loads(response.text))


if __name__ == '__main__':
    unittest.main()
