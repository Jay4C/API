import unittest
import requests


# https://www.coingecko.com/api/documentations/v3
class Unit_Tests_CoinGecko_API_Ping(unittest.TestCase):
    def test_get_check_api_server_status(self):
        print('test_get_check_api_server_status')

        headers = {
            'accept': 'application/json',
        }

        response = requests.get('https://api.coingecko.com/api/v3/ping', headers=headers)

        print(response.text)


class Unit_Tests_CoinGecko_API_Simple(unittest.TestCase):
    def test_get_simple_price(self):
        print("test_get_simple_price")

        headers = {
            'accept': 'application/json',
        }

        params = (
            ('ids', 'id'),
            ('vs_currencies', 'vs_currencies'),
            ('include_market_cap', 'include_market_cap'),
            ('include_24hr_vol', 'include_24hr_vol'),
            ('include_24hr_change', 'include_24hr_change'),
            ('include_last_updated_at', 'include_last_updated_at'),
        )

        response = requests.get('https://api.coingecko.com/api/v3/simple/price', headers=headers, params=params)

        print(response.text)

    def test_get_simple_token_price(self):
        print("test_get_simple_token_price")

        headers = {
            'accept': 'application/json',
        }

        params = (
            ('contract_addresses', 'contract_addresses'),
            ('vs_currencies', 'vs_currencies'),
            ('include_market_cap', 'include_market_cap'),
            ('include_24hr_vol', 'include_24hr_vol'),
            ('include_24hr_change', 'include_24hr_change'),
            ('include_last_updated_at', 'include_last_updated_at'),
        )

        response = requests.get('https://api.coingecko.com/api/v3/simple/token_price/id', headers=headers,
                                params=params)

        print(response.text)

    def test_get_simple_supported_vs_currencies(self):
        print("test_get_simple_supported_vs_currencies")

        headers = {
            'accept': 'application/json',
        }

        response = requests.get('https://api.coingecko.com/api/v3/simple/supported_vs_currencies', headers=headers)

        print(response.text)


class Unit_Tests_CoinGecko_API_Coins(unittest.TestCase):
    def test_get_coins_list(self):
        print("test_get_coins_list")

        headers = {
            'accept': 'application/json',
        }

        params = (
            ('include_platform', 'false')
        )

        response = requests.get('https://api.coingecko.com/api/v3/coins/list', headers=headers,
                                params=params)

        print(response.text)

    def test_get_coins_markets(self):
        print("test_get_coins_markets")

        headers = {
            'accept': 'application/json',
        }

        params = (
            ('vs_currency', 'vs_currency'),
            ('ids', 'ids'),
            ('category', 'category'),
            ('order', 'market_cap_desc'),
            ('per_page', '100'),
            ('page', '1'),
            ('sparkline', 'false'),
            ('price_change_percentage', 'price_change_percentage'),
        )

        response = requests.get('https://api.coingecko.com/api/v3/coins/markets', headers=headers, params=params)

        print(response.text)

    def test_get_coins_id(self):
        print("test_get_coins_id")

        headers = {
            'accept': 'application/json',
        }

        params = (
            ('localization', 'localization'),
            ('tickers', 'true'),
            ('market_data', 'true'),
            ('community_data', 'true'),
            ('developer_data', 'true'),
            ('sparkline', 'true'),
        )

        response = requests.get('https://api.coingecko.com/api/v3/coins/id', headers=headers, params=params)

        print(response.text)

    def test_get_coins_id_tickets(self):
        print("test_get_coin_id_tickets")

        headers = {
            'accept': 'application/json',
        }

        params = (
            ('exchange_ids', 'exchange_ids'),
            ('include_exchange_logo', 'include_exchange_logo'),
            ('page', '1'),
            ('order', 'order'),
            ('depth', 'depth'),
        )

        response = requests.get('https://api.coingecko.com/api/v3/coins/id/tickers', headers=headers, params=params)

        print(response.text)

    def test_get_coins_id_history(self):
        print("test_get_coins_id_history")

        headers = {
            'accept': 'application/json',
        }

        params = (
            ('date', 'date'),
            ('localization', 'localization'),
        )

        response = requests.get('https://api.coingecko.com/api/v3/coins/id/history', headers=headers, params=params)

        print(response.text)

    def test_get_coins_id_market_chart(self):
        print("test_get_coins_id_market_chart")

        headers = {
            'accept': 'application/json',
        }

        params = (
            ('vs_currency', 'vs_currency'),
            ('days', 'days'),
            ('interval', 'interval'),
        )

        response = requests.get('https://api.coingecko.com/api/v3/coins/id/market_chart', headers=headers,
                                params=params)

        print(response.text)

    def test_get_coins_id_market_chart_range(self):
        print("test_get_coins_id_market_chart_range")

        headers = {
            'accept': 'application/json',
        }

        params = (
            ('vs_currency', 'vs_currency'),
            ('from', 'from'),
            ('to', 'to'),
        )

        response = requests.get('https://api.coingecko.com/api/v3/coins/id/market_chart/range', headers=headers,
                                params=params)

        print(response.text)

    def test_get_coins_id_status_updates(self):
        print("test_get_coins_id_status_updates")

        headers = {
            'accept': 'application/json',
        }

        params = (
            ('per_page', '1'),
            ('page', '1'),
        )

        response = requests.get('https://api.coingecko.com/api/v3/coins/id/status_updates', headers=headers,
                                params=params)

        print(response.text)

    def test_get_coins_id_ohlc(self):
        print('test_get_coins_id_ohlc')

        headers = {
            'accept': 'application/json',
        }

        params = (
            ('vs_currency', 'vs_currency'),
            ('days', '1'),
        )

        response = requests.get('https://api.coingecko.com/api/v3/coins/id/ohlc', headers=headers, params=params)

        print(response.text)


