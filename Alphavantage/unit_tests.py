import unittest
from requests_tor import RequestsTor
import csv


# https://www.alphavantage.co/documentation/
class UnitTestsAlphavantageForTimeSeriesStockDataAPIsWithTorRequest(unittest.TestCase):
    # ok
    def test_TIME_SERIES_INTRADAY(self):
        print("test_TIME_SERIES_INTRADAY")

        # replace the "demo" apikey below with your own key from https://www.alphavantage.co/support/#api-key
        api_key = "demo"

        url = 'https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=IBM&interval=5min&apikey=' \
              + api_key

        headers = {
            "Accept": "application/json",
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103'
        }

        rt = RequestsTor()

        r = rt.get(url, headers=headers)

        data = r.json()

        print(data)

    # ok
    def test_Intraday(self):
        print("test_Intraday")

        import csv

        # replace the "demo" apikey below with your own key from https://www.alphavantage.co/support/#api-key

        api_key = "demo"

        CSV_URL = 'https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY_EXTENDED' \
                  '&symbol=IBM&interval=15min&slice=year1month1&apikey=' + api_key

        rt = RequestsTor()

        headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103'
        }

        download = rt.get(CSV_URL, headers=headers)

        decoded_content = download.content.decode('utf-8')

        cr = csv.reader(decoded_content.splitlines(), delimiter=',')

        my_list = list(cr)

        for row in my_list:
            print(row)

    # ok
    def test_TIME_SERIES_DAILY(self):
        print("test_TIME_SERIES_DAILY")

        # replace the "demo" apikey below with your own key from https://www.alphavantage.co/support/#api-key
        api_key = "demo"

        url = 'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=IBM&apikey=' + api_key

        rt = RequestsTor()

        headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103'
        }

        r = rt.get(url, headers=headers)

        data = r.json()

        print(data)

    # ok
    def test_TIME_SERIES_DAILY_ADJUSTED(self):
        print("test_TIME_SERIES_DAILY_ADJUSTED")

        # replace the "demo" apikey below with your own key from https://www.alphavantage.co/support/#api-key
        api_key = "demo"

        url = 'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY_ADJUSTED&symbol=IBM&apikey=' + api_key

        rt = RequestsTor()

        headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103'
        }

        r = rt.get(url, headers=headers)

        data = r.json()

        print(data)

    # ok
    def test_TIME_SERIES_WEEKLY(self):
        print('test_TIME_SERIES_WEEKLY')

        # replace the "demo" apikey below with your own key from https://www.alphavantage.co/support/#api-key
        api_key = "demo"

        url = 'https://www.alphavantage.co/query?function=TIME_SERIES_WEEKLY&symbol=IBM&apikey=' + api_key

        rt = RequestsTor()

        headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103'
        }

        r = rt.get(url, headers=headers)

        data = r.json()

        print(data)

    # ok
    def test_TIME_SERIES_WEEKLY_ADJUSTED(self):
        print('test_TIME_SERIES_WEEKLY_ADJUSTED')

        # replace the "demo" apikey below with your own key from https://www.alphavantage.co/support/#api-key
        api_key = "demo"

        url = 'https://www.alphavantage.co/query?function=TIME_SERIES_WEEKLY_ADJUSTED&symbol=IBM&apikey=' + api_key

        rt = RequestsTor()

        headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103'
        }

        r = rt.get(url, headers=headers)

        data = r.json()

        print(data)

    # ok
    def test_TIME_SERIES_MONTHLY(self):
        print('test_TIME_SERIES_MONTHLY')

        # replace the "demo" apikey below with your own key from https://www.alphavantage.co/support/#api-key
        api_key = "demo"

        url = 'https://www.alphavantage.co/query?function=TIME_SERIES_MONTHLY&symbol=IBM&apikey=' + api_key

        rt = RequestsTor()

        headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103'
        }

        r = rt.get(url, headers=headers)

        data = r.json()

        print(data)

    # ok
    def test_TIME_SERIES_MONTHLY_ADJUSTED(self):
        print("test_TIME_SERIES_MONTHLY_ADJUSTED")

        # replace the "demo" apikey below with your own key from https://www.alphavantage.co/support/#api-key
        api_key = "demo"

        url = 'https://www.alphavantage.co/query?function=TIME_SERIES_MONTHLY_ADJUSTED&symbol=IBM&apikey=' + api_key

        rt = RequestsTor()

        headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103'
        }

        r = rt.get(url, headers=headers)

        data = r.json()

        print(data)

    # ok
    def test_Quote_Endpoint(self):
        print("test_Quote_Endpoint")

        # replace the "demo" apikey below with your own key from https://www.alphavantage.co/support/#api-key
        api_key = "demo"

        url = 'https://www.alphavantage.co/query?function=GLOBAL_QUOTE&symbol=IBM&apikey=' + api_key

        rt = RequestsTor()

        headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103'
        }

        r = rt.get(url, headers=headers)

        data = r.json()

        print(data)

    # ok
    def test_Search_Endpoint(self):
        print('test_Search_Endpoint')

        # replace the "demo" apikey below with your own key from https://www.alphavantage.co/support/#api-key
        api_key = "demo"

        url = 'https://www.alphavantage.co/query?function=SYMBOL_SEARCH&keywords=tesco&apikey=' + api_key

        rt = RequestsTor()

        headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103'
        }

        r = rt.get(url, headers=headers)

        data = r.json()

        print(data)


