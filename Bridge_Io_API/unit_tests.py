import unittest
import requests


class Unit_Tests_Bridge_Io_API_Quickstart(unittest.TestCase):
    def test_get_the_credentials(self):
        print('test_get_the_credentials')

        headers = {
            'Bridge-Version': '2021-06-01',
            'Client-Id': 'MY_CLIENT_ID',
            'Client-Secret': 'MY_CLIENT_SECRET',
        }

        response = requests.get('https://api.bridgeapi.io/v2/banks', headers=headers)

        print(response.json())


class Unit_Tests_Bridge_Io_API_Payments_Initiation(unittest.TestCase):
    def test_allow_payments_to_different_beneficiaries(self):
        print('test_allow_payments_to_different_beneficiaries')

        headers = {
            'Bridge-Version': '2021-06-01',
            'Client-Id': 'MY_CLIENT_ID',
            'Client-Secret': 'MY_CLIENT_SECRET',
            'Content-Type': 'application/json',
        }

        data = '{ "successful_callback_url": "https://my-callback-url.com:8080/pay/success", ' \
               '"unsuccessful_callback_url": "https://my-callback-url.com:8080/pay/error", "transactions": ' \
               '[ { "end_to_end_id": "12345678-AFERS", "currency": "EUR", "label": "Payment label", "amount": ' \
               '99.5, "client_reference": "12345678-AZERTY" } ], "user": { "name": "Firstname Lastname", ' \
               '"ip_address": "0.0.0.0", "external_reference": "AEF142536-890" }, "beneficiary": { "name": ' \
               '"Firstname Lastname", "iban": "FR76XXXXXXXXXXXXXXXX" }, "client_reference": "12345678-AZERTY", ' \
               '"bank_id": 6 }'

        response = requests.post('https://api.bridgeapi.io/v2/payment-requests', headers=headers, data=data)

        print(response.json())

    def test_initiate_your_first_payment_to_a_default_beneficiary(self):
        print("test_initiate_your_first_payment_to_a_default_beneficiary")

        headers = {
            'Bridge-Version': '2021-06-01',
            'Client-Id': 'MY_CLIENT_ID',
            'Client-Secret': 'MY_CLIENT_SECRET',
            'Content-Type': 'application/json',
        }

        data = '{ "successful_callback_url": "https://my-callback-url.com:8080/pay/success", ' \
               '"unsuccessful_callback_url": "https://my-callback-url.com:8080/pay/error", "transactions": ' \
               '[ { "end_to_end_id": "12345678-AFERS", "currency": "EUR", "label": "Payment label", ' \
               '"amount": 99.5, "client_reference": "12345678-AZERTY" } ], "user": { "name": "Firstname Lastname", ' \
               '"ip_address": "0.0.0.0", "external_reference": "AEF142536-890" }, "client_reference": ' \
               '"12345678-AZERTY", "bank_id": 6 }'

        response = requests.post('https://api.bridgeapi.io/v2/payment-requests', headers=headers, data=data)

        print(response.json())

    def test_initiate_your_first_payment_to_different_beneficiaries(self):
        print("test_initiate_your_first_payment_to_different_beneficiaries")

        headers = {
            'Bridge-Version': '2021-06-01',
            'Client-Id': 'MY_CLIENT_ID',
            'Client-Secret': 'MY_CLIENT_SECRET',
            'Content-Type': 'application/json',
        }

        data = '{ "successful_callback_url": "https://my-callback-url.com:8080/pay/success", ' \
               '"unsuccessful_callback_url": "https://my-callback-url.com:8080/pay/error", "transactions": ' \
               '[ { "end_to_end_id": "12345678-AFERS", "currency": "EUR", "label": "Payment label", "amount": 99.5, ' \
               '"beneficiary": { "name": "Firstname Lastname", "iban": "0.0.0.0" }, "client_reference": ' \
               '"12345678-AZERTY" ], "user": { "name": "Firstname Lastname", "ip_address": "0.0.0.0", ' \
               '"external_reference": "AEF142536-890" }, "bank_id": 6 }'

        response = requests.post('https://api.bridgeapi.io/v2/payment-requests', headers=headers, data=data)

        print(response.json())

    def test_post_create_a_payment_request(self):
        print("test_post_create_a_payment_request")

        headers = {
            'Bridge-Version': '2021-06-01',
            'Client-Id': 'MY_CLIENT_ID',
            'Client-Secret': 'MY_CLIENT_SECRET',
            'Content-Type': 'application/json',
        }

        data = '{ "successful_callback_url": "https://my-callback-url.com:8080/pay/success", ' \
               '"unsuccessful_callback_url": "https://my-callback-url.com:8080/pay/error", "transactions": ' \
               '[ { "end_to_end_id": "12345678-AFERS", "currency": "EUR", "label": "Payment label", "amount": 99.5, ' \
               '"client_reference": "12345678-AZERTY" } ], "user": { "name": "Firstname Lastname", "ip_address": ' \
               '"0.0.0.0", "external_reference": "AEF142536-890" }, "client_reference": "12345678-AZERTY", ' \
               '"bank_id": 6 }'

        response = requests.post('https://api.bridgeapi.io/v2/payment-requests', headers=headers, data=data)

        print(response.json())

    def test_get_a_payment_request(self):
        print("test_get_a_payment_request")

        headers = {
            'Bridge-Version': '2021-06-01',
            'Client-Id': 'MY_CLIENT_ID',
            'Client-Secret': 'MY_CLIENT_SECRET',
        }

        response = requests.get('https://api.bridgeapi.io/v2/payment-requests/e959dccd632c49d7922a766e946ad9e9',
                                headers=headers)

        print(response.json())

    def test_get_list_payment_requests(self):
        print("test_get_list_payment_requests")

        headers = {
            'Bridge-Version': '2021-06-01',
            'Client-Id': 'MY_CLIENT_ID',
            'Client-Secret': 'MY_CLIENT_SECRET',
        }

        params = (
            ('status', 'ACSC,RJCT,CANC'),
        )

        response = requests.get('https://api.bridgeapi.io/v2/payment-requests', headers=headers, params=params)

        print(response.json())


