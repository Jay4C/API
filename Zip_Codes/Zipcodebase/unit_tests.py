import unittest
import requests

endpoint = "https://app.zipcodebase.com/api/v1"
apikey = ""


# https://app.zipcodebase.com/documentation
class UnitTestsZipcodebaseWithTorNetwork(unittest.TestCase):
    def test_Authentification_Remaining_Credits(self):
        print("test_Authentification_Remaining_Credits")

        headers = {
            'apikey': apikey
        }

        url = endpoint + "/status"

        r = requests.get(url, headers=headers)

        print(r.text)

    def test_Postal_code_to_location_information(self):
        print("test_Postal_code_to_location_information")

        headers = {
            'apikey': apikey
        }

        params = (
            ("codes", "10005,51503"),
        )

        url = endpoint + "/search"

        r = requests.get(url, headers=headers, params=params)

        print(r.text)

    def test_Distance_calculation_between_postal_codes(self):
        print("test_Distance_calculation_between_postal_codes")

        headers = {
            'apikey': apikey
        }

        params = (
            ("code", "10005"),
            ("compare", "10006,10007"),
            ("country", "us"),
        )

        url = endpoint + "/distance"

        r = requests.get(url, headers=headers, params=params)

        print(r.text)

    def test_Postal_codes_within_a_radius(self):
        print("test_Postal_codes_within_a_radius")

        headers = {
            'apikey': apikey
        }

        params = (
            ("code", "10005"),
            ("radius", "100"),
            ("country", "us"),
        )

        url = endpoint + "/radius"

        r = requests.get(url, headers=headers, params=params)

        print(r.text)

    def test_Postal_codes_within_a_certain_distance(self):
        print("test_Postal_codes_within_a_certain_distance")

        headers = {
            'apikey': apikey
        }

        params = (
            ("codes", "10005,10006,10009,90001"),
            ("distance", "100"),
            ("country", "us"),
        )

        url = endpoint + "/match"

        r = requests.get(url, headers=headers, params=params)

        print(r.text)

    def test_Postal_codes_by_city(self):
        print("test_Postal_codes_by_city")

        headers = {
            'apikey': apikey
        }

        params = (
            ("city", "Amsterdam"),
            ("state_name", "Noord-Holland"),
            ("country", "nl"),
        )

        url = endpoint + "/code/city"

        r = requests.get(url, headers=headers, params=params)

        print(r.text)

    def test_Postal_codes_by_state(self):
        print("test_Postal_codes_by_state")

        headers = {
            'apikey': apikey
        }

        params = (
            ("state_name", "Noord-Holland"),
            ("country", "nl"),
        )

        url = endpoint + "/code/state"

        r = requests.get(url, headers=headers, params=params)

        print(r.text)

    def test_Provinces_states_of_a_country(self):
        print("test_Provinces_states_of_a_country")

        headers = {
            'apikey': apikey
        }

        params = (
            ("country", "de"),
        )

        url = endpoint + "/country/province"

        r = requests.get(url, headers=headers, params=params)

        print(r.text)


if __name__ == '__main__':
    unittest.main()