class UnitTestsAlphavantageForFundamentalDataAPIsWithTorRequest(unittest.TestCase):
    def test_INCOME_STATEMENT(self):
        print("test_INCOME_STATEMENT")

        # replace the "demo" apikey below with your own key from https://www.alphavantage.co/support/#api-key
        api_key = "demo"

        url = 'https://www.alphavantage.co/query?function=INCOME_STATEMENT&symbol=IBM&apikey=' + api_key

        rt = RequestsTor()

        headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103'
        }

        r = rt.get(url, headers=headers)

        data = r.json()

        print(data)

    def test_BALANCE_SHEET(self):
        print("test_BALANCE_SHEET")

        # replace the "demo" apikey below with your own key from https://www.alphavantage.co/support/#api-key
        api_key = "demo"

        url = 'https://www.alphavantage.co/query?function=BALANCE_SHEET&symbol=IBM&apikey=' + api_key

        rt = RequestsTor()

        headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103'
        }

        r = rt.get(url, headers=headers)

        data = r.json()

        print(data)

    def test_CASH_FLOW(self):
        print("test_CASH_FLOW")

        # replace the "demo" apikey below with your own key from https://www.alphavantage.co/support/#api-key
        api_key = "demo"

        url = 'https://www.alphavantage.co/query?function=CASH_FLOW&symbol=IBM&apikey=' + api_key

        rt = RequestsTor()

        headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103'
        }

        r = rt.get(url, headers=headers)

        data = r.json()

        print(data)

    def test_Earnings(self):
        print("test_Earnings")

        # replace the "demo" apikey below with your own key from https://www.alphavantage.co/support/#api-key
        api_key = "demo"

        url = 'https://www.alphavantage.co/query?function=EARNINGS&symbol=IBM&apikey=' + api_key

        rt = RequestsTor()

        headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103'
        }

        r = rt.get(url, headers=headers)

        data = r.json()

        print(data)

    def test_Company_Overview(self):
        print("test_Company_Overview")

        # replace the "demo" apikey below with your own key from https://www.alphavantage.co/support/#api-key
        api_key = "demo"

        url = 'https://www.alphavantage.co/query?function=OVERVIEW&symbol=IBM&apikey=' + api_key

        rt = RequestsTor()

        headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103'
        }

        r = rt.get(url, headers=headers)

        data = r.json()

        print(data)

    def test_Listing_And_Delisting_Status(self):
        print("test_Listing_And_Delisting_Status")

        # replace the "demo" apikey below with your own key from https://www.alphavantage.co/support/#api-key
        api_key = "demo"

        CSV_URL = 'https://www.alphavantage.co/query?function=LISTING_STATUS&apikey=' + api_key

        rt = RequestsTor()

        headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103'
        }

        download = rt.get(CSV_URL, headers=headers)

        decoded_content = download.content.decode('utf-8')

        cr = csv.reader(decoded_content.splitlines(), delimiter=',')

        my_list = list(cr)

        for row in my_list:
            print(row)

    def test_Earnings_Calendar(self):
        print("test_Earnings_Calendar")

        # replace the "demo" apikey below with your own key from https://www.alphavantage.co/support/#api-key
        api_key = "demo"

        CSV_URL = 'https://www.alphavantage.co/query?function=EARNINGS_CALENDAR&horizon=3month&apikey=' + api_key

        rt = RequestsTor()

        headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103'
        }

        download = rt.get(CSV_URL, headers=headers)

        decoded_content = download.content.decode('utf-8')

        cr = csv.reader(decoded_content.splitlines(), delimiter=',')

        my_list = list(cr)

        for row in my_list:
            print(row)

    def test_IPO_Calendar(self):
        print('test_IPO_Calendar')

        # replace the "demo" apikey below with your own key from https://www.alphavantage.co/support/#api-key
        api_key = "demo"

        CSV_URL = 'https://www.alphavantage.co/query?function=IPO_CALENDAR&apikey=' + api_key

        rt = RequestsTor()

        headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103'
        }

        download = rt.get(CSV_URL, headers=headers)

        decoded_content = download.content.decode('utf-8')

        cr = csv.reader(decoded_content.splitlines(), delimiter=',')

        my_list = list(cr)

        for row in my_list:
            print(row)


class UnitTestsAlphavantageForForeignExchangeAPIsWithTorRequest(unittest.TestCase):
    def test_CURRENCY_EXCHANGE_RATE(self):
        print("test_CURRENCY_EXCHANGE_RATE")

        # replace the "demo" apikey below with your own key from https://www.alphavantage.co/support/#api-key
        api_key = 'demo'

        url = 'https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE' \
              '&from_currency=USD&to_currency=JPY&apikey=' + api_key

        rt = RequestsTor()

        headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103'
        }

        r = rt.get(url, headers=headers)

        data = r.json()

        print(data)

    def test_FX_INTRADAY(self):
        print("test_FX_INTRADAY")

        # replace the "demo" apikey below with your own key from https://www.alphavantage.co/support/#api-key
        api_key = "demo"

        url = 'https://www.alphavantage.co/query?function=FX_INTRADAY&from_symbol=EUR' \
              '&to_symbol=USD&interval=5min&apikey=' + api_key

        rt = RequestsTor()

        headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103'
        }

        r = rt.get(url, headers=headers)

        data = r.json()

        print(data)

    def test_FX_DAILY(self):
        print("test_FX_DAILY")

        # replace the "demo" apikey below with your own key from https://www.alphavantage.co/support/#api-key
        api_key = "demo"

        url = 'https://www.alphavantage.co/query?function=FX_DAILY&from_symbol=EUR&to_symbol=USD&apikey=' + api_key

        rt = RequestsTor()

        headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103'
        }

        r = rt.get(url, headers=headers)

        data = r.json()

        print(data)

    def test_FX_WEEKLY(self):
        print("test_FX_WEEKLY")

        # replace the "demo" apikey below with your own key from https://www.alphavantage.co/support/#api-key
        api_key = "demo"

        url = 'https://www.alphavantage.co/query?function=FX_WEEKLY&from_symbol=EUR&to_symbol=USD&apikey=' + api_key

        rt = RequestsTor()

        headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103'
        }

        r = rt.get(url, headers=headers)

        data = r.json()

        print(data)

    def test_FX_MONTHLY(self):
        print("test_FX_MONTHLY")

        # replace the "demo" apikey below with your own key from https://www.alphavantage.co/support/#api-key
        api_key = "demo"

        url = 'https://www.alphavantage.co/query?function=FX_MONTHLY&from_symbol=EUR&to_symbol=USD&apikey=' + api_key

        rt = RequestsTor()

        headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103'
        }

        r = rt.get(url, headers=headers)

        data = r.json()

        print(data)