class Unit_Tests_Bridge_Io_API_Banks(unittest.TestCase):
    def test_get_list_banks(self):
        print("test_get_list_banks")

        headers = {
            'Bridge-Version': '2021-06-01',
            'Client-Id': 'MY_CLIENT_ID',
            'Client-Secret': 'MY_CLIENT_SECRET',
        }

        response = requests.get('https://api.bridgeapi.io/v2/banks', headers=headers)

        print(response.json())

    def test_get_a_single_bank(self):
        print("test_get_a_single_bank")

        headers = {
            'Bridge-Version': '2021-06-01',
            'Client-Id': 'MY_CLIENT_ID',
            'Client-Secret': 'MY_CLIENT_SECRET',
        }

        response = requests.get('https://api.bridgeapi.io/v2/banks/17', headers=headers)

        print(response.json())

    def test_get_connectors_status(self):
        print("test_get_connectors_status")

        headers = {
            'Bridge-Version': '2021-06-01',
            'Client-Id': 'MY_CLIENT_ID',
            'Client-Secret': 'MY_CLIENT_SECRET',
        }

        response = requests.get('https://api.bridgeapi.io/v2/banks/insights', headers=headers)

        print(response.json())


class Unit_Tests_Bridge_Io_API_Users(unittest.TestCase):
    def test_post_create_a_user(self):
        print("test_create_a_user")

        headers = {
            'Bridge-Version': '2021-06-01',
            'Content-Type': 'application/json',
            'Client-Id': 'MY_CLIENT_ID',
            'Client-Secret': 'MY_CLIENT_SECRET',
        }

        data = '${ "email": "john.doe@email.com", "password": "password123" }'

        response = requests.post('https://api.bridgeapi.io/v2/users', headers=headers, data=data)

        print(response.json())

    def test_post_authenticate_a_user(self):
        print("test_post_authenticate_a_user")

        headers = {
            'Bridge-Version': '2021-06-01',
            'Content-Type': 'application/json',
            'Client-Id': 'MY_CLIENT_ID',
            'Client-Secret': 'MY_CLIENT_SECRET',
        }

        data = '${ "email": "john.doe@email.com", "password": "password123" }'

        response = requests.post('https://api.bridgeapi.io/v2/authenticate', headers=headers, data=data)

        print(response.json())

    def test_post_log_out_a_user(self):
        print("test_post_log_out_a_user")

        headers = {
            'Bridge-Version': '2021-06-01',
            'Client-Id': 'MY_CLIENT_ID',
            'Client-Secret': 'MY_CLIENT_SECRET',
            'Authorization': 'Bearer TOP_SECRET_ACCESS_TOKEN',
        }

        response = requests.post('https://api.bridgeapi.io/v2/logout', headers=headers)

        print(response.json())

    def test_get_list_users(self):
        print("test_get_list_users")

        headers = {
            'Bridge-Version': '2021-06-01',
            'Client-Id': 'MY_CLIENT_ID',
            'Client-Secret': 'MY_CLIENT_SECRET',
        }

        params = (
            ('limit', '100'),
        )

        response = requests.get('https://api.bridgeapi.io/v2/users', headers=headers, params=params)

        print(response.json())

    def test_get_get_a_single_user(self):
        print("test_get_get_a_single_user")

        headers = {
            'Bridge-Version': '2021-06-01',
            'Client-Id': 'MY_CLIENT_ID',
            'Client-Secret': 'MY_CLIENT_SECRET',
        }

        response = requests.get('https://api.bridgeapi.io/v2/users/d3751ede-cb1e-4d49-bd59-69917021540e',
                                headers=headers)

        print(response.json())

    def test_put_edit_user_email(self):
        print("test_put_edit_user_email")

        headers = {
            'Bridge-Version': '2021-06-01',
            'Content-Type': 'application/json',
            'Client-Id': 'MY_CLIENT_ID',
            'Client-Secret': 'MY_CLIENT_SECRET',
        }

        data = '${ "new_email": "john.doe@email.com", "password": "password123" }'

        response = requests.put('https://api.bridgeapi.io/v2/users/79c8961c-bdf7-11e5-88a3-4f2c2aec0665/email',
                                headers=headers, data=data)

        print(response.json())

    def test_put_edit_user_password(self):
        print("test_put_edit_user_password")

        headers = {
            'Bankin-Version': '2019-02-18',
            'Content-Type': 'application/json',
            'Client-Id': 'MY_CLIENT_ID',
            'Client-Secret': 'MY_CLIENT_SECRET',
        }

        data = '${ "current_password": "password123", "new_password": "P@ssw0rd123" }'

        response = requests.put('https://api.bridgeapi.io/v2/users/79c8961c-bdf7-11e5-88a3-4f2c2aec0665/password',
                                headers=headers, data=data)

        print(response.json())

    def test_post_delete_a_user(self):
        print("test_post_delete_a_user")

        headers = {
            'Bridge-Version': '2021',
            'Client-Id': 'MY_CLIENT_ID',
            'Client-Secret': 'MY_CLIENT_SECRET',
        }

        data = '${ "password": "P@ssw0rd123", }'

        response = requests.post('https://api.bridgeapi.io/v2/users/79c8961c-bdf7-11e5-88a3-4f2c2aec0665',
                                 headers=headers, data=data)

        print(response.json())

    def test_delete_delete_all_users(self):
        print("test_delete_delete_all_users")

        headers = {
            'Bridge-Version': '2021-06-01',
            'Client-Id': 'MY_CLIENT_ID',
            'Client-Secret': 'MY_CLIENT_SECRET',
        }

        response = requests.delete('https://api.bridgeapi.io/v2/users', headers=headers)

        print(response.json())

    def test_get_check_email_validation(self):
        print("test_get_check_email_validation")

        headers = {
            'Bridge-Version': '2021-06-01',
            'Client-Id': 'MY_CLIENT_ID',
            'Client-Secret': 'MY_CLIENT_SECRET',
            'Authorization': 'Bearer TOP_SECRET_ACCESS_TOKEN',
        }

        response = requests.get('https://api.bridgeapi.io/v2/users/me/email/confirmation', headers=headers)

        print(response.json())


