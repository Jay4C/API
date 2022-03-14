import unittest
import requests


class UnitTestsShineAPIAuthentication(unittest.TestCase):
    # https://developers.shine.fr/reference#authorize
    def test_get_authorize(self):
        print("test_get_authorize")

        url = "https://api.shine.fr/v2/authentication/oauth2/authorize"

        querystring = {"client_id": "client_id", "scope": "scope",
                       "redirect_uri": "redirect_uri", "state": "state",
                       "response_type": "response_type"}

        headers = {"Accept": "application/json"}

        response = requests.request("GET", url, headers=headers, params=querystring)

        print(response.text)

    # https://developers.shine.fr/reference#token
    def test_post_token(self):
        print("test_post_token")

        url = "https://api.shine.fr/v2/authentication/oauth2/token"

        payload = {
            "client_id": "client_id",
            "client_secret": "client_secret",
            "grant_type": "grant_type",
            "redirect_uri": "redirect_uri",
            "code": "code",
            "refresh_token": "refresh_token"
        }
        headers = {
            "Accept": "application/json",
            "Content-Type": "application/json"
        }

        response = requests.request("POST", url, json=payload, headers=headers)

        print(response.text)

    # https://developers.shine.fr/reference#revoke
    def test_post_revoke(self):
        print("test_post_revoke")

        url = "https://api.shine.fr/v2/authentication/oauth2/token/revoke"

        payload = {
            "client_id": "client_id",
            "client_secret": "client_secret",
            "token": "token"
        }
        headers = {
            "Accept": "application/json",
            "Content-Type": "application/json"
        }

        response = requests.request("POST", url, json=payload, headers=headers)

        print(response.text)

    # https://developers.shine.fr/reference#jwks
    def test_get_jwks(self):
        print("test_get_jwks")

        url = "https://api.shine.fr/v2/authentication/oauth2/jwks.json"

        headers = {"Accept": "application/json"}

        response = requests.request("GET", url, headers=headers)

        print(response.text)

    # https://developers.shine.fr/reference#pollactionrequest
    def test_post_pollactionrequest(self):
        print("test_post_pollactionrequest")

        url = "https://api.shine.fr/v2/authentication/oauth2/action_request/authenticationActionRequestId/poll"

        payload = {
            "client_id": "client_id",
            "client_secret": "client_secret"
        }
        headers = {
            "Accept": "application/json",
            "Content-Type": "application/json"
        }

        response = requests.request("POST", url, json=payload, headers=headers)

        print(response.text)

    # https://developers.shine.fr/reference#createactionrequest
    def test_post_createactionrequest(self):
        print("test_post_createactionrequest")

        url = "https://api.shine.fr/v2/authentication/oauth2/action_request"

        payload = {
            "payload": {"newKey": "New Value"},
            "action": "action",
            "client_id": "client_id",
            "client_secret": "client_secret",
            "uid": "uid"
        }
        headers = {
            "Accept": "application/json",
            "Content-Type": "application/json"
        }

        response = requests.request("POST", url, json=payload, headers=headers)

        print(response.text)


class UnitTestsShineAPIUsersProfiles(unittest.TestCase):
    # https://developers.shine.fr/reference#getuserprofile
    def test_get_getuserprofile(self):
        print('test_get_getuserprofile')

        url = "https://api.shine.fr/v2/users/profiles"

        headers = {"Accept": "application/json"}

        response = requests.request("GET", url, headers=headers)

        print(response.text)

    # https://developers.shine.fr/reference#get
    def test_get_get(self):
        print('test_get_get')

        url = "https://api.shine.fr/v2/users/profiles/uid"

        headers = {"Accept": "application/json"}

        response = requests.request("GET", url, headers=headers)

        print(response.text)


class UnitTestsShineAPICompaniesProfiles(unittest.TestCase):
    # https://developers.shine.fr/reference#getusercompaniesprofiles
    def test_get_getusercompaniesprofiles(self):
        print("test_get_getusercompaniesprofiles")

        url = "https://api.shine.fr/v2/companies/profiles"

        headers = {"Accept": "application/json"}

        response = requests.request("GET", url, headers=headers)

        print(response.text)

    # https://developers.shine.fr/reference#get-2
    def test_get_get_2(self):
        print("test_get_get_2")

        url = "https://api.shine.fr/v2/companies/profiles/companyProfileId"

        headers = {"Accept": "application/json"}

        response = requests.request("GET", url, headers=headers)

        print(response.text)


