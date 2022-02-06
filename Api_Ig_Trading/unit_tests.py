import unittest
import requests


demo_api_key = ""
# demo
base_endpoint = "https://demo-api.ig.com/gateway/deal"

# prod
# base_endpoint = "https://api.ig.com/gateway/deal"


class UnitTestsApiIgAccount(unittest.TestCase):
    # https://labs.ig.com/rest-trading-api-reference/service-detail?id=619
    def test_accounts(self):
        print('test_accounts')

        url_session = base_endpoint + "/session"

        payload = {
            "identifier": "A12345",
            "password": "112233"
        }

        headers = {
            'Content-Type': 'application/json; charset=UTF-8',
            'Accept': 'application/json; charset=UTF-8',
            'VERSION': '2',
            'X-IG-API-KEY': demo_api_key
        }

        response_session = requests.request("POST", url_session, headers=headers, data=payload)

        cst = response_session.headers.get('CST')

        x_security_token = response_session.headers.get('X-SECURITY-TOKEN')

        url_accounts = base_endpoint + "/accounts"

        headers = {
            'Content-Type': 'application/json; charset=UTF-8',
            'Accept': 'application/json; charset=UTF-8',
            'X-IG-API-KEY': demo_api_key,
            'CST': cst,
            'X-SECURITY-TOKEN': x_security_token
        }

        response_accounts = requests.request("GET", url_accounts, headers=headers)

        print(response_accounts.text)

    # https://labs.ig.com/rest-trading-api-reference/service-detail?id=597
    def test_accounts_preferences(self):
        print('test_accounts_preferences')

        url_session = base_endpoint + "/session"

        payload = {
            "identifier": "A12345",
            "password": "112233"
        }

        headers = {
            'Content-Type': 'application/json; charset=UTF-8',
            'Accept': 'application/json; charset=UTF-8',
            'VERSION': '2',
            'X-IG-API-KEY': demo_api_key
        }

        response_session = requests.request("POST", url_session, headers=headers, data=payload)

        cst = response_session.headers.get('CST')

        x_security_token = response_session.headers.get('X-SECURITY-TOKEN')

        url_accounts_preferences = base_endpoint + "/accounts/preferences"

        headers = {
            'Content-Type': 'application/json; charset=UTF-8',
            'Accept': 'application/json; charset=UTF-8',
            'X-IG-API-KEY': demo_api_key,
            'CST': cst,
            'X-SECURITY-TOKEN': x_security_token
        }

        response_accounts_preferences = requests.request("GET", url_accounts_preferences, headers=headers)

        print(response_accounts_preferences.text)

    # https://labs.ig.com/rest-trading-api-reference/service-detail?id=609
    def test_history_activity(self):
        print('test_history_activity')

        url_session = base_endpoint + "/session"

        payload = {
            "identifier": "A12345",
            "password": "112233"
        }

        headers = {
            'Content-Type': 'application/json; charset=UTF-8',
            'Accept': 'application/json; charset=UTF-8',
            'VERSION': '2',
            'X-IG-API-KEY': demo_api_key
        }

        response_session = requests.request("POST", url_session, headers=headers, data=payload)

        cst = response_session.headers.get('CST')

        x_security_token = response_session.headers.get('X-SECURITY-TOKEN')

        url_history_activity = base_endpoint + "/history/activity"

        headers = {
            'Content-Type': 'application/json; charset=UTF-8',
            'Accept': 'application/json; charset=UTF-8',
            'X-IG-API-KEY': demo_api_key,
            'CST': cst,
            'X-SECURITY-TOKEN': x_security_token
        }

        response_history_activity = requests.request("GET", url_history_activity, headers=headers)

        print(response_history_activity.text)

    # https://labs.ig.com/rest-trading-api-reference/service-detail?id=605
    def test_history_activity_fromDate_toDate(self):
        print('test_history_activity_fromDate_toDate')

        url_session = base_endpoint + "/session"

        payload = {
            "identifier": "A12345",
            "password": "112233"
        }

        headers = {
            'Content-Type': 'application/json; charset=UTF-8',
            'Accept': 'application/json; charset=UTF-8',
            'VERSION': '2',
            'X-IG-API-KEY': demo_api_key
        }

        response_session = requests.request("POST", url_session, headers=headers, data=payload)

        cst = response_session.headers.get('CST')

        x_security_token = response_session.headers.get('X-SECURITY-TOKEN')

        from_date = "dd-mm-yyyy"

        to_date = "dd-mm-yyyy"

        url_history_activity_fromdate_todate = base_endpoint + "/history/activity/" + from_date + "/" + to_date

        headers = {
            'Content-Type': 'application/json; charset=UTF-8',
            'Accept': 'application/json; charset=UTF-8',
            'X-IG-API-KEY': demo_api_key,
            'CST': cst,
            'X-SECURITY-TOKEN': x_security_token
        }

        response_history_activity_fromdate_todate = requests.request("GET", url_history_activity_fromdate_todate, headers=headers)

        print(response_history_activity_fromdate_todate.text)

    # https://labs.ig.com/rest-trading-api-reference/service-detail?id=615
    def test_history_activity_lastPeriod(self):
        print('test_history_activity_lastPeriod')

        url_session = base_endpoint + "/session"

        payload = {
            "identifier": "A12345",
            "password": "112233"
        }

        headers = {
            'Content-Type': 'application/json; charset=UTF-8',
            'Accept': 'application/json; charset=UTF-8',
            'VERSION': '2',
            'X-IG-API-KEY': demo_api_key
        }

        response_session = requests.request("POST", url_session, headers=headers, data=payload)

        cst = response_session.headers.get('CST')

        x_security_token = response_session.headers.get('X-SECURITY-TOKEN')

        last_period = 111

        url_history_activity_lastperiod = base_endpoint + "/history/activity/" + str(last_period)

        headers = {
            'Content-Type': 'application/json; charset=UTF-8',
            'Accept': 'application/json; charset=UTF-8',
            'X-IG-API-KEY': demo_api_key,
            'CST': cst,
            'X-SECURITY-TOKEN': x_security_token
        }

        response_history_activity_lastperiod = requests.request("GET", url_history_activity_lastperiod, headers=headers)

        print(response_history_activity_lastperiod.text)

    # https://labs.ig.com/rest-trading-api-reference/service-detail?id=591
    def test_history_transactions(self):
        print('test_history_transactions')

        url_session = base_endpoint + "/session"

        payload = {
            "identifier": "A12345",
            "password": "112233"
        }

        headers = {
            'Content-Type': 'application/json; charset=UTF-8',
            'Accept': 'application/json; charset=UTF-8',
            'VERSION': '2',
            'X-IG-API-KEY': demo_api_key
        }

        response_session = requests.request("POST", url_session, headers=headers, data=payload)

        cst = response_session.headers.get('CST')

        x_security_token = response_session.headers.get('X-SECURITY-TOKEN')

        url_history_transactions = base_endpoint + "/history/transactions"

        headers = {
            'Content-Type': 'application/json; charset=UTF-8',
            'Accept': 'application/json; charset=UTF-8',
            'X-IG-API-KEY': demo_api_key,
            'CST': cst,
            'X-SECURITY-TOKEN': x_security_token
        }

        response_history_transactions = requests.request("GET", url_history_transactions, headers=headers)

        print(response_history_transactions.text)

    # https://labs.ig.com/rest-trading-api-reference/service-detail?id=601
    def test_history_transactions_transactiontype_fromdate_todate(self):
        print('test_history_transactions_transactiontype_fromdate_todate')

        url_session = base_endpoint + "/session"

        payload = {
            "identifier": "A12345",
            "password": "112233"
        }

        headers = {
            'Content-Type': 'application/json; charset=UTF-8',
            'Accept': 'application/json; charset=UTF-8',
            'VERSION': '2',
            'X-IG-API-KEY': demo_api_key
        }

        response_session = requests.request("POST", url_session, headers=headers, data=payload)

        cst = response_session.headers.get('CST')

        x_security_token = response_session.headers.get('X-SECURITY-TOKEN')

        transactiontype = "ALL"

        fromdate = ""

        todate = ""

        url_history_transactions_transactiontype_fromdate_todate = base_endpoint + "/history/transactions/" \
                                                                   + transactiontype \
                                                                   + "/" + fromdate \
                                                                   + "/" + todate

        headers = {
            'Content-Type': 'application/json; charset=UTF-8',
            'Accept': 'application/json; charset=UTF-8',
            'X-IG-API-KEY': demo_api_key,
            'CST': cst,
            'X-SECURITY-TOKEN': x_security_token
        }

        response_history_transactions_transactiontype_fromdate_todate = requests.request("GET", url_history_transactions_transactiontype_fromdate_todate, headers=headers)

        print(response_history_transactions_transactiontype_fromdate_todate.text)

    # https://labs.ig.com/rest-trading-api-reference/service-detail?id=623
    def test_history_transactions_transactiontype_lastperiod(self):
        print('test_history_transactions_transactiontype_lastperiod')

        url_session = base_endpoint + "/session"

        payload = {
            "identifier": "A12345",
            "password": "112233"
        }

        headers = {
            'Content-Type': 'application/json; charset=UTF-8',
            'Accept': 'application/json; charset=UTF-8',
            'VERSION': '2',
            'X-IG-API-KEY': demo_api_key
        }

        response_session = requests.request("POST", url_session, headers=headers, data=payload)

        cst = response_session.headers.get('CST')

        x_security_token = response_session.headers.get('X-SECURITY-TOKEN')

        transactiontype = "ALL"

        lastperiod = str(111)

        url_history_transactions_transactiontype_lastperiod = base_endpoint + "/history/transactions/" \
                                                              + transactiontype \
                                                              + "/" + lastperiod

        headers = {
            'Content-Type': 'application/json; charset=UTF-8',
            'Accept': 'application/json; charset=UTF-8',
            'X-IG-API-KEY': demo_api_key,
            'CST': cst,
            'X-SECURITY-TOKEN': x_security_token
        }

        response_history_transactions_transactiontype_lastperiod = requests.request("GET",
                                                                                    url_history_transactions_transactiontype_lastperiod,
                                                                                    headers=headers)

        print(response_history_transactions_transactiontype_lastperiod.text)


