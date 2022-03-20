import unittest
from requests_tor import RequestsTor

endpoint = "https://api.bondora.com"
client_id = ''
client_secret = ''
scope = 'BidsEdit BidsRead Investments ReportRead'


# https://api.bondora.com/doc?v=1
class UnitTestsBondoraAPIWithTorRequest(unittest.TestCase):
    def test_Authorization_Code_Request(self):
        print("test_Authorization_Code_Request")

        url = endpoint + "/oauth/authorize"

        params = {
            'response_type': 'code',
            'client_id': client_id,
            'scope': scope,
        }

        rt = RequestsTor()

        r = rt.get(url, params=params)

        print(r.text)


class UnitTestsBondoraAPIOAuthWithTorRequest(unittest.TestCase):
    def test_POST_oauth__access_token(self):
        print("test_POST_oauth__access_token")

        url = endpoint + "/oauth/access_token"

        params = {
            'grant_type': 'refresh_token ',
            'client_id': client_id,
            'client_secret': client_secret
        }
        rt = RequestsTor()

        r = rt.post(url, params=params)

        data = r.json()

        access_token = str(data['access_token'])

        print(access_token)

    def test_POST_oauth__access_token__revoke(self):
        print("test_POST_oauth__access_token__revoke")

        url = endpoint + "/oauth/access_token"

        params = {
            'grant_type': 'refresh_token ',
            'client_id': client_id,
            'client_secret': client_secret
        }
        rt = RequestsTor()

        r = rt.post(url, params=params)

        data = r.json()

        access_token = str(data['access_token'])

        headers = {
            'Authorization': 'Bearer ' + access_token,
            'Content-Type': 'application/json',
            'Accept': 'application/json'
        }

        response = rt.post(endpoint + '/oauth/access_token/revoke', headers=headers)

        print(response.json())


class UnitTestsBondoraAPIAccountWithTorRequest(unittest.TestCase):
    def test_GET_api__v1__account__balance(self):
        print("test_GET_api__v1__account__balance")

        url = endpoint + "/oauth/access_token"

        params = {
            'grant_type': 'refresh_token ',
            'client_id': client_id,
            'client_secret': client_secret
        }

        rt = RequestsTor()

        r = rt.post(url, params=params)

        data = r.json()

        access_token = str(data['access_token'])

        headers = {
            'Authorization': 'Bearer ' + access_token,
            'Content-Type': 'application/json',
            'Accept': 'application/json'
        }

        response = rt.get(endpoint + '/api/v1/account/balance', headers=headers)

        print(response.json())

    def test_GET_api__v1__account__investments(self):
        print("test_GET_api__v1__account__investments")

        url = endpoint + "/oauth/access_token"

        params = {
            'grant_type': 'refresh_token ',
            'client_id': client_id,
            'client_secret': client_secret
        }

        rt = RequestsTor()

        r = rt.post(url, params=params)

        data = r.json()

        access_token = str(data['access_token'])

        headers = {
            'Authorization': 'Bearer ' + access_token,
            'Content-Type': 'application/json',
            'Accept': 'application/json'
        }

        params_1 = {
            'scope': 'Investments',
        }

        response = rt.get(endpoint + '/api/v1/account/investments', headers=headers, params=params_1)

        print(response.json())

    def test_GET_api__v1__eventlog(self):
        print('test_GET_api__v1__eventlog')

        url = endpoint + "/oauth/access_token"

        params = {
            'grant_type': 'refresh_token ',
            'client_id': client_id,
            'client_secret': client_secret
        }

        rt = RequestsTor()

        r = rt.post(url, params=params)

        data = r.json()

        access_token = str(data['access_token'])

        headers = {
            'Authorization': 'Bearer ' + access_token,
            'Content-Type': 'application/json',
            'Accept': 'application/json'
        }

        response = rt.get(endpoint + '/api/v1/eventlog', headers=headers)

        print(response.json())


