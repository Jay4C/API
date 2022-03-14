import unittest
import requests


class UnitTestsIbanAPI(unittest.TestCase):
    # https://ibanapi.com/get-api
    def test_get_get_api(self):
        print('test_get_get_api')

        params = (
            ('api_key', 'API_KEY'),
        )

        iban = "EE471000001020145685"

        url = "https://api.ibanapi.com/v1/validate/" + iban

        response = requests.get(url, params=params)

        print(response.text)

    def test_get_validate_basic(self):
        print('test_get_validate_basic')

        params = (
            ('api_key', 'API_KEY'),
        )

        iban = "EE471000001020145685"

        url = "https://api.ibanapi.com/v1/validate-basic/" + iban

        response = requests.get(url, params=params)

        print(response.text)

    def test_get_balance(self):
        print("test_get_balance")

        params = (
            ('api_key', 'API_KEY'),
        )

        iban = "EE471000001020145685"

        url = "https://api.ibanapi.com/v1/balance/" + iban

        response = requests.get(url, params=params)

        print(response.text)


if __name__ == '__main__':
    unittest.main()
