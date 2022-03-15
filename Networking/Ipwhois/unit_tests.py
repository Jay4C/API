import unittest
from requests_tor import RequestsTor


# https://ipwhois.io/documentation
class UnitTestsIpwhoisWithTorNetwork(unittest.TestCase):
    def test_get_ip_information(self):
        print("test_get_ip_information")

        headers = {
            "Accept": "application/json",
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103'
        }

        rt = RequestsTor()

        ip = "102.135.232.0"

        r = rt.get("http://ipwhois.app/json/" + ip, headers=headers)

        print(r.json())


if __name__ == '__main__':
    unittest.main()
