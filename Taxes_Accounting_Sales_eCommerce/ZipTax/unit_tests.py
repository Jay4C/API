import unittest
from requests_tor import RequestsTor

endpoint = "https://api.zip-tax.com/request/v40"
key = ''


# http://www.zip-tax.com/documentation/
class UnitTestsZipTaxAPIWithTorRequest(unittest.TestCase):
    def test_Request(self):
        print("test_Request")

        headers = {
            "Accept": "application/json"
        }

        url = endpoint

        rt = RequestsTor()

        r = rt.get(url, headers=headers)

        print(r.text)

    def test_Core_Plan_Level_API_Request(self):
        print("test_Core_Plan_Level_API_Request")

        headers = {
            "Accept": "application/json"
        }

        params = {
            'key': key,
            'postalcode': 'postalcode'
        }

        url = endpoint

        rt = RequestsTor()

        r = rt.get(url, headers=headers, params=params)

        print(r.text)

    def test_Geo_Plan_Level_API_Request(self):
        print("test_Geo_Plan_Level_API_Request")

        headers = {
            "Accept": "application/json"
        }

        params = {
            'key': key,
            'address': 'address'
        }

        url = endpoint

        rt = RequestsTor()

        r = rt.get(url, headers=headers, params=params)

        print(r.text)


if __name__ == '__main__':
    unittest.main()