class Unit_Tests_Bridge_Io_API_Financial_Data_Aggregation(unittest.TestCase):
    def test_user_creation(self):
        print('test_user_creation')

        headers = {
            'Bridge-Version': '2021-06-01',
            'Content-Type': 'application/json',
            'Client-Id': 'MY_CLIENT_ID',
            'Client-Secret': 'MY_CLIENT_SECRET',
        }

        data = '${ "email": "john.doe@email.com", "password": "password123" }'

        response = requests.post('https://api.bridgeapi.io/v2/users', headers=headers, data=data)

        print(response.json())

    def test_user_authentication(self):
        print('test_user_authentication')

        headers = {
            'Bridge-Version': '2021-06-01',
            'Content-Type': 'application/json',
            'Client-Id': 'MY_CLIENT_ID',
            'Client-Secret': 'MY_CLIENT_SECRET',
        }

        data = '${ "email": "john.doe@email.com", "password": "password123" }'

        response = requests.post('https://api.bridgeapi.io/v2/authenticate', headers=headers, data=data)

        print(response.json())

    def test_first_synchronization(self):
        print("test_first_synchronization")

        headers = {
            'Bridge-Version': '2021-06-01',
            'Client-Id': 'MY_CLIENT_ID',
            'Client-Secret': 'MY_CLIENT_SECRET',
            'Authorization': 'Bearer TOP_SECRET_ACCESS_TOKEN',
        }

        data = '${ "country": "fr", "prefill_email": "email@gmail.com", "iban": "FR7430003000502537446929K93", ' \
               '"capabilities": ["ais", "bulk_transfer"], "bank_id": 408 }'

        response = requests.post('https://api.bridgeapi.io/v2/connect/items/add', headers=headers, data=data)

        print(response.json())

    def test_data_fetching(self):
        print('test_data_fetching')

        headers = {
            'Bridge-Version': '2021-06-01',
            'Client-Id': 'MY_CLIENT_ID',
            'Client-Secret': 'MY_CLIENT_SECRET',
            'Authorization': 'Bearer TOP_SECRET_ACCESS_TOKEN',
        }

        params = (
            ('since', '2019-06-21T18:44:09.523Z'),
            ('limit', '12'),
        )

        response = requests.get('https://api.bridgeapi.io/v2/transactions/updated', headers=headers, params=params)

        print(response.json())


