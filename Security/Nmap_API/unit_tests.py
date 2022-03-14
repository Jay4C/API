import unittest
from requests_tor import RequestsTor

endpoint = "https://api.nmap.online"


class UnitTestsNmapAPIScanWithTorNetwork(unittest.TestCase):
    def test_Create_Nmap_scan(self):
        print('test_Create_Nmap_scan')

        payload = {
            'scan_type': "string",
            'command': "string",
            'options': "string",
            'schedule': "string",
            'target': "string",
            'target_end': "string"
        }

        headers = {
            'content-type': "multipart/form-data",
            'NMAP-API-KEY': "YOUR_API_KEY_HERE"
        }

        url = endpoint + "/v01/start_scan"

        rt = RequestsTor()

        r = rt.post(url, headers=headers, payload=payload)

        data = r.json()

        print(data.decode("utf-8"))


class UnitTestsNmapAPIInformationsWithTorNetwork(unittest.TestCase):
    def test_Get_scan_info(self):
        print("test_Get_scan_info")

        payload = {
            'scan_id': "string"
        }

        headers = {
            'content-type': "multipart/form-data",
            'NMAP-API-KEY': "YOUR_API_KEY_HERE"
        }

        url = endpoint + "/v01/scan_info"

        rt = RequestsTor()

        r = rt.post(url, headers=headers, payload=payload)

        data = r.json()

        print(data.decode("utf-8"))

    def test_Check_scan_status(self):
        print("test_Check_scan_status")

        payload = {
            'scan_id': "string"
        }

        headers = {
            'content-type': "multipart/form-data",
            'NMAP-API-KEY': "YOUR_API_KEY_HERE"
        }

        url = endpoint + "/v01/check_scan_status"

        rt = RequestsTor()

        r = rt.post(url, headers=headers, payload=payload)

        data = r.json()

        print(data.decode("utf-8"))

    def test_Get_scan_report(self):
        print('test_Get_scan_report')

        payload = {
            'scan_id': "string"
        }

        headers = {
            'content-type': "multipart/form-data",
            'NMAP-API-KEY': "YOUR_API_KEY_HERE"
        }

        url = endpoint + "/v01/scan_result"

        rt = RequestsTor()

        r = rt.post(url, headers=headers, payload=payload)

        data = r.json()

        print(data.decode("utf-8"))


class UnitTestsNmapAPISystemWithTorNetwork(unittest.TestCase):
    def test_API_calls_report(self):
        print("test_API_calls_report")

        payload = {
        }

        headers = {
            'NMAP-API-KEY': "YOUR_API_KEY_HERE"
        }

        url = endpoint + "/v01/api_report"

        rt = RequestsTor()

        r = rt.get(url, headers=headers, payload=payload)

        data = r.json()

        print(data.decode("utf-8"))


if __name__ == '__main__':
    unittest.main()
