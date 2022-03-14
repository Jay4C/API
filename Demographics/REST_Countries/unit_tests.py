import json
import unittest
import requests


class UnitTestsRestCountriesAPI(unittest.TestCase):
    def test_all(self):
        url = "https://restcountries.eu/rest/v2/all"
        payload = {}
        headers = {}
        response = requests.request("GET", url, headers=headers, data=payload)
        print(response.text.encode('utf8'))

    def test_list_of_countries(self):
        url = "https://restcountries.eu/rest/v2/all"
        payload = {}
        headers = {}
        response = requests.request("GET", url, headers=headers, data=payload)

        countries = []

        all_countries = json.loads(response.text.encode('utf8'))

        for one_country in all_countries:
            countries.append(one_country['name'].lower())

        for country in countries:
            print("country : " + country)

    def test_name(self):
        name = "france"
        url = "https://restcountries.eu/rest/v2/name/" + name
        payload = {}
        headers = {}
        response = requests.request("GET", url, headers=headers, data=payload)
        print(response.text.encode('utf8'))

    def test_full_name(self):
        full_name = "aruba"
        url = "https://restcountries.eu/rest/v2/name/" + full_name + "?fullText=true"
        payload = {}
        headers = {}
        response = requests.request("GET", url, headers=headers, data=payload)
        print(response.text.encode('utf8'))

    def test_code(self):
        code = "co"
        url = "https://restcountries.eu/rest/v2/alpha/" + code
        payload = {}
        headers = {}
        response = requests.request("GET", url, headers=headers, data=payload)
        print(response.text.encode('utf8'))

    def test_list_of_codes(self):
        codes = "col;no;ee"
        url = "https://restcountries.eu/rest/v2/alpha?codes=" + codes
        payload = {}
        headers = {}
        response = requests.request("GET", url, headers=headers, data=payload)
        print(response.text.encode('utf8'))

    def test_currency(self):
        currency = "cop"
        url = "https://restcountries.eu/rest/v2/currency/" + currency
        payload = {}
        headers = {}
        response = requests.request("GET", url, headers=headers, data=payload)
        print(response.text.encode('utf8'))

    def test_language(self):
        language = "es"
        url = "https://restcountries.eu/rest/v2/lang/" + language
        payload = {}
        headers = {}
        response = requests.request("GET", url, headers=headers, data=payload)
        print(response.text.encode('utf8'))

    def test_capital_city(self):
        capital_city = "tallinn"
        url = "https://restcountries.eu/rest/v2/capital/" + capital_city
        payload = {}
        headers = {}
        response = requests.request("GET", url, headers=headers, data=payload)
        print(response.text.encode('utf8'))

    def test_calling_code(self):
        calling_code = "372"
        url = "https://restcountries.eu/rest/v2/callingcode/" + calling_code
        payload = {}
        headers = {}
        response = requests.request("GET", url, headers=headers, data=payload)
        print(response.text.encode('utf8'))

    def test_region(self):
        region = "europe"
        url = "https://restcountries.eu/rest/v2/region/" + region
        payload = {}
        headers = {}
        response = requests.request("GET", url, headers=headers, data=payload)
        print(response.text.encode('utf8'))

    def test_regional_bloc(self):
        regional_bloc = "eu"
        url = "https://restcountries.eu/rest/v2/regionalbloc/" + regional_bloc
        payload = {}
        headers = {}
        response = requests.request("GET", url, headers=headers, data=payload)
        print(response.text.encode('utf8'))

    def test_filter_response(self):
        filters = "name;capital;currencies"
        url = "https://restcountries.eu/rest/v2/all?fields=" + filters
        payload = {}
        headers = {}
        response = requests.request("GET", url, headers=headers, data=payload)
        print(response.text.encode('utf8'))


if __name__ == '__main__':
    unittest.main()
