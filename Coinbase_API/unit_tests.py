import unittest
import requests


class UnitTestsCoinBaseAPINotifications(unittest.TestCase):
    # https://developers.coinbase.com/api/v2#list-notifications
    def test_get_list_notifications(self):
        print("test_get_list_notifications")

        headers = {
            'CB-ACCESS-KEY': '<your api key>',
            'CB-ACCESS-SIGN': '<the user generated message signature>',
            'CB-ACCESS-TIMESTAMP': '<a timestamp for your request>',
        }

        response = requests.get('https://api.coinbase.com/v2/notifications', headers=headers)

        print(response.text)

    # https://developers.coinbase.com/api/v2#show-a-notification
    def test_get_show_a_notification(self):
        print('test_get_show_a_notification')

        headers = {
            'CB-ACCESS-KEY': '<your api key>',
            'CB-ACCESS-SIGN': '<the user generated message signature>',
            'CB-ACCESS-TIMESTAMP': '<a timestamp for your request>',
        }

        response = requests.get('https://api.coinbase.com/v2/notifications/0fdfb26e-bd26-5e1c-b055-7b935e57fa33',
                                headers=headers)

        print(response.text)


class UnitTestsCoinBaseAPIUsers(unittest.TestCase):
    # https://developers.coinbase.com/api/v2#show-a-user
    def test_get_show_a_user(self):
        print('test_get_show_a_user')

        headers = {
            'CB-ACCESS-KEY': '<your api key>',
            'CB-ACCESS-SIGN': '<the user generated message signature>',
            'CB-ACCESS-TIMESTAMP': '<a timestamp for your request>',
        }

        response = requests.get('https://api.coinbase.com/v2/users/:user_id', headers=headers)

        print(response.text)

    # https://developers.coinbase.com/api/v2#show-current-user
    def test_get_show_current_user(self):
        print("test_get_show_current_user")

        headers = {
            'CB-ACCESS-KEY': '<your api key>',
            'CB-ACCESS-SIGN': '<the user generated message signature>',
            'CB-ACCESS-TIMESTAMP': '<a timestamp for your request>',
        }

        response = requests.get('https://api.coinbase.com/v2/user', headers=headers)

        print(response.text)

    # https://developers.coinbase.com/api/v2#show-authorization-information
    def test_get_show_authorization_information(self):
        print("test_get_show_authorization_information")

        headers = {
            'CB-ACCESS-KEY': '<your api key>',
            'CB-ACCESS-SIGN': '<the user generated message signature>',
            'CB-ACCESS-TIMESTAMP': '<a timestamp for your request>',
        }

        response = requests.get('https://api.coinbase.com/v2/user/auth', headers=headers)

        print(response.text)

    # https://developers.coinbase.com/api/v2#update-current-user
    def test_get_update_current_user(self):
        print("test_get_update_current_user")

        headers = {
            'Content-Type': 'application/json',
            'CB-ACCESS-KEY': '<your api key>',
            'CB-ACCESS-SIGN': '<the user generated message signature>',
            'CB-ACCESS-TIMESTAMP': '<a timestamp for your request>',
        }

        data = '{"name": "James Smith"}'

        response = requests.put('https://api.coinbase.com/v2/user', headers=headers, data=data)

        print(response.text)


class UnitTestsCoinBaseAPIAccounts(unittest.TestCase):
    # https://developers.coinbase.com/api/v2#list-accounts
    def test_get_list_accounts(self):
        print('test_get_list_accounts')

        headers = {
            'CB-ACCESS-KEY': '<your api key>',
            'CB-ACCESS-SIGN': '<the user generated message signature>',
            'CB-ACCESS-TIMESTAMP': '<a timestamp for your request>',
        }

        response = requests.get('https://api.coinbase.com/v2/accounts', headers=headers)

        print(response.text)

    # https://developers.coinbase.com/api/v2#show-an-account
    def test_get_show_an_account(self):
        print("test_get_show_an_account")

        headers = {
            'CB-ACCESS-KEY': '<your api key>',
            'CB-ACCESS-SIGN': '<the user generated message signature>',
            'CB-ACCESS-TIMESTAMP': '<a timestamp for your request>',
        }

        response = requests.get('https://api.coinbase.com/v2/accounts/:account_id', headers=headers)

        print(response.text)

    # https://developers.coinbase.com/api/v2#update-account
    def test_put_update_account(self):
        print("test_put_update_account")

        headers = {
            'CB-ACCESS-KEY': '<your api key>',
            'CB-ACCESS-SIGN': '<the user generated message signature>',
            'CB-ACCESS-TIMESTAMP': '<a timestamp for your request>',
        }

        data = '{"name": "New account name"}'

        response = requests.put('https://api.coinbase.com/v2/accounts/82de7fcd-db72-5085-8ceb-bee19303080b',
                                headers=headers, data=data)

        print(response.text)

    # https://developers.coinbase.com/api/v2#delete-account
    def test_delete_account(self):
        print("test_delete_account")

        headers = {
            'CB-ACCESS-KEY': '<your api key>',
            'CB-ACCESS-SIGN': '<the user generated message signature>',
            'CB-ACCESS-TIMESTAMP': '<a timestamp for your request>',
        }

        response = requests.delete('https://api.coinbase.com/v2/accounts/82de7fcd-db72-5085-8ceb-bee19303080b',
                                   headers=headers)

        print(response.text)


