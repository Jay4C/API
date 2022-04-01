import unittest
from requests_tor import RequestsTor


# https://www.fishwatch.gov/resources
class UnitTestsFishbaseAPI(unittest.TestCase):
    def test_Single_species_example(self):
        print('test_Single_species_example')

        rt = RequestsTor()

        response = rt.get("https://www.fishwatch.gov/api/species/red-snapper")

        print(response.text)

    def test_All_species_API_call(self):
        print("test_All_species_API_call")

        rt = RequestsTor()

        response = rt.get("https://www.fishwatch.gov/api/species")

        print(response.text)


if __name__ == '__main__':
    unittest.main()
