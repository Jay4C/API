import unittest
from requests_tor import RequestsTor

# Sandbox environment: https://apisandbox.greenly.earth/v1.5
# Production environment: https://api.greenly.earth/v1.5
endpoint = "https://api.greenly.earth/v1.5"


# https://greenly.redoc.ly/#section/Introduction
class UnitTestsGreenlyAPIAlternativesWithTorNetwork(unittest.TestCase):
    def test_Get_all_alternatives(self):
        print("test_Get_all_alternatives")

        headers = {
            'api-key': "YOUR_API_KEY_HERE"
        }

        url = endpoint + "/alternatives"

        rt = RequestsTor()

        r = rt.get(url, headers=headers)

        data = r.json()

        print(data)

    def test_Get_alternative(self):
        print("test_Get_alternative")

        headers = {
            'api-key': "YOUR_API_KEY_HERE"
        }

        id = ""

        url = endpoint + "/alternatives/" + id

        rt = RequestsTor()

        r = rt.get(url, headers=headers)

        data = r.json()

        print(data)


class UnitTestsGreenlyAPIOffsetProjectsWithTorNetwork(unittest.TestCase):
    def test_Get_all_offset_projects(self):
        print("test_Get_all_offset_projects")

        headers = {
            'api-key': "YOUR_API_KEY_HERE"
        }

        url = endpoint + "/offsetProjects"

        rt = RequestsTor()

        r = rt.get(url, headers=headers)

        data = r.json()

        print(data)

    def test_Get_offset_project(self):
        print("test_Get_offset_project")

        headers = {
            'api-key': "YOUR_API_KEY_HERE"
        }

        id = ""

        url = endpoint + "/offsetProjects/" + id

        rt = RequestsTor()

        r = rt.get(url, headers=headers)

        data = r.json()

        print(data)

    def test_Book_offset_project(self):
        print("test_Book_offset_project")

        payload = {
            "email": "string",
            "bookedOffsetInTCO2eq": 0,
            "offsetProjectId": "string"
        }

        headers = {
            'api-key': "YOUR_API_KEY_HERE"
        }

        url = endpoint + "/offsetProjects/bookOffsetQuantity"

        rt = RequestsTor()

        r = rt.post(url, headers=headers, payload=payload)

        data = r.json()

        print(data)


class UnitTestsGreenlyAPIPurchaseCategoriesWithTorNetwork(unittest.TestCase):
    def test_Get_all_purchase_categories(self):
        print("test_Get_all_purchase_categories")

        headers = {
            'api-key': "YOUR_API_KEY_HERE"
        }

        url = endpoint + "/purchaseCategories"

        rt = RequestsTor()

        r = rt.get(url, headers=headers)

        data = r.json()

        print(data)

    def test_Get_purchase_category(self):
        print("test_Get_purchase_category")

        headers = {
            'api-key': "YOUR_API_KEY_HERE"
        }

        id = ""

        url = endpoint + "/purchaseCategories/" + id

        rt = RequestsTor()

        r = rt.get(url, headers=headers)

        data = r.json()

        print(data)


class UnitTestsGreenlyAPITransactionsWithTorNetwork(unittest.TestCase):
    def test_Calculate_carbon_footprints(self):
        print("test_Calculate_carbon_footprints")

        payload = {
          "transactions": [
            {
              "countryCode": "string",
              "tagValues": [
                {
                  "value": "string",
                  "tagId": "string"
                }
              ],
              "purchaseCategoryId": "string",
              "mccCode": "string",
              "amount": 0,
              "type": "CREDIT",
              "label": "string",
              "amountInEur": 0,
              "id": "string"
            }
          ],
          "userId": "string"
        }

        headers = {
            'api-key': "YOUR_API_KEY_HERE"
        }

        url = endpoint + "/transactions/calculateCarbonFootprints"

        rt = RequestsTor()

        r = rt.post(url, headers=headers, payload=payload)

        data = r.json()

        print(data)


class UnitTestsGreenlyAPIUsersWithTorNetwork(unittest.TestCase):
    def test_Create_user(self):
        print("test_Create_user")

        payload = {
          "defaultTagValues": [
            {
              "value": "string",
              "tagId": "string"
            }
          ],
          "userId": "string"
        }

        headers = {
            'api-key': "YOUR_API_KEY_HERE"
        }

        url = endpoint + "/users/createUser"

        rt = RequestsTor()

        r = rt.post(url, headers=headers, payload=payload)

        data = r.json()

        print(data)

    def test_Update_user(self):
        print("test_Update_user")

        payload = {
          "defaultTagValues": [
            {
              "value": "string",
              "tagId": "string"
            }
          ]
        }

        headers = {
            'api-key': "YOUR_API_KEY_HERE"
        }

        user_id = ""

        url = endpoint + "/users/" + user_id

        rt = RequestsTor()

        r = rt.put(url, headers=headers, payload=payload)

        data = r.json()

        print(data)

    def test_Get_user(self):
        print("test_Get_user")

        headers = {
            'api-key': "YOUR_API_KEY_HERE"
        }

        id = ""

        url = endpoint + "/users/" + id

        rt = RequestsTor()

        r = rt.get(url, headers=headers)

        data = r.json()

        print(data)

    def test_Delete_user(self):
        print("test_Delete_user")

        headers = {
            'api-key': "YOUR_API_KEY_HERE"
        }

        id = ""

        url = endpoint + "/users/" + id

        rt = RequestsTor()

        r = rt.delete(url, headers=headers)

        data = r.json()

        print(data)


if __name__ == '__main__':
    unittest.main()