class UnitTestsApiIgDealing(unittest.TestCase):
    # https://labs.ig.com/rest-trading-api-reference/service-detail?id=612
    def test_confirms_dealreference(self):
        print('test_confirms_dealreference')

        url_session = base_endpoint + "/session"

        payload = {
            "identifier": "A12345",
            "password": "112233"
        }

        headers = {
            'Content-Type': 'application/json; charset=UTF-8',
            'Accept': 'application/json; charset=UTF-8',
            'VERSION': '2',
            'X-IG-API-KEY': demo_api_key
        }

        response_session = requests.request("POST", url_session, headers=headers, data=payload)

        cst = response_session.headers.get('CST')

        x_security_token = response_session.headers.get('X-SECURITY-TOKEN')

        dealreference = ""

        url_confirms_dealreference = base_endpoint + "/confirms/" + dealreference

        headers = {
            'Content-Type': 'application/json; charset=UTF-8',
            'Accept': 'application/json; charset=UTF-8',
            'X-IG-API-KEY': demo_api_key,
            'CST': cst,
            'X-SECURITY-TOKEN': x_security_token
        }

        response_confirms_dealreference = requests.request("GET", url_confirms_dealreference, headers=headers)

        print(response_confirms_dealreference.text)

    # https://labs.ig.com/rest-trading-api-reference/service-detail?id=611
    def test_positions(self):
        print('test_positions')

        url_session = base_endpoint + "/session"

        payload = {
            "identifier": "A12345",
            "password": "112233"
        }

        headers = {
            'Content-Type': 'application/json; charset=UTF-8',
            'Accept': 'application/json; charset=UTF-8',
            'VERSION': '2',
            'X-IG-API-KEY': demo_api_key
        }

        response_session = requests.request("POST", url_session, headers=headers, data=payload)

        cst = response_session.headers.get('CST')

        x_security_token = response_session.headers.get('X-SECURITY-TOKEN')

        url_positions = base_endpoint + "/positions"

        headers = {
            'Content-Type': 'application/json; charset=UTF-8',
            'Accept': 'application/json; charset=UTF-8',
            'X-IG-API-KEY': demo_api_key,
            'CST': cst,
            'X-SECURITY-TOKEN': x_security_token
        }

        response_positions = requests.request("GET", url_positions, headers=headers)

        print(response_positions.text)

    # https://labs.ig.com/rest-trading-api-reference/service-detail?id=607
    def test_positions_dealid(self):
        print('test_positions_dealid')

        url_session = base_endpoint + "/session"

        payload = {
            "identifier": "A12345",
            "password": "112233"
        }

        headers = {
            'Content-Type': 'application/json; charset=UTF-8',
            'Accept': 'application/json; charset=UTF-8',
            'VERSION': '2',
            'X-IG-API-KEY': demo_api_key
        }

        response_session = requests.request("POST", url_session, headers=headers, data=payload)

        cst = response_session.headers.get('CST')

        x_security_token = response_session.headers.get('X-SECURITY-TOKEN')

        dealid = "string"

        url_positions_dealid = base_endpoint + "/positions/" + dealid

        headers = {
            'Content-Type': 'application/json; charset=UTF-8',
            'Accept': 'application/json; charset=UTF-8',
            'X-IG-API-KEY': demo_api_key,
            'CST': cst,
            'X-SECURITY-TOKEN': x_security_token
        }

        response_positions_dealid = requests.request("GET", url_positions_dealid, headers=headers)

        print(response_positions_dealid.text)

    # https://labs.ig.com/rest-trading-api-reference/service-detail?id=608
    def test_positions_otc(self):
        print('test_positions_otc')

        url_session = base_endpoint + "/session"

        payload = {
            "identifier": "A12345",
            "password": "112233"
        }

        headers = {
            'Content-Type': 'application/json; charset=UTF-8',
            'Accept': 'application/json; charset=UTF-8',
            'VERSION': '2',
            'X-IG-API-KEY': demo_api_key
        }

        response_session = requests.request("POST", url_session, headers=headers, data=payload)

        cst = response_session.headers.get('CST')

        x_security_token = response_session.headers.get('X-SECURITY-TOKEN')

        url_positions_otc = base_endpoint + "/positions/otc"

        payload = {
            'dealId': 'String',
            'direction': 'Constant',
            'epic': 'String',
            'expiry': 'String',
            'level': 'Number',
            'orderType': 'Constant',
            'quoteId': 'String',
            'size': 'Number',
            'timeInForce': 'Constant'
        }

        headers = {
            'Content-Type': 'application/json; charset=UTF-8',
            'Accept': 'application/json; charset=UTF-8',
            'X-IG-API-KEY': demo_api_key,
            'CST': cst,
            'X-SECURITY-TOKEN': x_security_token
        }

        response_positions_otc = requests.request("POST", url_positions_otc, headers=headers, data=payload)

        print(response_positions_otc.text)

    # https://labs.ig.com/rest-trading-api-reference/service-detail?id=593
    def test_positions_otc_dealid(self):
        print('test_positions_otc_dealid')

        url_session = base_endpoint + "/session"

        payload = {
            "identifier": "A12345",
            "password": "112233"
        }

        headers = {
            'Content-Type': 'application/json; charset=UTF-8',
            'Accept': 'application/json; charset=UTF-8',
            'VERSION': '2',
            'X-IG-API-KEY': demo_api_key
        }

        response_session = requests.request("POST", url_session, headers=headers, data=payload)

        cst = response_session.headers.get('CST')

        x_security_token = response_session.headers.get('X-SECURITY-TOKEN')

        dealid = "String"

        url_positions_otc_dealid = base_endpoint + "/positions/otc/" + dealid

        payload = {
            'guaranteedStop': 'Boolean',
            'limitLevel': 'Number',
            'stopLevel': 'Number',
            'trailingStop': 'Boolean',
            'trailingStopDistance': 'Number',
            'trailingStopIncrement': 'Number'
        }

        headers = {
            'Content-Type': 'application/json; charset=UTF-8',
            'Accept': 'application/json; charset=UTF-8',
            'X-IG-API-KEY': demo_api_key,
            'CST': cst,
            'X-SECURITY-TOKEN': x_security_token
        }

        response_positions_otc_dealid = requests.request("PUT", url_positions_otc_dealid, headers=headers, data=payload)

        print(response_positions_otc_dealid.text)

    # https://labs.ig.com/rest-trading-api-reference/service-detail?id=598
    def test_positions_sprintmarkets(self):
        print('test_positions_sprintmarkets')

        url_session = base_endpoint + "/session"

        payload = {
            "identifier": "A12345",
            "password": "112233"
        }

        headers = {
            'Content-Type': 'application/json; charset=UTF-8',
            'Accept': 'application/json; charset=UTF-8',
            'VERSION': '2',
            'X-IG-API-KEY': demo_api_key
        }

        response_session = requests.request("POST", url_session, headers=headers, data=payload)

        cst = response_session.headers.get('CST')

        x_security_token = response_session.headers.get('X-SECURITY-TOKEN')

        url_positions_sprintmarkets = base_endpoint + "/positions/sprintmarkets"

        headers = {
            'Content-Type': 'application/json; charset=UTF-8',
            'Accept': 'application/json; charset=UTF-8',
            'X-IG-API-KEY': demo_api_key,
            'CST': cst,
            'X-SECURITY-TOKEN': x_security_token
        }

        response_positions_sprintmarkets = requests.request("GET", url_positions_sprintmarkets, headers=headers)

        print(response_positions_sprintmarkets.text)

    # https://labs.ig.com/rest-trading-api-reference/service-detail?id=621
    def test_workingorders(self):
        print('test_workingorders')

        url_session = base_endpoint + "/session"

        payload = {
            "identifier": "A12345",
            "password": "112233"
        }

        headers = {
            'Content-Type': 'application/json; charset=UTF-8',
            'Accept': 'application/json; charset=UTF-8',
            'VERSION': '2',
            'X-IG-API-KEY': demo_api_key
        }

        response_session = requests.request("POST", url_session, headers=headers, data=payload)

        cst = response_session.headers.get('CST')

        x_security_token = response_session.headers.get('X-SECURITY-TOKEN')

        url_workingorders = base_endpoint + "/workingorders"

        headers = {
            'Content-Type': 'application/json; charset=UTF-8',
            'Accept': 'application/json; charset=UTF-8',
            'X-IG-API-KEY': demo_api_key,
            'CST': cst,
            'X-SECURITY-TOKEN': x_security_token
        }

        response_workingorders = requests.request("GET", url_workingorders, headers=headers)

        print(response_workingorders.text)

    # https://labs.ig.com/rest-trading-api-reference/service-detail?id=599
    def test_workingorders_otc(self):
        print('test_workingorders_otc')

        url_session = base_endpoint + "/session"

        payload = {
            "identifier": "A12345",
            "password": "112233"
        }

        headers = {
            'Content-Type': 'application/json; charset=UTF-8',
            'Accept': 'application/json; charset=UTF-8',
            'VERSION': '2',
            'X-IG-API-KEY': demo_api_key
        }

        response_session = requests.request("POST", url_session, headers=headers, data=payload)

        cst = response_session.headers.get('CST')

        x_security_token = response_session.headers.get('X-SECURITY-TOKEN')

        url_workingorders_otc = base_endpoint + "/workingorders/otc"

        payload = {
            'currencyCode': 'String',
            'dealReference': 'String',
            'direction': 'Constant',
            'epic': 'String',
            'expiry': 'String',
            'forceOpen': 'Boolean',
            'goodTillDate': 'String',
            'guaranteedStop': 'Boolean',
            'level': 'Number',
            'limitDistance': 'Number',
            'limitLevel': 'Number',
            'size': 'Number',
            'stopDistance': 'Number',
            'stopLevel': 'Number',
            'timeInForce': 'Constant',
            'type': 'Constant'
        }

        headers = {
            'Content-Type': 'application/json; charset=UTF-8',
            'Accept': 'application/json; charset=UTF-8',
            'X-IG-API-KEY': demo_api_key,
            'CST': cst,
            'X-SECURITY-TOKEN': x_security_token
        }

        response_workingorders_otc = requests.request("POST", url_workingorders_otc, headers=headers, data=payload)

        print(response_workingorders_otc.text)

    # https://labs.ig.com/rest-trading-api-reference/service-detail?id=592
    def test_workingorders_otc_dealid_delete(self):
        print('test_workingorders_otc_dealid_delete')

        url_session = base_endpoint + "/session"

        payload = {
            "identifier": "A12345",
            "password": "112233"
        }

        headers = {
            'Content-Type': 'application/json; charset=UTF-8',
            'Accept': 'application/json; charset=UTF-8',
            'VERSION': '2',
            'X-IG-API-KEY': demo_api_key
        }

        response_session = requests.request("POST", url_session, headers=headers, data=payload)

        cst = response_session.headers.get('CST')

        x_security_token = response_session.headers.get('X-SECURITY-TOKEN')

        dealid = "String"

        url_workingorders_otc = base_endpoint + "/workingorders/otc/" + dealid

        payload = {
            'currencyCode': 'String',
            'dealReference': 'String',
            'direction': 'Constant',
            'epic': 'String',
            'expiry': 'String',
            'forceOpen': 'Boolean',
            'goodTillDate': 'String',
            'guaranteedStop': 'Boolean',
            'level': 'Number',
            'limitDistance': 'Number',
            'limitLevel': 'Number',
            'size': 'Number',
            'stopDistance': 'Number',
            'stopLevel': 'Number',
            'timeInForce': 'Constant',
            'type': 'Constant'
        }

        headers = {
            'Content-Type': 'application/json; charset=UTF-8',
            'Accept': 'application/json; charset=UTF-8',
            'X-IG-API-KEY': demo_api_key,
            'CST': cst,
            'X-SECURITY-TOKEN': x_security_token
        }

        response_workingorders_otc = requests.request("DELETE", url_workingorders_otc, headers=headers, data=payload)

        print(response_workingorders_otc.text)

    # https://labs.ig.com/rest-trading-api-reference/service-detail?id=592
    def test_workingorders_otc_dealid_put(self):
        print('test_workingorders_otc_dealid_put')

        url_session = base_endpoint + "/session"

        payload = {
            "identifier": "A12345",
            "password": "112233"
        }

        headers = {
            'Content-Type': 'application/json; charset=UTF-8',
            'Accept': 'application/json; charset=UTF-8',
            'VERSION': '2',
            'X-IG-API-KEY': demo_api_key
        }

        response_session = requests.request("POST", url_session, headers=headers, data=payload)

        cst = response_session.headers.get('CST')

        x_security_token = response_session.headers.get('X-SECURITY-TOKEN')

        dealid = "String"

        url_workingorders_otc = base_endpoint + "/workingorders/otc/" + dealid

        payload = {
            'goodTillDate': 'String',
            'guaranteedStop': 'Boolean',
            'level': 'Number',
            'limitDistance': 'Number',
            'limitLevel': 'Number',
            'stopDistance': 'Number',
            'timeInForce': 'Constant',
            'type': 'Constant'
        }

        headers = {
            'Content-Type': 'application/json; charset=UTF-8',
            'Accept': 'application/json; charset=UTF-8',
            'X-IG-API-KEY': demo_api_key,
            'CST': cst,
            'X-SECURITY-TOKEN': x_security_token
        }

        response_workingorders_otc = requests.request("PUT", url_workingorders_otc, headers=headers, data=payload)

        print(response_workingorders_otc.text)


