import unittest
from requests_tor import RequestsTor

endpoint = "https://bayut.p.rapidapi.com"
key = ''


# https://rapidapi.com/apidojo/api/bayut/
class UnitTestsBayutAPIWithTorRequest(unittest.TestCase):
    def test_List_agencies_or_search_for_agencies_by_name(self):
        print("test_List_agencies_or_search_for_agencies_by_name")

        headers = {
            "Accept": "application/json",
            'x-rapidapi-host': "bayut.p.rapidapi.com",
            'x-rapidapi-key': key
        }

        querystring = {
            "query": "patriot",
            "hitsPerPage": "25",
            "page": "0",
            "lang": "en"
        }

        url = endpoint + "/agencies/list"

        rt = RequestsTor()

        r = rt.get(url, headers=headers, params=querystring)

        print(r.text)

    def test_Get_detail_information_of_a_property(self):
        print("test_Get_detail_information_of_a_property")

        headers = {
            "Accept": "application/json",
            'x-rapidapi-host': "bayut.p.rapidapi.com",
            'x-rapidapi-key': key
        }

        querystring = {
            "externalID": "4937770"
        }

        url = endpoint + "/properties/detail"

        rt = RequestsTor()

        r = rt.get(url, headers=headers, params=querystring)

        print(r.text)

    def test_List_properties_with_options_and_filters(self):
        print("test_List_properties_with_options_and_filters")

        headers = {
            "Accept": "application/json",
            'x-rapidapi-host': "bayut.p.rapidapi.com",
            'x-rapidapi-key': key
        }

        querystring = {
            "locationExternalIDs": "5002,6020",
            "purpose": "for-rent",
            "hitsPerPage": "25",
            "page": "0",
            "lang": "en",
            "sort": "city-level-score",
            "rentFrequency": "monthly",
            "categoryExternalID": "4"
        }

        url = endpoint + "/properties/list"

        rt = RequestsTor()

        r = rt.get(url, headers=headers, params=querystring)

        print(r.text)

    def test_Get_suggestions_of_locations_by_term_or_phrase(self):
        print("test_Get_suggestions_of_locations_by_term_or_phrase")

        headers = {
            "Accept": "application/json",
            'x-rapidapi-host': "bayut.p.rapidapi.com",
            'x-rapidapi-key': key
        }

        querystring = {
            "query": "abu dhabi",
            "hitsPerPage": "25",
            "page": "0",
            "lang": "en"
        }

        url = endpoint + "/auto-complete"

        rt = RequestsTor()

        r = rt.get(url, headers=headers, params=querystring)

        print(r.text)


if __name__ == '__main__':
    unittest.main()