class Unit_Tests_Bridge_Io_API_Bridge_Connect(unittest.TestCase):
    def test_strong_customer_authentication(self):
        print("test_strong_customer_authentication")

        headers = {
            'Bridge-Version': '2021-06-01',
            'Client-Id': 'MY_CLIENT_ID',
            'Client-Secret': 'MY_CLIENT_SECRET',
            'Authorization': 'Bearer TOP_SECRET_ACCESS_TOKEN',
        }

        params = (
            ('item_id', 'ITEM_ID'),
        )

        response = requests.get('https://api.bridgeapi.io/v2/connect/items/sync', headers=headers, params=params)

        print(response.json())

    def test_post_connect_an_item(self):
        print("test_post_connect_an_item")

        headers = {
            'Bridge-Version': '2021-06-01',
            'Client-Id': 'MY_CLIENT_ID',
            'Client-Secret': 'MY_CLIENT_SECRET',
            'Authorization': 'Bearer TOP_SECRET_ACCESS_TOKEN',
        }

        data = '${ "country": "fr", "prefill_email": "email@gmail.com", "iban": "FR7430003000502537446929K93", ' \
               '"capabilities": ["ais", "bulk_transfer"], "bank_id": 408 }'

        response = requests.post('https://api.bridgeapi.io/v2/connect/items/add', headers=headers, data=data)

        print(response.json())

    def test_get_edit_an_item(self):
        print("test_get_edit_an_item")

        headers = {
            'Bridge-Version': '2021-06-01',
            'Client-Id': 'MY_CLIENT_ID',
            'Client-Secret': 'MY_CLIENT_SECRET',
            'Authorization': 'Bearer TOP_SECRET_ACCESS_TOKEN',
        }

        params = (
            ('item_id', 'ITEM_ID'),
        )

        response = requests.get('https://api.bridgeapi.io/v2/connect/items/edit', headers=headers, params=params)

        print(response.json())

    def test_get_manage_sca_and_sync(self):
        print("test_get_manage_sca_and_sync")

        headers = {
            'Bridge-Version': '2021-06-01',
            'Client-Id': 'MY_CLIENT_ID',
            'Client-Secret': 'MY_CLIENT_SECRET',
            'Authorization': 'Bearer TOP_SECRET_ACCESS_TOKEN',
        }

        params = (
            ('item_id', 'ITEM_ID'),
        )

        response = requests.get('https://api.bridgeapi.io/v2/connect/items/sync', headers=headers, params=params)

        print(response.json())

    def test_get_validate_pro_items(self):
        print("test_get_validate_pro_items")

        headers = {
            'Bridge-Version': '2021-06-01',
            'Client-Id': 'MY_CLIENT_ID',
            'Client-Secret': 'MY_CLIENT_SECRET',
            'Authorization': 'Bearer TOP_SECRET_ACCESS_TOKEN',
        }

        response = requests.get('https://api.bridgeapi.io/v2/connect/items/pro/confirmation', headers=headers)

        print(response.json())

    def test_get_manage_accounts(self):
        print("test_get_manage_accounts")

        headers = {
            'Bridge-Version': '2021-06-01',
            'Client-Id': 'MY_CLIENT_ID',
            'Client-Secret': 'MY_CLIENT_SECRET',
            'Authorization': 'Bearer TOP_SECRET_ACCESS_TOKEN',
        }

        response = requests.get('https://api.bridgeapi.io/v2/connect/manage/accounts/iban', headers=headers)

        print(response.json())


