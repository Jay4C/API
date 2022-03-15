import unittest
from requests_tor import RequestsTor


# https://ip-fast.com/docs/
class UnitTestsIpFastWithTorNetwork(unittest.TestCase):
    def test_get_ip(self):
        print("test_get_ip")

        headers = {
            "Accept": "application/json",
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103'
        }

        rt = RequestsTor()

        r = rt.get("https://ip-fast.com/api/ip/?format=json&location=True", headers=headers)

        print(r.text)


if __name__ == '__main__':
    unittest.main()
