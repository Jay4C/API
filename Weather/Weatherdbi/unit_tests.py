import unittest
from requests_tor import RequestsTor


# https://weatherdbi.herokuapp.com/documentation/v1
class UnitTestsWeatherdbiWithTorNetwork(unittest.TestCase):
    def test_get_weather_with_location(self):
        print("test_get_weather_with_location")

        rt = RequestsTor()

        location = "paris"

        r = rt.get("https://weatherdbi.herokuapp.com/data/weather/" + location)

        data = r.json()

        print(data)


if __name__ == '__main__':
    unittest.main()