class Unit_Tests_Bridge_Io_API_Bridge_Pay(unittest.TestCase):
    def test_initiate_your_first_single_transfer(self):
        print("test_initiate_your_first_single_transfer")

        headers = {
            'Bridge-Version': '2021-06-01',
            'Client-Id': 'MY_CLIENT_ID',
            'Client-Secret': 'MY_CLIENT_SECRET',
            'Authorization': 'Bearer TOP_SECRET_ACCESS_TOKEN',
        }

        data = '{ "beneficiary": { "name": "Test Name", "iban": "FR3130003000709222579823U36" }, "amount": 1500.59, ' \
               '"editable_amount": false, "label": "Label example", "sender_account_id": 123456789, ' \
               '"sender_account_editable": false, "client_reference": "reference-test-1234" }'

        response = requests.post('https://api.bridgeapi.io/v2/pay/transfer', headers=headers, data=data)

        print(response.json())

    def test_initiate_your_first_bulk_transfers(self):
        print("test_initiate_your_first_bulk_transfers")

        headers = {
            'Bridge-Version': '2021-06-01',
            'Client-Id': 'MY_CLIENT_ID',
            'Client-Secret': 'MY_CLIENT_SECRET',
            'Authorization': 'Bearer TOP_SECRET_ACCESS_TOKEN',
            'Content-Type': 'application/json',
        }

        data = '{ "client_reference": "av4y28c4-3aw1-387r-co0f-4ni3jl78sd23", "transfers": [ { "amount": 1500.50, ' \
               '"label": "Your optional label", "beneficiary": { "name": "John Doe", "iban": ' \
               '"FR3130003000709222579823U36" }, "client_reference": "3bc40e21-3ea5-4274-9744-c2f984f7072e" }, ' \
               '{ "amount": 2500.13, "beneficiary": { "name": "Cristen Patience", "iban": ' \
               '"FR0210096000404753378717C40" }, "client_reference": "fd5d81c5-4be2-412f-bb4d-5aa1db98dc99", }, ' \
               '{ "amount": 29999, "beneficiary": { "name": "Kaelyn Ebert", "iban": "FR4214508000507483296188O17" }, ' \
               '} ], "sender_account_id": 123456789, "sender_account_editable": true }'

        response = requests.post('https://api.bridgeapi.io/v2/pay/bulk-transfers', headers=headers, data=data)

        print(response.json())

    def test_post_refresh_accounts(self):
        print("test_post_refresh_accounts")

        headers = {
            'Bridge-Version': '2021-06-01',
            'Client-Id': 'MY_CLIENT_ID',
            'Client-Secret': 'MY_CLIENT_SECRET',
            'Authorization': 'Bearer TOP_SECRET_ACCESS_TOKEN',
            'Content-Type': 'application/json',
        }

        response = requests.post('https://api.bridgeapi.io/v2/transfers/accounts/refresh', headers=headers)

        print(response.json())

    def test_post_send_a_transfer(self):
        print("test_post_send_a_transfer")

        headers = {
            'Bridge-Version': '2021-06-01',
            'Client-Id': 'MY_CLIENT_ID',
            'Client-Secret': 'MY_CLIENT_SECRET',
            'Authorization': 'Bearer TOP_SECRET_ACCESS_TOKEN',
        }

        data = '{ "beneficiary": { "name": "Test Name", "iban": "FR3130003000709222579823U36" }, "amount": 1500.59, "editable_amount": false, "label": "Label example", "sender_account_id": 123456789, "sender_account_editable": false, "client_reference": "reference-test-1234" }'

        response = requests.post('https://api.bridgeapi.io/v2/pay/transfer', headers=headers, data=data)

        print(response.json())

    def test_send_bulk_transfers(self):
        print("test_send_bulk_transfers")

        headers = {
            'Bridge-Version': '2021-06-01',
            'Client-Id': 'MY_CLIENT_ID',
            'Client-Secret': 'MY_CLIENT_SECRET',
            'Authorization': 'Bearer TOP_SECRET_ACCESS_TOKEN',
            'Content-Type': 'application/json',
        }

        data = '{ "client_reference": "av4y28c4-3aw1-387r-co0f-4ni3jl78sd23", "transfers": [ { "amount": 1500.50, "label": "Your optional label", "beneficiary": { "name": "John Doe", "iban": "FR3130003000709222579823U36" }, "client_reference": "3bc40e21-3ea5-4274-9744-c2f984f7072e" }, { "amount": 2500.13, "beneficiary": { "name": "Cristen Patience", "iban": "FR0210096000404753378717C40" }, "client_reference": "fd5d81c5-4be2-412f-bb4d-5aa1db98dc99", }, { "amount": 29999, "beneficiary": { "name": "Kaelyn Ebert", "iban": "FR4214508000507483296188O17" }, } ], "sender_account_id": 123456789, "sender_account_editable": true }'

        response = requests.post('https://api.bridgeapi.io/v2/pay/bulk-transfers', headers=headers, data=data)

        print(response.json())

    def test_get_list_transfers(self):
        print("test_get_list_transfers")

        headers = {
            'Bridge-Version': '2021-06-01',
            'Client-Id': 'MY_CLIENT_ID',
            'Client-Secret': 'MY_CLIENT_SECRET',
            'Authorization': 'Bearer TOP_SECRET_ACCESS_TOKEN',
        }

        params = (
            ('limit', '100'),
        )

        response = requests.get('https://api.bridgeapi.io/v2/transfers', headers=headers, params=params)

        print(response.json())

    def test_get_get_a_single_transfer(self):
        print("test_get_get_a_single_transfer")

        headers = {
            'Bridge-Version': '2021-06-01',
            'Client-Id': 'MY_CLIENT_ID',
            'Client-Secret': 'MY_CLIENT_SECRET',
            'Authorization': 'Bearer TOP_SECRET_ACCESS_TOKEN',
        }

        response = requests.get('https://api.bridgeapi.io/v2/transfers/a73981be-c9b0-4320-a092-326e09e1e256',
                                headers=headers)

        print(response.json())

    def test_get_list_bulks(self):
        print("test_get_list_bulks")

        headers = {
            'Bridge-Version': '2021-06-01',
            'Client-Id': 'MY_CLIENT_ID',
            'Client-Secret': 'MY_CLIENT_SECRET',
            'Authorization': 'Bearer TOP_SECRET_ACCESS_TOKEN',
        }

        response = requests.get('https://api.bridgeapi.io/v2/bulk-transfers', headers=headers)

        print(response.json())

    def test_get_get_a_single_bulk(self):
        print("test_get_get_a_single_bulk")

        headers = {
            'Bridge-Version': '2021-06-01',
            'Client-Id': 'MY_CLIENT_ID',
            'Client-Secret': 'MY_CLIENT_SECRET',
            'Authorization': 'Bearer TOP_SECRET_ACCESS_TOKEN',
        }

        response = requests.get('https://api.bridgeapi.io/v2/bulk-transfers/5de1c4ef-895d-4a14-86a5-8e19adbf63c4',
                                headers=headers)

        print(response.json())

    def test_list_sender_accounts(self):
        print("test_list_sender_accounts")

        headers = {
            'Bridge-Version': '2021-06-01',
            'Client-Id': 'MY_CLIENT_ID',
            'Client-Secret': 'MY_CLIENT_SECRET',
            'Authorization': 'Bearer TOP_SECRET_ACCESS_TOKEN',
        }

        response = requests.get('https://api.bridgeapi.io/v2/transfers/accounts/senders', headers=headers)

        print(response.json())


