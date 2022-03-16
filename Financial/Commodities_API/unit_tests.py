import unittest
import requests

# https://commodities-api.com/documentation

endpoint = "https://commodities-api.com/api"


class UnitTestsCommodityAPIEndpoints(unittest.TestCase):
    def test_get_Supported_Symbols_Endpoint(self):
        print("test_get_Supported_Symbols_Endpoint")

        headers = {
            'accept': 'application/json',
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103'
        }

        url = endpoint + "/symbols"

        params = {
            ('access_key', 'API_KEY')
        }

        r = requests.get(url, params=params, headers=headers)

        print(r.text)

    def test_Latest_Rates_Endpoint(self):
        print("test_Latest_Rates_Endpoint")

        headers = {
            'accept': 'application/json',
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103'
        }

        url = endpoint + "/latest"

        params = {
            ('access_key', 'API_KEY'),
            ('base', 'USD'),
            ('symbols', 'GBP,JPY,EUR')
        }

        r = requests.get(url, params=params, headers=headers)

        print(r.text)

    def test_Historical_Rates_Endpoint(self):
        print("test_Historical_Rates_Endpoint")

        headers = {
            'accept': 'application/json',
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103'
        }

        url = endpoint + "/2013-12-24"

        params = {
            ('access_key', 'API_KEY'),
            ('base', 'USD'),
            ('symbols', 'GBP,JPY,EUR')
        }

        r = requests.get(url, params=params, headers=headers)

        print(r.text)

    def test_Specify_Symbols(self):
        print("test_Specify_Symbols")

        headers = {
            'accept': 'application/json',
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103'
        }

        url = endpoint + "/latest"

        params = {
            ('access_key', 'API_KEY'),
            ('symbols', 'USD,CAD,JPY')
        }

        r = requests.get(url, params=params, headers=headers)

        print(r.text)

    def test_Changing_base_currency(self):
        print("test_Changing_base_currency")

        headers = {
            'accept': 'application/json',
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103'
        }

        url = endpoint + "/latest"

        params = {
            ('access_key', 'API_KEY'),
            ('base', 'USD')
        }

        r = requests.get(url, params=params, headers=headers)

        print(r.text)

    def test_Convert_Endpoint(self):
        print("test_Convert_Endpoint")

        headers = {
            'accept': 'application/json',
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103'
        }

        url = endpoint + "/convert"

        params = {
            ('access_key', 'API_KEY'),
            ('from', 'GBP'),
            ('to', 'JPY'),
            ('amount', '25')
        }

        r = requests.get(url, params=params, headers=headers)

        print(r.text)

    def test_Time_Series_Endpoint(self):
        print("test_Time_Series_Endpoint")

        headers = {
            'accept': 'application/json',
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103'
        }

        url = endpoint + "/timeseries"

        params = {
            ('access_key', 'API_KEY'),
            ('start_date', '2012-05-01'),
            ('end_date', '2012-05-25')
        }

        r = requests.get(url, params=params, headers=headers)

        print(r.text)

    def test_Fluctuation_Endpoint(self):
        print("test_Fluctuation_Endpoint")

        headers = {
            'accept': 'application/json',
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103'
        }

        url = endpoint + "/fluctuation"

        params = {
            ('access_key', 'API_KEY'),
            ('start_date', '2012-05-01'),
            ('end_date', '2012-05-25')
        }

        r = requests.get(url, params=params, headers=headers)

        print(r.text)


if __name__ == '__main__':
    unittest.main()