class Unit_Tests_CoinGecko_API_Contract(unittest.TestCase):
    def test_get_coins_id_contract_contract_address(self):
        print('test_get_coins_id_contract_contract_address')

        headers = {
            'accept': 'application/json',
        }

        response = requests.get('https://api.coingecko.com/api/v3/coins/id/contract/contract_address', headers=headers)

        print(response.text)

    def test_get_coins_id_contract_contract_address_market_chart(self):
        print("test_get_coins_id_contract_contract_address_market_chart")

        headers = {
            'accept': 'application/json',
        }

        params = (
            ('vs_currency', 'vs_currency'),
            ('days', 'days'),
        )

        response = requests.get('https://api.coingecko.com/api/v3/coins/id/contract/contract_address/market_chart/',
                                headers=headers, params=params)

        print(response.text)

    def test_get_coins_id_contract_contract_address_market_chart_range(self):
        print("test_get_coins_id_contract_contract_address_market_chart_range")

        headers = {
            'accept': 'application/json',
        }

        params = (
            ('vs_currency', 'vs_currency'),
            ('from', 'from'),
            ('to', 'to'),
        )

        response = requests.get(
            'https://api.coingecko.com/api/v3/coins/id/contract/contract_address/market_chart/range', headers=headers,
            params=params)

        print(response.text)


class Unit_Tests_CoinGecko_API_Asset_Platforms(unittest.TestCase):
    def test_get_asset_platforms(self):
        print("test_get_asset_platforms")

        headers = {
            'accept': 'application/json',
        }

        response = requests.get('https://api.coingecko.com/api/v3/asset_platforms', headers=headers)

        print(response.text)


class Unit_Tests_CoinGecko_API_Categories(unittest.TestCase):
    def test_get_coins_categories_list(self):
        print("test_get_coins_categories_list")

        headers = {
            'accept': 'application/json',
        }

        response = requests.get('https://api.coingecko.com/api/v3/coins/categories/list', headers=headers)

        print(response.text)

    def test_get_coins_categories(self):
        print("test_get_coins_categories")

        headers = {
            'accept': 'application/json',
        }

        params = (
            ('order', 'order'),
        )

        response = requests.get('https://api.coingecko.com/api/v3/coins/categories', headers=headers, params=params)

        print(response.text)