class Unit_Tests_Bridge_Io_API_Items(unittest.TestCase):
    def test_get_list_sender_accounts(self):
        print("test_get_list_sender_accounts")

        headers = {
            'Bridge-Version': '2021-06-01',
            'Client-Id': 'MY_CLIENT_ID',
            'Client-Secret': 'MY_CLIENT_SECRET',
            'Authorization': 'Bearer TOP_SECRET_ACCESS_TOKEN',
        }

        response = requests.get('https://api.bridgeapi.io/v2/transfers/accounts/senders', headers=headers)

        print(response.json())

    def test_get_get_a_single_item(self):
        print("test_get_get_a_single_item")

        headers = {
            'Bridge-Version': '2021-06-01',
            'Client-Id': 'MY_CLIENT_ID',
            'Client-Secret': 'MY_CLIENT_SECRET',
            'Authorization': 'Bearer TOP_SECRET_ACCESS_TOKEN',
        }

        response = requests.get('https://api.bridgeapi.io/v2/items/187791', headers=headers)

        print(response.json())

    def test_post_refresh_an_item(self):
        print("test_post_refresh_an_item")

        headers = {
            'Bridge-Version': '2021-06-01',
            'Client-Id': 'MY_CLIENT_ID',
            'Client-Secret': 'MY_CLIENT_SECRET',
            'Authorization': 'Bearer TOP_SECRET_ACCESS_TOKEN',
        }

        response = requests.post('https://api.bridgeapi.io/v2/items/123456/refresh', headers=headers)

        print(response.json())

    def test_get_get_an_item_refresh_status(self):
        print("test_get_get_an_item_refresh_status")

        headers = {
            'Bridge-Version': '2021-06-01',
            'Client-Id': 'MY_CLIENT_ID',
            'Client-Secret': 'MY_CLIENT_SECRET',
            'Authorization': 'Bearer TOP_SECRET_ACCESS_TOKEN',
        }

        response = requests.get('https://api.bridgeapi.io/v2/items/123456/refresh/status', headers=headers)

        print(response.json())

    def test_delete_delete_an_item(self):
        print("test_delete_delete_an_item")

        headers = {
            'Bankin-Version': '2021-06-01',
            'Client-Id': 'MY_CLIENT_ID',
            'Client-Secret': 'MY_CLIENT_SECRET',
            'Authorization': 'Bearer TOP_SECRET_ACCESS_TOKEN',
        }

        response = requests.delete('https://api.bridgeapi.io/v2/items/123456', headers=headers)

        print(response.json())


class Unit_Tests_Bridge_Io_API_Accounts(unittest.TestCase):
    def test_get_list_accounts(self):
        print("test_get_list_accounts")

        headers = {
            'Bridge-Version': '2021-06-01',
            'Client-Id': 'MY_CLIENT_ID',
            'Client-Secret': 'MY_CLIENT_SECRET',
            'Authorization': 'Bearer TOP_SECRET_ACCESS_TOKEN',
        }

        params = (
            ('item_id', '123456789'),
            ('limit', '10'),
        )

        response = requests.get('https://api.bridgeapi.io/v2/accounts', headers=headers, params=params)

        print(response.json())

    def test_get_get_a_single_account(self):
        print("test_get_get_a_single_account")

        headers = {
            'Bridge-Version': '2021-06-01',
            'Client-Id': 'MY_CLIENT_ID',
            'Client-Secret': 'MY_CLIENT_SECRET',
            'Authorization': 'Bearer TOP_SECRET_ACCESS_TOKEN',
        }

        response = requests.get('https://api.bridgeapi.io/v2/accounts/2341501', headers=headers)

        print(response.json())