class UnitTestsAlphavantageForDigitalCryptoCurrenciesAPIsWithTorRequest(unittest.TestCase):
    def test_CURRENCY_EXCHANGE_RATE(self):
        print("test_CURRENCY_EXCHANGE_RATE")

        # replace the "demo" apikey below with your own key from https://www.alphavantage.co/support/#api-key
        api_key = "demo"

        url = 'https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE&from_currency=BTC' \
              '&to_currency=CNY&apikey=' + api_key

        rt = RequestsTor()

        headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103'
        }

        r = rt.get(url, headers=headers)

        data = r.json()

        print(data)

    def test_CRYPTO_INTRADAY(self):
        print("test_CRYPTO_INTRADAY")

        # replace the "demo" apikey below with your own key from https://www.alphavantage.co/support/#api-key
        api_key = "demo"

        url = 'https://www.alphavantage.co/query?function=CRYPTO_INTRADAY&symbol=ETH&market=USD' \
              '&interval=5min&apikey=' + api_key

        rt = RequestsTor()

        headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103'
        }

        r = rt.get(url, headers=headers)

        data = r.json()

        print(data)

    def test_DIGITAL_CURRENCY_DAILY(self):
        print("test_DIGITAL_CURRENCY_DAILY")

        # replace the "demo" apikey below with your own key from https://www.alphavantage.co/support/#api-key
        api_key = "demo"

        url = 'https://www.alphavantage.co/query?function=DIGITAL_CURRENCY_DAILY&symbol=BTC&market=CNY&apikey=' \
              + api_key

        rt = RequestsTor()

        headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103'
        }

        r = rt.get(url, headers=headers)

        data = r.json()

        print(data)

    def test_DIGITAL_CURRENCY_WEEKLY(self):
        print("test_DIGITAL_CURRENCY_WEEKLY")

        # replace the "demo" apikey below with your own key from https://www.alphavantage.co/support/#api-key
        api_key = "demo"

        url = 'https://www.alphavantage.co/query?function=DIGITAL_CURRENCY_WEEKLY' \
              '&symbol=BTC&market=CNY&apikey=' + api_key

        rt = RequestsTor()

        headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103'
        }

        r = rt.get(url, headers=headers)

        data = r.json()

        print(data)

    def test_DIGITAL_CURRENCY_MONTHLY(self):
        print("test_DIGITAL_CURRENCY_MONTHLY")

        # replace the "demo" apikey below with your own key from https://www.alphavantage.co/support/#api-key
        api_key = "demo"

        url = 'https://www.alphavantage.co/query?function=DIGITAL_CURRENCY_MONTHLY&symbol=BTC&market=CNY&apikey=' + api_key

        rt = RequestsTor()

        headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103'
        }

        r = rt.get(url, headers=headers)

        data = r.json()

        print(data)