class UnitTestsShineAPIBankAccounts(unittest.TestCase):
    # https://developers.shine.fr/reference#getuserbankaccounts
    def test_get_getuserbankaccounts(self):
        print("test_get_getuserbankaccounts")

        url = "https://api.shine.fr/v2/bank/accounts"

        headers = {"Accept": "application/json"}

        response = requests.request("GET", url, headers=headers)

        print(response.text)

    # https://developers.shine.fr/reference#coveragecheck
    def test_post_coveragecheck(self):
        print("test_post_coveragecheck")

        url = "https://api.shine.fr/v2/bank/accounts/bankAccountId/coverage-check"

        payload = {"amount": 1}
        headers = {
            "Accept": "application/json",
            "Content-Type": "application/json"
        }

        response = requests.request("POST", url, json=payload, headers=headers)

        print(response.text)

    # https://developers.shine.fr/reference#get-5
    def test_get_get_5(self):
        print('test_get_get_5')

        url = "https://api.shine.fr/v2/bank/accounts/bankAccountId"

        headers = {"Accept": "application/json"}

        response = requests.request("GET", url, headers=headers)

        print(response.text)


class UnitTestsShineAPITransactions(unittest.TestCase):
    # https://developers.shine.fr/reference#query-4
    def test_get_query_4(self):
        print('test_get_query_4')

        url = "https://api.shine.fr/v3/transactions/query"

        querystring = {"bankAccountId": "bankAccountId", "first": "1", "last": "1", "after": "after",
                       "before": "before", "status": "VALIDATED", "paymentMethod": "CARD",
                       "feeType": "FREE",
                       "category": "DEFAULT", "q": "q", "type": "payin", "hasReceipts": "true",
                       "isPersonal": "true",
                       "isRefund": "true", "isHidden": "true", "transactionAfter": "1",
                       "transactionBefore": "1",
                       "minValue": "2", "maxValue": "1", "transactionId": "transactionId"}

        headers = {"Accept": "application/json"}

        response = requests.request("GET", url, headers=headers, params=querystring)

        print(response.text)

    # https://developers.shine.fr/reference#get-4
    def test_get_get_4(self):
        print('test_get_get_4')

        url = "https://api.shine.fr/v3/transactions/transactionId"

        headers = {"Accept": "application/json"}

        response = requests.request("GET", url, headers=headers)

        print(response.text)


