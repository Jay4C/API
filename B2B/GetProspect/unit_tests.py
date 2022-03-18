import unittest
import requests

endpoint = "https://api.getprospect.com"
apiKey = ""


# https://developers.getprospect.com/#/
class UnitTestsGetprospectAPILists(unittest.TestCase):
    def test_Get_all_contacts_lists(self):
        print('test_Get_all_contacts_lists')

        headers = {
            "accept": "*/*",
            'content-type': "application/json",
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103',
            'apiKey': apiKey
        }

        url = endpoint + "/api/v1/contacts/lists"

        response = requests.get(url, headers=headers)

        print(response.text)

    def test_Add_new_contact_list(self):
        print("test_Add_new_contact_list")

        payload = {
            "name": "string"
        }

        headers = {
            "accept": "*/*",
            'content-type': "application/json",
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103',
            'apiKey': apiKey
        }

        url = endpoint + "/api/v1/contacts/lists"

        response = requests.post(url, headers=headers, data=payload)

        print(response.text)

    def test_Update_multiple_lists(self):
        print("test_Update_multiple_lists")

        payload = {
          "listsIds": [
            "string"
          ],
          "updateContactsStatus": True,
          "operationType": "string"
        }

        headers = {
            "accept": "*/*",
            'content-type': "application/json",
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103',
            'apiKey': apiKey
        }

        url = endpoint + "/api/v1/contacts/lists"

        response = requests.patch(url, headers=headers, data=payload)

        print(response.text)

    def test_Permanently_delete_multiple_lists(self):
        print("test_Permanently_delete_multiple_lists")

        payload = {
            bytes("string", "UTF-8")
        }

        headers = {
            "accept": "*/*",
            'content-type': "application/json",
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103',
            'apiKey': apiKey
        }

        url = endpoint + "/api/v1/contacts/lists"

        response = requests.delete(url, headers=headers, data=payload)

        print(response.text)

    def test_Get_lists_count_dy_list_id(self):
        print("test_Get_lists_count_dy_list_id")

        payload = {

        }

        headers = {
            "accept": "*/*",
            'content-type': "application/json",
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103',
            'apiKey': apiKey
        }

        url = endpoint + "/api/v1/contacts/lists/lists-sizes"

        response = requests.post(url, headers=headers, data=payload)

        print(response.text)

    def test_Update_list_by_id(self):
        print("test_Update_list_by_id")

        params = {
            ('listId', 'listId')
        }

        payload = {
            "name": "string"
        }

        headers = {
            "accept": "*/*",
            'content-type': "application/json",
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103',
            'apiKey': apiKey
        }

        url = endpoint + "/api/v1/contacts/lists"

        response = requests.patch(url, headers=headers, data=payload, params=params)

        print(response.text)

    def test_Save_new_contacts_to_list(self):
        print("test_Save_new_contacts_to_list")

        params = {
            ('list', 'list')
        }

        payload = {
          "contactsIds": [
            "string"
          ]
        }

        headers = {
            "accept": "*/*",
            'content-type': "application/json",
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103',
            'apiKey': apiKey
        }

        url = endpoint + "/api/v1/contacts/lists/add"

        response = requests.post(url, headers=headers, data=payload, params=params)

        print(response.text)

    def test_Search_contacts_by_filter_related_to_list(self):
        print("test_Search_contacts_by_filter_related_to_list")

        params = {
            ('list', 'list')
        }

        headers = {
            "accept": "*/*",
            'content-type': "application/json",
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103',
            'apiKey': apiKey
        }

        url = endpoint + "/api/v1/contacts/lists/contacts/search"

        response = requests.get(url, headers=headers, params=params)

        print(response.text)

    def test_Get_all_lists_tree(self):
        print("test_Get_all_lists_tree")

        headers = {
            "accept": "*/*",
            'content-type': "application/json",
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103',
            'apiKey': apiKey
        }

        url = endpoint + "/api/v1/contacts/lists/tree"

        response = requests.get(url, headers=headers)

        print(response.text)

    def test_Get_paginated_lists_results(self):
        print("test_Get_paginated_lists_results")

        params = {
            ('order', 'order')
        }

        headers = {
            "accept": "*/*",
            'content-type': "application/json",
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103',
            'apiKey': apiKey
        }

        url = endpoint + "/api/v1/contacts/lists/paginated"

        response = requests.get(url, headers=headers, params=params)

        print(response.text)

    def test_Search_through_lists_by_name(self):
        print("test_Search_through_lists_by_name")

        payload = {
          "withParentFolder": True
        }

        headers = {
            "accept": "*/*",
            'content-type': "application/json",
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103',
            'apiKey': apiKey
        }

        url = endpoint + "/api/v1/contacts/lists/search/name"

        response = requests.post(url, headers=headers, data=payload)

        print(response.text)

    def test_Search_lists_by_search_type(self):
        print("test_Search_lists_by_search_type")

        params = {
            ('order', 'order')
        }

        headers = {
            "accept": "*/*",
            'content-type': "application/json",
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103',
            'apiKey': apiKey
        }

        url = endpoint + "/api/v1/contacts/lists/search"

        response = requests.post(url, headers=headers, params=params)

        print(response.text)


