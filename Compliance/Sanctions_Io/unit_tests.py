import unittest
from requests_tor import RequestsTor

endpoint = "https://api.sanctions.io"
api_token = ""


# https://api.sanctions.io
class UnitTestsSanctionIoAPISearches(unittest.TestCase):
    def test_get_search_for_sanctions_and_police_records(self):
        print('test_get_search_for_sanctions_and_police_records')

        rt = RequestsTor()

        headers = {
            'Accept': "application/json; version=1.8",
            'Authorization': 'Bearer ' + api_token
        }

        params = {
            'name': 'name'
        }

        url = endpoint + "/search/"

        response = rt.get(url, headers=headers, params=params)

        print(response.text)

    def test_get_search_for_PEP_records(self):
        print('test_get_search_for_PEP_records')

        rt = RequestsTor()

        headers = {
            'Accept': "application/json; version=1.8",
            'Authorization': 'Bearer ' + api_token
        }

        params = {
            'name': 'name'
        }

        url = endpoint + "/pep-search/"

        response = rt.get(url, headers=headers, params=params)

        print(response.text)

    def test_get_full_database_export(self):
        print('test_get_full_database_export')

        rt = RequestsTor()

        headers = {
            'Accept': "application/json; version=1.8",
            'Authorization': 'Bearer ' + api_token
        }

        url = endpoint + "/exporter/"

        response = rt.get(url, headers=headers)

        print(response.text)


class UnitTestsSanctionIoAPIBackoffice(unittest.TestCase):
    def test_get_shows_your_current_plan_status(self):
        print('test_get_shows_your_current_plan_status')

        rt = RequestsTor()

        headers = {
            'Accept': "application/json; version=1.8",
            'Authorization': 'Bearer ' + api_token
        }

        url = endpoint + "/plans/"

        response = rt.get(url, headers=headers)

        print(response.text)

    def test_get_Check_your_historic_searches(self):
        print("test_get_Check_your_historic_searches")

        rt = RequestsTor()

        headers = {
            'Accept': "application/json; version=1.8",
            'Authorization': 'Bearer ' + api_token
        }

        url = endpoint + "/searches/historic"

        response = rt.get(url, headers=headers)

        print(response.text)

    def test_get_List_of_tokens_available_for_user(self):
        print('test_get_List_of_tokens_available_for_user')

        rt = RequestsTor()

        headers = {
            'Accept': "application/json; version=1.8",
            'Authorization': 'Bearer ' + api_token
        }

        url = endpoint + "/tokens"

        response = rt.get(url, headers=headers)

        print(response.text)

    def test_delete_Delete_the_token_specified_by_its_key(self):
        print('test_delete_Delete_the_token_specified_by_its_key')

        rt = RequestsTor()

        headers = {
            'Accept': "application/json; version=1.8",
            'Authorization': 'Bearer ' + api_token
        }

        tokenKey = ""

        url = endpoint + "/tokens/" + tokenKey

        response = rt.delete(url, headers=headers)

        print(response.text)


class UnitTestsSanctionIoAPISources(unittest.TestCase):
    def test_get_list_of_sources_available(self):
        print('test_get_list_of_sources_available')

        rt = RequestsTor()

        headers = {
            'Accept': "application/json; version=1.8",
            'Authorization': 'Bearer ' + api_token
        }

        url = endpoint + "/sources/"

        response = rt.get(url, headers=headers)

        print(response.text)

    def test_get_list_of_programs_available(self):
        print("test_get_list_of_programs_available")

        rt = RequestsTor()

        headers = {
            'Accept': "application/json; version=1.8",
            'Authorization': 'Bearer ' + api_token
        }

        url = endpoint + "/programs/"

        response = rt.get(url, headers=headers)

        print(response.text)


if __name__ == '__main__':
    unittest.main()