class Unit_Tests_Bridge_Io_API_Transactions(unittest.TestCase):
    def test_get_list_transactions(self):
        print("test_get_list_transactions")

        headers = {
            'Bridge-Version': '2021-06-01',
            'Client-Id': 'MY_CLIENT_ID',
            'Client-Secret': 'MY_CLIENT_SECRET',
            'Authorization': 'Bearer TOP_SECRET_ACCESS_TOKEN',
        }

        params = (
            ('limit', '12'),
            ('until', '2019-04-06'),
        )

        response = requests.get('https://api.bridgeapi.io/v2/transactions', headers=headers, params=params)

        print(response.json())

    def test_get_list_updated_transactions(self):
        print("test_get_list_updated_transactions")

        headers = {
            'Bridge-Version': '2021-06-01',
            'Client-Id': 'MY_CLIENT_ID',
            'Client-Secret': 'MY_CLIENT_SECRET',
            'Authorization': 'Bearer TOP_SECRET_ACCESS_TOKEN',
        }

        params = (
            ('since', '2019-06-21T18:44:09.523Z'),
            ('limit', '12'),
        )

        response = requests.get('https://api.bridgeapi.io/v2/transactions/updated', headers=headers, params=params)

        print(response.json())

    def test_get_get_a_single_transaction(self):
        print("test_get_get_a_single_transaction")

        headers = {
            'Bridge-Version': '2021-06-01',
            'Client-Id': 'MY_CLIENT_ID',
            'Client-Secret': 'MY_CLIENT_SECRET',
            'Authorization': 'Bearer TOP_SECRET_ACCESS_TOKEN',
        }

        response = requests.get('https://api.bridgeapi.io/v2/transactions/1000013102238', headers=headers)

        print(response.json())

    def test_get_list_transactions_by_account(self):
        print("test_get_list_transactions_by_account")

        headers = {
            'Bridge-Version': '2021-06-01',
            'Client-Id': 'MY_CLIENT_ID',
            'Client-Secret': 'MY_CLIENT_SECRET',
            'Authorization': 'Bearer TOP_SECRET_ACCESS_TOKEN',
        }

        params = (
            ('limit', '12'),
            ('until', '2019-04-06'),
        )

        response = requests.get('https://api.bridgeapi.io/v2/accounts/2341498/transactions', headers=headers,
                                params=params)

        print(response.json())

    def test_get_list_updated_transactions_by_account(self):
        print("test_get_list_updated_transactions_by_account")

        headers = {
            'Bridge-Version': '2021-06-01',
            'Client-Id': 'MY_CLIENT_ID',
            'Client-Secret': 'MY_CLIENT_SECRET',
            'Authorization': 'Bearer TOP_SECRET_ACCESS_TOKEN',
        }

        params = (
            ('since', '2019-06-21T18:44:09.523Z'),
            ('limit', '12'),
        )

        response = requests.get('https://api.bridgeapi.io/v2/accounts/2341498/transactions/updated', headers=headers,
                                params=params)

        print(response.json())


class Unit_Tests_Bridge_Io_API_Stocks(unittest.TestCase):
    def test_get_list_stocks(self):
        print("test_get_list_stocks")

        headers = {
            'Bridge-Version': '2021-06-01',
            'Client-Id': 'MY_CLIENT_ID',
            'Client-Secret': 'MY_CLIENT_SECRET',
            'Authorization': 'Bearer TOP_SECRET_ACCESS_TOKEN',
        }

        params = (
            ('limit', '2'),
        )

        response = requests.get('https://api.bridgeapi.io/v2/stocks', headers=headers, params=params)

        print(response.json())

    def test_get_list_updated_stocks(self):
        print("test_get_list_updated_stocks")

        headers = {
            'Bridge-Version': '2021-06-01',
            'Client-Id': 'MY_CLIENT_ID',
            'Client-Secret': 'MY_CLIENT_SECRET',
            'Authorization': 'Bearer TOP_SECRET_ACCESS_TOKEN',
        }

        params = (
            ('after', 'MjAxNi0wOC0yOVQxMjowMDozNS45NTFaXzky'),
            ('limit', '2'),
            ('since', '2019-01-01T08:00:00Z'),
        )

        response = requests.get('https://api.bridgeapi.io/v2/stocks/updated', headers=headers, params=params)

        print(response.json())

    def test_get_get_a_single_stock(self):
        print("test_get_get_a_single_stock")

        headers = {
            'Bridge-Version': '2021-06-01',
            'Client-Id': 'MY_CLIENT_ID',
            'Client-Secret': 'MY_CLIENT_SECRET',
            'Authorization': 'Bearer TOP_SECRET_ACCESS_TOKEN',
        }

        response = requests.get('https://api.bridgeapi.io/v2/stocks/75', headers=headers)

        print(response.json())


