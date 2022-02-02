import json
import unittest
import requests


# https://exchangeratesapi.io/
class UnitTestsExchangeRatesAPI(unittest.TestCase):
    def test_get_the_latest_foreign_exchange_reference_rates(self):
        print('test_get_the_latest_foreign_exchange_reference_rates')

        url = "https://api.exchangeratesapi.io/latest"

        response = requests.request("GET", url)

        print(json.loads(response.text))

    def test_list_all_available_symbols(self):
        print('test_list_all_available_symbols')

        url = "https://api.exchangeratesapi.io/latest"

        response = requests.request("GET", url)

        rates = json.loads(response.text)['rates']

        for rate in rates:
            print(rate)

    def test_list_all_available_rates(self):
        print('test_list_all_available_symbols')

        url = "https://api.exchangeratesapi.io/latest"

        response = requests.request("GET", url)

        rates = json.loads(response.text)['rates']

        for rate in rates:
            print(rate + " : " + str(json.loads(response.text)['rates'][str(rate)]))

    def test_get_historical_rates_for_any_day_since_1999(self):
        print('test_get_historical_rates_for_any_day_since_1999')

        url = "https://api.exchangeratesapi.io/2010-01-12"

        response = requests.request("GET", url)

        print(json.loads(response.text))

    def test_get_the_latest_foreign_exchange_reference_rates_for_a_specific_currency(self):
        print('test_get_the_latest_foreign_exchange_reference_rates_for_a_specific_currency')

        url = "https://api.exchangeratesapi.io/latest?base=USD"

        response = requests.request("GET", url)

        print(json.loads(response.text))

    def test_request_specific_exchange_rates_by_setting_the_symbols_parameter(self):
        print('test_request_specific_exchange_rates_by_setting_the_symbols_parameter')

        url = "https://api.exchangeratesapi.io/latest?symbols=USD,GBP"

        response = requests.request("GET", url)

        USD = json.loads(response.text)['rates']['USD']

        GBP = json.loads(response.text)['rates']['GBP']

        print("USD : " + str(USD) + " ; GBP : " + str(GBP))

    def test_get_historical_rates_for_a_time_period(self):
        print('test_get_historical_rates_for_a_time_period')

        url = "https://api.exchangeratesapi.io/history?start_at=2018-01-01&end_at=2018-02-01"

        response = requests.request("GET", url)

        print(json.loads(response.text))

    def test_limit_results_to_specific_exchange_rates_to_save_bandwidth_with_the_symbols_parameter(self):
        print('test_limit_results_to_specific_exchange_rates_to_save_bandwidth_with_the_symbols_parameter')

        url = "https://api.exchangeratesapi.io/history?start_at=2018-01-01&end_at=2018-02-01&symbols=ILS,JPY"

        response = requests.request("GET", url)

        print(json.loads(response.text))

    def test_quote_the_historical_rates_against_a_different_currency(self):
        print('test_quote_the_historical_rates_against_a_different_currency')

        url = "https://api.exchangeratesapi.io/history?start_at=2018-01-01&end_at=2018-02-01&base=USD"

        response = requests.request("GET", url)

        print(json.loads(response.text))


if __name__ == '__main__':
    unittest.main()
