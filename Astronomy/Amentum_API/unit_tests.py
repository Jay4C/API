import unittest
import requests


# https://amentum.io/gravity_docs
class UnitTestsAmentumEGM2008API(unittest.TestCase):
    def test_Calculate_the_geoid_height(self):
        print('test_Calculate_the_geoid_height')

        headers = {"API-Key": "<add_your_key>"}

        params = {
            "latitude": "-45",
            "longitude": "45"
        }

        # Make the API call
        response_json = None
        try:
            response = requests.get(
                "https://gravity.amentum.io/egm2008/geoid_height",
                params=params, headers=headers)
            response_json = response.json()
            response.raise_for_status()
        except requests.exceptions.HTTPError as e:
            print(response_json['error'] + ' : ' + str(e))
        else:
            # Extract the height
            height = response_json['height']['value']
            h_unit = response_json['height']['units']
            print("Height: ", height, h_unit)

    def test_Calculate_gravity_anomaly_values(self):
        print("test_Calculate_gravity_anomaly_values")

        import requests

        headers = {"API-Key": "<add_your_key>"}

        params = {
            "latitude": "-45",
            "longitude": "45"
        }

        # Make the API call
        response_json = None
        try:
            response = requests.get(
                "https://gravity.amentum.io/egm2008/gravity_anomaly",
                params=params, headers=headers)
            response_json = response.json()
            response.raise_for_status()
        except requests.exceptions.HTTPError as e:
            print(response_json['error'] + ' : ' + str(e))
        else:
            # Extract eta
            eta = response_json['eta']['value']
            e_unit = response_json['eta']['units']
            print("Eta: ", eta, e_unit)

            # Extract gravity anomaly
            ga = response_json['gravity_anomaly']['value']
            ga_unit = response_json['gravity_anomaly']['units']
            print("Gravity Anomaly: ", ga, ga_unit)

            # Extract xi
            xi = response_json['xi']['value']
            xi_unit = response_json['xi']['units']
            print("Xi: ", xi, xi_unit)


if __name__ == '__main__':
    unittest.main()