class Unit_Tests_Bridge_Io_API_Categories(unittest.TestCase):
    def test_get_list_categories(self):
        print("test_get_list_categories")

        headers = {
            'Bridge-Version': '2021-06-01',
            'Client-Id': 'MY_CLIENT_ID',
            'Client-Secret': 'MY_CLIENT_SECRET',
        }

        params = (
            ('limit', '12'),
        )

        response = requests.get('https://api.bridgeapi.io/v2/categories', headers=headers, params=params)

        print(response.json())

    def test_get_get_a_single_category(self):
        print("test_get_get_a_single_category")

        headers = {
            'Bridge-Version': '2021-06-01',
            'Client-Id': 'MY_CLIENT_ID',
            'Client-Secret': 'MY_CLIENT_SECRET',
        }

        response = requests.get('https://api.bridgeapi.io/v2/categories/321', headers=headers)

        print(response.json())


class Unit_Tests_Bridge_Io_API_Insights(unittest.TestCase):
    def test_get_get_categories_insights(self):
        print('test_get_get_categories_insights')

        headers = {
            'Bridge-Version': '2021-06-01',
            'Client-Id': 'MY_CLIENT_ID',
            'Client-Secret': 'MY_CLIENT_SECRET',
            'Authorization': 'Bearer TOP_SECRET_ACCESS_TOKEN',
        }

        params = (
            ('fully_analyzed_month', '3'),
        )

        response = requests.get('https://api.bridgeapi.io/v2/insights/category', headers=headers, params=params)

        print(response.json())


class Unit_Tests_Bridge_Io_API_Bank_Statements(unittest.TestCase):
    def test_post_create_fetching_bank_statements_request(self):
        print("test_post_create_fetching_bank_statements_request")

        headers = {
            'Bridge-Version': '2021-06-01',
            'Client-Id': '<MY_CLIENT_ID>',
            'Client-Secret': '<MY_CLIENT_SECRET>',
            'Authorization': 'Bearer <SESSION_TOKEN>',
            'Content-Type': 'application/json; charset=utf-8',
        }

        data = '${}'

        response = requests.post('https://api.bridgeapi.io/v2/items/%3CMY_ITEM_ID%3E/statements-fetching-requests',
                                 headers=headers, data=data)

        print(response.json())

    def test_get_get_fetching_bank_statements_request(self):
        print("test_get_get_fetching_bank_statements_request")

        headers = {
            'Bridge-Version': '2021-06-01',
            'Client-Id': '<MY_CLIENT_ID>',
            'Client-Secret': '<MY_CLIENT_SECRET>',
            'Authorization': 'Bearer <SESSION_TOKEN>',
        }

        response = requests.get(
            'https://api.bridgeapi.io/v2/items/%3CITEM_ID%3E/statements-fetching-requests/%3CREQUEST_ID%3E',
            headers=headers)

        print(response.json())

    def test_get_get_statement(self):
        print("test_get_get_statement")

        headers = {
            'Bridge-Version': '2021-06-01',
            'Client-Id': '<MY_CLIENT_ID>',
            'Client-Secret': '<MY_CLIENT_SECRET>',
            'Authorization': 'Bearer <SESSION_TOKEN>',
        }

        response = requests.get(
            'https://api.bridgeapi.io/v2/items/%3CITEM_ID%3E/statements-fetching-requests/%3CREQUEST_ID%3E/statements/%3CSTATEMENT_ID%3E',
            headers=headers)

        print(response.json())


class Unit_Tests_Bridge_Io_API_Subscriptions(unittest.TestCase):
    def test_list_subscriptions(self):
        print("test_list_subscriptions")

        headers = {
            'Bankin-Version': '2021-06-01',
            'Client-Id': 'MY_CLIENT_ID',
            'Client-Secret': 'MY_CLIENT_SECRET',
            'Authorization': 'Bearer <token>',
        }

        response = requests.get('https://api.bridgeapi.io/v2/subscriptions', headers=headers)

        print(response.json())

    def test_get_list_transactions_linked_to_subscriptions(self):
        print("test_get_list_transactions_linked_to_subscriptions")

        headers = {
            'Bridge-Version': '2021-06-01',
            'Client-Id': 'MY_CLIENT_ID',
            'Client-Secret': 'MY_CLIENT_SECRET',
            'Authorization': 'Bearer <token>',
        }

        response = requests.get('https://api.bridgeapi.io/v2/subscriptions/transactions', headers=headers)

        print(response.json())


if __name__ == '__main__':
    unittest.main()
