import unittest
import requests


# https://developer-psd2.skrill.com/api-reference
class UnitTestsSkrillAPITokenManagement(unittest.TestCase):
    # https://developer-psd2.skrill.com/api-reference/client-management/token-management/oauth2authorize
    def test_get_auth_realms_dw_v1_authorize(self):
        print('test_get_auth_realms_dw_v1_authorize')

        url = "https://account.skrill.com/psd2-oauth2/auth/realms/dw/v1/authorize"

        querystring = {"code_challenge_method": "code_challenge_method", "code_challenge": "code_challenge",
                       "state": "state", "scope": "scope", "redirect_uri": "redirect_uri",
                       "client_id": "client_id",
                       "response_type": "response_type"}

        response = requests.request("GET", url, params=querystring)

        print(response.text)

    # https://developer-psd2.skrill.com/api-reference/client-management/token-management/oauth2tokenpost
    def test_post_auth_realms_dw_v1_token(self):
        print('test_post_auth_realms_dw_v1_token')

        url = "https://oauth2-psd2.skrill.com/psd2-oauth2/auth/realms/dw/v1/token"

        payload = "grant_type=authorization_code"
        headers = {'content-type': 'application/x-www-form-urlencoded'}

        response = requests.request("POST", url, data=payload, headers=headers)

        print(response.text)


class UnitTestsSkrillAPIClientManagement(unittest.TestCase):
    # https://developer-psd2.skrill.com/api-reference/client-management/client-management/oauth2registrationpost
    def test_post_v1_registrations(self):
        print('test_post_v1_registrations')

        headers = {
            'content-type': 'application/json',
        }

        data = '{"redirect_uris":["string"],"token_endpoint_auth_method":"urn:paysafe:oauth:' \
               'token-endpoint-auth-method:eidas-qwac:psd","grant_types":["string"],' \
               '"response_types":["string"],"client_name":"string","logo_uri":"string",' \
               '"scope":"string","jwks":{"keys":[{"kty":"RSA","use":"sig","key_ops":' \
               '["string"],"kid":"string","x5c":["string"],"x5u":"string"}]}}'

        response = requests.post('https://oauth2-psd2.skrill.com/psd2-oauth2/v1/registrations', headers=headers,
                                 data=data)

        print(response.json())

    # https://developer-psd2.skrill.com/api-reference/client-management/client-management/oauth2registrationget
    def test_get_v1_registrations_clientId(self):
        print('test_get_v1_registrations_clientId')

        url = "https://oauth2-psd2.skrill.com/psd2-oauth2/v1/registrations/clientId"

        response = requests.request("GET", url)

        print(response.text)

    # https://developer-psd2.skrill.com/api-reference/client-management/client-management/oauth2registrationput
    def test_put_v1_registrations_clientId(self):
        print('test_put_v1_registrations_clientId')

        headers = {
            'content-type': 'application/json',
        }

        data = '{"redirect_uris":["string"],"token_endpoint_auth_method":"urn:paysafe:' \
               'oauth:token-endpoint-auth-method:eidas-qwac:psd","grant_types":["string"],' \
               '"response_types":["string"],"client_name":"string","logo_uri":"string",' \
               '"scope":"string","jwks":{"keys":[{"kty":"RSA","use":"sig","key_ops":' \
               '["string"],"kid":"string","x5c":["string"],"x5u":"string"}]}}'

        response = requests.post('https://oauth2-psd2.skrill.com/psd2-oauth2/v1/registrations/clientId',
                                 headers=headers, data=data)

        print(response.json())

    # https://developer-psd2.skrill.com/api-reference/client-management/client-management/oauth2registrationdelete
    def test_delete_v1_registrations_clientId(self):
        print('test_delete_v1_registrations_clientId')

        url = "https://oauth2-psd2.skrill.com/psd2-oauth2/v1/registrations/clientId"

        response = requests.request("DELETE", url)

        print(response.text)


class UnitTestsSkrillAPIReference(unittest.TestCase):
    # https://developer-psd2.skrill.com/api-reference/client-management/reference/auth-realms-dw-v1-authorize/serversauthrealmsdwv1authorize
    def test_servers_auth_realms_dw_v1_authorize(self):
        print('test_servers_auth_realms_dw_v1_authorize')

        url = "https://account.skrill.com/psd2-oauth2/auth/realms/dw/v1/authorize"

        response = requests.request("SERVERS", url)

        print(response.text)