class UnitTestsCoinBaseAPIAddresses(unittest.TestCase):
    # https://developers.coinbase.com/api/v2#list-addresses
    def test_get_list_addresses(self):
        print('test_get_list_addresses')

        headers = {
            'CB-ACCESS-KEY': '<your api key>',
            'CB-ACCESS-SIGN': '<the user generated message signature>',
            'CB-ACCESS-TIMESTAMP': '<a timestamp for your request>',
        }

        response = requests.get('https://api.coinbase.com/v2/accounts/:account_id/addresses', headers=headers)

        print(response.text)

    # https://developers.coinbase.com/api/v2#show-addresss
    def test_get_show_address(self):
        print('test_get_show_address')

        headers = {
            'CB-ACCESS-KEY': '<your api key>',
            'CB-ACCESS-SIGN': '<the user generated message signature>',
            'CB-ACCESS-TIMESTAMP': '<a timestamp for your request>',
        }

        response = requests.get('https://api.coinbase.com/v2/accounts/:account_id/addresses/:address_id',
                                headers=headers)

        print(response.text)

    # https://developers.coinbase.com/api/v2#list-address39s-transactions
    def test_get_list_address39s_transactions(self):
        print("test_get_list_address39s_transactions")

        headers = {
            'CB-ACCESS-KEY': '<your api key>',
            'CB-ACCESS-SIGN': '<the user generated message signature>',
            'CB-ACCESS-TIMESTAMP': '<a timestamp for your request>',
        }

        response = requests.get('https://api.coinbase.com/v2/accounts/:account_id/addresses/:address_id/transactions',
                                headers=headers)

        print(response.text)

    # https://developers.coinbase.com/api/v2#create-address
    def test_post_create_address(self):
        print('test_post_create_address')

        headers = {
            'CB-ACCESS-KEY': '<your api key>',
            'CB-ACCESS-SIGN': '<the user generated message signature>',
            'CB-ACCESS-TIMESTAMP': '<a timestamp for your request>',
        }

        data = '{"name": "New receive address"}'

        response = requests.post('https://api.coinbase.com/v2/accounts/:account_id/addresses', headers=headers,
                                 data=data)

        print(response.text)


