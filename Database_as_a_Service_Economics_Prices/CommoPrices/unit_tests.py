import unittest
from requests_tor import RequestsTor

endpoint = "https://api.commoprices.com"
api_key = ""


# https://api.commoprices.com/docs/v2?javascript#Introduction
class UnitTestsCommopricesAPIWithTorRequest(unittest.TestCase):
    def test_Authentication(self):
        print("test_Authentication")

        url = endpoint

        rt = RequestsTor()

        headers = {
            'authorization': 'Bearer ' + api_key,
            'accept': "application/json"
        }

        response = rt.request("GET", url, headers=headers)

        print(response.text)


class UnitTestsCommopricesAPI0WithTorRequest(unittest.TestCase):
    def test_Get_open_dataseries(self):
        print("test_Get_open_dataseries")

        url = endpoint + '/v2/open'

        rt = RequestsTor()

        headers = {
            'authorization': 'Bearer ' + api_key,
            'accept': "application/json"
        }

        response = rt.request("GET", url, headers=headers)

        print(response.text)

    def test_Get_all_dataseries(self):
        print("test_Get_all_dataseries")

        url = endpoint + '/v2/all'

        rt = RequestsTor()

        headers = {
            'authorization': 'Bearer ' + api_key,
            'accept': "application/json"
        }

        response = rt.request("GET", url, headers=headers)

        print(response.text)


class UnitTestsCommopricesAPI1WithTorRequest(unittest.TestCase):
    def test_GET_infos_for_all_commodities(self):
        print("test_GET_infos_for_all_commodities")

        url = endpoint + '/v2/prices'

        rt = RequestsTor()

        headers = {
            'authorization': 'Bearer ' + api_key,
            'accept': "application/json"
        }

        response = rt.request("GET", url, headers=headers)

        print(response.text)

    def test_GET_info_for_one_commodity(self):
        print("test_GET_info_for_one_commodity")

        url = endpoint + '/v2/dataseries/JMQWQ'

        rt = RequestsTor()

        headers = {
            'authorization': 'Bearer ' + api_key,
            'accept': "application/json"
        }

        response = rt.request("GET", url, headers=headers)

        print(response.text)

    def test_GET_data_for_one_commodity(self):
        print("test_GET_data_for_one_commodity")

        url = endpoint + '/v2/dataseries/JMQWQ/data'

        rt = RequestsTor()

        headers = {
            'authorization': 'Bearer ' + api_key,
            'accept': "application/json"
        }

        response = rt.request("GET", url, headers=headers)

        print(response.text)


class UnitTestsCommopricesAPI2WithTorRequest(unittest.TestCase):
    def test_GET_infos_for_all_indexes(self):
        print("test_GET_infos_for_all_indexes")

        url = endpoint + '/v2/trades'

        rt = RequestsTor()

        headers = {
            'authorization': 'Bearer ' + api_key,
            'accept': "application/json"
        }

        response = rt.request("GET", url, headers=headers)

        print(response.text)

    def test_GET_info_for_one_index(self):
        print("test_GET_info_for_one_index")

        url = endpoint + '/v2/dataseries/SAYBQ'

        rt = RequestsTor()

        headers = {
            'authorization': 'Bearer ' + api_key,
            'accept': "application/json"
        }

        response = rt.request("GET", url, headers=headers)

        print(response.text)

    def test_GET_data_for_one_index(self):
        print("test_GET_data_for_one_index")

        url = endpoint + '/v2/dataseries/SAYBQ/data'

        rt = RequestsTor()

        headers = {
            'authorization': 'Bearer ' + api_key,
            'accept': "application/json"
        }

        response = rt.request("GET", url, headers=headers)

        print(response.text)


class UnitTestsCommopricesAPI3WithTorRequest(unittest.TestCase):
    def test_GET_infos_for_all_commodities(self):
        print("test_GET_infos_for_all_commodities")

        url = endpoint + '/v2/trades'

        rt = RequestsTor()

        headers = {
            'authorization': 'Bearer ' + api_key,
            'accept': "application/json"
        }

        response = rt.request("GET", url, headers=headers)

        print(response.text)

    def test_GET_info_for_one_commodity(self):
        print("test_GET_info_for_one_commodity")

        url = endpoint + '/v2/dataseries/ZQTLR'

        rt = RequestsTor()

        headers = {
            'authorization': 'Bearer ' + api_key,
            'accept': "application/json"
        }

        response = rt.request("GET", url, headers=headers)

        print(response.text)

    def test_GET_data_for_one_commodity(self):
        print("test_GET_data_for_one_commodity")

        url = endpoint + '/v2/dataseries/ZQTLR/data'

        rt = RequestsTor()

        headers = {
            'authorization': 'Bearer ' + api_key,
            'accept': "application/json"
        }

        response = rt.request("GET", url, headers=headers)

        print(response.text)


class UnitTestsCommopricesAPIQueryParametersWithTorRequest(unittest.TestCase):
    def test_Query_parameters(self):
        print("test_Query_parameters")

        url = endpoint + '/v2/dataseries/ZQTLR/data'

        rt = RequestsTor()

        headers = {
            'authorization': 'Bearer ' + api_key,
            'accept': "application/json"
        }

        params = {
            'lang': 'fr',
            'start_date': '2017-01-01',
            'currency': 'GBP'
        }

        response = rt.request("GET", url, headers=headers, params=params)

        print(response.text)


if __name__ == '__main__':
    unittest.main()
