import unittest
import requests


class UnitTestsGeoNamesAPI(unittest.TestCase):
    # astergdem
    def test_astergdem(self):
        lat = "50.01"
        lng = "10.2"
        username = ""
        url = "http://api.geonames.org/astergdem?lat=" \
              + lat \
              + "&lng=" + lng \
              + "&username=" + username
        payload = {}
        headers = {}
        response = requests.request("GET", url, headers=headers, data=payload)
        print(response.text.encode('utf8'))

    def test_astergdem_xml(self):
        lat = "50.01"
        lng = "10.2"
        username = ""
        url = "http://api.geonames.org/astergdemXML?lat=" \
              + lat \
              + "&lng=" + lng \
              + "&username=" + username
        payload = {}
        headers = {}
        response = requests.request("GET", url, headers=headers, data=payload)
        print(response.text.encode('utf8'))

    def test_astergdem_json(self):
        lat = "50.01"
        lng = "10.2"
        username = ""
        url = "http://api.geonames.org/astergdemJSON?lat=" \
              + lat \
              + "&lng=" + lng \
              + "&username=" + username
        payload = {}
        headers = {}
        response = requests.request("GET", url, headers=headers, data=payload)
        print(response.text.encode('utf8'))
    # astergdem

    # children
    def test_children(self):
        geonameId = "3175395"
        username = ""
        url = "http://api.geonames.org/children?geonameId=" \
              + geonameId \
              + "&username=" + username
        payload = {}
        headers = {}
        response = requests.request("GET", url, headers=headers, data=payload)
        print(response.text.encode('utf8'))

    def test_children_json(self):
        geonameId = "3175395"
        username = ""
        url = "http://api.geonames.org/childrenJSON?geonameId=" \
              + geonameId \
              + "&username=" + username
        payload = {}
        headers = {}
        response = requests.request("GET", url, headers=headers, data=payload)
        print(response.text.encode('utf8'))

    def test_children_hierarchy(self):
        geonameId = "3175395"
        username = ""
        hierarchy = "tourism"
        url = "http://api.geonames.org/children?geonameId=" + geonameId \
              + "&username=" + username \
              + "&hierarchy=" + hierarchy
        payload = {}
        headers = {}
        response = requests.request("GET", url, headers=headers, data=payload)
        print(response.text.encode('utf8'))

    def test_children_hierarchy_json(self):
        geonameId = "3175395"
        username = ""
        hierarchy = "tourism"
        url = "http://api.geonames.org/childrenJSON?geonameId=" + geonameId \
              + "&username=" + username \
              + "&hierarchy=" + hierarchy
        payload = {}
        headers = {}
        response = requests.request("GET", url, headers=headers, data=payload)
        print(response.text.encode('utf8'))
    # children

    # contains
    def test_contains(self):
        geonameId = "2746385&"
        username = ""
        url = "http://api.geonames.org/contains?geonameId=" + geonameId + "&username=" + username
        payload = {}
        headers = {}
        response = requests.request("GET", url, headers=headers, data=payload)
        print(response.text.encode('utf8'))

    def test_contains_json(self):
        geonameId = "2746385&"
        username = ""
        url = "http://api.geonames.org/containsJSON?geonameId=" + geonameId + "&username=" + username
        payload = {}
        headers = {}
        response = requests.request("GET", url, headers=headers, data=payload)
        print(response.text.encode('utf8'))
    # contains

    # countryCode
    def test_countryCode(self):
        username = ""
        lat = "47.03"
        lng = "10.2"
        url = "http://api.geonames.org/countryCode?lat=" + lat + "&lng=" + lng + "&username=" + username
        payload = {}
        headers = {}
        response = requests.request("GET", url, headers=headers, data=payload)
        print(response.text.encode('utf8'))

    def test_countryCode_json(self):
        username = ""
        lat = "47.03"
        lng = "10.2"
        url = "http://api.geonames.org/countryCodeJSON?lat=" + lat + "&lng=" + lng + "&username=" + username
        payload = {}
        headers = {}
        response = requests.request("GET", url, headers=headers, data=payload)
        print(response.text.encode('utf8'))
    # countryCode

    # countryInfo
    def test_countryInfo(self):
        username = ""
        url = "http://api.geonames.org/countryInfo?username=" + username
        payload = {}
        headers = {}
        response = requests.request("GET", url, headers=headers, data=payload)
        print(response.text.encode('utf8'))

    def test_countryInfo_csv(self):
        username = ""
        lang = "it"
        country = "DE"
        url = "http://api.geonames.org/countryInfoCSV?lang=" + lang + "&country=" + country + "&username=" + username
        payload = {}
        headers = {}
        response = requests.request("GET", url, headers=headers, data=payload)
        print(response.text.encode('utf8'))

    def test_countryInfo_json(self):
        username = ""
        lang = "it"
        country = "DE"
        url = " http://api.geonames.org/countryInfoJSON?lang=" + lang + "&country=" + country + "&username=" + username
        payload = {}
        headers = {}
        response = requests.request("GET", url, headers=headers, data=payload)
        print(response.text.encode('utf8'))
    # countryInfo

    # countrySubdivision
    def test_countrySubdivision(self):
        username = ""
        lat = "47.03"
        lng = "10.2"
        url = "http://api.geonames.org/countrySubdivision?lat=" + lat + "&lng=" + lng + "&username=" + username
        payload = {}
        headers = {}
        response = requests.request("GET", url, headers=headers, data=payload)
        print(response.text.encode('utf8'))

    def test_countrySubdivision_lat_lng_maxRows_radius(self):
        username = ""
        lat = "47.03"
        lng = "10.2"
        maxRows = "10"
        radius = "40"
        url = "http://api.geonames.org/countrySubdivision?lat=" + lat \
              + "&lng=" + lng \
              + "&maxRows=" + maxRows \
              + "&radius=" + radius \
              + "&username=" + username
        payload = {}
        headers = {}
        response = requests.request("GET", url, headers=headers, data=payload)
        print(response.text.encode('utf8'))

    def test_countrySubdivision_json(self):
        username = ""
        lat = "47.03"
        lng = "10.2"
        url = "http://api.geonames.org/countrySubdivisionJSON?lat=" + lat + "&lng=" + lng + "&username=" + username
        payload = {}
        headers = {}
        response = requests.request("GET", url, headers=headers, data=payload)
        print(response.text.encode('utf8'))
    # countrySubdivision

    # earthquakes
    def test_earthquakes_json(self):
        username = ""
        north = "44.1"
        south = "-9.9"
        east = "-22.4"
        west = "55.2"
        url = "http://api.geonames.org/earthquakesJSON?north=" + north \
              + "&south=" + south \
              + "&east=" + east \
              + "&west=" + west \
              + "&username=" + username
        payload = {}
        headers = {}
        response = requests.request("GET", url, headers=headers, data=payload)
        print(response.text.encode('utf8'))

    def test_earthquakes(self):
        username = ""
        north = "44.1"
        south = "-9.9"
        east = "-22.4"
        west = "55.2"
        url = "http://api.geonames.org/earthquakes?north=" + north \
              + "&south=" + south \
              + "&east=" + east \
              + "&west=" + west \
              + "&username=" + username
        payload = {}
        headers = {}
        response = requests.request("GET", url, headers=headers, data=payload)
        print(response.text.encode('utf8'))
    # earthquakes

    # extendedFindNearby
    def test_extendedFindNearby(self):
        username = ""
        lat = "47.3"
        lng = "9"
        url = "http://api.geonames.org/extendedFindNearby?lat=" + lat \
              + "&lng=" + lng \
              + "&username=" + username
        payload = {}
        headers = {}
        response = requests.request("GET", url, headers=headers, data=payload)
        print(response.text.encode('utf8'))

    def test_extendedFindNearby_json(self):
        username = ""
        lat = "47.3"
        lng = "9"
        url = "http://api.geonames.org/extendedFindNearbyJSON?lat=" + lat + "&lng=" + lng + "&username=" + username
        payload = {}
        headers = {}
        response = requests.request("GET", url, headers=headers, data=payload)
        print(response.text.encode('utf8'))
    # extendedFindNearby

    # findNearby
    def test_findNearby(self):
        username = ""
        lat = "47.3"
        lng = "9"
        url = "http://api.geonames.org/findNearby?lat=" + lat + "&lng=" + lng + "&username=" + username
        payload = {}
        headers = {}
        response = requests.request("GET", url, headers=headers, data=payload)
        print(response.text.encode('utf8'))

    def test_findNearby_json(self):
        username = ""
        lat = "47.3"
        lng = "9"
        url = "http://api.geonames.org/findNearbyJSON?lat=" + lat + "&lng=" + lng + "&username=" + username
        payload = {}
        headers = {}
        response = requests.request("GET", url, headers=headers, data=payload)
        print(response.text.encode('utf8'))
    # findNearby

    # findNearbyPlaceName
    def test_findNearbyPlaceName(self):
        username = ""
        lat = "47.3"
        lng = "9"
        url = "http://api.geonames.org/findNearbyPlaceName?lat=" + lat + "&lng=" + lng + "&username=" + username
        payload = {}
        headers = {}
        response = requests.request("GET", url, headers=headers, data=payload)
        print(response.text.encode('utf8'))

    def test_findNearbyPlaceName_json(self):
        username = ""
        lat = "47.3"
        lng = "9"
        url = "http://api.geonames.org/findNearbyPlaceNameJSON?lat=" + lat + "&lng=" + lng + "&username=" + username
        payload = {}
        headers = {}
        response = requests.request("GET", url, headers=headers, data=payload)
        print(response.text.encode('utf8'))
    # findNearbyPlaceName

    # findNearbyPostalCodes
    def test_findNearbyPostalCodes(self):
        username = ""
        lat = "47"
        lng = "9"
        url = "http://api.geonames.org/findNearbyPostalCodes?lat=" + lat + "&lng=" + lng + "&username=" + username
        payload = {}
        headers = {}
        response = requests.request("GET", url, headers=headers, data=payload)
        print(response.text.encode('utf8'))

    def test_findNearbyPostalCodes_postalcode_country_radius_username(self):
        username = ""
        postalcode = "8775"
        country = "CH"
        radius = "10"
        url = "http://api.geonames.org/findNearbyPostalCodes?postalcode=" + postalcode \
              + "&country=" + country \
              + "&radius=" + radius \
              + "&username=" + username
        payload = {}
        headers = {}
        response = requests.request("GET", url, headers=headers, data=payload)
        print(response.text.encode('utf8'))

    def test_findNearbyPostalCodes_json(self):
        username = ""
        postalcode = "8775"
        country = "CH"
        radius = "10"
        url = "http://api.geonames.org/findNearbyPostalCodesJSON?postalcode=" + postalcode \
              + "&country=" + country \
              + "&radius=" + radius \
              + "&username=" + username
        payload = {}
        headers = {}
        response = requests.request("GET", url, headers=headers, data=payload)
        print(response.text.encode('utf8'))
    # findNearbyPostalCodes

    # findNearbyStreets_usa
    def test_findNearbyStreets_usa(self):
        username = ""
        lat = "37.451"
        lng = "-122.18"
        url = "http://api.geonames.org/findNearbyStreets?lat=" + lat \
              + "&lng=" + lng \
              + "&username=" + username
        payload = {}
        headers = {}
        response = requests.request("GET", url, headers=headers, data=payload)
        print(response.text.encode('utf8'))

    def test_findNearbyStreets_usa_json(self):
        username = ""
        lat = "37.451"
        lng = "-122.18"
        url = "http://api.geonames.org/findNearbyStreetsJSON?lat=" + lat \
              + "&lng=" + lng \
              + "&username=" + username
        payload = {}
        headers = {}
        response = requests.request("GET", url, headers=headers, data=payload)
        print(response.text.encode('utf8'))
    # findNearbyStreets_usa

    # findNearbyStreetsOSM
    def test_findNearbyStreetsOSM(self):
        username = ""
        lat = "37.451"
        lng = "-122.18"
        url = "http://api.geonames.org/findNearbyStreetsOSM?lat=" + lat \
              + "&lng=" + lng \
              + "&username=" + username
        payload = {}
        headers = {}
        response = requests.request("GET", url, headers=headers, data=payload)
        print(response.text.encode('utf8'))

    def test_findNearbyStreetsOSM_json(self):
        username = ""
        lat = "37.451"
        lng = "-122.18"
        url = "http://api.geonames.org/findNearbyStreetsJSON?lat=" + lat \
              + "&lng=" + lng \
              + "&username=" + username
        payload = {}
        headers = {}
        response = requests.request("GET", url, headers=headers, data=payload)
        print(response.text.encode('utf8'))
    # findNearbyStreetsOSM

    # findNearByWeather
    def test_findNearByWeather_xml(self):
        username = ""
        lat = "37.451"
        lng = "-122.18"
        url = "http://api.geonames.org/findNearByWeatherXML?lat=" + lat \
              + "&lng=" + lng \
              + "&username=" + username
        payload = {}
        headers = {}
        response = requests.request("GET", url, headers=headers, data=payload)
        print(response.text.encode('utf8'))

    def test_findNearByWeather_json(self):
        username = ""
        lat = "37.451"
        lng = "-122.18"
        url = "http://api.geonames.org/findNearByWeatherJSON?" \
              + "lat=" + lat \
              + "&lng=" + lng \
              + "&username=" + username
        payload = {}
        headers = {}
        response = requests.request("GET", url, headers=headers, data=payload)
        print(response.text.encode('utf8'))
    # findNearByWeather

    # findNearbyWikipedia
    def test_findNearbyWikipedia_lat_lng_xml(self):
        username = ""
        lat = "47"
        lng = "9"
        url = "http://api.geonames.org/findNearbyWikipedia?lat=" + lat + "&lng=" + lng + "&username=" + username
        payload = {}
        headers = {}
        response = requests.request("GET", url, headers=headers, data=payload)
        print(response.text.encode('utf8'))

    def test_findNearbyWikipedia_lat_lng_json(self):
        username = ""
        lat = "47"
        lng = "9"
        url = "http://api.geonames.org/findNearbyWikipediaJSON?lat=" + lat \
              + "&lng=" + lng \
              + "&username=" + username
        payload = {}
        headers = {}
        response = requests.request("GET", url, headers=headers, data=payload)
        print(response.text.encode('utf8'))

    def test_findNearbyWikipedia_postalcode_country_radius_xml(self):
        username = ""
        postalcode = "8775"
        country = "CH"
        radius = "10"
        url = "http://api.geonames.org/findNearbyWikipedia?postalcode=" + postalcode \
              + "&country=" + country \
              + "&radius=" + radius \
              + "&username=" + username
        payload = {}
        headers = {}
        response = requests.request("GET", url, headers=headers, data=payload)
        print(response.text.encode('utf8'))

    def test_findNearbyWikipedia_postalcode_country_radius_json(self):
        username = ""
        postalcode = "8775"
        country = "CH"
        radius = "10"
        url = "http://api.geonames.org/findNearbyWikipediaJSON?postalcode=" + postalcode \
              + "&country=" + country \
              + "&radius=" + radius \
              + "&username=" + username
        payload = {}
        headers = {}
        response = requests.request("GET", url, headers=headers, data=payload)
        print(response.text.encode('utf8'))
    # findNearbyWikipedia

    # Cities
    def test_cities_north_south_east_west(self):
        username = ""
        north = "44.1"
        south = "-9.9"
        east = "-22.4"
        west = "55.2"
        url = "http://api.geonames.org/cities?north=" + north \
              + "&south=" + south \
              + "&east=" + east \
              + "&west=" + west\
              + "&username=" + username
        payload = {}
        headers = {}
        response = requests.request("GET", url, headers=headers, data=payload)
        print(response.text.encode('utf8'))

    def test_cities_north_south_east_west_json(self):
        username = ""
        north = "44.1"
        south = "-9.9"
        east = "-22.4"
        west = "55.2"
        url = "http://api.geonames.org/citiesJSON?north=" + north \
              + "&south=" + south \
              + "&east=" + east \
              + "&west=" + west\
              + "&username=" + username
        payload = {}
        headers = {}
        response = requests.request("GET", url, headers=headers, data=payload)
        print(response.text.encode('utf8'))
    # Cities

    # findNearestAddress_usa
    def test_findNearestAddress_usa_lat_lng(self):
        username = ""
        lat = "37.451"
        lng = "-122.18"
        url = "http://api.geonames.org/findNearestAddress?lat=" + lat \
              + "&lng=" + lng \
              + "&username=" + username
        payload = {}
        headers = {}
        response = requests.request("GET", url, headers=headers, data=payload)
        print(response.text.encode('utf8'))

    def test_findNearestAddress_usa_lat_lng_json(self):
        username = ""
        lat = "37.451"
        lng = "-122.18"
        url = "http://api.geonames.org/findNearestAddressJSON?lat=" + lat \
              + "&lng=" + lng \
              + "&username=" + username
        payload = {}
        headers = {}
        response = requests.request("GET", url, headers=headers, data=payload)
        print(response.text.encode('utf8'))
    # findNearestAddress_usa

    # findNearestIntersection_usa
    def test_findNearestIntersection_usa_lat_lng(self):
        username = ""
        lat = "37.451"
        lng = "-122.18"
        url = "http://api.geonames.org/findNearestIntersection?lat=" + lat \
              + "&lng=" + lng \
              + "&username=" + username
        payload = {}
        headers = {}
        response = requests.request("GET", url, headers=headers, data=payload)
        print(response.text.encode('utf8'))

    def test_findNearestIntersection_usa_lat_lng_json(self):
        username = ""
        lat = "37.451"
        lng = "-122.18"
        url = "http://api.geonames.org/findNearestIntersectionJSON?lat=" + lat \
              + "&lng=" + lng \
              + "&username=" + username
        payload = {}
        headers = {}
        response = requests.request("GET", url, headers=headers, data=payload)
        print(response.text.encode('utf8'))
    # findNearestIntersection_usa

    # findNearestIntersectionOSM
    def test_findNearestIntersectionOSM_lat_lng(self):
        username = ""
        lat = "37.451"
        lng = "-122.18"
        url = "http://api.geonames.org/findNearestIntersectionOSM?lat=" + lat \
              + "&lng=" + lng\
              + "&username=" + username
        payload = {}
        headers = {}
        response = requests.request("GET", url, headers=headers, data=payload)
        print(response.text.encode('utf8'))

    def test_findNearestIntersectionOSM_lat_lng_json(self):
        username = ""
        lat = "37.451"
        lng = "-122.18"
        url = "http://api.geonames.org/findNearestIntersectionOSMJSON?lat=" + lat \
              + "&lng=" + lng\
              + "&username=" + username
        payload = {}
        headers = {}
        response = requests.request("GET", url, headers=headers, data=payload)
        print(response.text.encode('utf8'))
    # findNearestIntersectionOSM

    # findNearbyPOIsOSM
    def test_findNearbyPOIsOSM_lat_lng(self):
        username = ""
        lat = "37.451"
        lng = "-122.18"
        url = "http://api.geonames.org/findNearbyPOIsOSM?lat=" + lat \
              + "&lng=" + lng\
              + "&username=" + username
        payload = {}
        headers = {}
        response = requests.request("GET", url, headers=headers, data=payload)
        print(response.text.encode('utf8'))

    def test_findNearbyPOIsOSM_lat_lng_json(self):
        username = ""
        lat = "37.451"
        lng = "-122.18"
        url = "http://api.geonames.org/findNearbyPOIsOSMJSON?lat=" + lat \
              + "&lng=" + lng\
              + "&username=" + username
        payload = {}
        headers = {}
        response = requests.request("GET", url, headers=headers, data=payload)
        print(response.text.encode('utf8'))
    # findNearbyPOIsOSM

    # address
    def test_address_lat_lng(self):
        username = ""
        lat = "52.3545828"
        lng = "4.7638761"
        url = "http://api.geonames.org/address?lat=" + lat \
              + "&lng=" + lng \
              + "&username=" + username
        payload = {}
        headers = {}
        response = requests.request("GET", url, headers=headers, data=payload)
        print(response.text.encode('utf8'))

    def test_address_lat_lng_json(self):
        username = ""
        lat = "52.3545828"
        lng = "4.7638761"
        url = "http://api.geonames.org/addressJSON?lat=" + lat \
              + "&lng=" + lng \
              + "&username=" + username
        payload = {}
        headers = {}
        response = requests.request("GET", url, headers=headers, data=payload)
        print(response.text.encode('utf8'))
    # address

    # geoCodeAddress
    def test_geoCodeAddress(self):
        username = ""
        q = "Museumplein+6+amsterdam"
        url = "http://api.geonames.org/geoCodeAddress?q=" + q \
              + "&username=" + username
        payload = {}
        headers = {}
        response = requests.request("GET", url, headers=headers, data=payload)
        print(response.text.encode('utf8'))

    def test_geoCodeAddress_json(self):
        username = ""
        q = "Museumplein+6+amsterdam"
        url = "http://api.geonames.org/geoCodeAddressJSON?q=" + q \
              + "&username=" + username
        payload = {}
        headers = {}
        response = requests.request("GET", url, headers=headers, data=payload)
        print(response.text.encode('utf8'))

    def test_geoCodeAddress_json_for_latitude(self):
        print('test_geoCodeAddress_json_for_latitude')

        username = ""
        q = "Museumplein+6+amsterdam"
        url = "http://api.geonames.org/geoCodeAddressJSON?q=" + q \
              + "&username=" + username
        payload = {}
        headers = {}
        response = requests.request("GET", url, headers=headers, data=payload)
        latitude = str(response.json()['address']['lat'])
        print("latitude : " + latitude)

    def test_geoCodeAddress_json_for_longitude(self):
        print('test_geoCodeAddress_json_for_longitude')

        username = ""
        q = ""
        url = "http://api.geonames.org/geoCodeAddressJSON?q=" + q \
              + "&username=" + username
        payload = {}
        headers = {}
        response = requests.request("GET", url, headers=headers, data=payload)
        longitude = str(response.json()['address']['lng'])
        print("longitude : " + longitude)

    # streetNameLookup
    def test_streetNameLookup(self):
        username = ""
        q = "Museum"
        url = "http://api.geonames.org/streetNameLookup?q=" + q + "&username=" + username
        payload = {}
        headers = {}
        response = requests.request("GET", url, headers=headers, data=payload)
        print(response.text.encode('utf8'))

    def test_streetNameLookup_json(self):
        username = ""
        q = "Museum"
        url = "http://api.geonames.org/streetNameLookupJSON?q=" + q + "&username=" + username
        payload = {}
        headers = {}
        response = requests.request("GET", url, headers=headers, data=payload)
        print(response.text.encode('utf8'))
    # streetNameLookup

    # get
    def test_get(self):
        username = ""
        geonameId = "1"
        url = "http://api.geonames.org/get?geonameId=" + geonameId \
              + "&username=" + username
        payload = {}
        headers = {}
        response = requests.request("GET", url, headers=headers, data=payload)
        print(response.text.encode('utf8'))
    # get

    # gtopo30
    def test_gtopo30(self):
        username = ""
        lat = "47.01"
        lng = "10.2"
        url = "http://api.geonames.org/gtopo30?lat=" + lat \
              + "&lng=" + lng \
              + "&username=" + username
        payload = {}
        headers = {}
        response = requests.request("GET", url, headers=headers, data=payload)
        print(response.text.encode('utf8'))

    def test_gtopo30_json(self):
        username = ""
        lat = "47.01"
        lng = "10.2"
        url = "http://api.geonames.org/gtopo30JSON?lat=" + lat \
              + "&lng=" + lng \
              + "&username=" + username
        payload = {}
        headers = {}
        response = requests.request("GET", url, headers=headers, data=payload)
        print(response.text.encode('utf8'))
    # gtopo30

    # hierarchy
    def test_hierarchy(self):
        username = ""
        geonameId = "2657896"
        url = "http://api.geonames.org/hierarchy?geonameId=" + geonameId \
              + "&username=" + username
        payload = {}
        headers = {}
        response = requests.request("GET", url, headers=headers, data=payload)
        print(response.text.encode('utf8'))

    def test_hierarchy_json(self):
        username = ""
        geonameId = "2657896"
        url = "http://api.geonames.org/hierarchyJSON?geonameId=" + geonameId \
              + "&username=" + username
        payload = {}
        headers = {}
        response = requests.request("GET", url, headers=headers, data=payload)
        print(response.text.encode('utf8'))
    # hierarchy

    # neighbourhood_usa
    def test_neighbourhood_usa(self):
        username = ""
        lat = "40.78343"
        lng = "-73.96625"
        url = "http://api.geonames.org/neighbourhood?lat=" + lat \
              + "&lng=" + lng \
              + "&username=" + username
        payload = {}
        headers = {}
        response = requests.request("GET", url, headers=headers, data=payload)
        print(response.text.encode('utf8'))

    def test_neighbourhood_usa_json(self):
        username = ""
        lat = "40.78343"
        lng = "-73.96625"
        url = "http://api.geonames.org/neighbourhoodJSON?lat=" + lat \
              + "&lng=" + lng \
              + "&username=" + username
        payload = {}
        headers = {}
        response = requests.request("GET", url, headers=headers, data=payload)
        print(response.text.encode('utf8'))
    # neighbourhood_usa

    # neighbours
    def test_neighbours(self):
        username = ""
        geonameId = "2658434"
        url = "http://api.geonames.org/neighbours?geonameId=" + geonameId \
              + "&username=" + username
        payload = {}
        headers = {}
        response = requests.request("GET", url, headers=headers, data=payload)
        print(response.text.encode('utf8'))

    def test_neighbours_json(self):
        username = ""
        geonameId = "2658434"
        url = "http://api.geonames.org/neighboursJSON?geonameId=" + geonameId \
              + "&username=" + username
        payload = {}
        headers = {}
        response = requests.request("GET", url, headers=headers, data=payload)
        print(response.text.encode('utf8'))
    # neighbours

    # ocean
    def test_ocean(self):
        username = ""
        lat = "40.78343"
        lng = "-43.96625"
        url = "http://api.geonames.org/ocean?lat=" + lat \
              + "&lng=" + lng \
              + "&username=" + username
        payload = {}
        headers = {}
        response = requests.request("GET", url, headers=headers, data=payload)
        print(response.text.encode('utf8'))

    def test_ocean_json(self):
        username = ""
        lat = "40.78343"
        lng = "-43.96625"
        url = "http://api.geonames.org/oceanJSON?lat=" + lat \
              + "&lng=" + lng \
              + "&username=" + username
        payload = {}
        headers = {}
        response = requests.request("GET", url, headers=headers, data=payload)
        print(response.text.encode('utf8'))
    # ocean

    # postalCodeCountryInfo
    def test_postalCodeCountryInfo(self):
        username = ""
        url = "http://api.geonames.org/postalCodeCountryInfo?username=" + username
        payload = {}
        headers = {}
        response = requests.request("GET", url, headers=headers, data=payload)
        print(response.text.encode('utf8'))

    def test_postalCodeCountryInfo_json(self):
        username = ""
        url = "http://api.geonames.org/postalCodeCountryInfoJSON?username=" + username
        payload = {}
        headers = {}
        response = requests.request("GET", url, headers=headers, data=payload)
        print(response.text.encode('utf8'))
    # postalCodeCountryInfo

    # postalCodeLookup
    def test_postalCodeLookup_json(self):
        username = ""
        url = "http://api.geonames.org/postalCodeLookupJSON?postalcode=6600&country=AT&username=" + username
        payload = {}
        headers = {}
        response = requests.request("GET", url, headers=headers, data=payload)
        print(response.text.encode('utf8'))
    # postalCodeLookup

    # postalCodeSearch
    def test_postalCodeSearch(self):
        username = ""
        postalcode = "9011"
        maxRows = "10"
        url = "http://api.geonames.org/postalCodeSearch?postalcode=" + postalcode \
              + "&maxRows=" + maxRows \
              + "&username=" + username
        payload = {}
        headers = {}
        response = requests.request("GET", url, headers=headers, data=payload)
        print(response.text.encode('utf8'))

    def test_postalCodeSearch_json(self):
        username = ""
        postalcode = "9011"
        maxRows = "10"
        url = "http://api.geonames.org/postalCodeSearchJSON?postalcode=" + postalcode \
              + "&maxRows=" + maxRows \
              + "&username=" + username
        payload = {}
        headers = {}
        response = requests.request("GET", url, headers=headers, data=payload)
        print(response.text.encode('utf8'))
    # postalCodeSearch

    # rssToGeo
    def test_rssToGeo(self):
        username = ""
        feedUrl = "http://feeds.reuters.com/reuters/worldNews"
        url = "http://api.geonames.org/rssToGeoRSS?feedUrl=" + feedUrl \
              + "&username=" + username
        payload = {}
        headers = {}
        response = requests.request("GET", url, headers=headers, data=payload)
        print(response.text.encode('utf8'))
    # rssToGeo

    # search
    def test_search(self):
        username = ""
        q = "london"
        maxRows = "10"
        url = "http://api.geonames.org/search?q=" + q \
              + "&maxRows=" + maxRows \
              + "&username=" + username
        payload = {}
        headers = {}
        response = requests.request("GET", url, headers=headers, data=payload)
        print(response.text.encode('utf8'))

    def test_search_json(self):
        username = ""
        q = "london"
        maxRows = "10"
        url = "http://api.geonames.org/searchJSON?q=" + q \
              + "&maxRows=" + maxRows \
              + "&username=" + username
        payload = {}
        headers = {}
        response = requests.request("GET", url, headers=headers, data=payload)
        print(response.text.encode('utf8'))
    # search

    # siblings
    def test_siblings(self):
        username = ""
        geonameId = "3017382"
        url = "http://api.geonames.org/siblings?geonameId=" + geonameId \
              + "&username=" + username
        payload = {}
        headers = {}
        response = requests.request("GET", url, headers=headers, data=payload)
        print(response.text.encode('utf8'))

    def test_siblings_json(self):
        username = ""
        geonameId = "3017382"
        url = "http://api.geonames.org/siblingsJSON?geonameId=" + geonameId \
              + "&username=" + username
        payload = {}
        headers = {}
        response = requests.request("GET", url, headers=headers, data=payload)
        print(response.text.encode('utf8'))
    # siblings

    # srtm1
    def test_srtm1(self):
        username = ""
        lat = "50.01"
        lng = "10.2"
        url = "http://api.geonames.org/srtm1?lat=" + lat \
              + "&lng=" + lng \
              + "&username=" + username
        payload = {}
        headers = {}
        response = requests.request("GET", url, headers=headers, data=payload)
        print(response.text.encode('utf8'))

    def test_srtm1_xml(self):
        username = ""
        lat = "50.01"
        lng = "10.2"
        url = "http://api.geonames.org/srtm1XML?lat=" + lat \
              + "&lng=" + lng \
              + "&username=" + username
        payload = {}
        headers = {}
        response = requests.request("GET", url, headers=headers, data=payload)
        print(response.text.encode('utf8'))

    def test_srtm1_json(self):
        username = ""
        lat = "50.01"
        lng = "10.2"
        url = "http://api.geonames.org/srtm1JSON?lat=" + lat \
              + "&lng=" + lng \
              + "&username=" + username
        payload = {}
        headers = {}
        response = requests.request("GET", url, headers=headers, data=payload)
        print(response.text.encode('utf8'))

    def test_srtm1_lats_lngs(self):
        username = ""
        lats = "50.01,51.01"
        lngs = "10.2,11.2"
        url = "http://api.geonames.org/srtm1?lats=" + lats \
              + "&lngs=" + lngs\
              + "&username=" + username
        payload = {}
        headers = {}
        response = requests.request("GET", url, headers=headers, data=payload)
        print(response.text.encode('utf8'))
    # srtm1

    # srtm3
    def test_srtm3(self):
        lats = "50.01,51.01"
        lngs = "10.2,11.2"
        username = ""
        url = "http://api.geonames.org/srtm3?lats=" \
              + lats \
              + "&lngs=" + lngs \
              + "&username=" + username
        payload = {}
        headers = {}
        response = requests.request("GET", url, headers=headers, data=payload)
        print(response.text.encode('utf8'))

    def test_srtm3_xml(self):
        lats = "50.01,51.01"
        lngs = "10.2,11.2"
        username = ""
        url = "http://api.geonames.org/srtm3XML?lats=" \
              + lats \
              + "&lngs=" + lngs \
              + "&username=" + username
        payload = {}
        headers = {}
        response = requests.request("GET", url, headers=headers, data=payload)
        print(response.text.encode('utf8'))

    def test_srtm3_json(self):
        lats = "50.01,51.01"
        lngs = "10.2,11.2"
        username = ""
        url = "http://api.geonames.org/srtm3JSON?lats=" \
              + lats \
              + "&lngs=" + lngs \
              + "&username=" + username
        payload = {}
        headers = {}
        response = requests.request("GET", url, headers=headers, data=payload)
        print(response.text.encode('utf8'))
    # srtm3

    # timezone
    def test_timezone_lat_lng(self):
        username = ""
        lat = "47.01"
        lng = "10.2"
        url = "http://api.geonames.org/timezone?lat=" + lat \
              + "&lng=" + lng\
              + "&username=" + username
        payload = {}
        headers = {}
        response = requests.request("GET", url, headers=headers, data=payload)
        print(response.text.encode('utf8'))

    def test_timezone_lat_lng_json(self):
        username = ""
        lat = "47.01"
        lng = "10.2"
        url = "http://api.geonames.org/timezoneJSON?lat=" + lat \
              + "&lng=" + lng\
              + "&username=" + username
        payload = {}
        headers = {}
        response = requests.request("GET", url, headers=headers, data=payload)
        print(response.text.encode('utf8'))
    # timezone

    # weather
    def test_weather_north_south_east_west_xml(self):
        username = ""
        north = "44.1"
        south = "-9.9"
        east = "-22.4"
        west = "55.2"
        url = "http://api.geonames.org/weatherXML?north=" + north\
              + "&south=" + south \
              + "&east=" + east \
              + "&west=" + west \
              + "&username=" + username
        payload = {}
        headers = {}
        response = requests.request("GET", url, headers=headers, data=payload)
        print(response.text.encode('utf8'))

    def test_weather_north_south_east_west_json(self):
        username = ""
        north = "44.1"
        south = "-9.9"
        east = "-22.4"
        west = "55.2"
        url = "http://api.geonames.org/weatherJSON?north=" + north\
              + "&south=" + south \
              + "&east=" + east \
              + "&west=" + west \
              + "&username=" + username
        payload = {}
        headers = {}
        response = requests.request("GET", url, headers=headers, data=payload)
        print(response.text.encode('utf8'))
    # weather

    # weatherIcao
    def test_weatherIcao_ICAO_json(self):
        username = ""
        ICAO = "LSZH"
        url = "http://api.geonames.org/weatherIcaoJSON?ICAO=" + ICAO \
              + "&username=" + username
        payload = {}
        headers = {}
        response = requests.request("GET", url, headers=headers, data=payload)
        print(response.text.encode('utf8'))

    def test_weatherIcao_ICAO_xml(self):
        username = ""
        ICAO = "LSZH"
        url = "http://api.geonames.org/weatherIcaoXML?ICAO=" + ICAO \
              + "&username=" + username
        payload = {}
        headers = {}
        response = requests.request("GET", url, headers=headers, data=payload)
        print(response.text.encode('utf8'))
    # weatherIcao

    # wikipediaBoundingBox
    def test_wikipediaBoundingBox(self):
        username = ""
        north = "44.1"
        south = "-9.9"
        east = "-22.4"
        west = "55.2"
        url = "http://api.geonames.org/wikipediaBoundingBox?north=" + north \
              + "&south=" + south \
              + "&east=" + east \
              + "&west=" + west \
              + "&username=" + username
        payload = {}
        headers = {}
        response = requests.request("GET", url, headers=headers, data=payload)
        print(response.text.encode('utf8'))

    def test_wikipediaBoundingBoxJSON(self):
        username = ""
        north = "44.1"
        south = "-9.9"
        east = "-22.4"
        west = "55.2"
        url = "http://api.geonames.org/wikipediaBoundingBoxJSON?north=" + north \
              + "&south=" + south \
              + "&east=" + east \
              + "&west=" + west \
              + "&username=" + username
        payload = {}
        headers = {}
        response = requests.request("GET", url, headers=headers, data=payload)
        print(response.text.encode('utf8'))
    # wikipediaBoundingBox

    # wikipediaSearch
    def test_wikipediaSearch_xml(self):
        username = ""
        q = "london"
        maxRows = "10"
        url = "http://api.geonames.org/wikipediaSearch?q=" + q \
              + "&maxRows=" + maxRows \
              + "&username=" + username
        payload = {}
        headers = {}
        response = requests.request("GET", url, headers=headers, data=payload)
        print(response.text.encode('utf8'))

    def test_wikipediaSearch_json(self):
        username = ""
        q = "london"
        maxRows = "10"
        url = "http://api.geonames.org/wikipediaSearchJSON?q=" + q \
              + "&maxRows=" + maxRows \
              + "&username=" + username
        payload = {}
        headers = {}
        response = requests.request("GET", url, headers=headers, data=payload)
        print(response.text.encode('utf8'))
    # wikipediaSearch


if __name__ == '__main__':
    unittest.main()
