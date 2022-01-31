import unittest
import requests
import json


class Unit_Tests_Algoan_API_Authentication(unittest.TestCase):
    def test_post_create_a_new_access_token(self):
        print('test_post_create_a_new_access_token')

        url = "https://api.algoan.com/v2/oauth/token"

        payload = 'client_id=string&client_secret=string&grant_type=client_credentials'

        headers = {
            'Content-Type': 'application/x-www-form-urlencoded'
        }

        response = requests.request("POST", url, headers=headers, data=payload)

        print(response.text)


class Unit_Tests_Algoan_API_Customer(unittest.TestCase):
    def test_get_get_a_list_of_all_the_customers(self):
        print('test_get_get_a_list_of_all_the_customers')

        url = "https://api.algoan.com/v2/customers?limit=string&page=string"

        payload = {}

        headers = {}

        response = requests.request("GET", url, headers=headers, data=payload)

        print(response.text)

    def test_post_create_a_customer(self):
        print('test_post_create_a_customer')

        url = "https://api.algoan.com/v2/customers"

        payload = json.dumps({
            "customIdentifier": "my_id_43523",
            "aggregationDetails": {
                "callbackUrl": "string",
                "token": "string",
                "redirectUrl": "string",
                "apiUrl": "string",
                "userId": "string",
                "clientId": "string"
            },
            "personalDetails": {
                "identity": {
                    "nationality": "FR",
                    "firstName": "John",
                    "lastName": "Smith",
                    "birthName": "Smith",
                    "birthDate": "1990-01-01T00:00:00.000Z",
                    "birthCity": "Paris",
                    "birthZipCode": "75001",
                    "birthCountry": "FR"
                },
                "contact": {
                    "email": "test@algoan.com",
                    "phoneNumber": "+33611223344",
                    "street": "151 rue saint denis",
                    "additionalInformation": "second Floor",
                    "city": "Paris",
                    "zipCode": 75002,
                    "country": "FR"
                },
                "household": {
                    "maritalStatus": "CIVIL_PARTNERSHIP",
                    "numberOfDependentChildren": 2,
                    "numberOfOtherDependents": 0
                }
            }
        })

        headers = {
            'Content-Type': 'application/json'
        }

        response = requests.request("POST", url, headers=headers, data=payload)

        print(response.text)

    def test_get_get_a_single_customer(self):
        print("test_get_get_a_single_customer")

        url = "https://api.algoan.com/v2/customers/{id}"

        payload = {}

        headers = {}

        response = requests.request("GET", url, headers=headers, data=payload)

        print(response.text)

    def test_delete_delete_a_single_customer(self):
        print("test_delete_delete_a_single_customer")

        url = "https://api.algoan.com/v2/customers/{id}"

        payload = {}

        headers = {}

        response = requests.request("DELETE", url, headers=headers, data=payload)

        print(response.text)

    def test_patch_update_a_customer(self):
        print("test_patch_update_a_customer")

        url = "https://api.algoan.com/v2/customers/{id}"

        payload = json.dumps({
            "aggregationDetails": {
                "callbackUrl": "string",
                "token": "string",
                "redirectUrl": "string",
                "apiUrl": "string",
                "userId": "string",
                "clientId": "string"
            }
        })
        headers = {
            'Content-Type': 'application/json'
        }

        response = requests.request("PATCH", url, headers=headers, data=payload)

        print(response.text)