class Unit_Tests_CoinGecko_API_Exchanges(unittest.TestCase):
    def test_get_exchanges(self):
        print("test_get_exchanges")

        headers = {
            'accept': 'application/json',
        }

        params = (
            ('per_page', '1'),
            ('page', 'page'),
        )

        response = requests.get('https://api.coingecko.com/api/v3/exchanges', headers=headers, params=params)

        print(response.text)

    def test_get_exchanges_list(self):
        print("test_get_exchanges_list")

        headers = {
            'accept': 'application/json',
        }

        response = requests.get('https://api.coingecko.com/api/v3/exchanges/list', headers=headers)

        print(response.text)

    def test_get_exchanges_id(self):
        print("test_get_exchanges_id")

        headers = {
            'accept': 'application/json',
        }

        response = requests.get('https://api.coingecko.com/api/v3/exchanges/id', headers=headers)

        print(response.text)

    def test_get_exchanges_id_tickers(self):
        print("test_get_exchanges_id_tickers")

        headers = {
            'accept': 'application/json',
        }

        params = (
            ('coin_ids', 'coin_ids'),
            ('include_exchange_logo', 'include_exchange_logo'),
            ('page', '1'),
            ('depth', 'depth'),
            ('order', 'order'),
        )

        response = requests.get('https://api.coingecko.com/api/v3/exchanges/id/tickers', headers=headers, params=params)

        print(response.text)

    def test_get_exchanges_id_status_updates(self):
        print("test_get_exchanges_id_status_updates")

        headers = {
            'accept': 'application/json',
        }

        params = (
            ('per_page', '1'),
            ('page', '1'),
        )

        response = requests.get('https://api.coingecko.com/api/v3/exchanges/id/status_updates', headers=headers,
                                params=params)

        print(response.text)

    def test_get_exchanges_id_volume_chart(self):
        print("test_get_exchanges_id_volume_chart")

        headers = {
            'accept': 'application/json',
        }

        params = (
            ('days', '1'),
        )

        response = requests.get('https://api.coingecko.com/api/v3/exchanges/id/volume_chart', headers=headers,
                                params=params)

        print(response.text)


class Unit_Tests_CoinGecko_API_Finance(unittest.TestCase):
    def test_get_finance_platforms(self):
        print("test_get_finance_platforms")

        headers = {
            'accept': 'application/json',
        }

        params = (
            ('per_page', '1'),
        )

        response = requests.get('https://api.coingecko.com/api/v3/finance_platforms', headers=headers, params=params)

        print(response.text)

    def test_get_finance_products(self):
        print("test_get_finance_products")

        headers = {
            'accept': 'application/json',
        }

        params = (
            ('per_page', '1'),
        )

        response = requests.get('https://api.coingecko.com/api/v3/finance_products', headers=headers, params=params)

        print(response.text)


class Unit_Tests_CoinGecko_API_Indexes(unittest.TestCase):
    def test_get_indexes(self):
        print('test_get_indexes')

        headers = {
            'accept': 'application/json',
        }

        params = (
            ('per_page', '1'),
            ('page', '1'),
        )

        response = requests.get('https://api.coingecko.com/api/v3/indexes', headers=headers, params=params)

        print(response.text)

    def test_get_indexes_market_id_id(self):
        print("test_get_indexes_market_id_id")

        headers = {
            'accept': 'application/json',
        }

        response = requests.get('https://api.coingecko.com/api/v3/indexes/market_id/id', headers=headers)

        print(response.text)

    def test_get_indexes_list(self):
        print("test_get_indexes_list")

        headers = {
            'accept': 'application/json',
        }

        response = requests.get('https://api.coingecko.com/api/v3/indexes/list', headers=headers)

        print(response.text)


