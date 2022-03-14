import unittest
from requests_tor import RequestsTor
from base64 import b64encode


# https://developers.wattics.com/
class UnitTestsWatticsDataPushAPIWithTorRequest(unittest.TestCase):
    def test_Push_Data(self):
        print("test_Push_Data")

        url = "https://web-collector.wattics.com/measurements/v2/unifiedjson/"

        user_and_password = b64encode(b"username:password").decode("ascii")

        payload = "{ \"id\": \"uniqueMeterId\", \"tsISO8601\": \"2019-06-02T00:00:00.000+00:00\", " \
                  "\"aP_1\":1000.0, \"pC_1\":2000.0 }"

        headers = {
            'Content-Type': 'text/json',
            'Authorization': 'Basic %s' % user_and_password
        }

        rt = RequestsTor()

        r = rt.post(url, headers=headers, payload=payload)

        data = r.json()

        print(data)

    def test_Push_Partial_Data(self):
        print("test_Push_Partial_Data")

        url = "https://web-collector.wattics.com/measurements/v2/unifiedjson_partial/"

        user_and_password = b64encode(b"username:password").decode("ascii")

        payload = "{ \"id\": \"uniqueMeterId\", \"tsISO8601\": \"2019-06-02T00:00:00.000+00:00\", " \
                  "\"aP_1\":1000.0, \"pC_1\":2000.0 }"

        headers = {
            'Content-Type': 'text/json',
            'Authorization': 'Basic %s' % user_and_password
        }

        rt = RequestsTor()

        r = rt.post(url, headers=headers, payload=payload)

        data = r.json()

        print(data)

    def test_Get_Last_Data_Received(self):
        print("test_Get_Last_Data_Received")

        url = "https://web-collector.wattics.com/measurements/v2/unifiedjson/?stream=uniqueMeterId"

        user_and_password = b64encode(b"username:password").decode("ascii")

        headers = {
            'Content-Type': 'text/json',
            'Authorization': 'Basic %s' % user_and_password
        }

        rt = RequestsTor()

        r = rt.get(url, headers=headers)

        data = r.json()

        print(data)