class UnitTestsGetprospectAPIContacts(unittest.TestCase):
    def test_Create_new_contact(self):
        print("test_Create_new_contact")

        payload = {
          "properties": [
            {
              "property": "string",
              "value": {}
            }
          ],
          "listRelations": [
            "string"
          ]
        }

        headers = {
            "accept": "*/*",
            'content-type': "application/json",
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103',
            'apiKey': apiKey
        }

        url = endpoint + "/api/v1/contacts/contact"

        response = requests.post(url, headers=headers, data=payload)

        print(response.text)

    def test_Get_contact_by_id(self):
        print("test_Get_contact_by_id")

        params = {
            ('contactId', 'contactId')
        }

        headers = {
            "accept": "*/*",
            'content-type': "application/json",
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103',
            'apiKey': apiKey
        }

        url = endpoint + "/api/v1/contacts/contact"

        response = requests.get(url, headers=headers, params=params)

        print(response.text)

    def test_Update_contact_by_id(self):
        print("test_Update_contact_by_id")

        params = {
            ('contactId', 'contactId')
        }

        payload = {
          "properties": [
            {
              "property": "string",
              "value": {}
            }
          ],
          "listRelations": [
            "string"
          ]
        }

        headers = {
            "accept": "*/*",
            'content-type': "application/json",
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103',
            'apiKey': apiKey
        }

        url = endpoint + "/api/v1/contacts/contact"

        response = requests.patch(url, headers=headers, params=params, data=payload)

        print(response.text)

    def test_Delete_contact_by_id(self):
        print("test_Delete_contact_by_id")

        params = {
            ('contactId', 'contactId')
        }

        headers = {
            "accept": "*/*",
            'content-type': "application/json",
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103',
            'apiKey': apiKey
        }

        url = endpoint + "/api/v1/contacts/contact"

        response = requests.delete(url, headers=headers, params=params)

        print(response.text)

    def test_Search_contacts_by_filter(self):
        print("test_Search_contacts_by_filter")

        params = {
            ('order', 'order')
        }

        payload = {
          "filters": [
            {
              "operator": "string",
              "property": "string",
              "value": "string",
              "included": {
                "operator": "string",
                "value": {}
              }
            }
          ],
          "search": {
            "value": "string",
            "properties": [
              "string"
            ]
          },
          "includeRelations": True
        }

        headers = {
            "accept": "*/*",
            'content-type': "application/json",
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103',
            'apiKey': apiKey
        }

        url = endpoint + "/api/v1/contacts/contact/search"

        response = requests.post(url, headers=headers, params=params, data=payload)

        print(response.text)

    def test_Search_contacts_by_filter_count(self):
        print("test_Search_contacts_by_filter_count")

        params = {
            ('order', 'order')
        }

        payload = {
          "filters": [
            {
              "operator": "string",
              "property": "string",
              "value": "string",
              "included": {
                "operator": "string",
                "value": {}
              }
            }
          ],
          "search": {
            "value": "string",
            "properties": [
              "string"
            ]
          },
          "includeRelations": True
        }

        headers = {
            "accept": "*/*",
            'content-type': "application/json",
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103',
            'apiKey': apiKey
        }

        url = endpoint + "/api/v1/contacts/contact/search/count"

        response = requests.post(url, headers=headers, params=params, data=payload)

        print(response.text)

    def test_Create_a_new_contact_company_relations(self):
        print("test_Create_a_new_contact_company_relations")

        params = {
            ('contactId', 'contactId')
        }

        payload = {
          "companies": [
            {
              "companyId": "string",
              "email": "string",
              "status": "string",
              "position": "string"
            }
          ]
        }

        headers = {
            "accept": "*/*",
            'content-type': "application/json",
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103',
            'apiKey': apiKey
        }

        url = endpoint + "/api/v1/contacts/contact/companies"

        response = requests.post(url, headers=headers, params=params, data=payload)

        print(response.text)