class UnitTestsApiIgMarkets(unittest.TestCase):
    # https://labs.ig.com/rest-trading-api-reference/service-detail?id=616
    def test_marketnavigation(self):
        print('test_marketnavigation')

        url_session = base_endpoint + "/session"

        payload = {
            "identifier": "A12345",
            "password": "112233"
        }

        headers = {
            'Content-Type': 'application/json; charset=UTF-8',
            'Accept': 'application/json; charset=UTF-8',
            'VERSION': '2',
            'X-IG-API-KEY': demo_api_key
        }

        response_session = requests.request("POST", url_session, headers=headers, data=payload)

        cst = response_session.headers.get('CST')

        x_security_token = response_session.headers.get('X-SECURITY-TOKEN')

        url_marketnavigation = base_endpoint + "/marketnavigation"

        headers = {
            'Content-Type': 'application/json; charset=UTF-8',
            'Accept': 'application/json; charset=UTF-8',
            'X-IG-API-KEY': demo_api_key,
            'CST': cst,
            'X-SECURITY-TOKEN': x_security_token
        }

        response_marketnavigation = requests.request("GET", url_marketnavigation, headers=headers)

        print(response_marketnavigation.text)

    # https://labs.ig.com/rest-trading-api-reference/service-detail?id=610
    def test_marketnavigation_nodeid(self):
        print('test_marketnavigation_nodeid')

        url_session = base_endpoint + "/session"

        payload = {
            "identifier": "A12345",
            "password": "112233"
        }

        headers = {
            'Content-Type': 'application/json; charset=UTF-8',
            'Accept': 'application/json; charset=UTF-8',
            'VERSION': '2',
            'X-IG-API-KEY': demo_api_key
        }

        response_session = requests.request("POST", url_session, headers=headers, data=payload)

        cst = response_session.headers.get('CST')

        x_security_token = response_session.headers.get('X-SECURITY-TOKEN')

        nodeid = "String"

        url_marketnavigation_nodeid = base_endpoint + "/marketnavigation/" + nodeid

        headers = {
            'Content-Type': 'application/json; charset=UTF-8',
            'Accept': 'application/json; charset=UTF-8',
            'X-IG-API-KEY': demo_api_key,
            'CST': cst,
            'X-SECURITY-TOKEN': x_security_token
        }

        response_marketnavigation_nodeid = requests.request("GET", url_marketnavigation_nodeid, headers=headers)

        print(response_marketnavigation_nodeid.text)

    # https://labs.ig.com/rest-trading-api-reference/service-detail?id=590
    def test_markets(self):
        print('test_markets')

        url_session = base_endpoint + "/session"

        payload = {
            "identifier": "A12345",
            "password": "112233"
        }

        headers = {
            'Content-Type': 'application/json; charset=UTF-8',
            'Accept': 'application/json; charset=UTF-8',
            'VERSION': '2',
            'X-IG-API-KEY': demo_api_key
        }

        response_session = requests.request("POST", url_session, headers=headers, data=payload)

        cst = response_session.headers.get('CST')

        x_security_token = response_session.headers.get('X-SECURITY-TOKEN')

        url_markets = base_endpoint + "/markets"

        headers = {
            'Content-Type': 'application/json; charset=UTF-8',
            'Accept': 'application/json; charset=UTF-8',
            'X-IG-API-KEY': demo_api_key,
            'CST': cst,
            'X-SECURITY-TOKEN': x_security_token
        }

        response_markets = requests.request("GET", url_markets, headers=headers)

        print(response_markets.text)

    # https://labs.ig.com/rest-trading-api-reference/service-detail?id=594
    def test_markets_epic(self):
        print('test_markets_epic')

        url_session = base_endpoint + "/session"

        payload = {
            "identifier": "A12345",
            "password": "112233"
        }

        headers = {
            'Content-Type': 'application/json; charset=UTF-8',
            'Accept': 'application/json; charset=UTF-8',
            'VERSION': '2',
            'X-IG-API-KEY': demo_api_key
        }

        response_session = requests.request("POST", url_session, headers=headers, data=payload)

        cst = response_session.headers.get('CST')

        x_security_token = response_session.headers.get('X-SECURITY-TOKEN')

        epic = "String"

        url_markets_epic = base_endpoint + "/markets/" + epic

        headers = {
            'Content-Type': 'application/json; charset=UTF-8',
            'Accept': 'application/json; charset=UTF-8',
            'X-IG-API-KEY': demo_api_key,
            'CST': cst,
            'X-SECURITY-TOKEN': x_security_token
        }

        response_markets_epic = requests.request("GET", url_markets_epic, headers=headers)

        print(response_markets_epic.text)

    # https://labs.ig.com/rest-trading-api-reference/service-detail?id=613
    def test_markets_searchterm_searchterm(self):
        print('test_markets_searchterm_searchterm')

        url_session = base_endpoint + "/session"

        payload = {
            "identifier": "A12345",
            "password": "112233"
        }

        headers = {
            'Content-Type': 'application/json; charset=UTF-8',
            'Accept': 'application/json; charset=UTF-8',
            'VERSION': '2',
            'X-IG-API-KEY': demo_api_key
        }

        response_session = requests.request("POST", url_session, headers=headers, data=payload)

        cst = response_session.headers.get('CST')

        x_security_token = response_session.headers.get('X-SECURITY-TOKEN')

        searchterm = "String"

        url_markets_searchterm = base_endpoint + "/markets?searchTerm=" + searchterm

        headers = {
            'Content-Type': 'application/json; charset=UTF-8',
            'Accept': 'application/json; charset=UTF-8',
            'X-IG-API-KEY': demo_api_key,
            'CST': cst,
            'X-SECURITY-TOKEN': x_security_token
        }

        response_markets_searchterm = requests.request("GET", url_markets_searchterm, headers=headers)

        print(response_markets_searchterm.text)

    # https://labs.ig.com/rest-trading-api-reference/service-detail?id=587
    def test_prices_epic(self):
        print('test_prices_epic')

        url_session = base_endpoint + "/session"

        payload = {
            "identifier": "A12345",
            "password": "112233"
        }

        headers = {
            'Content-Type': 'application/json; charset=UTF-8',
            'Accept': 'application/json; charset=UTF-8',
            'VERSION': '2',
            'X-IG-API-KEY': demo_api_key
        }

        response_session = requests.request("POST", url_session, headers=headers, data=payload)

        cst = response_session.headers.get('CST')

        x_security_token = response_session.headers.get('X-SECURITY-TOKEN')

        epic = "String"

        url_prices_epic = base_endpoint + "/prices/" + epic

        headers = {
            'Content-Type': 'application/json; charset=UTF-8',
            'Accept': 'application/json; charset=UTF-8',
            'X-IG-API-KEY': demo_api_key,
            'CST': cst,
            'X-SECURITY-TOKEN': x_security_token
        }

        response_prices_epic = requests.request("GET", url_prices_epic, headers=headers)

        print(response_prices_epic.text)

    # https://labs.ig.com/rest-trading-api-reference/service-detail?id=618
    def test_prices_epic_resolution_numpoints(self):
        print('test_prices_epic_resolution_numpoints')

        url_session = base_endpoint + "/session"

        payload = {
            "identifier": "A12345",
            "password": "112233"
        }

        headers = {
            'Content-Type': 'application/json; charset=UTF-8',
            'Accept': 'application/json; charset=UTF-8',
            'VERSION': '2',
            'X-IG-API-KEY': demo_api_key
        }

        response_session = requests.request("POST", url_session, headers=headers, data=payload)

        cst = response_session.headers.get('CST')

        x_security_token = response_session.headers.get('X-SECURITY-TOKEN')

        epic = "String"

        resolution = "MINUTE"

        numpoints = str(11)

        url_prices_epic_resolution_numpoints = base_endpoint + "/prices/" + epic + "/" + resolution + "/" + numpoints

        headers = {
            'Content-Type': 'application/json; charset=UTF-8',
            'Accept': 'application/json; charset=UTF-8',
            'X-IG-API-KEY': demo_api_key,
            'CST': cst,
            'X-SECURITY-TOKEN': x_security_token
        }

        response_prices_epic_resolution_numpoints = requests.request("GET",
                                                                     url_prices_epic_resolution_numpoints,
                                                                     headers=headers)

        print(response_prices_epic_resolution_numpoints.text)

    # https://labs.ig.com/rest-trading-api-reference/service-detail?id=596
    def test_prices_epic_resolution_startdate_enddate(self):
        print('test_prices_epic_resolution_startdate_enddate')

        url_session = base_endpoint + "/session"

        payload = {
            "identifier": "A12345",
            "password": "112233"
        }

        headers = {
            'Content-Type': 'application/json; charset=UTF-8',
            'Accept': 'application/json; charset=UTF-8',
            'VERSION': '2',
            'X-IG-API-KEY': demo_api_key
        }

        response_session = requests.request("POST", url_session, headers=headers, data=payload)

        cst = response_session.headers.get('CST')

        x_security_token = response_session.headers.get('X-SECURITY-TOKEN')

        epic = "String"

        resolution = "MINUTE"

        startdate = "yyyy-MM-dd HH:mm:ss"

        enddate = "yyyy-MM-dd HH:mm:ss"

        url_prices_epic_resolution_numpoints = base_endpoint + "/prices/" \
                                               + epic + "/" \
                                               + resolution + "/" \
                                               + startdate + "/" \
                                               + enddate

        headers = {
            'Content-Type': 'application/json; charset=UTF-8',
            'Accept': 'application/json; charset=UTF-8',
            'X-IG-API-KEY': demo_api_key,
            'CST': cst,
            'X-SECURITY-TOKEN': x_security_token
        }

        response_prices_epic_resolution_numpoints = requests.request("GET",
                                                                     url_prices_epic_resolution_numpoints,
                                                                     headers=headers)

        print(response_prices_epic_resolution_numpoints.text)

    # https://labs.ig.com/rest-trading-api-reference/service-detail?id=604
    def test_prices_epic_resolution_startdate_startdate_enddate_enddate(self):
        print('test_prices_epic_resolution_startdate_startdate_enddate_enddate')

        url_session = base_endpoint + "/session"

        payload = {
            "identifier": "A12345",
            "password": "112233"
        }

        headers = {
            'Content-Type': 'application/json; charset=UTF-8',
            'Accept': 'application/json; charset=UTF-8',
            'VERSION': '2',
            'X-IG-API-KEY': demo_api_key
        }

        response_session = requests.request("POST", url_session, headers=headers, data=payload)

        cst = response_session.headers.get('CST')

        x_security_token = response_session.headers.get('X-SECURITY-TOKEN')

        epic = "String"

        resolution = "MINUTE"

        startdate = "yyyy-MM-dd HH:mm:ss"

        enddate = "yyyy-MM-dd HH:mm:ss"

        url_prices_epic_resolution_startdate_enddate = base_endpoint + "/prices/" \
                                               + epic + "/" \
                                               + resolution \
                                               + "?startdate=" + startdate \
                                               + "&enddate=" + enddate

        headers = {
            'Content-Type': 'application/json; charset=UTF-8',
            'Accept': 'application/json; charset=UTF-8',
            'X-IG-API-KEY': demo_api_key,
            'CST': cst,
            'X-SECURITY-TOKEN': x_security_token
        }

        response_prices_epic_resolution_startdate_enddate = requests.request("GET",
                                                                     url_prices_epic_resolution_startdate_enddate,
                                                                     headers=headers)

        print(response_prices_epic_resolution_startdate_enddate.text)