class UnitTestsAlphavantageForEconomicIndicatorsAPIsWithTorRequest(unittest.TestCase):
    def test_REAL_GDP(self):
        print('test_REAL_GDP')

        # replace the "demo" apikey below with your own key from https://www.alphavantage.co/support/#api-key
        api_key = "demo"

        url = 'https://www.alphavantage.co/query?function=REAL_GDP&interval=annual&apikey=' + api_key

        rt = RequestsTor()

        headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103'
        }

        r = rt.get(url, headers=headers)

        data = r.json()

        print(data)

    def test_REAL_GDP_PER_CAPITA(self):
        print('test_REAL_GDP_PER_CAPITA')

        # replace the "demo" apikey below with your own key from https://www.alphavantage.co/support/#api-key
        api_key = ""

        url = 'https://www.alphavantage.co/query?function=REAL_GDP_PER_CAPITA&apikey=' + api_key

        rt = RequestsTor()

        headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103'
        }

        r = rt.get(url, headers=headers)

        data = r.json()

        print(data)

    def test_TREASURY_YIELD(self):
        print("test_TREASURY_YIELD")

        # replace the "demo" apikey below with your own key from https://www.alphavantage.co/support/#api-key
        api_key = "demo"

        url = 'https://www.alphavantage.co/query?function=TREASURY_YIELD' \
              '&interval=monthly&maturity=10year&apikey=' + api_key

        rt = RequestsTor()

        headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103'
        }

        r = rt.get(url, headers=headers)

        data = r.json()

        print(data)

    def test_FEDERAL_FUNDS_RATE(self):
        print("test_FEDERAL_FUNDS_RATE")

        # replace the "demo" apikey below with your own key from https://www.alphavantage.co/support/#api-key
        api_key = "demo"

        url = 'https://www.alphavantage.co/query?function=FEDERAL_FUNDS_RATE&interval=monthly&apikey=' + api_key

        rt = RequestsTor()

        headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103'
        }

        r = rt.get(url, headers=headers)

        data = r.json()

        print(data)

    def test_CPI(self):
        print("test_CPI")

        # replace the "demo" apikey below with your own key from https://www.alphavantage.co/support/#api-key
        api_key = ""

        url = 'https://www.alphavantage.co/query?function=CPI&interval=monthly&apikey=' + api_key

        rt = RequestsTor()

        headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103'
        }

        r = rt.get(url, headers=headers)

        data = r.json()

        print(data)

    def test_INFLATION(self):
        print('test_INFLATION')

        # replace the "demo" apikey below with your own key from https://www.alphavantage.co/support/#api-key
        api_key = ""

        url = 'https://www.alphavantage.co/query?function=INFLATION&apikey=' + api_key

        rt = RequestsTor()

        headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103'
        }

        r = rt.get(url, headers=headers)

        data = r.json()

        print(data)

    def test_INFLATION_EXPECTATION(self):
        print('test_INFLATION_EXPECTATION')

        # replace the "demo" apikey below with your own key from https://www.alphavantage.co/support/#api-key
        api_key = "demo"

        url = 'https://www.alphavantage.co/query?function=INFLATION_EXPECTATION&apikey=' + api_key

        rt = RequestsTor()

        headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103'
        }

        r = rt.get(url, headers=headers)

        data = r.json()

        print(data)

    def test_CONSUMER_SENTIMENT(self):
        print('test_CONSUMER_SENTIMENT')

        # replace the "demo" apikey below with your own key from https://www.alphavantage.co/support/#api-key
        api_key = "demo"

        url = 'https://www.alphavantage.co/query?function=CONSUMER_SENTIMENT&apikey=' + api_key

        rt = RequestsTor()

        headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103'
        }

        r = rt.get(url, headers=headers)

        data = r.json()

        print(data)

    def test_RETAIL_SALES(self):
        print("test_RETAIL_SALES")

        # replace the "demo" apikey below with your own key from https://www.alphavantage.co/support/#api-key
        api_key = ""

        url = 'https://www.alphavantage.co/query?function=RETAIL_SALES&apikey=' + api_key

        rt = RequestsTor()

        headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103'
        }

        r = rt.get(url, headers=headers)

        data = r.json()

        print(data)

    def test_DURABLES(self):
        print("test_DURABLES")

        # replace the "demo" apikey below with your own key from https://www.alphavantage.co/support/#api-key
        api_key = "demo"

        url = 'https://www.alphavantage.co/query?function=DURABLES&apikey=' + api_key

        rt = RequestsTor()

        headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103'
        }

        r = rt.get(url, headers=headers)

        data = r.json()

        print(data)

    def test_UNEMPLOYMENT(self):
        print('test_UNEMPLOYMENT')

        # replace the "demo" apikey below with your own key from https://www.alphavantage.co/support/#api-key
        api_key = "demo"

        url = 'https://www.alphavantage.co/query?function=UNEMPLOYMENT&apikey=' + api_key

        rt = RequestsTor()

        headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103'
        }

        r = rt.get(url, headers=headers)

        data = r.json()

        print(data)

    def test_NONFARM_PAYROLL(self):
        print("test_NONFARM_PAYROLL")

        # replace the "demo" apikey below with your own key from https://www.alphavantage.co/support/#api-key
        api_key = "demo"

        url = 'https://www.alphavantage.co/query?function=NONFARM_PAYROLL&apikey=' + api_key

        rt = RequestsTor()

        headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103'
        }

        r = rt.get(url, headers=headers)

        data = r.json()

        print(data)