class UnitTestsBondoraAPIBidWithTorRequest(unittest.TestCase):
    def test_GET_api__v1__bids(self):
        print("test_GET_api__v1__bids")

        url = endpoint + "/oauth/access_token"

        params = {
            'grant_type': 'refresh_token ',
            'client_id': client_id,
            'client_secret': client_secret
        }

        rt = RequestsTor()

        r = rt.post(url, params=params)

        data = r.json()

        access_token = str(data['access_token'])

        headers = {
            'Authorization': 'Bearer ' + access_token,
            'Content-Type': 'application/json',
            'Accept': 'application/json'
        }

        params_1 = {
            'scope': 'BidsRead',
        }

        response = rt.get(endpoint + '/api/v1/bids', headers=headers, params=params_1)

        print(response.json())

    def test_POST_api__v1__bid(self):
        print("test_POST_api__v1__bid")

        url = endpoint + "/oauth/access_token"

        params = {
            'grant_type': 'refresh_token ',
            'client_id': client_id,
            'client_secret': client_secret
        }

        rt = RequestsTor()

        r = rt.post(url, params=params)

        data = r.json()

        access_token = str(data['access_token'])

        headers = {
            'Authorization': 'Bearer ' + access_token,
            'Content-Type': 'application/json',
            'Accept': 'application/json'
        }

        params_1 = {
            'scope': 'BidsEdit',
        }

        bids = {
          "Bids": [
            {
              "AuctionId": "60384b8f-4409-48ac-8139-2eb982a5e3fe",
              "Amount": 2.0,
              "MinAmount": 1.0
            },
            {
              "AuctionId": "60384b8f-4409-48ac-8139-2eb982a5e3fe",
              "Amount": 2.0,
              "MinAmount": 1.0
            }
          ]
        }

        response = rt.post(endpoint + '/api/v1/bid', headers=headers, params=params_1, data=bids)

        print(response.json())

    def test_GET_api_v1_bid__id(self):
        print("test_GET_api_v1_bid__id")

        url = endpoint + "/oauth/access_token"

        params = {
            'grant_type': 'refresh_token ',
            'client_id': client_id,
            'client_secret': client_secret
        }

        rt = RequestsTor()

        r = rt.post(url, params=params)

        data = r.json()

        access_token = str(data['access_token'])

        headers = {
            'Authorization': 'Bearer ' + access_token,
            'Content-Type': 'application/json',
            'Accept': 'application/json'
        }

        params_1 = {
            'scope': 'BidsRead',
        }

        id = ""

        response = rt.get(endpoint + '/api/v1/bid/' + id, headers=headers, params=params_1)

        print(response.json())

    def test_POST_api__v1__bid__id__cancel(self):
        print('test_POST_api__v1__bid__id__cancel')

        url = endpoint + "/oauth/access_token"

        params = {
            'grant_type': 'refresh_token ',
            'client_id': client_id,
            'client_secret': client_secret
        }

        rt = RequestsTor()

        r = rt.post(url, params=params)

        data = r.json()

        access_token = str(data['access_token'])

        headers = {
            'Authorization': 'Bearer ' + access_token,
            'Content-Type': 'application/json',
            'Accept': 'application/json'
        }

        params_1 = {
            'scope': 'BidsEdit',
        }

        id = ""

        response = rt.post(endpoint + '/api/v1/bid/' + id + '/cancel', headers=headers, params=params_1)

        print(response.json())


