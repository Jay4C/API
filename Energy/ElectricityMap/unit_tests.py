import unittest
from requests_tor import RequestsTor


# https://static.electricitymap.org/api/docs/index.html#introduction
class UnitTestsElectricityMapAPIAuthenticationWithTorRequest(unittest.TestCase):
    def test_Authentication(self):
        print("test_Authentication")

        rt = RequestsTor()

        headers = {
            'auth-token': 'myapitoken',
        }

        params = (
            ('zone', 'DE'),
        )

        response = rt.get('https://api.electricitymap.org/v3/carbon-intensity/latest',
                          headers=headers, params=params)

        data = response.json()

        print(data)


class UnitTestsElectricityMapAPIRoutesWithTorRequest(unittest.TestCase):
    def test_Zones(self):
        print("test_Zones")

        rt = RequestsTor()

        response = rt.get('https://api.electricitymap.org/v3/zones')

        data = response.json()

        print(data)

    def test_Live_carbon_intensity(self):
        print("test_Live_carbon_intensity")

        rt = RequestsTor()

        headers = {
            'auth-token': 'myapitoken',
        }

        params = (
            ('zone', 'DE'),
        )

        response = rt.get('https://api.electricitymap.org/v3/carbon-intensity/latest', headers=headers, params=params)

        data = response.json()

        print(data)

    def test_Live_power_breakdown(self):
        print("test_Live_power_breakdown")

        rt = RequestsTor()

        headers = {
            'auth-token': 'myapitoken',
        }

        params = (
            ('lat', '48.8566'),
            ('lon', '2.3522'),
        )

        response = rt.get('https://api.electricitymap.org/v3/power-breakdown/latest', headers=headers, params=params)

        data = response.json()

        print(data)

    def test_Recent_carbon_intensity_history(self):
        print("test_Recent_carbon_intensity_history")

        rt = RequestsTor()

        headers = {
            'auth-token': 'myapitoken',
        }

        params = (
            ('zone', 'DE'),
        )

        response = rt.get('https://api.electricitymap.org/v3/carbon-intensity/history', headers=headers,
                                params=params)

        data = response.json()

        print(data)

    def test_Recent_power_breakdown_history(self):
        print("test_Recent_power_breakdown_history")

        rt = RequestsTor()

        headers = {
            'auth-token': 'myapitoken',
        }

        params = (
            ('lat', '55.588189'),
            ('lon', '9.16826'),
        )

        response = rt.get('https://api.electricitymap.org/v3/power-breakdown/history', headers=headers,
                                params=params)

        data = response.json()

        print(data)

    def test_Past_carbon_intensity_history(self):
        print("test_Past_carbon_intensity_history")

        rt = RequestsTor()

        headers = {
            'auth-token': 'myapitoken',
        }

        params = (
            ('zone', 'DE'),
            ('datetime', '2019-05-21T00:00:00Z'),
        )

        response = rt.get('https://api.electricitymap.org/v3/carbon-intensity/past', headers=headers,
                                params=params)

        data = response.json()

        print(data)

    def test_Past_carbon_intensity_history_range(self):
        print("test_Past_carbon_intensity_history_range")

        rt = RequestsTor()

        headers = {
            'auth-token': 'myapitoken',
        }

        params = (
            ('zone', 'DE'),
            ('start', '2019-05-21T21:00:00Z'),
            ('end', '2019-05-22T00:00:00Z'),
        )

        response = rt.get('https://api.electricitymap.org/v3/carbon-intensity/past-range', headers=headers,
                                params=params)

        data = response.json()

        print(data)

    def test_Past_power_breakdown_history(self):
        print("test_Past_power_breakdown_history")

        rt = RequestsTor()

        headers = {
            'auth-token': 'myapitoken',
        }

        params = (
            ('zone', 'DK-DK1'),
            ('datetime', '2020-01-04T00:00:00Z'),
        )

        response = rt.get('https://api.electricitymap.org/v3/power-breakdown/past', headers=headers,
                                params=params)

        data = response.json()

        print(data)

    def test_Past_power_breakdown_history_range(self):
        print("test_Past_power_breakdown_history_range")

        rt = RequestsTor()

        headers = {
            'auth-token': 'myapitoken',
        }

        params = (
            ('zone', 'DK-DK1'),
            ('start', '2020-01-04T00:00:00Z'),
            ('end', '2020-01-04T01:00:00Z'),
        )

        response = rt.get('https://api.electricitymap.org/v3/power-breakdown/past-range', headers=headers,
                                params=params)

        data = response.json()

        print(data)

    def test_Forecasted_carbon_intensity(self):
        print("test_Forecasted_carbon_intensity")

        rt = RequestsTor()

        headers = {
            'auth-token': 'myapitoken',
        }

        params = (
            ('zone', 'DK-DK2'),
        )

        response = rt.get('https://api.electricitymap.org/v3/carbon-intensity/forecast', headers=headers,
                                params=params)

        data = response.json()

        print(data)

    def test_Forecasted_power_consumption_breakdown(self):
        print("test_Forecasted_power_consumption_breakdown")

        rt = RequestsTor()

        headers = {
            'auth-token': 'myapitoken',
        }

        params = (
            ('lat', '59.072820'),
            ('lon', '17.026826'),
        )

        response = rt.get('https://api.electricitymap.org/v3/power-consumption-breakdown/forecast',
                                headers=headers, params=params)

        data = response.json()

        print(data)

    def test_Forecasted_marginal_carbon_intensity(self):
        print("test_Forecasted_marginal_carbon_intensity")

        rt = RequestsTor()

        headers = {
            'auth-token': 'myapitoken',
        }

        params = (
            ('zone', 'GB')
        )

        response = rt.get('https://api.electricitymap.org/v3/marginal-carbon-intensity/forecast',
                          headers=headers, params=params)

        data = response.json()

        print(data)

    def test_Forecasted_marginal_power_consumption_breakdown(self):
        print("test_Forecasted_marginal_power_consumption_breakdown")

        rt = RequestsTor()

        headers = {
            'auth-token': 'myapitoken',
        }

        params = (
            ('lat', '59.600379'),
            ('lon', '15.671817'),
        )

        response = rt.get('https://api.electricitymap.org/v3/marginal-power-consumption-breakdown/forecast',
                                headers=headers, params=params)

        data = response.json()

        print(data)

    def test_Updated_Since(self):
        print('test_Updated_Since')

        rt = RequestsTor()

        headers = {
            'auth-token': 'myapitoken',
        }

        params = (
            ('zone', 'DK-DK1'),
            ('since', '2020-02-06T00:00:00Z'),
            ('start', '2020-02-05T00:00:00Z'),
            ('end', '2020-02-07T00:00:00Z'),
            ('limit', '100'),
            ('threshold', 'P1D'),
        )

        response = rt.get('https://api.electricitymap.org/v3/updated-since', headers=headers, params=params)

        data = response.json()

        print(data)


if __name__ == '__main__':
    unittest.main()
