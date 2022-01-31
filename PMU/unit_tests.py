import unittest
from datetime import date
from requests_tor import RequestsTor


# unibet race url
global_url = "https://www.unibet.fr/turf/race/16-12-2021-R1-C4-deauville-prix-de-lhotellerie.html"


class Unit_Tests_PMU_API(unittest.TestCase):
    # ok
    def test_get_participants_with_dark_web(self):
        print("test_get_participants_with_dark_web")

        url_unibet_race = global_url

        today = date.today()

        d1 = today.strftime("%d%m%Y")

        reunion = url_unibet_race\
            .replace("https://www.unibet.fr/turf/race/", "")\
            .replace(today.strftime("%d-%m-%Y") + "-", "")\
            .replace("-", "")[:2]

        course = url_unibet_race\
            .replace("https://www.unibet.fr/turf/race/", "")\
            .replace(today.strftime("%d-%m-%Y") + "-", "")\
            .replace("-", "")[2:4]

        url = "https://offline.turfinfo.api.pmu.fr/rest/client/1/programme/" \
              + d1 + "/" \
              + reunion + "/" \
              + course + "/participants"

        headers = {
            "Accept": "application/json",
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103'
        }

        rt = RequestsTor()

        response = rt.get(url, headers=headers)

        print(response.json())

    def test_get_the_number_of_runners_with_dark_web(self):
        print('test_get_the_number_of_runners_with_dark_web')

        url_unibet_race = global_url

        today = date.today()

        d1 = today.strftime("%d%m%Y")

        reunion = url_unibet_race \
                      .replace("https://www.unibet.fr/turf/race/", "") \
                      .replace(today.strftime("%d-%m-%Y") + "-", "") \
                      .replace("-", "")[:2]

        course = url_unibet_race \
                     .replace("https://www.unibet.fr/turf/race/", "") \
                     .replace(today.strftime("%d-%m-%Y") + "-", "") \
                     .replace("-", "")[2:4]

        url = "https://offline.turfinfo.api.pmu.fr/rest/client/1/programme/" + d1 + "/" + reunion + "/" + course + "/participants"

        headers = {
            "Accept": "application/json",
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103'
        }

        rt = RequestsTor()

        response = rt.get(url, headers=headers)

        number_of_runners = len(response.json()['participants'])

        print("number_of_runners : " + str(number_of_runners))


if __name__ == '__main__':
    unittest.main()
