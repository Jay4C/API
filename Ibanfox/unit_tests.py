import unittest
import requests


class UnitTestsIbanfoxAPI(unittest.TestCase):
    # https://ibanfox.com/docs/api-reference/#operation/validateIban
    def test_get_validateIban(self):
        print('test_get_validateIban')

        headers = {
            'x-api-key': '',
        }

        response = requests.get('https://api.ibanfox.com/v1/ibans/DE89370400440532013000/validity', headers=headers)

        print(response.text)

    # https://ibanfox.com/docs/api-reference/#operation/getIbanDetails
    def test_get_getIbanDetails(self):
        print('test_get_getIbanDetails')

        headers = {
            'x-api-key': '',
        }

        response = requests.get('https://api.ibanfox.com/v1/ibans/DE89370400440532013000', headers=headers)

        print(response.text)


if __name__ == '__main__':
    unittest.main()
