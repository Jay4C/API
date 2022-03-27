import unittest
import requests

endpoint = "https://apispot.io/api/v1"
api_key = ""


# https://apispot.io/docs/whois-and-domain-api-v1
class UnitTestsAPISpotBulkWHOISWithTorRequest(unittest.TestCase):
    def test_getWhois(self):
        print("test_getWhois")

        url = endpoint + "/whois"

        querystring = {
            "domain": "string",
            "domains": "string",
            "format": "string"
        }

        headers = {
            'X-API-KEY': api_key
        }

        response = requests.get(url, headers=headers, params=querystring)

        print(response.text)

    def test_getAvailability(self):
        print('test_getAvailability')

        url = endpoint + "/domain_check"

        querystring = {
            "domain": "string",
            "domains": "string"
        }

        headers = {
            'X-API-KEY': api_key
        }

        response = requests.get(url, headers=headers, params=querystring)

        print(response.text)


if __name__ == '__main__':
    unittest.main()