class UnitTestsApiIgWatchlists(unittest.TestCase):
    # https://labs.ig.com/rest-trading-api-reference/service-detail?id=606
    def test_watchlists(self):
        print("test_list_watchlists")

        url_session = base_endpoint + "/session"

        payload = {
            "identifier": "A12345",
            "password": "112233"
        }

        headers = {
            'Content-Type': 'application/json; charset=UTF-8',
            'Accept': 'application/json; charset=UTF-8',
            'VERSION': '2',
            'X-IG-API-KEY': demo_api_key
        }

        response_session = requests.request("POST", url_session, headers=headers, data=payload)

        cst = response_session.headers.get('CST')

        x_security_token = response_session.headers.get('X-SECURITY-TOKEN')

        url_watchlists = base_endpoint + "/watchlists"

        headers = {
            'Content-Type': 'application/json; charset=UTF-8',
            'Accept': 'application/json; charset=UTF-8',
            'X-IG-API-KEY': demo_api_key,
            'CST': cst,
            'X-SECURITY-TOKEN': x_security_token
        }

        response_watchlists = requests.request("GET", url_watchlists, headers=headers)

        print(response_watchlists.text)

    # https://labs.ig.com/rest-trading-api-reference/service-detail?id=603
    def test_watchlists_watchlistid(self):
        print("test_watchlists_watchlistid")

        url_session = base_endpoint + "/session"

        payload = {
            "identifier": "A12345",
            "password": "112233"
        }

        headers = {
            'Content-Type': 'application/json; charset=UTF-8',
            'Accept': 'application/json; charset=UTF-8',
            'VERSION': '2',
            'X-IG-API-KEY': demo_api_key
        }

        response_session = requests.request("POST", url_session, headers=headers, data=payload)

        cst = response_session.headers.get('CST')

        x_security_token = response_session.headers.get('X-SECURITY-TOKEN')

        watchlistid = "String"

        url_watchlists_watchlistid = base_endpoint + "/watchlists/" + watchlistid

        headers = {
            'Content-Type': 'application/json; charset=UTF-8',
            'Accept': 'application/json; charset=UTF-8',
            'X-IG-API-KEY': demo_api_key,
            'CST': cst,
            'X-SECURITY-TOKEN': x_security_token
        }

        response_watchlists_watchlistid = requests.request("DELETE", url_watchlists_watchlistid, headers=headers)

        print(response_watchlists_watchlistid.text)

    # https://labs.ig.com/rest-trading-api-reference/service-detail?id=614
    def test_watchlists_watchlistid_epic(self):
        print("test_watchlists_watchlistid_epic")

        url_session = base_endpoint + "/session"

        payload = {
            "identifier": "A12345",
            "password": "112233"
        }

        headers = {
            'Content-Type': 'application/json; charset=UTF-8',
            'Accept': 'application/json; charset=UTF-8',
            'VERSION': '2',
            'X-IG-API-KEY': demo_api_key
        }

        response_session = requests.request("POST", url_session, headers=headers, data=payload)

        cst = response_session.headers.get('CST')

        x_security_token = response_session.headers.get('X-SECURITY-TOKEN')

        watchlistid = "String"

        epic = "String"

        url_watchlists_watchlistid_epic = base_endpoint + "/watchlists/" + watchlistid + "/" + epic

        headers = {
            'Content-Type': 'application/json; charset=UTF-8',
            'Accept': 'application/json; charset=UTF-8',
            'X-IG-API-KEY': demo_api_key,
            'CST': cst,
            'X-SECURITY-TOKEN': x_security_token
        }

        response_watchlists_watchlistid_epic = requests.request("DELETE",
                                                                url_watchlists_watchlistid_epic,
                                                                headers=headers)

        print(response_watchlists_watchlistid_epic.text)


