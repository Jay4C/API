import json
import unittest
import requests


# http://worldtimeapi.org/
class UnitTestsWorldTimeApi(unittest.TestCase):
    # http://worldtimeapi.org/api/timezone
    def test_request_a_list_of_valid_timezones_as_json(self):
        print('test_request_a_list_of_valid_timezones_as_json')

        url = "http://worldtimeapi.org/api/timezone"

        response = requests.request("GET", url)

        print(json.loads(response.text))

    # http://worldtimeapi.org/api/timezone/:area
    def test_request_a_list_of_valid_locations_for_an_area_as_json(self):
        print('test_request_a_list_of_valid_locations_for_an_area_as_json')

        url = "http://worldtimeapi.org/api/timezone/Europe"

        response = requests.request("GET", url)

        print(json.loads(response.text))

    # http://worldtimeapi.org/api/timezone/:area/:location[/:region]
    def test_request_the_current_time_for_a_timezone_as_json(self):
        print('test_request_the_current_time_for_a_timezone_as_json')

        url = "http://worldtimeapi.org/api/timezone/Europe/London"

        # url = "http://worldtimeapi.org/api/timezone/America/Argentina/Salta"

        response = requests.request("GET", url)

        print(json.loads(response.text))

    # http://worldtimeapi.org/api/ip
    def test_request_the_current_time_based_on_your_public_ip_as_json(self):
        print('test_request_the_current_time_based_on_your_public_ip_as_json')

        url = "http://worldtimeapi.org/api/ip"

        response = requests.request("GET", url)

        print(json.loads(response.text))

    # http://worldtimeapi.org/api/ip/:ipv4
    def test_request_the_current_time_for_a_specific_ip_as_json(self):
        print('test_request_the_current_time_for_a_specific_ip_as_json')

        url = "http://worldtimeapi.org/api/ip/216.58.201.78"

        response = requests.request("GET", url)

        print(json.loads(response.text))


if __name__ == '__main__':
    unittest.main()