class UnitTestsGetprospectAPIFolders(unittest.TestCase):
    def test_Add_new_folder(self):
        print("test_Add_new_folder")

        payload = {
          "name": "string",
          "parent": "string"
        }

        headers = {
            "accept": "*/*",
            'content-type': "application/json",
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103',
            'apiKey': apiKey
        }

        url = endpoint + "/api/v1/contacts/folders"

        response = requests.post(url, headers=headers, data=payload)

        print(response.text)

    def test_Delete_multiple_folders(self):
        print("test_Delete_multiple_folders")

        payload = {
          "folderIds": [
            "string"
          ]
        }

        headers = {
            "accept": "*/*",
            'content-type': "application/json",
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103',
            'apiKey': apiKey
        }

        url = endpoint + "/api/v1/contacts/folders"

        response = requests.delete(url, headers=headers, data=payload)

        print(response.text)

    def test_Update_folder_by_id(self):
        print("test_Update_folder_by_id")

        params = {
            ('folderId', 'folderId')
        }

        payload = {
          "name": "string",
          "parent": "string"
        }

        headers = {
            "accept": "*/*",
            'content-type': "application/json",
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103',
            'apiKey': apiKey
        }

        url = endpoint + "/api/v1/contacts/folders"

        response = requests.patch(url, headers=headers, data=payload, params=params)

        print(response.text)

    def test_Get_folders_tree(self):
        print("test_Get_folders_tree")

        headers = {
            "accept": "*/*",
            'content-type': "application/json",
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103',
            'apiKey': apiKey
        }

        url = endpoint + "/api/v1/contacts/folders/tree"

        response = requests.get(url, headers=headers)

        print(response.text)

    def test_Move_lists_to_folder(self):
        print("test_Move_lists_to_folder")

        params = {
            ('folderId', 'folderId')
        }

        payload = {
          "listsIds": [
            "string"
          ]
        }

        headers = {
            "accept": "*/*",
            'content-type': "application/json",
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103',
            'apiKey': apiKey
        }

        url = endpoint + "/api/v1/contacts/folders/lists"

        response = requests.post(url, headers=headers, data=payload, params=params)

        print(response.text)

    def test_Retrive_all_lists_related_to_folder(self):
        print("test_Retrive_all_lists_related_to_folder")

        params = {
            ('folderId', 'folderId')
        }

        headers = {
            "accept": "*/*",
            'content-type': "application/json",
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103',
            'apiKey': apiKey
        }

        url = endpoint + "/api/v1/contacts/folders/lists"

        response = requests.get(url, headers=headers, params=params)

        print(response.text)

    def test_Remove_lists_from_folder(self):
        print("test_Remove_lists_from_folder")

        params = {
            ('folderId', 'folderId')
        }

        payload = {
          "listsIds": [
            "string"
          ]
        }

        headers = {
            "accept": "*/*",
            'content-type': "application/json",
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103',
            'apiKey': apiKey
        }

        url = endpoint + "/api/v1/contacts/folders/lists"

        response = requests.delete(url, headers=headers, params=params, data=payload)

        print(response.text)

    def test_Move_lists_with_folders_to_folder(self):
        print("test_Move_lists_with_folders_to_folder")

        params = {
            ('folderId', 'folderId')
        }

        payload = {
        }

        headers = {
            "accept": "*/*",
            'content-type': "application/json",
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103',
            'apiKey': apiKey
        }

        url = endpoint + "/api/v1/contacts/folders/all"

        response = requests.post(url, headers=headers, params=params, data=payload)

        print(response.text)

    def test_Get_folders_lists(self):
        print("test_Get_folders_lists")

        headers = {
            "accept": "*/*",
            'content-type': "application/json",
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103',
            'apiKey': apiKey
        }

        url = endpoint + "/api/v1/contacts/folders/lists"

        response = requests.get(url, headers=headers)

        print(response.text)