class Unit_Tests_Algoan_API_Score_And_Credit_Insights(unittest.TestCase):
    def test_post_create_a_new_analysis(self):
        print("test_post_create_a_new_analysis")

        url = "https://api.algoan.com/v2/customers/{id}/analyses"

        payload = json.dumps({
            "parameters": {
                "disableScores": False,
                "disableCreditInsights": False
            },
            "accounts": [
                {
                    "type": "CHECKING",
                    "balance": 3564.5,
                    "balanceDate": "2019-06-30T22:00:00.000Z",
                    "currency": "EUR",
                    "owners": [
                        {
                            "name": "John Doe"
                        }
                    ],
                    "iban": "FR7630001007941234567890185",
                    "bic": "BDFEFR2T",
                    "name": "compte de pierre paul jacques",
                    "bank": {
                        "id": "string",
                        "logoUrl": "string",
                        "name": "string",
                        "country": "string"
                    },
                    "usage": "PERSONAL",
                    "country": "FR",
                    "coming": 400,
                    "details": {
                        "savings": {
                            "type": "SHORT_TERM",
                            "openedAt": "2019-06-30T22:00:00.000Z",
                            "maximumAmount": 20000,
                            "interestRate": 0.1456
                        },
                        "loan": {
                            "type": "REVOLVING",
                            "amount": 10000,
                            "startDate": "2019-06-30T22:00:00.000Z",
                            "endDate": "2019-06-30T22:00:00.000Z",
                            "duration": 24,
                            "insuranceLabel": "Insurance A",
                            "payment": 10,
                            "remainingCapital": 1000,
                            "interestRate": 0.1456
                        }
                    },
                    "aggregator": {
                        "id": "string"
                    },
                    "transactions": [
                        {
                            "description": "Expenses",
                            "dates": {
                                "debitedAt": "2019-06-30T22:00:00.000Z",
                                "bookedAt": "2019-08-24T14:15:22Z"
                            },
                            "amount": 10000,
                            "currency": "EUR",
                            "isComing": False,
                            "aggregator": {
                                "id": "12a22",
                                "category": "string",
                                "type": "string"
                            }
                        }
                    ]
                }
            ]
        })

        headers = {
            'Content-Type': 'application/json'
        }

        response = requests.request("POST", url, headers=headers, data=payload)

        print(response.text)

    def test_get_get_all_analyses(self):
        print("test_get_get_all_analyses")

        url = "https://api.algoan.com/v2/customers/{id}/analyses"

        payload = ""

        headers = {}

        response = requests.request("GET", url, headers=headers, data=payload)

        print(response.text)

    def test_get_get_an_analysis(self):
        print('test_get_get_an_analysis')

        url = "https://api.algoan.com/v2/customers/{id}/analyses/{analysisId}"

        payload = ""

        headers = {}

        response = requests.request("GET", url, headers=headers, data=payload)

        print(response.text)

    def test_patch_update_an_analysis(self):
        print("test_patch_update_an_analysis")

        url = "https://api.algoan.com/v2/customers/{id}/analyses/{analysisId}"

        payload = json.dumps({
            "accounts": [
                {
                    "type": "CHECKING",
                    "balance": 3564.5,
                    "balanceDate": "2019-06-30T22:00:00.000Z",
                    "currency": "EUR",
                    "owners": [
                        {
                            "name": "John Doe"
                        }
                    ],
                    "iban": "FR7630001007941234567890185",
                    "bic": "BDFEFR2T",
                    "name": "compte de pierre paul jacques",
                    "bank": {
                        "id": "string",
                        "logoUrl": "string",
                        "name": "string",
                        "country": "string"
                    },
                    "usage": "PERSONAL",
                    "country": "FR",
                    "coming": 400,
                    "details": {
                        "savings": {
                            "type": "SHORT_TERM",
                            "openedAt": "2019-06-30T22:00:00.000Z",
                            "maximumAmount": 20000,
                            "interestRate": 0.1456
                        },
                        "loan": {
                            "type": "REVOLVING",
                            "amount": 10000,
                            "startDate": "2019-06-30T22:00:00.000Z",
                            "endDate": "2019-06-30T22:00:00.000Z",
                            "duration": 24,
                            "insuranceLabel": "Insurance A",
                            "payment": 10,
                            "remainingCapital": 1000,
                            "interestRate": 0.1456
                        }
                    },
                    "aggregator": {
                        "id": "string"
                    },
                    "transactions": [
                        {
                            "description": "Expenses",
                            "dates": {
                                "debitedAt": "2019-06-30T22:00:00.000Z",
                                "bookedAt": "2019-08-24T14:15:22Z"
                            },
                            "amount": 10000,
                            "currency": "EUR",
                            "isComing": False,
                            "aggregator": {
                                "id": "12a22",
                                "category": "string",
                                "type": "string"
                            }
                        }
                    ]
                }
            ]
        })

        headers = {
            'Content-Type': 'application/json'
        }

        response = requests.request("GET", url, headers=headers, data=payload)

        print(response.text)

    def test_get_incomes(self):
        print("test_get_incomes")

        url = "https://api.algoan.com/v2/customers/{id}/analyses/{analysisId}/credit-insights/incomes"

        payload = ""

        headers = {}

        response = requests.request("GET", url, headers=headers, data=payload)

        print(response.text)

    def test_get_expenses(self):
        print("test_get_expenses")

        url = "https://api.algoan.com/v2/customers/{id}/analyses/{analysisId}/credit-insights/expenses"

        payload = ""

        headers = {}

        response = requests.request("GET", url, headers=headers, data=payload)

        print(response.text)

    def test_get_loans(self):
        print("test_get_loans")

        url = "https://api.algoan.com/v2/customers/{id}/analyses/{analysisId}/credit-insights/loans"

        payload = ""

        headers = {}

        response = requests.request("GET", url, headers=headers, data=payload)

        print(response.text)

    def test_get_risk_indicators(self):
        print("test_get_risk_indicators")

        url = "https://api.algoan.com/v2/customers/{id}/analyses/{analysisId}/credit-insights/risks"

        payload = ""

        headers = {}

        response = requests.request("GET", url, headers=headers, data=payload)

        print(response.text)

    def test_get_cash_flows(self):
        print("test_get_cash_flows")

        url = "https://api.algoan.com/v2/customers/{id}/analyses/{analysisId}/credit-insights/cash-flows"

        payload = ""

        headers = {}

        response = requests.request("GET", url, headers=headers, data=payload)

        print(response.text)

    def test_get_get_scores(self):
        print("test_get_get_scores")

        url = "https://api.algoan.com/v2/customers/{id}/analyses/{analysisId}/scores"

        payload = ""

        headers = {}

        response = requests.request("GET", url, headers=headers, data=payload)

        print(response.text)


class Unit_Tests_Algoan_API_Banking_Data(unittest.TestCase):
    def test_get_get_all_accounts(self):
        print("test_get_get_all_accounts")

        url = "https://api.algoan.com/v2/customers/{id}/analyses/{analysisId}/accounts"

        payload = ""
        headers = {}

        response = requests.request("GET", url, headers=headers, data=payload)

        print(response.text)

    def test_get_get_all_transactions(self):
        print("test_get_get_all_transactions")

        url = "https://api.algoan.com/v2/customers/{id}/analyses/{analysisId}/transactions"

        payload = ""
        
        headers = {}

        response = requests.request("GET", url, headers=headers, data=payload)

        print(response.text)

    def test_get_get_all_account_transactions(self):
        print("test_get_get_all_account_transactions")

        url = "https://api.algoan.com/v2/customers/{id}/analyses/{analysisId}/accounts/{accountId}/transactions"

        payload = ""
        headers = {}

        response = requests.request("GET", url, headers=headers, data=payload)

        print(response.text)


if __name__ == '__main__':
    unittest.main()
