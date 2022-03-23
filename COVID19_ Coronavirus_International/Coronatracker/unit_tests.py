import unittest
from requests_tor import RequestsTor

endpoint = "http://api.coronatracker.com"


# https://api.coronatracker.com/#api-Analytics-FetchAffectedCountries
class UnitTestsCoronatrackerAPIAnalyticsWithTorNetwork(unittest.TestCase):
    def test_Analytics_By_country(self):
        print('test_Analytics_By_country')

        rt = RequestsTor()

        headers = {
            'accept': "application/json",
            'content-type': "application/json"
        }

        url = endpoint + "/v2/analytics/country"

        response = rt.get(url, headers=headers)

        print(response.text)

    def test_Analytics_By_new_daily_cases_and_deaths(self):
        print("test_Analytics_By_new_daily_cases_and_deaths")

        rt = RequestsTor()

        headers = {
            'accept': "application/json",
            'content-type': "application/json"
        }

        url = endpoint + "/v5/analytics/dailyNewStats"

        response = rt.get(url, headers=headers)

        print(response.text)

    def test_Analytics_get_daily_new_incidences_of_a_country_between_start_and_end_dates(self):
        print("test_Analytics_get_daily_new_incidences_of_a_country_between_start_and_end_dates")

        rt = RequestsTor()

        headers = {
            'accept': "application/json",
            'content-type': "application/json"
        }

        params = {
            'countryCode': 'FR',
            'startDate': '2020-01-01',
            'endDate': '2022-01-01'
        }

        url = endpoint + "/v5/analytics/newcases/country"

        response = rt.get(url, headers=headers, params=params)

        print(response.text)

    def test_Analytics_get_data_of_a_country_between_start_and_end_dates(self):
        print('test_Analytics_get_data_of_a_country_between_start_and_end_dates')

        rt = RequestsTor()

        headers = {
            'accept': "application/json",
            'content-type': "application/json"
        }

        params = {
            'countryCode': 'FR',
            'startDate': '2020-01-01',
            'endDate': '2022-01-01'
        }

        url = endpoint + "/v5/analytics/trend/country"

        response = rt.get(url, headers=headers, params=params)

        print(response.text)


class UnitTestsCoronatrackerAPICacheWithTorNetwork(unittest.TestCase):
    def test_Cache_Clear_cache(self):
        print('test_Cache_Clear_cache')

        rt = RequestsTor()

        headers = {
            'accept': "application/json",
            'content-type': "application/json"
        }

        params = {
            'key': 'aaa'
        }

        url = endpoint + "/v2/cache/clear"

        response = rt.get(url, headers=headers, params=params)

        print(response.text)


class UnitTestsCoronatrackerAPIHealthcareInstitutionWithTorNetwork(unittest.TestCase):
    def test_Healthcare_Institution_List(self):
        print("test_Healthcare_Institution_List")

        rt = RequestsTor()

        headers = {
            'accept': "application/json",
            'content-type': "application/json"
        }

        url = endpoint + "/v1/healthcare-institution"

        response = rt.get(url, headers=headers)

        print(response.text)


class UnitTestsCoronatrackerAPIMiscellaneousWithTorNetwork(unittest.TestCase):
    def test_Miscellaneous_Health_check(self):
        print("test_Miscellaneous_Health_check")

        rt = RequestsTor()

        headers = {
            'accept': "application/json",
            'content-type': "application/json"
        }

        url = endpoint + "/health"

        response = rt.get(url, headers=headers)

        print(response.text)

    def test_Miscellaneous_Timestamp_cache(self):
        print("test_Miscellaneous_Timestamp_cache")

        rt = RequestsTor()

        headers = {
            'accept': "application/json",
            'content-type': "application/json"
        }

        url = endpoint + "/timestamp-cache"

        response = rt.get(url, headers=headers)

        print(response.text)

    def test_Miscellaneous_Timestamp(self):
        print("test_Miscellaneous_Timestamp")

        rt = RequestsTor()

        headers = {
            'accept': "application/json",
            'content-type': "application/json"
        }

        url = endpoint + "/timestamp"

        response = rt.get(url, headers=headers)

        print(response.text)


class UnitTestsCoronatrackerAPINewsWithTorNetwork(unittest.TestCase):
    def test_News_List(self):
        print("test_News_List")

        rt = RequestsTor()

        headers = {
            'accept': "application/json",
            'content-type': "application/json"
        }

        url = endpoint + "/news/trending"

        response = rt.get(url, headers=headers)

        print(response.text)


class UnitTestsCoronatrackerAPIStatsWithTorNetwork(unittest.TestCase):
    def test_Stats(self):
        print("test_Stats")

        rt = RequestsTor()

        headers = {
            'accept': "application/json",
            'content-type': "application/json"
        }

        params = {
            'country': 'FR'
        }

        url = endpoint + "/v3/stats"

        response = rt.get(url, headers=headers, params=params)

        print(response.text)

    def test_Stats_Returns_total_trending_cases(self):
        print("test_Stats_Returns_total_trending_cases")

        rt = RequestsTor()

        headers = {
            'accept': "application/json",
            'content-type': "application/json"
        }

        params = {
            'limit': 10
        }

        url = endpoint + "/v3/stats/worldometer/totalTrendingCases"

        response = rt.get(url, headers=headers, params=params)

        print(response.text)

    def test_Stats_Custom_for_debug(self):
        print('test_Stats_Custom_for_debug')

        rt = RequestsTor()

        headers = {
            'accept': "application/json",
            'content-type': "application/json"
        }

        url = endpoint + "/v3/stats/custom-debug"

        response = rt.get(url, headers=headers)

        print(response.text)


class UnitTestsCoronatrackerAPIStatsWorldometerWithTorNetwork(unittest.TestCase):
    def test_Stats_Worldometer_Global_Stats_Overview(self):
        print("test_Stats_Worldometer_Global_Stats_Overview")

        rt = RequestsTor()

        headers = {
            'accept': "application/json",
            'content-type': "application/json"
        }

        url = endpoint + "/v3/stats/worldometer/global"

        response = rt.get(url, headers=headers)

        print(response.text)

    def test_Stats_Worldometer_all_country_or_country_specific_stats(self):
        print("test_Stats_Worldometer_all_country_or_country_specific_stats")

        rt = RequestsTor()

        headers = {
            'accept': "application/json",
            'content-type': "application/json"
        }

        params = {
            'countryCode': 'FR'
        }

        url = endpoint + "/v3/stats/worldometer/country"

        response = rt.get(url, headers=headers, params=params)

        print(response.text)


class UnitTestsCoronatrackerAPITravelAlertWithTorNetwork(unittest.TestCase):
    def test_Travel_Alert_List(self):
        print("test_Travel_Alert_List")

        rt = RequestsTor()

        headers = {
            'accept': "application/json",
            'content-type': "application/json"
        }

        url = endpoint + "/v1/travel-alert"

        response = rt.get(url, headers=headers)

        print(response.text)


if __name__ == '__main__':
    unittest.main()