class UnitTestsGetprospectAPICompanies(unittest.TestCase):
    def test_Return_all_companies_for_the_current_user(self):
        print("test_Return_all_companies_for_the_current_user")

        params = {
            ('order', 'order')
        }

        headers = {
            "accept": "*/*",
            'content-type': "application/json",
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103',
            'apiKey': apiKey
        }

        url = endpoint + "/api/v1/companies/company"

        response = requests.get(url, headers=headers, params=params)

        print(response.text)

    def test_Create_a_new_company(self):
        print("test_Create_a_new_company")

        payload = {
          "properties": {
            "property": "string",
            "value": {}
          }
        }

        headers = {
            "accept": "*/*",
            'content-type': "application/json",
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103',
            'apiKey': apiKey
        }

        url = endpoint + "/api/v1/companies/company"

        response = requests.post(url, headers=headers, data=payload)

        print(response.text)

    def test_Search_companies_with_name(self):
        print("test_Search_companies_with_name")

        params = {
            ('name', 'name')
        }

        headers = {
            "accept": "*/*",
            'content-type': "application/json",
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103',
            'apiKey': apiKey
        }

        url = endpoint + "/api/v1/companies/company/search/name"

        response = requests.get(url, headers=headers, params=params)

        print(response.text)

    def test_Get_company_by_id(self):
        print("test_Get_company_by_id")

        params = {
            ('companyId', 'companyId')
        }

        headers = {
            "accept": "*/*",
            'content-type': "application/json",
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103',
            'apiKey': apiKey
        }

        url = endpoint + "/api/v1/companies/company"

        response = requests.get(url, headers=headers, params=params)

        print(response.text)

    def test_Update_company_by_id(self):
        print("test_Update_company_by_id")

        params = {
            ('companyId', 'companyId')
        }

        headers = {
            "accept": "*/*",
            'content-type': "application/json",
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103',
            'apiKey': apiKey
        }

        url = endpoint + "/api/v1/companies/company"

        response = requests.patch(url, headers=headers, params=params)

        print(response.text)

    def test_Delete_company_by_id(self):
        print("test_Delete_company_by_id")

        params = {
            ('companyId', 'companyId')
        }

        headers = {
            "accept": "*/*",
            'content-type': "application/json",
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103',
            'apiKey': apiKey
        }

        url = endpoint + "/api/v1/companies/company"

        response = requests.delete(url, headers=headers, params=params)

        print(response.text)


class UnitTestsGetprospectAPIInsights(unittest.TestCase):
    def test_Search_leads_by_filter_options_inside_GetProspect_Database(self):
        print("test_Search_leads_by_filter_options_inside_GetProspect_Database")

        payload = {

        }

        headers = {
            "accept": "*/*",
            'content-type': "application/json",
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103',
            'apiKey': apiKey
        }

        url = endpoint + "/api/v1/insights/search"

        response = requests.post(url, headers=headers, data=payload)

        print(response.text)

    def test_Search_lead_by_LinkedIn_link(self):
        print("test_Search_lead_by_LinkedIn_link")

        params = {
            ('linkedinUrl', 'linkedinUrl')
        }

        headers = {
            "accept": "*/*",
            'content-type': "application/json",
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103',
            'apiKey': apiKey
        }

        url = endpoint + "/api/v1/insights/search/contact"

        response = requests.get(url, headers=headers, params=params)

        print(response.text)

    def test_Check_every_minute_status_of_this_search_to_know_when_it_finished(self):
        print("test_Check_every_minute_status_of_this_search_to_know_when_it_finished")

        params = {
            ('searchId', 'searchId')
        }

        headers = {
            "accept": "*/*",
            'content-type': "application/json",
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103',
            'apiKey': apiKey
        }

        url = endpoint + "/api/v1/insights/search"

        response = requests.get(url, headers=headers, params=params)

        print(response.text)


class UnitTestsGetprospectAPIEmail(unittest.TestCase):
    def test_Verify_email(self):
        print("test_Verify_email")

        params = {
            ('email', 'email')
        }

        headers = {
            "accept": "*/*",
            'content-type': "application/json",
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103',
            'apiKey': apiKey
        }

        url = endpoint + "/api/v1/email/verify"

        response = requests.post(url, headers=headers, params=params)

        print(response.text)

    def test_Find_email_by_name_and_company(self):
        print("test_Find_email_by_name_and_company")

        params = {
            ('name', 'name'),
            ('company', 'company')
        }

        headers = {
            "accept": "*/*",
            'content-type': "application/json",
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103',
            'apiKey': apiKey
        }

        url = endpoint + "/api/v1/email/verify"

        response = requests.get(url, headers=headers, params=params)

        print(response.text)


if __name__ == '__main__':
    unittest.main()
