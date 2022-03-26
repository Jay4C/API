import unittest
from requests_tor import RequestsTor

endpoint = "https://global-warming.org"


# https://global-warming.org/
class UnitTestsGlobalWarmingAPI(unittest.TestCase):
    def test_get_Global_temperature_anomalies_from_year_1_to_present(self):
        print('test_get_Global_temperature_anomalies_from_year_1_to_present')

        rt = RequestsTor()

        headers = {
            'content-type': "application/json"
        }

        url = endpoint + "/api/temperature-api"

        response = rt.get(url, headers=headers)

        print(response.text)

    def test_Carbon_Dioxide_levels_from_800000_years_ago_to_present(self):
        print('test_Carbon_Dioxide_levels_from_800000_years_ago_to_present')

        rt = RequestsTor()

        headers = {
            'content-type': "application/json"
        }

        url = endpoint + "/api/co2-api"

        response = rt.get(url, headers=headers)

        print(response.text)

    def test_Methane_levels_from_800000_years_ago_to_present(self):
        print("test_Methane_levels_from_800000_years_ago_to_present")

        rt = RequestsTor()

        headers = {
            'content-type': "application/json"
        }

        url = endpoint + "/api/methane-api"

        response = rt.get(url, headers=headers)

        print(response.text)

    def test_Nitrous_Oxide_levels_from_800000_years_ago_to_present(self):
        print("test_Nitrous_Oxide_levels_from_800000_years_ago_to_present")

        rt = RequestsTor()

        headers = {
            'content-type': "application/json"
        }

        url = endpoint + "/api/nitrous-oxide-api"

        response = rt.get(url, headers=headers)

        print(response.text)

    def test_Melted_Polar_Ice_Caps(self):
        print("test_Melted_Polar_Ice_Caps")

        rt = RequestsTor()

        headers = {
            'content-type': "application/json"
        }

        url = endpoint + "/api/arctic-api"

        response = rt.get(url, headers=headers)

        print(response.text)


if __name__ == '__main__':
    unittest.main()
