import json
import unittest
import requests


# https://htmlpreview.github.io/?https://github.com/wpgp/wopr/blob/master/doc/woprAPI.html
class UnitTestsWoprApi(unittest.TestCase):
    # Data Catalogue
    # https://wopr.worldpop.org/api/v1.0/data
    def test_data_catalogue(self):
        print('test_data_catalogue')

        url = "https://wopr.worldpop.org/api/v1.0/data"

        response = requests.request("GET", url)

        print(json.loads(response.text))

    # Spatial Queries
    # https://api.worldpop.org/v1/wopr/pointtotal
    def test_spatial_queries_point_total(self):
        print('test_spatial_queries_point_total')

        url = "https://api.worldpop.org/v1/wopr/pointtotal?iso3=NGA&ver=1.2&lat=11.53579&lon=4.850808"

        response_url = requests.request("GET", url)

        taskid = json.loads(response_url.text)['taskid']

        url_task = "https://api.worldpop.org/v1/tasks/" + taskid

        response_url_task = requests.request("GET", url_task)

        print(json.loads(response_url_task.text))

    # https://api.worldpop.org/v1/wopr/pointagesex
    def test_spatial_queries_point_age_sex(self):
        print('test_spatial_queries_point_age_sex')

        url = "https://api.worldpop.org/v1/wopr/pointagesex?iso3=NGA&ver=1.2&lat=11.53579" \
              "&lon=4.850808&agesex=m0,m1,f0,f1"

        response_url = requests.request("GET", url)

        taskid = json.loads(response_url.text)['taskid']

        url_task = "https://api.worldpop.org/v1/tasks/" + taskid

        response_url_task = requests.request("GET", url_task)

        print(json.loads(response_url_task.text))

    # https://api.worldpop.org/v1/wopr/polytotal
    def test_polygon_based_total_population(self):
        print('test_polygon_based_total_population')

        url = 'https://api.worldpop.org/v1/wopr/polytotal?iso3=NGA&ver=1.2&geojson=' \
              '{"type":"FeatureCollection","features":[{"type":"Feature","properties":{},' \
              '"geometry":{"type":"Polygon","coordinates":[[[3.2080078125,7.0027636819827475],' \
              '[3.7902832031250004,7.0027636819827475],[3.7902832031250004,7.612997502224103],' \
              '[3.2080078125,7.612997502224103],[3.2080078125,7.0027636819827475]]]}}]}'

        response_url = requests.request("GET", url)

        taskid = json.loads(response_url.text)['taskid']

        url_task = "https://api.worldpop.org/v1/tasks/" + taskid

        response_url_task = requests.request("GET", url_task)

        print(json.loads(response_url_task.text))

    # https://api.worldpop.org/v1/wopr/polyagesex
    def test_polygon_based_population_for_specific_age_sex_group(self):
        print('test_polygon_based_population_for_specific_age_sex_group')

        url = 'https://api.worldpop.org/v1/wopr/polyagesex?iso3=NGA&ver=1.2&agesex=m0,m1,f0,' \
              'f1&geojson={"type":"FeatureCollection","features":[{"type":"Feature",' \
              '"properties":{},"geometry":{"type":"Polygon","coordinates":' \
              '[[[3.2080078125,7.0027636819827475],[3.7902832031250004,7.0027636819827475],' \
              '[3.7902832031250004,7.612997502224103],[3.2080078125,7.612997502224103],' \
              '[3.2080078125,7.0027636819827475]]]}}]}'

        response_url = requests.request("GET", url)

        taskid = json.loads(response_url.text)['taskid']

        url_task = "https://api.worldpop.org/v1/tasks/" + taskid

        response_url_task = requests.request("GET", url_task)

        print(json.loads(response_url_task.text))


if __name__ == '__main__':
    unittest.main()
