import unittest
import requests


class UnitTestsFreeIPGeolocationAPI(unittest.TestCase):
    def test_get_my_ip(self):
        print('test_get_my_ip')

        url = "https://freegeoip.app/json/"

        headers = {
            'accept': "application/json",
            'content-type': "application/json"
        }

        response = requests.request("GET", url, headers=headers)

        print(response.text)


if __name__ == '__main__':
    unittest.main()
