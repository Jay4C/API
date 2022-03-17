import unittest
from requests_tor import RequestsTor

endpoint = "https://app.goflightlabs.com"


# https://app.goflightlabs.com/documentation
class UnitTestsFlightlabsAPIWithTorNetwork(unittest.TestCase):
    def test_Real_Time_Flights(self):
        print('test_Real_Time_Flights')

        rt = RequestsTor()

        headers = {
            'accept': "application/json",
            'content-type': "application/json"
        }

        params = {
            ('access_key', 'YOUR_ACCESS_KEY')
        }

        url = endpoint + "/flights"

        response = rt.get(url, headers=headers, params=params)

        print(response.text)

    def test_Historical_Flights(self):
        print("test_Historical_Flights")

        rt = RequestsTor()

        headers = {
            'accept': "application/json",
            'content-type': "application/json"
        }

        params = {
            ('access_key', 'YOUR_ACCESS_KEY')
        }

        url = endpoint + "/historical/2022-03-14"

        response = rt.get(url, headers=headers, params=params)

        print(response.text)

    def test_Airline_Routes(self):
        print("test_Airline_Routes")

        rt = RequestsTor()

        headers = {
            'accept': "application/json",
            'content-type': "application/json"
        }

        params = {
            ('access_key', 'YOUR_ACCESS_KEY')
        }

        url = endpoint + "/routes"

        response = rt.get(url, headers=headers, params=params)

        print(response.text)

    def test_Airports(self):
        print("test_Airports")

        rt = RequestsTor()

        headers = {
            'accept': "application/json",
            'content-type': "application/json"
        }

        params = {
            ('access_key', 'YOUR_ACCESS_KEY')
        }

        url = endpoint + "/airports"

        response = rt.get(url, headers=headers, params=params)

        print(response.text)

    def test_Airlines(self):
        print('test_Airlines')

        rt = RequestsTor()

        headers = {
            'accept': "application/json",
            'content-type': "application/json"
        }

        params = {
            ('access_key', 'YOUR_ACCESS_KEY')
        }

        url = endpoint + "/airlines"

        response = rt.get(url, headers=headers, params=params)

        print(response.text)

    def test_Airplanes(self):
        print('test_Airplanes')

        rt = RequestsTor()

        headers = {
            'accept': "application/json",
            'content-type': "application/json"
        }

        params = {
            ('access_key', 'YOUR_ACCESS_KEY')
        }

        url = endpoint + "/airplanes"

        response = rt.get(url, headers=headers, params=params)

        print(response.text)

    def test_Aircraft_Types(self):
        print('test_Aircraft_Types')

        rt = RequestsTor()

        headers = {
            'accept': "application/json",
            'content-type': "application/json"
        }

        params = {
            ('access_key', 'YOUR_ACCESS_KEY')
        }

        url = endpoint + "/aircraft_types"

        response = rt.get(url, headers=headers, params=params)

        print(response.text)

    def test_Aviation_Taxes(self):
        print("test_Aviation_Taxes")

        rt = RequestsTor()

        headers = {
            'accept': "application/json",
            'content-type': "application/json"
        }

        params = {
            ('access_key', 'YOUR_ACCESS_KEY')
        }

        url = endpoint + "/taxes"

        response = rt.get(url, headers=headers, params=params)

        print(response.text)

    def test_Cities(self):
        print("test_Cities")

        rt = RequestsTor()

        headers = {
            'accept': "application/json",
            'content-type': "application/json"
        }

        params = {
            ('access_key', 'YOUR_ACCESS_KEY')
        }

        url = endpoint + "/cities"

        response = rt.get(url, headers=headers, params=params)

        print(response.text)

    def test_Countries(self):
        print('test_Countries')

        rt = RequestsTor()

        headers = {
            'accept': "application/json",
            'content-type': "application/json"
        }

        params = {
            ('access_key', 'YOUR_ACCESS_KEY')
        }

        url = endpoint + "/countries"

        response = rt.get(url, headers=headers, params=params)

        print(response.text)


if __name__ == '__main__':
    unittest.main()