class UnitTestsApiIgClientSentiment(unittest.TestCase):
    # https://labs.ig.com/rest-trading-api-reference/service-detail?id=617
    def test_clientsentiment(self):
        print("test_clientsentiment")

        url_session = base_endpoint + "/session"

        payload = {
            "identifier": "A12345",
            "password": "112233"
        }

        headers = {
            'Content-Type': 'application/json; charset=UTF-8',
            'Accept': 'application/json; charset=UTF-8',
            'VERSION': '2',
            'X-IG-API-KEY': demo_api_key
        }

        response_session = requests.request("POST", url_session, headers=headers, data=payload)

        cst = response_session.headers.get('CST')

        x_security_token = response_session.headers.get('X-SECURITY-TOKEN')

        url_clientsentiment = base_endpoint + "/clientsentiment"

        headers = {
            'Content-Type': 'application/json; charset=UTF-8',
            'Accept': 'application/json; charset=UTF-8',
            'X-IG-API-KEY': demo_api_key,
            'CST': cst,
            'X-SECURITY-TOKEN': x_security_token
        }

        response_clientsentiment = requests.request("GET", url_clientsentiment, headers=headers)

        print(response_clientsentiment.text)

    # https://labs.ig.com/rest-trading-api-reference/service-detail?id=620
    def test_clientsentiment_marketid(self):
        print("test_clientsentiment_marketid")

        url_session = base_endpoint + "/session"

        payload = {
            "identifier": "A12345",
            "password": "112233"
        }

        headers = {
            'Content-Type': 'application/json; charset=UTF-8',
            'Accept': 'application/json; charset=UTF-8',
            'VERSION': '2',
            'X-IG-API-KEY': demo_api_key
        }

        response_session = requests.request("POST", url_session, headers=headers, data=payload)

        cst = response_session.headers.get('CST')

        x_security_token = response_session.headers.get('X-SECURITY-TOKEN')

        marketid = "marketid"

        url_clientsentiment_marketid = base_endpoint + "/clientsentiment/" + marketid

        headers = {
            'Content-Type': 'application/json; charset=UTF-8',
            'Accept': 'application/json; charset=UTF-8',
            'X-IG-API-KEY': demo_api_key,
            'CST': cst,
            'X-SECURITY-TOKEN': x_security_token
        }

        response_clientsentiment_marketid = requests.request("GET", url_clientsentiment_marketid, headers=headers)

        print(response_clientsentiment_marketid.text)

    # https://labs.ig.com/rest-trading-api-reference/service-detail?id=602
    def test_clientsentiment_related_marketid(self):
        print("test_clientsentiment_related_marketid")

        url_session = base_endpoint + "/session"

        payload = {
            "identifier": "A12345",
            "password": "112233"
        }

        headers = {
            'Content-Type': 'application/json; charset=UTF-8',
            'Accept': 'application/json; charset=UTF-8',
            'VERSION': '2',
            'X-IG-API-KEY': demo_api_key
        }

        response_session = requests.request("POST", url_session, headers=headers, data=payload)

        cst = response_session.headers.get('CST')

        x_security_token = response_session.headers.get('X-SECURITY-TOKEN')

        marketid = "marketid"

        url_clientsentiment_related_marketid = base_endpoint + "/clientsentiment/related/" + marketid

        headers = {
            'Content-Type': 'application/json; charset=UTF-8',
            'Accept': 'application/json; charset=UTF-8',
            'X-IG-API-KEY': demo_api_key,
            'CST': cst,
            'X-SECURITY-TOKEN': x_security_token
        }

        response_clientsentiment_related_marketid = requests.request("GET",
                                                                     url_clientsentiment_related_marketid,
                                                                     headers=headers)

        print(response_clientsentiment_related_marketid.text)