class UnitTestsCoinBaseAPITransactions(unittest.TestCase):
    # https://developers.coinbase.com/api/v2#list-transactions
    def test_get_list_transactions(self):
        print('test_get_list_transactions')

        headers = {
            'CB-ACCESS-KEY': '<your api key>',
            'CB-ACCESS-SIGN': '<the user generated message signature>',
            'CB-ACCESS-TIMESTAMP': '<a timestamp for your request>',
        }

        response = requests.get('https://api.coinbase.com/v2/accounts/:account_id/transactions', headers=headers)

        print(response.text)

    # https://developers.coinbase.com/api/v2#show-a-transaction
    def test_get_show_a_transaction(self):
        print("test_show_a_transaction")

        headers = {
            'CB-ACCESS-KEY': '<your api key>',
            'CB-ACCESS-SIGN': '<the user generated message signature>',
            'CB-ACCESS-TIMESTAMP': '<a timestamp for your request>',
        }

        response = requests.get('https://api.coinbase.com/v2/accounts/:account_id/transactions/:transaction_id',
                                headers=headers)

        print(response.text)

    # https://developers.coinbase.com/api/v2#send-money
    def test_post_send_money(self):
        print('test_post_send_money')

        headers = {
            'Content-Type': 'application/json',
            'CB-ACCESS-KEY': '<your api key>',
            'CB-ACCESS-SIGN': '<the user generated message signature>',
            'CB-ACCESS-TIMESTAMP': '<a timestamp for your request>',
        }

        data = '{ "type": "send", "to": "1AUJ8z5RuHRTqD1eikyfUUetzGmdWLGkpT", "amount": "0.1", "currency": "BTC", "idem": "9316dd16-0c05" }'

        response = requests.post('https://api.coinbase.com/v2/accounts/:account_id/transactions',
                                 headers=headers, data=data)

        print(response.text)

    # https://developers.coinbase.com/api/v2#transfer-money-between-accounts
    def test_post_transfer_money_between_accounts(self):
        print("test_post_transfer_money_between_accounts")

        headers = {
            'Content-Type': 'application/json',
            'CB-ACCESS-KEY': '<your api key>',
            'CB-ACCESS-SIGN': '<the user generated message signature>',
            'CB-ACCESS-TIMESTAMP': '<a timestamp for your request>',
        }

        data = '{ "type": "transfer", "to": "58542935-67b5-56e1-a3f9-42686e07fa40", "amount": "1" }'

        response = requests.post('https://api.coinbase.com/v2/accounts/:account_id/transactions', headers=headers, data=data)

        print(response.text)

    # https://developers.coinbase.com/api/v2#request-money
    def test_post_request_money(self):
        print('test_post_request_money')

        headers = {
            'Content-Type': 'application/json',
            'CB-ACCESS-KEY': '<your api key>',
            'CB-ACCESS-SIGN': '<the user generated message signature>',
            'CB-ACCESS-TIMESTAMP': '<a timestamp for your request>',
        }

        data = '{ "type": "request", "to": "email@example.com", "amount": "1", "currency": "BTC" }'

        response = requests.post('https://api.coinbase.com/v2/accounts/:account_id/transactions', headers=headers,
                                 data=data)

        print(response.text)

    # https://developers.coinbase.com/api/v2#complete-request-money
    def test_post_complete_request_money(self):
        print('test_post_complete_request_money')

        headers = {
            'CB-ACCESS-KEY': '<your api key>',
            'CB-ACCESS-SIGN': '<the user generated message signature>',
            'CB-ACCESS-TIMESTAMP': '<a timestamp for your request>',
        }

        response = requests.post(
            'https://api.coinbase.com/v2/accounts/:account_id/transactions/:transaction_id/complete', headers=headers)

        print(response.text)

    # https://developers.coinbase.com/api/v2#re-send-request-money
    def test_post_re_send_request_money(self):
        print("test_post_re_send_request_money")

        headers = {
            'CB-ACCESS-KEY': '<your api key>',
            'CB-ACCESS-SIGN': '<the user generated message signature>',
            'CB-ACCESS-TIMESTAMP': '<a timestamp for your request>',
        }

        response = requests.post('https://api.coinbase.com/v2/accounts/:account_id/transactions/:transaction_id/resend',
                                 headers=headers)

        print(response.text)

    # https://developers.coinbase.com/api/v2#cancel-request-money
    def test_cancel_request_money(self):
        print("test_cancel_request_money")

        headers = {
            'CB-ACCESS-KEY': '<your api key>',
            'CB-ACCESS-SIGN': '<the user generated message signature>',
            'CB-ACCESS-TIMESTAMP': '<a timestamp for your request>',
        }

        response = requests.delete('https://api.coinbase.com/v2/accounts/:account_id/transactions/:transaction_id',
                                   headers=headers)

        print(response.text)


