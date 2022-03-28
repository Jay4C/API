import unittest
from requests_tor import RequestsTor

endpoint = "https://api.getfestivo.com"
api_key = ""


# https://docs.getfestivo.com/docs/products/public-holidays-api/list-countries
class UnitTestsFestivoAPI(unittest.TestCase):
    def test_List_holidays(self):
        print('test_List_holidays')

        rt = RequestsTor()

        headers = {
            'Authorization': 'API-Key ' + api_key,
            'content-type': "application/json"
        }

        params = {
            'country': "US",
            'year': 2020
        }

        url = endpoint + "/v2/holidays"

        response = rt.get(url, headers=headers, params=params)

        print(response.text)

    def test_List_available_countries(self):
        print("test_List_available_countries")

        rt = RequestsTor()

        headers = {
            'Authorization': 'API-Key ' + api_key,
            'content-type': "application/json"
        }

        url = endpoint + "/v2/countries"

        response = rt.get(url, headers=headers)

        print(response.text)


if __name__ == '__main__':
    unittest.main()