class UnitTestsApiIgLogin(unittest.TestCase):
    # https://labs.ig.com/rest-trading-api-reference/service-detail?id=600
    def test_session_v2(self):
        print('test_session_v2')

        url_session = base_endpoint + "/session"

        payload = {
            "identifier": "A12345",
            "password": "112233"
        }

        headers = {
            'Content-Type': 'application/json; charset=UTF-8',
            'Accept': 'application/json; charset=UTF-8',
            'VERSION': '2',
            'X-IG-API-KEY': demo_api_key
        }

        response_session = requests.request("POST", url_session, headers=headers, data=payload)

        cst = response_session.headers.get('CST')

        x_security_token = response_session.headers.get('X-SECURITY-TOKEN')

        print(response_session.text)

        print('cst : ' + str(cst) + ' _ x_security_token : ' + str(x_security_token))

    # https://labs.ig.com/rest-trading-api-reference/service-detail?id=588
    def test_session_encryptionKey(self):
        print('test_session_encryptionKey')

        url_session = base_endpoint + "/session/encryptionKey"

        headers = {
            'Content-Type': 'application/json; charset=UTF-8',
            'Accept': 'application/json; charset=UTF-8',
            'VERSION': '2',
            'X-IG-API-KEY': demo_api_key
        }

        response_session = requests.request("GET", url_session, headers=headers)

        print(response_session.text)

    # https://labs.ig.com/rest-trading-api-reference/service-detail?id=589
    def test_session_refresh_token(self):
        print('test_session_refresh_token')

        url_session = base_endpoint + "/session/refresh-token"

        payload = {
            "refresh_token": ""
        }

        headers = {
            'Content-Type': 'application/json; charset=UTF-8',
            'Accept': 'application/json; charset=UTF-8',
            'VERSION': '2',
            'X-IG-API-KEY': demo_api_key
        }

        response_session = requests.request("POST", url_session, headers=headers)

        print(response_session.text)