class UnitTestsCoinBaseAPIBuys(unittest.TestCase):
    # https://developers.coinbase.com/api/v2#list-buys
    def test_get_list_buys(self):
        print("test_get_list_buys")

        headers = {
            'CB-ACCESS-KEY': '<your api key>',
            'CB-ACCESS-SIGN': '<the user generated message signature>',
            'CB-ACCESS-TIMESTAMP': '<a timestamp for your request>',
        }

        response = requests.get('https://api.coinbase.com/v2/accounts/:account_id/buys', headers=headers)

        print(response.text)

    # https://developers.coinbase.com/api/v2#show-a-buy
    def test_get_show_a_buy(self):
        print("test_get_show_a_buy")

        headers = {
            'CB-ACCESS-KEY': '<your api key>',
            'CB-ACCESS-SIGN': '<the user generated message signature>',
            'CB-ACCESS-TIMESTAMP': '<a timestamp for your request>',
        }

        response = requests.get('https://api.coinbase.com/v2/accounts/:account_id/buys/:buy_id', headers=headers)

        print(response.text)

    # https://developers.coinbase.com/api/v2#place-buy-order
    def test_post_place_buy_order(self):
        print("test_post_place_buy_order")

        headers = {
            'Content-Type': 'application/json',
            'CB-ACCESS-KEY': '<your api key>',
            'CB-ACCESS-SIGN': '<the user generated message signature>',
            'CB-ACCESS-TIMESTAMP': '<a timestamp for your request>',
        }

        data = '{"amount": "10", "currency": "BTC", "payment_method": "83562370-3e5c-51db-87da-752af5ab9559"}'

        response = requests.post('https://api.coinbase.com/v2/accounts/82de7fcd-db72-5085-8ceb-bee19303080b/buys',
                                 headers=headers, data=data)

        print(response.text)

    # https://developers.coinbase.com/api/v2#commit-a-buy
    def test_post_commit_a_buy(self):
        print('test_post_commit_a_buy')

        headers = {
            'CB-ACCESS-KEY': '<your api key>',
            'CB-ACCESS-SIGN': '<the user generated message signature>',
            'CB-ACCESS-TIMESTAMP': '<a timestamp for your request>',
        }

        response = requests.post(
            'https://api.coinbase.com/v2/accounts/82de7fcd-db72-5085-8ceb-bee19303080b/buys/a333743d-184a-5b5b-abe8-11612fc44ab5/commit',
            headers=headers)

        print(response.text)


class UnitTestsCoinBaseAPISells(unittest.TestCase):
    # https://developers.coinbase.com/api/v2#list-sells
    def test_get_list_sells(self):
        print('test_get_list_sells')

        headers = {
            'CB-ACCESS-KEY': '<your api key>',
            'CB-ACCESS-SIGN': '<the user generated message signature>',
            'CB-ACCESS-TIMESTAMP': '<a timestamp for your request>',
        }

        response = requests.get('https://api.coinbase.com/v2/accounts/:account_id/sells', headers=headers)

        print(response.text)

    # https://developers.coinbase.com/api/v2#show-a-sell
    def test_get_show_a_sell(self):
        print("test_get_show_a_sell")

        headers = {
            'CB-ACCESS-KEY': '<your api key>',
            'CB-ACCESS-SIGN': '<the user generated message signature>',
            'CB-ACCESS-TIMESTAMP': '<a timestamp for your request>',
        }

        response = requests.get('https://api.coinbase.com/v2/accounts/:account_id/sells/:sell_id', headers=headers)

        print(response.text)

    # https://developers.coinbase.com/api/v2#place-sell-order
    def test_post_place_sell_order(self):
        print('test_post_place_sell_order')

        headers = {
            'Content-Type': 'application/json',
            'CB-ACCESS-KEY': '<your api key>',
            'CB-ACCESS-SIGN': '<the user generated message signature>',
            'CB-ACCESS-TIMESTAMP': '<a timestamp for your request>',
        }

        data = '{ "amount": "10", "currency": "BTC", "payment_method": "83562370-3e5c-51db-87da-752af5ab9559" }'

        response = requests.post('https://api.coinbase.com/v2/accounts/82de7fcd-db72-5085-8ceb-bee19303080b/sells',
                                 headers=headers, data=data)

        print(response.text)

    # https://developers.coinbase.com/api/v2#commit-a-sell
    def test_post_commit_a_sell(self):
        print('test_post_commit_a_sell')

        headers = {
            'CB-ACCESS-KEY': '<your api key>',
            'CB-ACCESS-SIGN': '<the user generated message signature>',
            'CB-ACCESS-TIMESTAMP': '<a timestamp for your request>',
        }

        response = requests.post(
            'https://api.coinbase.com/v2/accounts/82de7fcd-db72-5085-8ceb-bee19303080b/sells/a333743d-184a-5b5b-abe8-11612fc44ab5/commit',
            headers=headers)

        print(response.text)


