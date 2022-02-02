import json
import unittest
import requests


class UnitTestsFreeForexApi(unittest.TestCase):
    def test_current_rate_EUR_USD(self):
        print('test_current_rate_EUR_USD')

        url = "https://www.freeforexapi.com/api/live?pairs=EURUSD"

        response = requests.request("GET", url)

        rate = json.loads(response.text)['rates']['EURUSD']['rate']

        print("EUR_USD_rate : " + str(rate))

    def test_current_rate_EUR_GBP(self):
        print('test_current_rate_EUR_GBP')

        url = "https://www.freeforexapi.com/api/live?pairs=EURGBP"

        response = requests.request("GET", url)

        rate = json.loads(response.text)['rates']['EURGBP']['rate']

        print("EUR_GBP_rate : " + str(rate))

    def test_current_rate_GBP_USD(self):
        print('test_current_rate_GBP_USD')

        url = "https://www.freeforexapi.com/api/live?pairs=GBPUSD"

        response = requests.request("GET", url)

        rate = json.loads(response.text)['rates']['GBPUSD']['rate']

        print("GBP_USD_rate : " + str(rate))

    def test_current_rate_USD_JPY(self):
        print('test_current_rate_USD_JPY')

        url = "https://www.freeforexapi.com/api/live?pairs=USDJPY"

        response = requests.request("GET", url)

        rate = json.loads(response.text)['rates']['USDJPY']['rate']

        print("USD_JPY_rate : " + str(rate))

    def test_current_rate_AUD_USD(self):
        print('test_current_rate_AUD_USD')

        url = "https://www.freeforexapi.com/api/live?pairs=AUDUSD"

        response = requests.request("GET", url)

        rate = json.loads(response.text)['rates']['AUDUSD']['rate']

        print("AUD_USD_rate : " + str(rate))

    def test_current_rate_USD_CHF(self):
        print('test_current_rate_USD_CHF')

        url = "https://www.freeforexapi.com/api/live?pairs=USDCHF"

        response = requests.request("GET", url)

        rate = json.loads(response.text)['rates']['USDCHF']['rate']

        print("USD_CHF_rate : " + str(rate))

    def test_current_rate_NZD_USD(self):
        print('test_current_rate_NZD_USD')

        url = "https://www.freeforexapi.com/api/live?pairs=NZDUSD"

        response = requests.request("GET", url)

        rate = json.loads(response.text)['rates']['NZDUSD']['rate']

        print("NZD_USD_rate : " + str(rate))

    def test_current_rate_USD_CAD(self):
        print('test_current_rate_USD_CAD')

        url = "https://www.freeforexapi.com/api/live?pairs=USDCAD"

        response = requests.request("GET", url)

        rate = json.loads(response.text)['rates']['USDCAD']['rate']

        print("USD_CAD_rate : " + str(rate))

    def test_current_rate_USD_ZAR(self):
        print('test_current_rate_USD_ZAR')

        url = "https://www.freeforexapi.com/api/live?pairs=USDZAR"

        response = requests.request("GET", url)

        rate = json.loads(response.text)['rates']['USDZAR']['rate']

        print("USD_ZAR_rate : " + str(rate))


if __name__ == '__main__':
    unittest.main()