class UnitTestsApiIgGeneral(unittest.TestCase):
    # https://labs.ig.com/rest-trading-api-reference/service-detail?id=595
    def test_operations_application(self):
        print("test_operations_application")

        url_session = base_endpoint + "/session"

        payload = {
            "identifier": "A12345",
            "password": "112233"
        }

        headers = {
            'Content-Type': 'application/json; charset=UTF-8',
            'Accept': 'application/json; charset=UTF-8',
            'VERSION': '2',
            'X-IG-API-KEY': demo_api_key
        }

        response_session = requests.request("POST", url_session, headers=headers, data=payload)

        cst = response_session.headers.get('CST')

        x_security_token = response_session.headers.get('X-SECURITY-TOKEN')

        url_operations_application = base_endpoint + "/operations/application"

        headers = {
            'Content-Type': 'application/json; charset=UTF-8',
            'Accept': 'application/json; charset=UTF-8',
            'X-IG-API-KEY': demo_api_key,
            'CST': cst,
            'X-SECURITY-TOKEN': x_security_token
        }

        response_operations_application = requests.request("GET", url_operations_application, headers=headers)

        print(response_operations_application.text)

    # https://labs.ig.com/rest-trading-api-reference/service-detail?id=622
    def test_operations_application_disable(self):
        print("test_operations_application_disable")

        url_session = base_endpoint + "/session"

        payload = {
            "identifier": "A12345",
            "password": "112233"
        }

        headers = {
            'Content-Type': 'application/json; charset=UTF-8',
            'Accept': 'application/json; charset=UTF-8',
            'VERSION': '2',
            'X-IG-API-KEY': demo_api_key
        }

        response_session = requests.request("POST", url_session, headers=headers, data=payload)

        cst = response_session.headers.get('CST')

        x_security_token = response_session.headers.get('X-SECURITY-TOKEN')

        url_operations_application_disable = base_endpoint + "/operations/application/disable"

        headers = {
            'Content-Type': 'application/json; charset=UTF-8',
            'Accept': 'application/json; charset=UTF-8',
            'X-IG-API-KEY': demo_api_key,
            'CST': cst,
            'X-SECURITY-TOKEN': x_security_token
        }

        response_operations_application_disable = requests.request("PUT",
                                                                   url_operations_application_disable,
                                                                   headers=headers)

        print(response_operations_application_disable.text)


if __name__ == '__main__':
    unittest.main()