class UnitTestsShineAPIBankTransfers(unittest.TestCase):
    # https://developers.shine.fr/reference#query-3
    def test_get_query_3(self):
        print("test_get_query_3")

        url = "https://api.shine.fr/v3/bank/transfers/query"

        querystring = {"uid": "uid", "first": "1", "after": "after",
                       "bankTransferRecipientId": "bankTransferRecipientId",
                       "bankProviderTransferId": "bankProviderTransferId",
                       "bankAccountId": "bankAccountId", "min": "1",
                       "max": "1", "status": "status"}

        headers = {"Accept": "application/json"}

        response = requests.request("GET", url, headers=headers, params=querystring)

        print(response.text)

    # https://developers.shine.fr/reference#queryrecipient
    def test_get_queryrecipient(self):
        print('test_get_queryrecipient')

        url = "https://api.shine.fr/v3/bank/transfers/recipients/query"

        querystring = {"uid": "uid", "name": "name", "first": "1", "after": "1",
                       "bankProvider": "TREEZOR",
                       "bankProviderTransferRecipientId": "bankProviderTransferRecipientId",
                       "usableForSct": "true",
                       "sepaCreditorIdentifier": "sepaCreditorIdentifier",
                       "isTreezorBeneficiary": "true",
                       "includeDeleted": "true"}

        headers = {"Accept": "application/json"}

        response = requests.request("GET", url, headers=headers, params=querystring)

        print(response.text)

    # https://developers.shine.fr/reference#get-3
    def test_get_get_3(self):
        print("test_get_get_3")

        url = "https://api.shine.fr/v3/bank/transfers/bankTransferId"

        headers = {"Accept": "application/json"}

        response = requests.request("GET", url, headers=headers)

        print(response.text)

    # https://developers.shine.fr/reference#getrecipient
    def test_get_getrecipient(self):
        print("test_get_getrecipient")

        url = "https://api.shine.fr/v3/bank/transfers/recipients/bankTransferRecipientId"

        headers = {"Accept": "application/json"}

        response = requests.request("GET", url, headers=headers)

        print(response.text)

    # https://developers.shine.fr/reference#updaterecipient
    def test_put_updaterecipient(self):
        print("test_put_updaterecipient")

        url = "https://api.shine.fr/v3/bank/transfers/recipients/bankTransferRecipientId"

        payload = {
            "iban": "iban",
            "swiftBic": "swiftBic",
            "label": "label",
            "name": "name",
            "phoneNumber": "phoneNumber",
            "sepaCreditorIdentifier": "sepaCreditorIdentifier",
            "isUserBankAccount": True
        }
        headers = {
            "Accept": "application/json",
            "Content-Type": "application/json"
        }

        response = requests.request("PUT", url, json=payload, headers=headers)

        print(response.text)

    # https://developers.shine.fr/reference#cancel
    def test_delete_cancel(self):
        print("test_delete_cancel")

        url = "https://api.shine.fr/v3/bank/transfers/bankTransferId"

        headers = {"Accept": "application/json"}

        response = requests.request("DELETE", url, headers=headers)

        print(response.text)

    # https://developers.shine.fr/reference#deleterecipient
    def test_delete_deleterecipient(self):
        print("test_delete_deleterecipient")

        url = "https://api.shine.fr/v3/bank/transfers/recipients/bankTransferRecipientId"

        headers = {"Accept": "application/json"}

        response = requests.request("DELETE", url, headers=headers)

        print(response.text)

    # https://developers.shine.fr/reference#create
    def test_post_create(self):
        print("test_post_create")

        url = "https://api.shine.fr/v3/bank/transfers"

        payload = {
            "uid": "uid",
            "recurrence": "recurrence",
            "bankTransferRecipientId": "bankTransferRecipientId",
            "operatorNote": "operatorNote",
            "operatorFlag": "operatorFlag",
            "startAt": 1,
            "startRecurringAt": 1,
            "endRecurringAt": 1,
            "userLabel": "userLabel",
            "currency": "currency",
            "amount": 1,
            "receiptUrl": "receiptUrl"
        }
        headers = {
            "Accept": "application/json",
            "Content-Type": "application/json"
        }

        response = requests.request("POST", url, json=payload, headers=headers)

        print(response.text)

    # https://developers.shine.fr/reference#createrecipient
    def test_post_createrecipient(self):
        print("test_post_createrecipient")

        url = "https://api.shine.fr/v3/bank/transfers/recipients"

        payload = {
            "uid": "uid",
            "iban": "iban",
            "swiftBic": "swiftBic",
            "label": "label",
            "name": "name",
            "phoneNumber": "phoneNumber",
            "isUserBankAccount": True,
            "usableForSct": True,
            "sepaCreditorIdentifier": "sepaCreditorIdentifier"
        }
        headers = {
            "Accept": "application/json",
            "Content-Type": "application/json"
        }

        response = requests.request("POST", url, json=payload, headers=headers)

        print(response.text)