class UnitTestsCoinBaseAPIDeposits(unittest.TestCase):
    # https://developers.coinbase.com/api/v2#list-deposits
    def test_get_list_deposits(self):
        print("test_get_list_deposits")

        headers = {
            'CB-ACCESS-KEY': '<your api key>',
            'CB-ACCESS-SIGN': '<the user generated message signature>',
            'CB-ACCESS-TIMESTAMP': '<a timestamp for your request>',
        }

        response = requests.get('https://api.coinbase.com/v2/accounts/:account_id/deposits', headers=headers)

        print(response.text)

    # https://developers.coinbase.com/api/v2#show-a-deposit
    def test_get_show_a_deposit(self):
        print("test_get_show_a_deposit")

        headers = {
            'CB-ACCESS-KEY': '<your api key>',
            'CB-ACCESS-SIGN': '<the user generated message signature>',
            'CB-ACCESS-TIMESTAMP': '<a timestamp for your request>',
        }

        response = requests.get('https://api.coinbase.com/v2/accounts/:account_id/deposits/:deposit_id',
                                headers=headers)

        print(response.text)

    # https://developers.coinbase.com/api/v2#deposit-funds
    def test_post_deposit_funds(self):
        print("test_post_deposit_funds")

        headers = {
            'Content-Type': 'application/json',
            'CB-ACCESS-KEY': '<your api key>',
            'CB-ACCESS-SIGN': '<the user generated message signature>',
            'CB-ACCESS-TIMESTAMP': '<a timestamp for your request>',
        }

        data = '{ "amount": "10", "currency": "USD", "payment_method": "83562370-3e5c-51db-87da-752af5ab9559" }'

        response = requests.post('https://api.coinbase.com/v2/accounts/82de7fcd-db72-5085-8ceb-bee19303080b/deposits',
                                 headers=headers, data=data)

        print(response.text)

    # https://developers.coinbase.com/api/v2#commit-a-deposit
    def test_post_commit_a_deposit(self):
        print("test_post_commit_a_deposit")

        headers = {
            'CB-ACCESS-KEY': '<your api key>',
            'CB-ACCESS-SIGN': '<the user generated message signature>',
            'CB-ACCESS-TIMESTAMP': '<a timestamp for your request>',
        }

        response = requests.post(
            'https://api.coinbase.com/v2/accounts/82de7fcd-db72-5085-8ceb-bee19303080b/deposits/a333743d-184a-5b5b-abe8-11612fc44ab5/commit',
            headers=headers)

        print(response.text)


class UnitTestsCoinBaseAPIWithdrawals(unittest.TestCase):
    # https://developers.coinbase.com/api/v2#list-withdrawals
    def test_get_list_withdrawals(self):
        print('test_get_list_withdrawals')

        headers = {
            'CB-ACCESS-KEY': '<your api key>',
            'CB-ACCESS-SIGN': '<the user generated message signature>',
            'CB-ACCESS-TIMESTAMP': '<a timestamp for your request>',
        }

        response = requests.get('https://api.coinbase.com/v2/accounts/:account_id/withdrawals', headers=headers)

        print(response.text)

    # https://developers.coinbase.com/api/v2#show-a-withdrawal
    def test_get_show_a_withdrawal(self):
        print('test_get_show_a_withdrawal')

        headers = {
            'CB-ACCESS-KEY': '<your api key>',
            'CB-ACCESS-SIGN': '<the user generated message signature>',
            'CB-ACCESS-TIMESTAMP': '<a timestamp for your request>',
        }

        response = requests.get('https://api.coinbase.com/v2/accounts/:account_id/withdrawals/:withdrawal_id',
                                headers=headers)

        print(response.text)

    # https://developers.coinbase.com/api/v2#withdraw-funds
    def test_post_withdraw_funds(self):
        print("test_post_withdraw_funds")

        headers = {
            'Content-Type': 'application/json',
            'CB-ACCESS-KEY': '<your api key>',
            'CB-ACCESS-SIGN': '<the user generated message signature>',
            'CB-ACCESS-TIMESTAMP': '<a timestamp for your request>',
        }

        data = '{ "amount": "10", "currency": "USD", "payment_method": "83562370-3e5c-51db-87da-752af5ab9559" }'

        response = requests.post(
            'https://api.coinbase.com/v2/accounts/82de7fcd-db72-5085-8ceb-bee19303080b/withdrawals', headers=headers,
            data=data)

        print(response.text)

    # https://developers.coinbase.com/api/v2#commit-a-withdrawal
    def test_post_commit_a_withdrawal(self):
        print('test_post_commit_a_withdrawal')

        headers = {
            'CB-ACCESS-KEY': '<your api key>',
            'CB-ACCESS-SIGN': '<the user generated message signature>',
            'CB-ACCESS-TIMESTAMP': '<a timestamp for your request>',
        }

        response = requests.post(
            'https://api.coinbase.com/v2/accounts/82de7fcd-db72-5085-8ceb-bee19303080b/withdrawals/a333743d-184a-5b5b-abe8-11612fc44ab5/commit',
            headers=headers)

        print(response.text)


