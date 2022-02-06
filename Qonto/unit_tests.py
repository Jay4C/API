import json
import unittest
import requests


class Unit_Tests_Qonto_API(unittest.TestCase):
    def test_get_token_endpoint(self):
        print("test_get_token_endpoint")

        url = "https://oauth.qonto.com/oauth2/token"

        payload = 'code=code&client_id=client_id&client_secret=client_secret' \
                  '&redirect_uri=redirect_uri&grant_type=grant_type'

        headers = {
            'Content-Type': 'application/x-www-form-urlencoded'
        }

        response = requests.request("POST", url, headers=headers, data=payload)

        print(response.text)

    def test_get_show_organization_v1(self):
        print("test_get_show_organization_v1")

        url = "https://thirdparty.qonto.com/v1/organizations/{id}"

        payload = {}
        headers = {
            'Authorization': '{organization-slug}:{secret-key}'
        }

        response = requests.request("GET", url, headers=headers, data=payload)

        print(response.text)

    def test_get_list_transactions_v1(self):
        print("test_get_list_transactions_v1")

        url = "https://thirdparty.qonto.com/v1/transactions?slug=slug"

        payload = {}
        headers = {
            'Authorization': '{organization-slug}:{secret-key}'
        }

        response = requests.request("GET", url, headers=headers, data=payload)

        print(response.text)

    def test_get_list_transaction_v2(self):
        print("test_get_list_transaction_v2")

        url = "https://thirdparty.qonto.com/v2/transactions?iban=iban"

        payload = {}
        headers = {
            'Authorization': '{organization-slug}:{secret-key}'
        }

        response = requests.request("GET", url, headers=headers, data=payload)

        print(response.text)

    def test_get_show_transaction_v2(self):
        print("test_get_show_transaction_v2")

        url = "https://thirdparty.qonto.com/v2/transactions/{id}"

        payload = {}
        headers = {
            'Authorization': '{organization-slug}:{secret-key}'
        }

        response = requests.request("GET", url, headers=headers, data=payload)

        print(response.text)

    def test_get_show_organisation_v2(self):
        print("test_get_show_organisation_v2")

        url = "https://thirdparty.qonto.com/v2/organizations/{id}"

        payload = {}
        headers = {
            'Authorization': '{organization-slug}:{secret-key}'
        }

        response = requests.request("GET", url, headers=headers, data=payload)

        print(response.text)

    def test_get_list_organizations_v2(self):
        print("test_get_list_organizations")

        url = "https://thirdparty.qonto.com/v2/organization"

        payload = {}
        headers = {
            'Authorization': '{organization-slug}:{secret-key}'
        }

        response = requests.request("GET", url, headers=headers, data=payload)

        print(response.text)

    def test_get_list_labels_v2(self):
        print("test_get_list_labels_v2")

        url = "https://thirdparty.qonto.com/v2/labels"

        payload = {}
        headers = {
            'Authorization': '{organization-slug}:{secret-key}'
        }

        response = requests.request("GET", url, headers=headers, data=payload)

        print(response.text)

    def test_get_show_label_v2(self):
        print("test_get_show_label_v2")

        url = "https://thirdparty.qonto.com/v2/labels/{id}"

        payload = {}
        headers = {
            'Authorization': '{organization-slug}:{secret-key}'
        }

        response = requests.request("GET", url, headers=headers, data=payload)

        print(response.text)

    def test_get_list_memberships_v2(self):
        print("test_get_list_memberships_v2")

        url = "https://thirdparty.qonto.com/v2/memberships"

        payload = {}
        headers = {
            'Authorization': '{organization-slug}:{secret-key}'
        }

        response = requests.request("GET", url, headers=headers, data=payload)

        print(response.text)

    def test_get_show_attachment_v2(self):
        print("test_get_show_attachment_v2")

        url = "https://thirdparty.qonto.com/v2/attachments/{id}"

        payload = {}
        headers = {
            'Authorization': '{organization-slug}:{secret-key}'
        }

        response = requests.request("GET", url, headers=headers, data=payload)

        print(response.text)

    def test_get_list_of_attachments_within_a_transaction_v2(self):
        print("test_get_list_of_attachments_within_a_transaction_v2")

        url = "https://thirdparty.qonto.com/v2/transactions/{transaction_id}/attachments"

        payload = {}
        headers = {
            'Authorization': '{organization-slug}:{secret-key}'
        }

        response = requests.request("GET", url, headers=headers, data=payload)

        print(response.text)

    def test_delete_list_of_attachments_within_a_transaction_v2(self):
        print("test_delete_list_of_attachments_within_a_transaction_v2")

        url = "https://thirdparty.qonto.com/v2/transactions/{transaction_id}/attachments"

        payload = {}
        headers = {
            'Authorization': '{organization-slug}:{secret-key}'
        }

        response = requests.request("DELETE", url, headers=headers, data=payload)

        print(response.text)

    def test_delete_remove_an_attachment_from_a_transaction_v2(self):
        print("test_delete_remove_an_attachment_from_a_transaction_v2")

        url = "https://thirdparty.qonto.com/v2/transactions/{transaction_id}/attachments/{id}"

        payload = {}
        headers = {
            'Authorization': '{organization-slug}:{secret-key}'
        }

        response = requests.request("DELETE", url, headers=headers, data=payload)

        print(response.text)

    def test_post_upload_an_attachment_to_a_transaction_v2(self):
        print("test_post_upload_an_attachment_to_a_transaction_v2")

        url = "https://thirdparty.qonto.com/v2/transactions/{transaction_id}/attachments"

        payload = json.dumps({
            "file": "string"
        })
        headers = {
            'Authorization': '{organization-slug}:{secret-key}',
            'X-Qonto-Idempotency-Key': 'X-Qonto-Idempotency-Key',
            'Content-Type': 'application/json'
        }

        response = requests.request("POST", url, headers=headers, data=payload)

        print(response.text)

    def test_post_transfers_between_accounts_of_the_same_organization_v2(self):
        print("test_post_transfers_between_accounts_of_the_same_organization_v2")

        url = "https://thirdparty.qonto.com/v2/internal_transfers"

        payload = json.dumps({
            "internal_transfer": {
                "debit_iban": "string",
                "credit_iban": "string",
                "reference": "string",
                "amount": "string",
                "currency": "string"
            }
        })
        headers = {
            'Authorization': '{organization-slug}:{secret-key}',
            'X-Qonto-Idempotency-Key': 'X-Qonto-Idempotency-Key',
            'Content-Type': 'application/json'
        }

        response = requests.request("POST", url, headers=headers, data=payload)

        print(response.text)


if __name__ == '__main__':
    unittest.main()