class UnitTestsBondoraAPIReportWithTorRequest(unittest.TestCase):
    def test_GET_api__v1__publicdataset(self):
        print("test_GET_api__v1__publicdataset")

        url = endpoint + "/oauth/access_token"

        params = {
            'grant_type': 'refresh_token ',
            'client_id': client_id,
            'client_secret': client_secret
        }

        rt = RequestsTor()

        r = rt.post(url, params=params)

        data = r.json()

        access_token = str(data['access_token'])

        headers = {
            'Authorization': 'Bearer ' + access_token,
            'Content-Type': 'application/json',
            'Accept': 'application/json'
        }

        response = rt.get(endpoint + '/api/v1/publicdataset', headers=headers)

        print(response.json())

    def test_GET_api__v1__reports(self):
        print("test_GET_api__v1__reports")

        url = endpoint + "/oauth/access_token"

        params = {
            'grant_type': 'refresh_token ',
            'client_id': client_id,
            'client_secret': client_secret
        }

        rt = RequestsTor()

        r = rt.post(url, params=params)

        data = r.json()

        access_token = str(data['access_token'])

        headers = {
            'Authorization': 'Bearer ' + access_token,
            'Content-Type': 'application/json',
            'Accept': 'application/json'
        }

        params_1 = {
            'scope': 'ReportRead',
        }

        response = rt.get(endpoint + '/api/v1/reports', headers=headers, params=params_1)

        print(response.json())

    def test_GET_api__v1__report__id(self):
        print("test_GET_api__v1__report__id")

        url = endpoint + "/oauth/access_token"

        params = {
            'grant_type': 'refresh_token ',
            'client_id': client_id,
            'client_secret': client_secret
        }

        rt = RequestsTor()

        r = rt.post(url, params=params)

        data = r.json()

        access_token = str(data['access_token'])

        headers = {
            'Authorization': 'Bearer ' + access_token,
            'Content-Type': 'application/json',
            'Accept': 'application/json'
        }

        params_1 = {
            'scope': 'ReportRead',
        }

        id = ""

        response = rt.get(endpoint + '/api/v1/report/' + id, headers=headers, params=params_1)

        print(response.json())

    def test_POST_api__v1__report(self):
        print("test_POST_api__v1__report")

        url = endpoint + "/oauth/access_token"

        params = {
            'grant_type': 'refresh_token ',
            'client_id': client_id,
            'client_secret': client_secret
        }

        rt = RequestsTor()

        r = rt.post(url, params=params)

        data = r.json()

        access_token = str(data['access_token'])

        headers = {
            'Authorization': 'Bearer ' + access_token,
            'Content-Type': 'application/json',
            'Accept': 'application/json'
        }

        params_1 = {
            'scope': 'ReportCreate',
        }

        payload = {
          "ReportType": 1,
          "PeriodStart": "2022-03-18T14:20:42.5535999+02:00",
          "PeriodEnd": "2022-03-18T14:20:42.5535999+02:00"
        }

        response = rt.post(endpoint + '/api/v1/report', headers=headers, params=params_1, data=payload)

        print(response.json())


class UnitTestsBondoraAPIAuctionWithTorRequest(unittest.TestCase):
    def test_GET_api__v1__auctions(self):
        print("test_GET_api__v1__auctions")

        url = endpoint + "/oauth/access_token"

        params = {
            'grant_type': 'refresh_token ',
            'client_id': client_id,
            'client_secret': client_secret
        }

        rt = RequestsTor()

        r = rt.post(url, params=params)

        data = r.json()

        access_token = str(data['access_token'])

        headers = {
            'Authorization': 'Bearer ' + access_token,
            'Content-Type': 'application/json',
            'Accept': 'application/json'
        }

        response = rt.get(endpoint + '/api/v1/auctions', headers=headers)

        print(response.json())

    def test_GET_api__v1__auction__id(self):
        print("test_GET_api__v1__auction__id")

        url = endpoint + "/oauth/access_token"

        params = {
            'grant_type': 'refresh_token ',
            'client_id': client_id,
            'client_secret': client_secret
        }

        rt = RequestsTor()

        r = rt.post(url, params=params)

        data = r.json()

        access_token = str(data['access_token'])

        headers = {
            'Authorization': 'Bearer ' + access_token,
            'Content-Type': 'application/json',
            'Accept': 'application/json'
        }

        id = ""

        response = rt.get(endpoint + '/api/v1/auction/' + id, headers=headers)

        print(response.json())