class UnitTestsAlphavantageForTechnicalIndicatorsAPIsWithTorRequest(unittest.TestCase):
    def test_SMA(self):
        print('test_SMA')

        # replace the "demo" apikey below with your own key from https://www.alphavantage.co/support/#api-key
        api_key = "demo"

        url = 'https://www.alphavantage.co/query?function=SMA&symbol=IBM&interval=weekly&time_period=10' \
              '&series_type=open&apikey=' + api_key

        rt = RequestsTor()

        headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103'
        }

        r = rt.get(url, headers=headers)

        data = r.json()

        print(data)

    def test_EMA(self):
        print("test_EMA")

        # replace the "demo" apikey below with your own key from https://www.alphavantage.co/support/#api-key
        api_key = "demo"

        url = 'https://www.alphavantage.co/query?function=EMA&symbol=IBM&interval=weekly&time_period=10' \
              '&series_type=open&apikey=' + api_key

        rt = RequestsTor()

        headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103'
        }

        r = rt.get(url, headers=headers)

        data = r.json()

        print(data)

    def test_WMA(self):
        print("test_WMA")

        # replace the "demo" apikey below with your own key from https://www.alphavantage.co/support/#api-key
        api_key = "demo"

        url = 'https://www.alphavantage.co/query?function=WMA&symbol=IBM&interval=weekly&time_period=10' \
              '&series_type=open&apikey=' + api_key

        rt = RequestsTor()

        headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103'
        }

        r = rt.get(url, headers=headers)

        data = r.json()

        print(data)

    def test_DEMA(self):
        print("test_DEMA")

        # replace the "demo" apikey below with your own key from https://www.alphavantage.co/support/#api-key
        api_key = "demo"

        url = 'https://www.alphavantage.co/query?function=DEMA&symbol=IBM&interval=weekly' \
              '&time_period=10&series_type=open&apikey=' + api_key

        rt = RequestsTor()

        headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103'
        }

        r = rt.get(url, headers=headers)

        data = r.json()

        print(data)

    def test_TEMA(self):
        print('test_TEMA')

        # replace the "demo" apikey below with your own key from https://www.alphavantage.co/support/#api-key
        api_key = ""

        url = 'https://www.alphavantage.co/query?function=TEMA&symbol=IBM&interval=weekly&time_period=10' \
              '&series_type=open&apikey=' + api_key

        rt = RequestsTor()

        headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103'
        }

        r = rt.get(url, headers=headers)

        data = r.json()

        print(data)

    def test_TRIMA(self):
        print("test_TRIMA")

        # replace the "demo" apikey below with your own key from https://www.alphavantage.co/support/#api-key
        api_key = "demo"

        url = 'https://www.alphavantage.co/query?function=TRIMA&symbol=IBM&interval=weekly' \
              '&time_period=10&series_type=open&apikey=' + api_key

        rt = RequestsTor()

        headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103'
        }

        r = rt.get(url, headers=headers)

        data = r.json()

        print(data)

    def test_KAMA(self):
        print('')

        # replace the "demo" apikey below with your own key from https://www.alphavantage.co/support/#api-key
        api_key = "demo"

        url = 'https://www.alphavantage.co/query?function=KAMA&symbol=IBM&interval=weekly' \
              '&time_period=10&series_type=open&apikey=' + api_key

        rt = RequestsTor()

        headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103'
        }

        r = rt.get(url, headers=headers)

        data = r.json()

        print(data)

    def test_MAMA(self):
        print("test_MAMA")

        # replace the "demo" apikey below with your own key from https://www.alphavantage.co/support/#api-key
        api_key = "demo"

        url = 'https://www.alphavantage.co/query?function=MAMA&symbol=IBM&interval=daily' \
              '&series_type=close&fastlimit=0.02&apikey=' + api_key

        rt = RequestsTor()

        headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103'
        }

        r = rt.get(url, headers=headers)

        data = r.json()

        print(data)

    def test_VWAP(self):
        print("test_VWAP")

        # replace the "demo" apikey below with your own key from https://www.alphavantage.co/support/#api-key
        api_key = "demo"

        url = 'https://www.alphavantage.co/query?function=VWAP&symbol=IBM&interval=15min&apikey=' + api_key

        rt = RequestsTor()

        headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103'
        }

        r = rt.get(url, headers=headers)

        data = r.json()

        print(data)

    def test_T3(self):
        print("test_T3")

        # replace the "demo" apikey below with your own key from https://www.alphavantage.co/support/#api-key
        api_key = "demo"

        url = 'https://www.alphavantage.co/query?function=T3&symbol=IBM&interval=weekly' \
              '&time_period=10&series_type=open&apikey=' + api_key

        rt = RequestsTor()

        headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103'
        }

        r = rt.get(url, headers=headers)

        data = r.json()

        print(data)

    def test_MACD(self):
        print("test_MACD")

        # replace the "demo" apikey below with your own key from https://www.alphavantage.co/support/#api-key
        api_key = "demo"

        url = 'https://www.alphavantage.co/query?function=MACD&symbol=IBM' \
              '&interval=daily&series_type=open&apikey=' + api_key

        rt = RequestsTor()

        headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103'
        }

        r = rt.get(url, headers=headers)

        data = r.json()

        print(data)

    def test_MACDEXT(self):
        print("test_MACDEXT")

        # replace the "demo" apikey below with your own key from https://www.alphavantage.co/support/#api-key
        api_key = ""

        url = 'https://www.alphavantage.co/query?function=MACDEXT&symbol=IBM&interval=daily' \
              '&series_type=open&apikey=' + api_key

        rt = RequestsTor()

        headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103'
        }

        r = rt.get(url, headers=headers)

        data = r.json()

        print(data)

    def test_STOCH(self):
        print("test_STOCH")

        # replace the "demo" apikey below with your own key from https://www.alphavantage.co/support/#api-key
        api_key = "demo"

        url = 'https://www.alphavantage.co/query?function=STOCH&symbol=IBM&interval=daily&apikey=' + api_key

        rt = RequestsTor()

        headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103'
        }

        r = rt.get(url, headers=headers)

        data = r.json()

        print(data)

    def test_STOCHF(self):
        print("test_STOCHF")

        # replace the "demo" apikey below with your own key from https://www.alphavantage.co/support/#api-key
        api_key = "demo"

        url = 'https://www.alphavantage.co/query?function=STOCHF&symbol=IBM&interval=daily&apikey=' + api_key

        rt = RequestsTor()

        headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103'
        }

        r = rt.get(url, headers=headers)

        data = r.json()

        print(data)

    def test_RSI(self):
        print("test_RSI")

        # replace the "demo" apikey below with your own key from https://www.alphavantage.co/support/#api-key
        api_key = ""

        url = 'https://www.alphavantage.co/query?function=RSI&symbol=IBM&interval=weekly' \
              '&time_period=10&series_type=open&apikey=' + api_key

        rt = RequestsTor()

        headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103'
        }

        r = rt.get(url, headers=headers)

        data = r.json()

        print(data)

    def test_STOCHRSI(self):
        print("test_STOCHRSI")

        # replace the "demo" apikey below with your own key from https://www.alphavantage.co/support/#api-key
        api_key = "demo"

        url = 'https://www.alphavantage.co/query?function=STOCHRSI&symbol=IBM&interval=daily' \
              '&time_period=10&series_type=close&fastkperiod=6&fastdmatype=1&apikey=' + api_key

        rt = RequestsTor()

        headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103'
        }

        r = rt.get(url, headers=headers)

        data = r.json()

        print(data)

    def test_WILLR(self):
        print("test_WILLR")

        # replace the "demo" apikey below with your own key from https://www.alphavantage.co/support/#api-key
        api_key = "demo"

        url = 'https://www.alphavantage.co/query?function=WILLR' \
              '&symbol=IBM&interval=daily&time_period=10&apikey=' + api_key

        rt = RequestsTor()

        headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103'
        }

        r = rt.get(url, headers=headers)

        data = r.json()

        print(data)

    def test_ADX(self):
        print("test_ADX")

        # replace the "demo" apikey below with your own key from https://www.alphavantage.co/support/#api-key
        api_key = "demo"

        url = 'https://www.alphavantage.co/query?function=ADX&symbol=IBM' \
              '&interval=daily&time_period=10&apikey=' + api_key

        rt = RequestsTor()

        headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103'
        }

        r = rt.get(url, headers=headers)

        data = r.json()

        print(data)

    def test_ADXR(self):
        print("test_ADXR")

        # replace the "demo" apikey below with your own key from https://www.alphavantage.co/support/#api-key
        api_key = "demo"

        url = 'https://www.alphavantage.co/query?function=ADXR&symbol=IBM' \
              '&interval=daily&time_period=10&apikey=' + api_key

        rt = RequestsTor()

        headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103'
        }

        r = rt.get(url, headers=headers)

        data = r.json()

        print(data)

    def test_APO(self):
        print("test_APO")

        # replace the "demo" apikey below with your own key from https://www.alphavantage.co/support/#api-key
        api_kay = "demo"

        url = 'https://www.alphavantage.co/query?function=APO&symbol=IBM&interval=daily' \
              '&series_type=close&fastperiod=10&matype=1&apikey=' + api_kay

        rt = RequestsTor()

        headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103'
        }

        r = rt.get(url, headers=headers)

        data = r.json()

        print(data)

    def test_PPO(self):
        print("test_PPO")

        # replace the "demo" apikey below with your own key from https://www.alphavantage.co/support/#api-key
        api_key = "demo"

        url = 'https://www.alphavantage.co/query?function=PPO&symbol=IBM&interval=daily' \
              '&series_type=close&fastperiod=10&matype=1&apikey=' + api_key

        rt = RequestsTor()

        headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103'
        }

        r = rt.get(url, headers=headers)

        data = r.json()

        print(data)

    def test_MOM(self):
        print("test_MOM")

        # replace the "demo" apikey below with your own key from https://www.alphavantage.co/support/#api-key
        api_key = ""

        url = 'https://www.alphavantage.co/query?function=MOM&symbol=IBM&interval=daily' \
              '&time_period=10&series_type=close&apikey=' + api_key

        rt = RequestsTor()

        headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103'
        }

        r = rt.get(url, headers=headers)

        data = r.json()

        print(data)

    def test_BOP(self):
        print('test_BOP')

        # replace the "demo" apikey below with your own key from https://www.alphavantage.co/support/#api-key
        api_key = "demo"

        url = 'https://www.alphavantage.co/query?function=BOP&symbol=IBM&interval=daily&apikey=' + api_key

        rt = RequestsTor()

        headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103'
        }

        r = rt.get(url, headers=headers)

        data = r.json()

        print(data)

    def test_CCI(self):
        print("test_CCI")

        # replace the "demo" apikey below with your own key from https://www.alphavantage.co/support/#api-key
        api_key = ""

        url = 'https://www.alphavantage.co/query?function=CCI' \
              '&symbol=IBM&interval=daily&time_period=10&apikey=' + api_key

        rt = RequestsTor()

        headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103'
        }

        r = rt.get(url, headers=headers)

        data = r.json()

        print(data)

    def test_CMO(self):
        print('test_CMO')

        # replace the "demo" apikey below with your own key from https://www.alphavantage.co/support/#api-key
        api_key = ""

        url = 'https://www.alphavantage.co/query?function=CMO&symbol=IBM&interval=weekly' \
              '&time_period=10&series_type=close&apikey=' + api_key

        rt = RequestsTor()

        headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103'
        }

        r = rt.get(url, headers=headers)

        data = r.json()

        print(data)

    def test_ROC(self):
        print('test_ROC')

        # replace the "demo" apikey below with your own key from https://www.alphavantage.co/support/#api-key
        api_key = "demo"

        url = 'https://www.alphavantage.co/query?function=ROC&symbol=IBM' \
              '&interval=weekly&time_period=10&series_type=close&apikey=' + api_key

        rt = RequestsTor()

        headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103'
        }

        r = rt.get(url, headers=headers)

        data = r.json()

        print(data)

    def test_ROCR(self):
        print("test_ROCR")

        # replace the "demo" apikey below with your own key from https://www.alphavantage.co/support/#api-key
        api_key = "demo"

        url = 'https://www.alphavantage.co/query?function=ROCR&symbol=IBM&interval=daily' \
              '&time_period=10&series_type=close&apikey=' + api_key

        rt = RequestsTor()

        headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103'
        }

        r = rt.get(url, headers=headers)

        data = r.json()

        print(data)

    def test_AROON(self):
        print('test_AROON')

        # replace the "demo" apikey below with your own key from https://www.alphavantage.co/support/#api-key
        api_key = "demo"

        url = 'https://www.alphavantage.co/query?function=AROON&symbol=IBM' \
              '&interval=daily&time_period=14&apikey=' + api_key

        rt = RequestsTor()

        headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103'
        }

        r = rt.get(url, headers=headers)

        data = r.json()

        print(data)

    def test_AROONOSC(self):
        print("test_AROONOSC")

        # replace the "demo" apikey below with your own key from https://www.alphavantage.co/support/#api-key
        api_key = "demo"

        url = 'https://www.alphavantage.co/query?function=AROONOSC&symbol=IBM&interval=daily' \
              '&time_period=10&apikey=' + api_key

        rt = RequestsTor()

        headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103'
        }

        r = rt.get(url, headers=headers)

        data = r.json()

        print(data)

    def test_MFI(self):
        print("test_MFI")

        # replace the "demo" apikey below with your own key from https://www.alphavantage.co/support/#api-key
        api_key = "demo"

        url = 'https://www.alphavantage.co/query?function=MFI' \
              '&symbol=IBM&interval=weekly&time_period=10&apikey=' + api_key

        rt = RequestsTor()

        headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103'
        }

        r = rt.get(url, headers=headers)

        data = r.json()

        print(data)

    def test_TRIX(self):
        print("test_TRIX")

        # replace the "demo" apikey below with your own key from https://www.alphavantage.co/support/#api-key
        api_key = "demo"

        url = 'https://www.alphavantage.co/query?function=TRIX&symbol=IBM' \
              '&interval=daily&time_period=10&series_type=close&apikey=' + api_key

        rt = RequestsTor()

        headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103'
        }

        r = rt.get(url, headers=headers)

        data = r.json()

        print(data)

    def test_ULTOSC(self):
        print("test_ULTOSC")

        # replace the "demo" apikey below with your own key from https://www.alphavantage.co/support/#api-key
        api_key = "demo"

        url = 'https://www.alphavantage.co/query?function=ULTOSC&symbol=IBM' \
              '&interval=daily&timeperiod1=8&apikey=' + api_key

        rt = RequestsTor()

        headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103'
        }

        r = rt.get(url, headers=headers)

        data = r.json()

        print(data)

    def test_DX(self):
        print('test_DX')

        # replace the "demo" apikey below with your own key from https://www.alphavantage.co/support/#api-key
        api_key = "demo"

        url = 'https://www.alphavantage.co/query?function=DX&symbol=IBM&interval=daily&time_period=10&apikey=' + api_key

        rt = RequestsTor()

        headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103'
        }

        r = rt.get(url, headers=headers)

        data = r.json()

        print(data)

    def test_MINUS_DI(self):
        print("test_MINUS_DI")

        # replace the "demo" apikey below with your own key from https://www.alphavantage.co/support/#api-key
        api_key = 'demo'

        url = 'https://www.alphavantage.co/query?function=MINUS_DI&symbol=IBM' \
              '&interval=weekly&time_period=10&apikey=' + api_key

        rt = RequestsTor()

        headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103'
        }

        r = rt.get(url, headers=headers)

        data = r.json()

        print(data)

    def test_PLUS_DI(self):
        print('test_PLUS_DI')

        # replace the "demo" apikey below with your own key from https://www.alphavantage.co/support/#api-key
        api_key = ""

        url = 'https://www.alphavantage.co/query?function=PLUS_DI&symbol=IBM' \
              '&interval=daily&time_period=10&apikey=' + api_key

        rt = RequestsTor()

        headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103'
        }

        r = rt.get(url, headers=headers)

        data = r.json()

        print(data)

    def test_MINUS_DM(self):
        print('test_MINUS_DM')

        # replace the "demo" apikey below with your own key from https://www.alphavantage.co/support/#api-key
        api_key = "demo"

        url = 'https://www.alphavantage.co/query?function=MINUS_DM&symbol=IBM' \
              '&interval=daily&time_period=10&apikey=' + api_key

        rt = RequestsTor()

        headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103'
        }

        r = rt.get(url, headers=headers)

        data = r.json()

        print(data)

    def test_PLUS_DM(self):
        print("test_PLUS_DM")

        # replace the "demo" apikey below with your own key from https://www.alphavantage.co/support/#api-key
        api_key = "demo"

        url = 'https://www.alphavantage.co/query?function=PLUS_DM&symbol=IBM' \
              '&interval=daily&time_period=10&apikey=' + api_key

        rt = RequestsTor()

        headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103'
        }

        r = rt.get(url, headers=headers)

        data = r.json()

        print(data)

    def test_BBANDS(self):
        print('test_BBANDS')

        # replace the "demo" apikey below with your own key from https://www.alphavantage.co/support/#api-key
        api_key = "demo"

        url = 'https://www.alphavantage.co/query?function=BBANDS&symbol=IBM&interval=weekly' \
              '&time_period=5&series_type=close&nbdevup=3&nbdevdn=3&apikey=' + api_key

        rt = RequestsTor()

        headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103'
        }

        r = rt.get(url, headers=headers)

        data = r.json()

        print(data)

    def test_MIDPOINT(self):
        print('test_MIDPOINT')

        # replace the "demo" apikey below with your own key from https://www.alphavantage.co/support/#api-key
        api_key = "demo"

        url = 'https://www.alphavantage.co/query?function=MIDPOINT&symbol=IBM&interval=daily' \
              '&time_period=10&series_type=close&apikey=' + api_key

        rt = RequestsTor()

        headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103'
        }

        r = rt.get(url, headers=headers)

        data = r.json()

        print(data)

    def test_MIDPRICE(self):
        print("test_MIDPRICE")

        # replace the "demo" apikey below with your own key from https://www.alphavantage.co/support/#api-key
        api_key = "demo"

        url = 'https://www.alphavantage.co/query?function=MIDPRICE&symbol=IBM' \
              '&interval=daily&time_period=10&apikey=' + api_key

        rt = RequestsTor()

        headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103'
        }

        r = rt.get(url, headers=headers)

        data = r.json()

        print(data)

    def test_SAR(self):
        print("test_SAR")

        # replace the "demo" apikey below with your own key from https://www.alphavantage.co/support/#api-key
        api_key = "demo"

        url = 'https://www.alphavantage.co/query?function=SAR&symbol=IBM&interval=weekly' \
              '&acceleration=0.05&maximum=0.25&apikey=' + api_key

        rt = RequestsTor()

        headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103'
        }

        r = rt.get(url, headers=headers)

        data = r.json()

        print(data)

    def test_TRANGE(self):
        print("test_TRANGE")

        # replace the "demo" apikey below with your own key from https://www.alphavantage.co/support/#api-key
        api_key = "demo"

        url = 'https://www.alphavantage.co/query?function=TRANGE&symbol=IBM&interval=daily&apikey=' + api_key

        rt = RequestsTor()

        headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103'
        }

        r = rt.get(url, headers=headers)

        data = r.json()

        print(data)

    def test_ATR(self):
        print("test_ATR")

        # replace the "demo" apikey below with your own key from https://www.alphavantage.co/support/#api-key
        api_key = "demo"

        url = 'https://www.alphavantage.co/query?function=ATR&symbol=IBM' \
              '&interval=daily&time_period=14&apikey=' + api_key

        rt = RequestsTor()

        headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103'
        }

        r = rt.get(url, headers=headers)

        data = r.json()

        print(data)

    def test_NATR(self):
        print("test_NATR")

        # replace the "demo" apikey below with your own key from https://www.alphavantage.co/support/#api-key
        api_key = "demo"

        url = 'https://www.alphavantage.co/query?function=NATR&symbol=IBM' \
              '&interval=weekly&time_period=14&apikey=' + api_key

        rt = RequestsTor()

        headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103'
        }

        r = rt.get(url, headers=headers)

        data = r.json()

        print(data)

    def test_AD(self):
        print("test_AD")

        # replace the "demo" apikey below with your own key from https://www.alphavantage.co/support/#api-key
        api_key = "demo"

        url = 'https://www.alphavantage.co/query?function=AD&symbol=IBM&interval=daily&apikey=demo'

        rt = RequestsTor()

        headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103'
        }

        r = rt.get(url, headers=headers)

        data = r.json()

        print(data)

    def test_ADOSC(self):
        print("test_ADOSC")

        # replace the "demo" apikey below with your own key from https://www.alphavantage.co/support/#api-key
        api_key = "demo"

        url = 'https://www.alphavantage.co/query?function=ADOSC' \
              '&symbol=IBM&interval=daily&fastperiod=5&apikey=' + api_key

        rt = RequestsTor()

        headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103'
        }

        r = rt.get(url, headers=headers)

        data = r.json()

        print(data)

    def test_OBV(self):
        print("test_OBV")

        # replace the "demo" apikey below with your own key from https://www.alphavantage.co/support/#api-key
        api_key = "demo"

        url = 'https://www.alphavantage.co/query?function=OBV&symbol=IBM&interval=weekly&apikey=' + api_key

        rt = RequestsTor()

        headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103'
        }

        r = rt.get(url, headers=headers)

        data = r.json()

        print(data)

    def test_HT_TRENDLINE(self):
        print("test_HT_TRENDLINE")

        # replace the "demo" apikey below with your own key from https://www.alphavantage.co/support/#api-key
        api_key = "demo"

        url = 'https://www.alphavantage.co/query?function=HT_TRENDLINE&symbol=IBM&interval=daily' \
              '&series_type=close&apikey=' + api_key

        rt = RequestsTor()

        headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103'
        }

        r = rt.get(url, headers=headers)

        data = r.json()

        print(data)

    def test_HT_SINE(self):
        print("test_HT_SINE")

        # replace the "demo" apikey below with your own key from https://www.alphavantage.co/support/#api-key
        api_key = "demo"

        url = 'https://www.alphavantage.co/query?function=HT_SINE&symbol=IBM' \
              '&interval=daily&series_type=close&apikey=' + api_key

        rt = RequestsTor()

        headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103'
        }

        r = rt.get(url, headers=headers)

        data = r.json()

        print(data)

    def test_HT_TRENDMODE(self):
        print("test_HT_TRENDMODE")

        # replace the "demo" apikey below with your own key from https://www.alphavantage.co/support/#api-key
        api_key = "demo"

        url = 'https://www.alphavantage.co/query?function=HT_TRENDMODE&symbol=IBM' \
              '&interval=weekly&series_type=close&apikey=' + api_key

        rt = RequestsTor()

        headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103'
        }

        r = rt.get(url, headers=headers)

        data = r.json()

        print(data)

    def test_HT_DCPERIOD(self):
        print("test_HT_DCPERIOD")

        # replace the "demo" apikey below with your own key from https://www.alphavantage.co/support/#api-key
        api_key = "demo"

        url = 'https://www.alphavantage.co/query?function=HT_DCPERIOD&symbol=IBM' \
              '&interval=daily&series_type=close&apikey=' + api_key

        rt = RequestsTor()

        headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103'
        }

        r = rt.get(url, headers=headers)

        data = r.json()

        print(data)

    def test_HT_DCPHASE(self):
        print("test_HT_DCPHASE")

        # replace the "demo" apikey below with your own key from https://www.alphavantage.co/support/#api-key
        api_key = "demo"

        url = 'https://www.alphavantage.co/query?function=HT_DCPHASE&symbol=IBM' \
              '&interval=daily&series_type=close&apikey=' + api_key

        rt = RequestsTor()

        headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103'
        }

        r = rt.get(url, headers=headers)

        data = r.json()

        print(data)

    def test_HT_PHASOR(self):
        print('test_HT_PHASOR')

        # replace the "demo" apikey below with your own key from https://www.alphavantage.co/support/#api-key
        api_key = "demo"

        url = 'https://www.alphavantage.co/query?function=HT_PHASOR&symbol=IBM' \
              '&interval=weekly&series_type=close&apikey=' + api_key

        rt = RequestsTor()

        headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103'
        }

        r = rt.get(url, headers=headers)

        data = r.json()

        print(data)


if __name__ == '__main__':
    unittest.main()