class Unit_Tests_CoinGecko_API_Derivatives(unittest.TestCase):
    def test_get_derivatives(self):
        print('test_get_derivatives')

        headers = {
            'accept': 'application/json',
        }

        params = (
            ('include_tickers', 'include_tickers')
        )

        response = requests.get('https://api.coingecko.com/api/v3/derivatives', headers=headers, params=params)

        print(response.text)

    def test_get_derivatives_eschanges(self):
        print("test_get_derivatives_eschanges")

        headers = {
            'accept': 'application/json',
        }

        params = (
            ('order', 'order'),
            ('per_page', '1'),
            ('page', '1'),
        )

        response = requests.get('https://api.coingecko.com/api/v3/derivatives/exchanges', headers=headers,
                                params=params)

        print(response.text)

    def test_get_derivatives_exchanges_id(self):
        print("test_get_derivatives_exchanges_id")

        headers = {
            'accept': 'application/json',
        }

        params = (
            ('include_tickers', 'include_tickers'),
        )

        response = requests.get('https://api.coingecko.com/api/v3/derivatives/exchanges/id', headers=headers,
                                params=params)

        print(response.text)

    def test_get_derivatives_exchanges_list(self):
        print("test_get_derivatives_exchanges_list")

        headers = {
            'accept': 'application/json',
        }

        response = requests.get('https://api.coingecko.com/api/v3/derivatives/exchanges/list', headers=headers)

        print(response.text)


class Unit_Tests_CoinGecko_API_Status_Updates(unittest.TestCase):
    def test_get_status_updates(self):
        print("test_get_status_updates")

        headers = {
            'accept': 'application/json',
        }

        params = (
            ('category', 'category'),
            ('project_type', 'project_type'),
            ('per_page', '1'),
            ('page', '1'),
        )

        response = requests.get('https://api.coingecko.com/api/v3/status_updates', headers=headers, params=params)

        print(response.text)


class Unit_Tests_CoinGecko_API_Events(unittest.TestCase):
    def test_get_events(self):
        print("test_get_events")

        headers = {
            'accept': 'application/json',
        }

        params = (
            ('country_code', 'country_code'),
            ('type', 'type'),
            ('page', 'page'),
            ('upcoming_events_only', 'upcoming_events_only'),
            ('from_date', 'from_date'),
            ('to_date', 'to_date'),
        )

        response = requests.get('https://api.coingecko.com/api/v3/events', headers=headers, params=params)

        print(response.text)

    def test_get_events_countries(self):
        print("test_get_events_countries")

        headers = {
            'accept': 'application/json',
        }

        response = requests.get('https://api.coingecko.com/api/v3/events/countries', headers=headers)

        print(response.text)

    def test_get_events_types(self):
        print('test_get_events_types')

        headers = {
            'accept': 'application/json',
        }

        response = requests.get('https://api.coingecko.com/api/v3/events/types', headers=headers)

        print(response.text)


class Unit_Tests_CoinGecko_API_Exchange_Rates(unittest.TestCase):
    def test_get_exchange_rates(self):
        print("test_get_exchange_rates")

        headers = {
            'accept': 'application/json',
        }

        response = requests.get('https://api.coingecko.com/api/v3/exchange_rates', headers=headers)

        print(response.text)


class Unit_Tests_CoinGecko_API_Trending(unittest.TestCase):
    def test_get_search_trending(self):
        print("test_get_search_trending")

        headers = {
            'accept': 'application/json',
        }

        response = requests.get('https://api.coingecko.com/api/v3/search/trending', headers=headers)

        print(response.text)


class Unit_Tests_CoinGecko_API_Global(unittest.TestCase):
    def test_get_global(self):
        print("test_get_global")

        headers = {
            'accept': 'application/json',
        }

        response = requests.get('https://api.coingecko.com/api/v3/global', headers=headers)

        print(response.text)

    def test_get_global_decentralized_finance_defi(self):
        print("test_get_global_decentralized_finance_defi")

        headers = {
            'accept': 'application/json',
        }

        response = requests.get('https://api.coingecko.com/api/v3/global/decentralized_finance_defi', headers=headers)

        print(response.text)


class Unit_Tests_CoinGecko_API_Companies_Beta(unittest.TestCase):
    def test_get_companies_public_treasury_coin_id(self):
        print("test_get_companies_public_treasury_coin_id")

        headers = {
            'accept': 'application/json',
        }

        response = requests.get('https://api.coingecko.com/api/v3/companies/public_treasury/coin_id', headers=headers)

        print(response.text)


if __name__ == '__main__':
    unittest.main()