class UnitTestsWatticsDashboardManagementAPIWithTorRequest(unittest.TestCase):
    def test_Authentication(self):
        print("test_Authentication")

        url = "http://api.wattics.com/api/v1/RESOURCE"

        payload = ""

        headers = {
            'Content-Type': "application/json",
            'Authorization': 'YOUR_API_TOKEN_HERE'
        }

        rt = RequestsTor()

        r = rt.get(url, headers=headers, payload=payload)

        data = r.json()

        print(data)

    def test_Users_Create(self):
        print("test_Users_Create")

        url = "https://api.wattics.com/api/v1/users"

        payload = "{\n\t\"user\": {\n\t\t\"name\": \"John\",\n\t\t\"surname\": \"Doe\",\n\t\t\"email\": " \
                  "\"john@email.com\",\n\t\t\"plan\": \"Data import\"\n\t}\n}"

        headers = {
            'Content-Type': "application/json",
            'Authorization': "YOUR_API_TOKEN_HERE"
        }

        rt = RequestsTor()

        r = rt.post(url, headers=headers, payload=payload)

        data = r.json()

        print(data)

    def test_Users_Associate_to_Site(self):
        url = "https://api.wattics.com/api/v1/users/USER_ID/grant_site_access"

        payload = "{\n\t\"site_id\": 1\n}"

        headers = {
            'Content-Type': "application/json",
            'Authorization': "YOUR_API_TOKEN_HERE"
        }

        rt = RequestsTor()

        r = rt.patch(url, headers=headers, payload=payload)

        data = r.json()

        print(data)

    def test_Users_Disassociate_from_Site(self):
        print("test_Users_Disassociate_from_Site")

        url = "https://api.wattics.com/api/v1/users/USER_ID/remove_site_access"

        payload = "{\n\t\"site_id\": 1\n}"

        headers = {
            'Content-Type': "application/json",
            'Authorization': "YOUR_API_TOKEN_HERE"
        }

        rt = RequestsTor()

        r = rt.patch(url, headers=headers, payload=payload)

        data = r.json()

        print(data)

    def test_Users_List_associated_sites(self):
        print("test_Users_List_associated_sites")

        url = "https://api.wattics.com/api/v1/users/USER_ID/associated_sites"

        payload = ""

        headers = {
            'Content-Type': 'application/json',
            'Authorization': 'YOUR_API_TOKEN_HERE'
        }

        rt = RequestsTor()

        r = rt.get(url, headers=headers, payload=payload)

        data = r.json()

        print(data)

    def test_Users_Show_Details_by_Email(self):
        print("test_Users_Show_Details_by_Email")

        url = "https://api.wattics.com/api/v1/users/show_by_email?email=john@email.com"

        payload = ""

        headers = {
            'Content-Type': "application/json",
            'Authorization': "YOUR_API_TOKEN_HERE"
        }

        rt = RequestsTor()

        r = rt.get(url, headers=headers, payload=payload)

        data = r.json()

        print(data)

    def test_Users_Add_to_Report_Definition(self):
        print("test_Users_Add_to_Report_Definition")

        url = "https://api.wattics.com/api/v1/users/USER_ID/associate_to_report"

        payload = "{\n\t\"report_definition_id\": REPORT_DEFINITION_ID\n}"

        headers = {
            'Content-Type': "application/json",
            'Authorization': "YOUR_API_TOKEN_HERE",
        }

        rt = RequestsTor()

        r = rt.patch(url, headers=headers, payload=payload)

        data = r.json()

        print(data)

    def test_Organizations_Create(self):
        print("test_Organizations_Create")

        url = "https://api.wattics.com/api/v1/organizations"

        payload = "{\n\t\"organization\": {\n\t\t\"name\": \"My New Organization\"\n\t}\n}"

        headers = {
            'Content-Type': "application/json",
            'Authorization': "YOUR_API_TOKEN_HERE",
        }

        rt = RequestsTor()

        r = rt.post(url, headers=headers, payload=payload)

        data = r.json()

        print(data)

    def test_Organizations_Update(self):
        print("test_Organizations_Update")

        url = "https://api.wattics.com/api/v1/organizations/ORGANIZATION_ID"

        payload = "{\n\t\"organization\": {\n\t\t\"name\": \"Other name\"\n\t}\n}"

        headers = {
            'Content-Type': "application/json",
            'Authorization': "YOUR_API_TOKEN_HERE",
        }

        rt = RequestsTor()

        r = rt.patch(url, headers=headers, payload=payload)

        data = r.json()

        print(data)

    def test_Organizations_Delete(self):
        print("test_Organizations_Delete")

        url = "https://api.wattics.com/api/v1/organizations/ORGANIZATION_ID"

        payload = "{\n\t\"organization\": {\n\t\t\"name\": \"Other name\"\n\t}\n}"

        headers = {
            'Content-Type': "application/json",
            'Authorization': "YOUR_API_TOKEN_HERE",
        }

        rt = RequestsTor()

        r = rt.delete(url, headers=headers, payload=payload)

        data = r.json()

        print(data)

    def test_Organizations_List(self):
        print("test_Organizations_List")

        url = "https://api.wattics.com/api/v1/organizations"

        payload = ""

        headers = {
            'Content-Type': "application/json",
            'Authorization': "YOUR_API_TOKEN_HERE",
        }

        rt = RequestsTor()

        r = rt.get(url, headers=headers, payload=payload)

        data = r.json()

        print(data)

    def test_Sites_Create(self):
        print("test_Sites_Create")

        url = "https://api.wattics.com/api/v1/sites"

        payload = "{ \n\t\"site\": {\n\t\t\"organization_id\": 1,\n\t\t\"name\": \"Dublin " \
                  "Office\",\n\t\t\"city\": \"Dublin\",\n\t\t\"country\": \"Ireland\",\n\t\t\"address\": " \
                  "\"Taylors Lane\",\n\t\t\"contact_name\": \"John Doe\",\n\t\t\"contact_email\": " \
                  "\"john.doe@wattics.com\"\n\t}\n}"

        headers = {
            'Content-Type': "application/json",
            'Authorization': "YOUR_API_TOKEN_HERE",
        }

        rt = RequestsTor()

        r = rt.post(url, headers=headers, payload=payload)

        data = r.json()

        print(data)

    def test_Sites_Update(self):
        print('test_Sites_Update')

        url = "https://api.wattics.com/api/v1/sites/SITE_ID"

        payload = "{\n\t\"organization\": {\n\t\t\"name\": \"Other name\"\n\t}\n}"

        headers = {
            'Content-Type': "application/json",
            'Authorization': "YOUR_API_TOKEN_HERE",
        }

        rt = RequestsTor()

        r = rt.patch(url, headers=headers, payload=payload)

        data = r.json()

        print(data)

    def test_Sites_Delete(self):
        print('test_Sites_Delete')

        url = "https://api.wattics.com/api/v1/sites/SITE_ID"

        payload = "{\n\t\"organization\": {\n\t\t\"name\": \"Other name\"\n\t}\n}"

        headers = {
            'Content-Type': "application/json",
            'Authorization': "YOUR_API_TOKEN_HERE",
        }

        rt = RequestsTor()

        r = rt.delete(url, headers=headers, payload=payload)

        data = r.json()

        print(data)

    def test_Sites_Get(self):
        print("test_Sites_Get")

        url = "https://api.wattics.com/api/v1/sites/1"

        payload = ""

        headers = {
            'Content-Type': "application/json",
            'Authorization': "YOUR_API_TOKEN_HERE",
        }

        rt = RequestsTor()

        r = rt.get(url, headers=headers, payload=payload)

        data = r.json()

        print(data)

    def test_Sites_List_from_Organization(self):
        print("test_Sites_List_from_Organization")

        url = "https://api.wattics.com/api/v1/sites?organization_id=1"

        payload = ""

        headers = {
            'Content-Type': "application/json",
            'Authorization': "YOUR_API_TOKEN_HERE",
        }

        rt = RequestsTor()

        r = rt.get(url, headers=headers, payload=payload)

        data = r.json()

        print(data)

    def test_Sites_List_users(self):
        print("test_Sites_List_users")

        url = "https://api.wattics.com/api/v1/sites/SITE_ID/associated_users"

        payload = ""

        headers = {
            'Content-Type': 'application/json',
            'Authorization': 'YOUR_API_TOKEN_HERE'
        }

        rt = RequestsTor()

        r = rt.get(url, headers=headers, payload=payload)

        data = r.json()

        print(data)

    def test_Meters_Create(self):
        print("test_Meters_Create")

        url = "https://api.wattics.com/api/v1/meters"

        payload = "{\n\t\"meter\": {\n\t\t\"name\": \"Meter 1\",\n\t\t\"site_id\": 1,\n\t\t\"type\": \"electricity\",\n\t\t\"reference\": \"meter-1234-0000\",\n\t\t\"param_type\": \"all\",\n\t\t\"reading\": \"cum\",\n\t\t\"process_sampling_rate\": 5\n\t}\n}"

        headers = {
            'Content-Type': "application/json",
            'Authorization': "YOUR_API_TOKEN_HERE",
        }

        rt = RequestsTor()

        r = rt.post(url, headers=headers, payload=payload)

        data = r.json()

        print(data)

    def test_Meters_Update(self):
        print("test_Meters_Update")

        url = "https://api.wattics.com/api/v1/meters/METER_ID"

        payload = "{\n\t\"meter\": {\n\t\t\"name\": \"Other name\"\n\t}\n}"

        headers = {
            'Content-Type': "application/json",
            'Authorization': "YOUR_API_TOKEN_HERE",
        }

        rt = RequestsTor()

        r = rt.patch(url, headers=headers, payload=payload)

        data = r.json()

        print(data)

    def test_Meters_Delete(self):
        print("test_Meters_Delete")

        url = "https://api.wattics.com/api/v1/meters/METER_ID"

        headers = {
            'Content-Type': "application/json",
            'Authorization': "YOUR_API_TOKEN_HERE",
        }

        rt = RequestsTor()

        r = rt.delete(url, headers=headers)

        data = r.json()

        print(data)

    def test_Meters_Get(self):
        print("test_Meters_Get")

        url = "https://api.wattics.com/api/v1/meters/1"

        payload = ""

        headers = {
            'Content-Type': "application/json",
            'Authorization': "YOUR_API_TOKEN_HERE",
        }

        rt = RequestsTor()

        r = rt.delete(url, headers=headers, payload=payload)

        data = r.json()

        print(data)

    def test_Meters_List_from_Site(self):
        print("test_Meters_List_from_Site")

        url = "https://api.wattics.com/api/v1/meters?organization_id=1&site_id=1"

        payload = ""

        headers = {
            'Content-Type': "application/json",
            'Authorization': "YOUR_API_TOKEN_HERE",
        }

        rt = RequestsTor()

        r = rt.get(url, headers=headers, payload=payload)

        data = r.json()

        print(data)

    def test_Appliances_Create(self):
        print("test_Appliances_Create")

        url = "https://api.wattics.com/api/v1/appliances"

        payload = "{\n\t\"appliance\": {\n\t\t\"meter_id\": 1, \n\t\t\"name\": \"Fan\",\n\t\t\"reference\": \"app0123-99\",\n\t\t\"process_sampling_rate\": 5,\n\t\t\"reading\": \"avg\",\n\t\t\"channel_param_type\": \"one\"\n\t}\n}"

        headers = {
            'Content-Type': "application/json",
            'Authorization': "YOUR_API_TOKEN_HERE",
        }

        rt = RequestsTor()

        r = rt.post(url, headers=headers, payload=payload)

        data = r.json()

        print(data)

    def test_Appliances_Update(self):
        print("test_Appliances_Update")

        url = "https://api.wattics.com/api/v1/appliances/APPLIANCE_ID"

        payload = "{\n\t\"meter\": {\n\t\t\"name\": \"Other name\"\n\t}\n}"

        headers = {
            'Content-Type': "application/json",
            'Authorization': "YOUR_API_TOKEN_HERE",
        }

        rt = RequestsTor()

        r = rt.patch(url, headers=headers, payload=payload)

        data = r.json()

        print(data)

    def test_Appliances_Delete(self):
        print('test_Appliances_Delete')

        url = "https://api.wattics.com/api/v1/appliances/APPLIANCE_ID"

        payload = "{\n\t\"organization\": {\n\t\t\"name\": \"Other name\"\n\t}\n}"

        headers = {
            'Content-Type': "application/json",
            'Authorization': "YOUR_API_TOKEN_HERE",
        }

        rt = RequestsTor()

        r = rt.delete(url, headers=headers, payload=payload)

        data = r.json()

        print(data)

    def test_Appliances_Get(self):
        print("test_Appliances_Get")

        url = "https://api.wattics.com/api/v1/appliances/1"

        payload = ""

        headers = {
            'Content-Type': "application/json",
            'Authorization': "YOUR_API_TOKEN_HERE",
        }

        rt = RequestsTor()

        r = rt.get(url, headers=headers, payload=payload)

        data = r.json()

        print(data)

    def test_Appliances_List_from_Meter(self):
        print("test_Appliances_List_from_Meter")

        url = "https://api.wattics.com/api/v1/appliances?organization_id=1&site_id=1&meter_id=1"

        payload = ""

        headers = {
            'Content-Type': "application/json",
            'Authorization': "YOUR_API_TOKEN_HERE",
        }

        rt = RequestsTor()

        r = rt.get(url, headers=headers, payload=payload)

        data = r.json()

        print(data)

    def test_Metadata_From_Site(self):
        print("test_Metadata_From_Site")

        url = "https://api.wattics.com/api/v1/sites/ID/metadata"

        payload = ""

        headers = {
            'Content-Type': "application/json",
            'Authorization': "YOUR_API_TOKEN_HERE",
        }

        rt = RequestsTor()

        r = rt.get(url, headers=headers, payload=payload)

        data = r.json()

        print(data)

    def test_Metadata_From_Meter(self):
        print("test_Metadata_From_Meter")

        url = "https://api.wattics.com/api/v1/meters/ID/metadata"

        payload = ""

        headers = {
            'Content-Type': "application/json",
            'Authorization': "YOUR_API_TOKEN_HERE",
        }

        rt = RequestsTor()

        r = rt.get(url, headers=headers, payload=payload)

        data = r.json()

        print(data)

    def test_Raw_Data_From_Meter(self):
        print("test_Raw_Data_From_Meter")

        url = "https://api.wattics.com/api/v1/meters/36/raw_data?from=01/01/2018&to=01/03/2018&data_type=active_power"

        payload = ""

        headers = {
            'Content-Type': "application/json",
            'Authorization': "YOUR_API_TOKEN_HERE",
        }

        rt = RequestsTor()

        r = rt.get(url, headers=headers, payload=payload)

        data = r.json()

        print(data)

    def test_Raw_Data_From_Appliance(self):
        print("test_Raw_Data_From_Appliance")

        url = "https://api.wattics.com/api/v1/appliances/1/raw_data?from=31/05/2018&to=30/06/2018&data_type=active_power&show_phases=true"

        payload = ""

        headers = {
            'Content-Type': "application/json",
            'Authorization': "YOUR_API_TOKEN_HERE",
        }

        rt = RequestsTor()

        r = rt.get(url, headers=headers, payload=payload)

        data = r.json()

        print(data)

    def test_Consumptions_From_Meter(self):
        print("test_Consumptions_From_Meter")

        url = "https://api.wattics.com/api/v1/meters/1/consumptions?month=10&year=2018&detailed=true"

        payload = ""

        headers = {
            'Content-Type': "application/json",
            'Authorization': "YOUR_API_TOKEN_HERE",
        }

        rt = RequestsTor()

        r = rt.get(url, headers=headers, payload=payload)

        data = r.json()

        print(data)

    def test_Consumptions_From_Appliance(self):
        print("test_Consumptions_From_Appliance")

        url = "https://api.wattics.com/api/v1/appliances/1/consumptions?month=10&year=2018&detailed=true"

        payload = ""

        headers = {
            'Content-Type': "application/json",
            'Authorization': "YOUR_API_TOKEN_HERE",
        }

        rt = RequestsTor()

        r = rt.get(url, headers=headers, payload=payload)

        data = r.json()

        print(data)

    def test_Costs_From_Meter(self):
        print("test_Costs_From_Meter")

        url = "https://api.wattics.com/api/v1/meters/1/costs?month=10&year=2018&detailed=true"

        payload = ""

        headers = {
            'Content-Type': "application/json",
            'Authorization': "YOUR_API_TOKEN_HERE",
        }

        rt = RequestsTor()

        r = rt.get(url, headers=headers, payload=payload)

        data = r.json()

        print(data)

    def test_Costs_From_Appliance(self):
        print("test_Costs_From_Appliance")

        url = "https://api.wattics.com/api/v1/appliances/1/costs?month=10&year=2018&detailed=true"

        payload = ""

        headers = {
            'Content-Type': "application/json",
            'Authorization': "YOUR_API_TOKEN_HERE",
        }

        rt = RequestsTor()

        r = rt.get(url, headers=headers, payload=payload)

        data = r.json()

        print(data)

    def test_Tariffs_Create(self):
        print("test_Tariffs_Create")

        url = "https://api.wattics.com/api/v1/tariffs"

        payload = "json..."

        headers = {
            'Content-Type': "application/json",
            'Authorization': "YOUR_API_TOKEN_HERE",
        }

        rt = RequestsTor()

        r = rt.post(url, headers=headers, payload=payload)

        data = r.json()

        print(data)

    def test_Tariffs_Update(self):
        print("test_Tariffs_Update")

        url = "https://api.wattics.com/api/v1/tariffs/TARIFF_ID"

        payload = "json..."

        headers = {
            'Content-Type': "application/json",
            'Authorization': "YOUR_API_TOKEN_HERE",
        }

        rt = RequestsTor()

        r = rt.put(url, headers=headers, payload=payload)

        data = r.json()

        print(data)

    def test_Tariffs_Delete(self):
        print("test_Tariffs_Delete")

        url = "https://api.wattics.com/api/v1/tariffs/TARIFF_ID"

        headers = {
            'Content-Type': "application/json",
            'Authorization': "YOUR_API_TOKEN_HERE",
        }

        rt = RequestsTor()

        r = rt.delete(url, headers=headers)

        data = r.json()

        print(data)

    def test_Tariffs_Get(self):
        print("test_Tariffs_Get")

        url = "https://api.wattics.com/api/v1/tariffs/ID"

        payload = ""

        headers = {
            'Content-Type': "application/json",
            'Authorization': "YOUR_API_TOKEN_HERE",
        }

        rt = RequestsTor()

        r = rt.get(url, headers=headers)

        data = r.json()

        print(data)

    def test_Tariffs_From_Site(self):
        print("test_Tariffs_From_Site")

        url = "https://api.wattics.com/api/v1/sites/ID/tariffs"

        payload = ""

        headers = {
            'Content-Type': "application/json",
            'Authorization': "YOUR_API_TOKEN_HERE",
        }

        rt = RequestsTor()

        r = rt.get(url, headers=headers)

        data = r.json()

        print(data)

    def test_Report_Definitions_List(self):
        print("test_Report_Definitions_List")

        url = "https://api.wattics.com/api/v1/report_definitions"

        headers = {
            'Content-Type': "application/json",
            'Authorization': "YOUR_API_TOKEN_HERE",
        }

        rt = RequestsTor()

        r = rt.get(url, headers=headers)

        data = r.json()

        print(data)


if __name__ == '__main__':
    unittest.main()
