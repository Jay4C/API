import unittest
import requests
import json


# https://api.gouv.fr/documentation/temps_reel_transport
class UnitTestsGeoApiGouvFrDecoupageAdministrative(unittest.TestCase):
    def test_first_api(self):
        print('test_first_api')

        url = "https://tr.transport.data.gouv.fr/"

        response = requests.request("GET", url)

        print(json.loads(response.text))

    def test_spec(self):
        print('test_spec')

        url = "https://tr.transport.data.gouv.fr/spec"

        response = requests.request("GET", url)

        print(json.loads(response.text))


if __name__ == '__main__':
    unittest.main()
