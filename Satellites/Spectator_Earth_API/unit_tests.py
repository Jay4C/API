import unittest
from requests_tor import RequestsTor
import requests

endpoint = "https://app.spectator.earth"
key = ''


# https://api.spectator.earth/?language=Python#acquisition-plan
class UnitTestsSpectatorEarthWithTorRequest(unittest.TestCase):
    def test_Acquisition_plan(self):
        print("test_Acquisition_plan")

        url = endpoint + "/acquisition-plan/"

        rt = RequestsTor()

        r = rt.get(url)

        print(r.text)

    def test_Satellites(self):
        print("test_Satellites")

        rt = RequestsTor()

        satellite_id = 1

        url = 'https://api.spectator.earth/satellite/{satellite_id}'.format(satellite_id=satellite_id)

        response = rt.get(url)

        data = response.json()

        print(data)

    def test_Trajectories(self):
        print("test_Trajectories")

        rt = RequestsTor()

        satellite_id = 1

        url = 'https://api.spectator.earth/satellite/{satellite_id}/trajectory'.format(satellite_id=satellite_id)

        response = rt.get(url)

        data = response.json()

        print(data)

    def test_Searching_for_images(self):
        print("test_Searching_for_images")

        api_key = 'KEY'

        bbox = '19.59,49.90,20.33,50.21'

        url = 'https://api.spectator.earth/imagery/?api_key={api_key}&bbox={bbox}'.format(api_key=api_key, bbox=bbox)

        response = requests.get(url)

        data = response.json()

        print(data)

    def test_Imagery_files(self):
        print("test_Imagery_files")

        api_key = 'KEY'

        url = 'https://api.spectator.earth/imagery/1/files/?api_key={api_key}'.format(api_key=api_key)

        response = requests.get(url)

        data = response.json()

        print(data)

    def test_Satellite_overpasses(self):
        print("test_Satellite_overpasses")

        api_key = 'KEY'

        bbox = '19.59,49.90,20.33,50.21'

        satellites = 'Sentinel-2A,Sentinel-2B'

        url = 'https://api.spectator.earth/overpass/?api_key={api_key}&bbox={bbox}&satellites={satellites}'.format(
            api_key=api_key, bbox=bbox, satellites=satellites)

        response = requests.get(url)

        data = response.json()

        print(data)


if __name__ == '__main__':
    unittest.main()