class UnitTestsShineAPIInvoicesService(unittest.TestCase):
    # https://developers.shine.fr/reference#querytasks
    def test_get_querytasks(self):
        print("test_get_querytasks")

        url = "https://api.shine.fr/v2/invoices/tasks/query"

        querystring = {"invoiceId": "invoiceId"}

        headers = {"Accept": "application/json"}

        response = requests.request("GET", url, headers=headers, params=querystring)

        print(response.text)

    # https://developers.shine.fr/reference#gettask
    def test_get_gettask(self):
        print("test_get_gettask")

        url = "https://api.shine.fr/v2/invoices/tasks/invoiceTaskId"

        headers = {"Accept": "application/json"}

        response = requests.request("GET", url, headers=headers)

        print(response.text)

    # https://developers.shine.fr/reference#query
    def test_get_query(self):
        print("test_get_query")

        url = "https://api.shine.fr/v2/invoices/query"

        querystring = {"uid": "uid", "first": "1", "last": "1", "after": "1", "before": "1",
                       "clientId": "clientId",
                       "fiscalId": "fiscalId", "deleted": "true",
                       "searchInput": "searchInput", "status": "PAID"}

        headers = {"Accept": "application/json"}

        response = requests.request("GET", url, headers=headers, params=querystring)

        print(response.text)

    # https://developers.shine.fr/reference#get-6
    def test_get_get_6(self):
        print("test_get_get_6")

        url = "https://api.shine.fr/v2/invoices/invoiceId"

        headers = {"Accept": "application/json"}

        response = requests.request("GET", url, headers=headers)

        print(response.text)


class UnitTestsShineAPIReceiptsService(unittest.TestCase):
    # https://developers.shine.fr/reference#insert-2
    def test_post_insert_2(self):
        print("test_post_insert_2")

        url = "https://api.shine.fr/v2/receipts"

        payload = {
            "bucketName": "bucketName",
            "bucketPath": "bucketPath",
            "category": "category",
            "currency": "currency",
            "deleted": True,
            "fileRef": "fileRef",
            "processing": True,
            "sellerName": "sellerName",
            "subtotal": 1,
            "thumbUrl": "thumbUrl",
            "total": 1,
            "transactionAt": 1,
            "transactionId": "transactionId",
            "url": "url",
            "uid": "uid",
            "vat": 1
        }
        headers = {
            "Accept": "application/json",
            "Content-Type": "application/json"
        }

        response = requests.request("POST", url, json=payload, headers=headers)

        print(response.text)

    # https://developers.shine.fr/reference#query-2
    def test_get_query_2(self):
        print("test_get_query_2")

        url = "https://api.shine.fr/v2/receipts/query"

        querystring = {"uid": "uid", "first": "1", "last": "1", "after": "1", "before": "1", "q": "q",
                       "category": "category", "transactionId": "transactionId", "url": "url"}

        headers = {"Accept": "application/json"}

        response = requests.request("GET", url, headers=headers, params=querystring)

        print(response.text)

    # https://developers.shine.fr/reference#get-7
    def test_get_get_7(self):
        print('test_get_get_7')

        url = "https://api.shine.fr/v2/receipts/receiptId"

        headers = {"Accept": "application/json"}

        response = requests.request("GET", url, headers=headers)

        print(response.text)

    # https://developers.shine.fr/reference#update
    def test_put_update(self):
        print("test_put_update")

        url = "https://api.shine.fr/v2/receipts/receiptId"

        payload = {
            "bucketName": "bucketName",
            "bucketPath": "bucketPath",
            "category": "category",
            "currency": "currency",
            "deleted": True,
            "fileRef": "fileRef",
            "processing": True,
            "sellerName": "sellerName",
            "subtotal": 1,
            "thumbUrl": "thumbUrl",
            "total": 1,
            "transactionAt": 1,
            "transactionId": "transactionId",
            "url": "url",
            "vat": 1
        }
        headers = {
            "Accept": "application/json",
            "Content-Type": "application/json"
        }

        response = requests.request("PUT", url, json=payload, headers=headers)

        print(response.text)


class UnitTestsShineAPITransactionEnrichmentService(unittest.TestCase):
    # https://developers.shine.fr/reference#queryinvoicemappings
    def test_get_queryinvoicemappings(self):
        print("test_get_queryinvoicemappings")

        url = "https://api.shine.fr/v2/transaction_enrichment/invoice_mappings"

        querystring = {"transactionId": "transactionId", "invoiceId": "invoiceId", "includeDeleted": "true"}

        headers = {"Accept": "application/json"}

        response = requests.request("GET", url, headers=headers, params=querystring)

        print(response.text)


if __name__ == '__main__':
    unittest.main()
