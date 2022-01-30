import unittest
import requests


class UnitTests7Timer(unittest.TestCase):
    def test_get_the_weather(self):
        print('test_get_the_weather')

        lon = "2.3522219"

        lat = "48.856614"

        ac = "0"

        lang = ""

        unit = "Metric"

        output = "json"

        product = "civil"

        tzshift = "0"

        url = "http://www.7timer.info/bin/api.pl?lon=" + lon \
              + "&lat=" + lat \
              + "&ac=" + ac \
              + "&unit=" + unit \
              + "&product=" + product \
              + "&tzshift=" + tzshift \
              + "&output=" + output

        response = requests.request("GET", url)

        dataseries = response.json()["dataseries"]

        print('length dataseries : ' + str(len(dataseries)))

        print(response.text)


if __name__ == '__main__':
    unittest.main()