class UnitTestsBondoraAPISecondMarketWithTorRequest(unittest.TestCase):
    def test_GET_api__v1__secondarymarket(self):
        print("test_GET_api__v1__secondarymarket")

        url = endpoint + "/oauth/access_token"

        params = {
            'grant_type': 'refresh_token ',
            'client_id': client_id,
            'client_secret': client_secret
        }

        rt = RequestsTor()

        r = rt.post(url, params=params)

        data = r.json()

        access_token = str(data['access_token'])

        headers = {
            'Authorization': 'Bearer ' + access_token,
            'Content-Type': 'application/json',
            'Accept': 'application/json'
        }

        response = rt.get(endpoint + '/api/v1/secondarymarket', headers=headers)

        print(response.json())

    def test_GET_api__v1__loanpart__id(self):
        print("test_GET_api__v1__loanpart__id")

        url = endpoint + "/oauth/access_token"

        params = {
            'grant_type': 'refresh_token ',
            'client_id': client_id,
            'client_secret': client_secret
        }

        rt = RequestsTor()

        r = rt.post(url, params=params)

        data = r.json()

        access_token = str(data['access_token'])

        headers = {
            'Authorization': 'Bearer ' + access_token,
            'Content-Type': 'application/json',
            'Accept': 'application/json'
        }

        id = ""

        response = rt.get(endpoint + '/api/v1/loanpart/' + id, headers=headers)

        print(response.json())

    def test_GET_api__v1__loanpart__list(self):
        print("test_GET_api__v1__loanpart__list")

        url = endpoint + "/oauth/access_token"

        params = {
            'grant_type': 'refresh_token ',
            'client_id': client_id,
            'client_secret': client_secret
        }

        rt = RequestsTor()

        r = rt.post(url, params=params)

        data = r.json()

        access_token = str(data['access_token'])

        headers = {
            'Authorization': 'Bearer ' + access_token,
            'Content-Type': 'application/json',
            'Accept': 'application/json'
        }

        itemIds = {
          "ItemIds": [
            "86f32e1c-11fd-4329-9387-da2c04546038",
            "7679d907-794f-4a0b-91c9-965f3bee7a64"
          ]
        }

        response = rt.get(endpoint + '/api/v1/loanpart/list', headers=headers, data=itemIds)

        print(response.json())

    def test_POST_api__v1__secondarymarket__buy(self):
        print("test_POST_api__v1__secondarymarket__buy")

        url = endpoint + "/oauth/access_token"

        params = {
            'grant_type': 'refresh_token ',
            'client_id': client_id,
            'client_secret': client_secret
        }

        rt = RequestsTor()

        r = rt.post(url, params=params)

        data = r.json()

        access_token = str(data['access_token'])

        headers = {
            'Authorization': 'Bearer ' + access_token,
            'Content-Type': 'application/json',
            'Accept': 'application/json'
        }

        itemIds = {
          "ItemIds": [
            "86f32e1c-11fd-4329-9387-da2c04546038",
            "7679d907-794f-4a0b-91c9-965f3bee7a64"
          ]
        }

        params_1 = {
            'scope': 'SmBuy'
        }

        response = rt.post(endpoint + '/api/v1/secondarymarket/buy', headers=headers, data=itemIds, params=params_1)

        print(response.json())

    def test_POST_api__v1__secondarymarket__sell(self):
        print("test_POST_api__v1__secondarymarket__sell")

        url = endpoint + "/oauth/access_token"

        params = {
            'grant_type': 'refresh_token ',
            'client_id': client_id,
            'client_secret': client_secret
        }

        rt = RequestsTor()

        r = rt.post(url, params=params)

        data = r.json()

        access_token = str(data['access_token'])

        headers = {
            'Authorization': 'Bearer ' + access_token,
            'Content-Type': 'application/json',
            'Accept': 'application/json'
        }

        payload = {
          "Items": [
            {
              "LoanPartId": "29224ad5-30b4-4f44-9257-6d34ca4ef9a8",
              "DesiredDiscountRate": 2
            },
            {
              "LoanPartId": "29224ad5-30b4-4f44-9257-6d34ca4ef9a8",
              "DesiredDiscountRate": 2
            }
          ],
          "CancelItemOnPaymentReceived": True,
          "CancelItemOnReschedule": True
        }

        params_1 = {
            'scope': 'SmSell'
        }

        response = rt.post(endpoint + '/api/v1/secondarymarket/sell', headers=headers, data=payload, params=params_1)

        print(response.json())

    def test_POST_api__v1__secondarymarket__id__cancel(self):
        print("test_POST_api__v1__secondarymarket__id__cancel")

        url = endpoint + "/oauth/access_token"

        params = {
            'grant_type': 'refresh_token ',
            'client_id': client_id,
            'client_secret': client_secret
        }

        rt = RequestsTor()

        r = rt.post(url, params=params)

        data = r.json()

        access_token = str(data['access_token'])

        headers = {
            'Authorization': 'Bearer ' + access_token,
            'Content-Type': 'application/json',
            'Accept': 'application/json'
        }

        params_1 = {
            'scope': 'SmSell'
        }

        id = ""

        response = rt.post(endpoint + '/api/v1/secondarymarket/' + id + '/cancel', headers=headers, params=params_1)

        print(response.json())

    def test_POST_api__v1__secondarymarket__cancel(self):
        print("test_POST_api__v1__secondarymarket__cancel")

        url = endpoint + "/oauth/access_token"

        params = {
            'grant_type': 'refresh_token ',
            'client_id': client_id,
            'client_secret': client_secret
        }

        rt = RequestsTor()

        r = rt.post(url, params=params)

        data = r.json()

        access_token = str(data['access_token'])

        headers = {
            'Authorization': 'Bearer ' + access_token,
            'Content-Type': 'application/json',
            'Accept': 'application/json'
        }

        params_1 = {
            'scope': 'SmSell'
        }

        itemIds = {
          "ItemIds": [
            "31ebcd0b-1542-4acc-8a8e-8d9077933fe8",
            "6c063178-ca22-43db-9983-1eac8d71d9dc"
          ]
        }

        response = rt.post(endpoint + '/api/v1/secondarymarket/cancel', headers=headers, params=params_1, data=itemIds)

        print(response.json())

    def test_GET_api__v1__secondarymarket__id(self):
        print("test_GET_api__v1__secondarymarket__id")

        url = endpoint + "/oauth/access_token"

        params = {
            'grant_type': 'refresh_token ',
            'client_id': client_id,
            'client_secret': client_secret
        }

        rt = RequestsTor()

        r = rt.post(url, params=params)

        data = r.json()

        access_token = str(data['access_token'])

        headers = {
            'Authorization': 'Bearer ' + access_token,
            'Content-Type': 'application/json',
            'Accept': 'application/json'
        }

        id = ""

        response = rt.get(endpoint + '/api/v1/secondarymarket/' + id, headers=headers)

        print(response.json())

    def test_GET_api__v1__secondarymarket__list(self):
        print("test_GET_api__v1__secondarymarket__list")

        url = endpoint + "/oauth/access_token"

        params = {
            'grant_type': 'refresh_token ',
            'client_id': client_id,
            'client_secret': client_secret
        }

        rt = RequestsTor()

        r = rt.post(url, params=params)

        data = r.json()

        access_token = str(data['access_token'])

        headers = {
            'Authorization': 'Bearer ' + access_token,
            'Content-Type': 'application/json',
            'Accept': 'application/json'
        }

        itemIds = {
          "ItemIds": [
            "56e65fce-ed23-43a2-a5e8-8929befb2800",
            "3689c09f-ff1d-425f-ba76-f6d5685b5181"
          ]
        }

        response = rt.get(endpoint + '/api/v1/secondarymarket/list', headers=headers, data=itemIds)

        print(response.json())


if __name__ == '__main__':
    unittest.main()
