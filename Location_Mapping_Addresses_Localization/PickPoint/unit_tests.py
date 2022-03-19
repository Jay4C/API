import unittest
from requests_tor import RequestsTor

endpoint = "https://api.pickpoint.io/v1"
key = ""


# https://pickpoint.io/api-reference
class UnitTestsPickPointAPIWithTorRequest(unittest.TestCase):
    def test_AUTHENTICATION(self):
        print("test_AUTHENTICATION")

        url = endpoint + "/"

        params = {
            ('key', key)
        }

        rt = RequestsTor()

        r = rt.get(url, params=params)

        data = r.json()

        print(data)

    def test_FORWARD_GEOCODING(self):
        print("test_FORWARD_GEOCODING")

        url = endpoint + "/forward"

        params = {
            ('key', key),
            ('city', 'Saint-Petersburg')
        }

        rt = RequestsTor()

        r = rt.get(url, params=params)

        data = r.json()

        print(data)

    def test_REVERSE_GEOCODING(self):
        print("test_REVERSE_GEOCODING")

        url = endpoint + "/reverse"

        params = {
            ('key', key),
            ('lat', '48.85881005'),
            ('lon', '2.32003101155031'),
            ('zoom', '0')
        }

        rt = RequestsTor()

        r = rt.get(url, params=params)

        data = r.json()

        print(data)

    def test_ADDRESS_LOOKUP(self):
        print("test_ADDRESS_LOOKUP")

        url = endpoint + "/lookup"

        params = {
            ('key', key),
            ('osm_ids', 'W481027013,N1809771508,R568660')
        }

        rt = RequestsTor()

        r = rt.get(url, params=params)

        data = r.json()

        print(data)

    def test_RESPONSE_FORMAT(self):
        print("test_RESPONSE_FORMAT")

        url = endpoint + "/forward"

        params = {
            ('key', key),
            ('q', 'Tokyo'),
            ('format', 'json')
        }

        rt = RequestsTor()

        r = rt.get(url, params=params)

        data = r.json()

        print(data)

    def test_LOCALIZATION(self):
        print('test_LOCALIZATION')

        url = endpoint + "/forward"

        params = {
            ('key', key),
            ('q', 'Tokyo'),
            ('accept-language', 'en')
        }

        rt = RequestsTor()

        r = rt.get(url, params=params)

        data = r.json()

        print(data)

    def test_EXTENDED_RESPONSE_v1(self):
        print("test_EXTENDED_RESPONSE_v1")

        url = endpoint + "/reverse"

        params = {
            ('key', key),
            ('lat', '48.8698899'),
            ('lon', '2.3084521'),
            ('zoom', '1'),
            ('addressdetails', '1')
        }

        rt = RequestsTor()

        r = rt.get(url, params=params)

        data = r.json()

        print(data)

    def test_EXTENDED_RESPONSE_v2(self):
        print("test_EXTENDED_RESPONSE_v2")

        url = endpoint + "/lookup"

        params = {
            ('key', key),
            ('osm_ids', 'R2360164'),
            ('namedetails', '1')
        }

        rt = RequestsTor()

        r = rt.get(url, params=params)

        data = r.json()

        print(data)

    def test_OUTPUT_GEOMETRY(self):
        print("test_OUTPUT_GEOMETRY")

        url = endpoint + "/forward"

        params = {
            ('key', key),
            ('q', 'Tokyo'),
            ('format', 'json')
        }

        rt = RequestsTor()

        r = rt.get(url, params=params)

        data = r.json()

        print(data)


if __name__ == '__main__':
    unittest.main()
