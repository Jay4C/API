import unittest
import requests

endpoint = "https://philosophy-quotes-api.glitch.me"


# https://github.com/KaranDahiya/philosophy-quotes-API
class UnitTestsPhilosophyQuotesAPI(unittest.TestCase):
    def test_retrieves_all_quotes(self):
        print('test_retrieves_all_quotes')

        url = endpoint + "/quotes"

        response = requests.get(url)

        print(response.text)

    def test_retrieves_quotes_by_author(self):
        print("test_retrieves_quotes_by_author")

        param = "Rumi"

        url = endpoint + "/quotes/author/" + param

        response = requests.get(url)

        print(response.text)

    def test_retrieves_quotes_by_philosophy(self):
        print("test_retrieves_quotes_by_philosophy")

        param = "Stoicism"

        url = endpoint + "/quotes/philosophy/" + param

        response = requests.get(url)

        print(response.text)


if __name__ == '__main__':
    unittest.main()
