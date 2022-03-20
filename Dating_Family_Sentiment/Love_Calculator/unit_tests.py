import unittest
from requests_tor import RequestsTor

endpoint = "https://love-calculator.p.rapidapi.com"
api_key = ""


# https://rapidapi.com/ajith/api/love-calculator
class UnitTestsLoveCalculatorAPIWithTorRequest(unittest.TestCase):
    def test_getPercentage(self):
        print("test_getPercentage")

        url = endpoint + "/getPercentage"

        rt = RequestsTor()

        querystring = {
            "sname": "Alice",
            "fname": "John"
        }

        headers = {
            'x-rapidapi-host': "love-calculator.p.rapidapi.com",
            'x-rapidapi-key': api_key
        }

        response = rt.request("GET", url, headers=headers, params=querystring)

        print(response.text)


if __name__ == '__main__':
    unittest.main()