class UnitTestsCoinBaseAPIPaymentMethods(unittest.TestCase):
    # https://developers.coinbase.com/api/v2#list-payment-methods
    def test_get_list_payment_methods(self):
        print("test_get_list_payment_methods")

        headers = {
            'CB-ACCESS-KEY': '<your api key>',
            'CB-ACCESS-SIGN': '<the user generated message signature>',
            'CB-ACCESS-TIMESTAMP': '<a timestamp for your request>',
        }

        response = requests.get('https://api.coinbase.com/v2/payment-methods', headers=headers)

        print(response.text)

    # https://developers.coinbase.com/api/v2#show-a-payment-method
    def test_get_show_a_payment_method(self):
        print("test_get_show_a_payment_method")

        headers = {
            'CB-ACCESS-KEY': '<your api key>',
            'CB-ACCESS-SIGN': '<the user generated message signature>',
            'CB-ACCESS-TIMESTAMP': '<a timestamp for your request>',
        }

        response = requests.get('https://api.coinbase.com/v2/payment-methods/:payment_method_id/', headers=headers)

        print(response.text)


class UnitTestsCoinBaseAPICurrencies(unittest.TestCase):
    # https://developers.coinbase.com/api/v2#get-currencies
    def test_get_get_currencies(self):
        print("test_get_get_currencies")

        response = requests.get('https://api.coinbase.com/v2/currencies')

        print(response.text)


class UnitTestsCoinBaseAPIExchangeRates(unittest.TestCase):
    # https://developers.coinbase.com/api/v2#get-exchange-rates
    def test_get_get_exchange_rates(self):
        print("test_get_get_exchange_rates")

        response = requests.get('https://api.coinbase.com/v2/exchange-rates')

        print(response.text)


class UnitTestsCoinBaseAPIPrices(unittest.TestCase):
    # https://developers.coinbase.com/api/v2#get-buy-price
    def test_get_get_buy_price(self):
        print("test_get_get_buy_price")

        headers = {
            'CB-ACCESS-KEY': '<your api key>',
            'CB-ACCESS-SIGN': '<the user generated message signature>',
            'CB-ACCESS-TIMESTAMP': '<a timestamp for your request>',
        }

        response = requests.get('https://api.coinbase.com/v2/prices/:currency_pair/buy', headers=headers)

        print(response.text)

    # https://developers.coinbase.com/api/v2#get-sell-price
    def test_get_get_sell_price(self):
        print("test_get_get_sell_price")

        headers = {
            'CB-ACCESS-KEY': '<your api key>',
            'CB-ACCESS-SIGN': '<the user generated message signature>',
            'CB-ACCESS-TIMESTAMP': '<a timestamp for your request>',
        }

        response = requests.get('https://api.coinbase.com/v2/prices/:currency_pair/sell', headers=headers)

        print(response.text)

    # https://developers.coinbase.com/api/v2#get-spot-price
    def test_get_get_spot_price(self):
        print('test_get_get_spot_price')

        headers = {
            'CB-ACCESS-KEY': '<your api key>',
            'CB-ACCESS-SIGN': '<the user generated message signature>',
            'CB-ACCESS-TIMESTAMP': '<a timestamp for your request>',
        }

        response = requests.get('https://api.coinbase.com/v2/prices/:currency_pair/spot', headers=headers)

        print(response.text)


class UnitTestsCoinBaseAPITime(unittest.TestCase):
    # https://developers.coinbase.com/api/v2#get-current-time
    def test_get_get_current_time(self):
        print("test_get_get_current_time")

        headers = {
            'CB-ACCESS-KEY': '<your api key>',
            'CB-ACCESS-SIGN': '<the user generated message signature>',
            'CB-ACCESS-TIMESTAMP': '<a timestamp for your request>',
        }

        response = requests.get('https://api.coinbase.com/v2/time', headers=headers)

        print(response.text)


if __name__ == '__main__':
    unittest.main()