class UnitTestsSkrillAPIAccountInformationService(unittest.TestCase):
    # https://developer-psd2.skrill.com/api-reference/skrill-mobile-api/account-information-service/getaccounts
    def test_get_v1_accounts(self):
        print('test_get_v1_accounts')

        url = "https://mobile-api.skrill.com/mobile/v1/accounts"

        headers = {'authorization': 'Bearer oauth_access_token'}

        response = requests.request("GET", url, headers=headers)

        print(response.text)

    # https://developer-psd2.skrill.com/api-reference/skrill-mobile-api/account-information-service/gettransactionhistory
    def test_get_v1_transactions_all_transactions_history(self):
        print('test_get_v1_transactions_all_transactions_history')

        url = "https://mobile-api.skrill.com/mobile/v1/transactions/all-transactions-history"

        querystring = {"countPerPage": "countPerPage", "page": "page", "toDate": "toDate",
                       "fromDate": "fromDate",
                       "accountId": "accountId"}

        headers = {'authorization': 'Bearer oauth_access_token'}

        response = requests.request("GET", url, headers=headers, params=querystring)

        print(response.text)


class UnitTestsSkrillAPIPaymentInitiationService(unittest.TestCase):
    # https://developer-psd2.skrill.com/api-reference/skrill-mobile-api/payment-initiation-service/sendmoneypreview
    def test_get_me_send_money_preview(self):
        print('test_get_me_send_money_preview')

        url = "https://mobile-api.skrill.com/mobile/me/send-money/preview"

        querystring = {"recipientEmail": "recipientEmail", "senderAccountId": "senderAccountId",
                       "currency": "currency",
                       "amount": "amount"}

        headers = {'authorization': 'Bearer oauth_access_token'}

        response = requests.request("GET", url, headers=headers, params=querystring)

        print(response.text)

    # https://developer-psd2.skrill.com/api-reference/skrill-mobile-api/payment-initiation-service/sendmoney
    def test_post_me_send_money(self):
        print('test_post_me_send_money')

        headers = {
            'authorization': 'Bearer oauth_access_token',
            'content-type': 'application/json',
        }

        data = '{"amount":123,"currency":"string","message":"string","recipientEmail":"string",' \
               '"senderAccountId":"string"}'

        response = requests.post('https://mobile-api.skrill.com/mobile/me/send-money',
                                 headers=headers, data=data)

        print(response.json())

    # https://developer-psd2.skrill.com/api-reference/skrill-mobile-api/payment-initiation-service/sendmoneyfinalize
    def test_post_me_send_money_slipid_finalize(self):
        print('test_post_me_send_money_slipid_finalize')

        headers = {
            'content-type': 'application/json',
        }

        data = '{"scaDetails":{"clientEventId":"string","eventId":"string","link":"string"}}'

        response = requests.post('https://mobile-api.skrill.com/mobile/me/send-money/slipID/finalize',
                                 headers=headers,
                                 data=data)

        print(response.json())


class UnitTestsSkrillAPIStrongCustomerAuthentication(unittest.TestCase):
    # https://developer-psd2.skrill.com/api-reference/skrill-mobile-api/strong-customer-authentication/verifyotp
    def test_post_api_2fa_v1_otp_verify(self):
        print('test_post_api_2fa_v1_otp_verify')

        headers = {
            'authorization': 'Bearer oauth_access_token',
            'content-type': 'application/json',
        }

        data = '{"clientEventId":"string","eventId":"string (uuid)","verifyCode":"string"}'

        response = requests.post('https://mobile-api.skrill.com/mobile/api/2fa/v1/otp-verify', headers=headers,
                                 data=data)

        print(response.json())

    # https://developer-psd2.skrill.com/api-reference/skrill-mobile-api/strong-customer-authentication/sendsms
    def test_post_api_2fa_v1_sms_challenge(self):
        print('test_post_api_2fa_v1_sms_challenge')

        headers = {
            'authorization': 'Bearer oauth_access_token',
            'content-type': 'application/json',
        }

        data = '{"clientEventId":"string","eventId":"string"}'

        response = requests.post('https://mobile-api.skrill.com/mobile/api/2fa/v1/sms-challenge', headers=headers,
                                 data=data)

        print(response.json())


if __name__ == '__main__':
    unittest.main()
