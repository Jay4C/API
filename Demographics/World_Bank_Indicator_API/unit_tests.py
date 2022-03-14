import unittest
import requests


class UnitTestsWorldBankCountryAPIQueries(unittest.TestCase):
    # Country API Queries
    # XML
    def test_all_country_xml(self):
        url = "https://api.worldbank.org/v2/country"
        payload = {}
        headers = {}
        response = requests.request("GET", url, headers=headers, data=payload)
        print(response.text.encode('utf8'))

    def test_country_xml(self):
        iso_code = "br"
        url = "https://api.worldbank.org/v2/country/" + iso_code
        payload = {}
        headers = {}
        response = requests.request("GET", url, headers=headers, data=payload)
        print(response.text.encode('utf8'))
    # XML

    # JSON
    def test_all_country_json(self):
        url = "https://api.worldbank.org/v2/country?format=json"
        payload = {}
        headers = {}
        response = requests.request("GET", url, headers=headers, data=payload)
        print(response.text.encode('utf8'))

    def test_country_json(self):
        iso_code = "br"
        url = "https://api.worldbank.org/v2/country/" + iso_code + "?format=json"
        payload = {}
        headers = {}
        response = requests.request("GET", url, headers=headers, data=payload)
        print(response.text.encode('utf8'))
    # JSON
    # Country API Queries


class UnitTestsWorldBankAggregateAPIQueries(unittest.TestCase):
    # Aggregate API Queries
    # XML
    def test_list_for_all_region_codes_xml(self):
        url = "https://api.worldbank.org/v2/region?format=xml"
        payload = {}
        headers = {}
        response = requests.request("GET", url, headers=headers, data=payload)
        print(response.text.encode('utf8'))

    def test_list_of_all_income_level_code_xml(self):
        url = "https://api.worldbank.org/v2/incomelevel"
        payload = {}
        headers = {}
        response = requests.request("GET", url, headers=headers, data=payload)
        print(response.text.encode('utf8'))

    def test_list_of_all_lending_type_code_xml(self):
        url = "https://api.worldbank.org/v2/lendingtypes"
        payload = {}
        headers = {}
        response = requests.request("GET", url, headers=headers, data=payload)
        print(response.text.encode('utf8'))

    def test_list_of_definitions_for_specific_region_xml(self):
        specific_region_code = "LCN"
        url = "https://api.worldbank.org/v2/region/LCN" + specific_region_code
        payload = {}
        headers = {}
        response = requests.request("GET", url, headers=headers, data=payload)
        print(response.text.encode('utf8'))

    def test_list_of_definitions_for_income_levels_xml(self):
        specific_income_level = "UMC"
        url = "https://api.worldbank.org/v2/incomelevel/" + specific_income_level
        payload = {}
        headers = {}
        response = requests.request("GET", url, headers=headers, data=payload)
        print(response.text.encode('utf8'))

    def test_list_of_definitions_for_lending_types_xml(self):
        specific_lending_types = "IBD;IDB"
        url = "https://api.worldbank.org/v2/lendingtype/" + specific_lending_types
        payload = {}
        headers = {}
        response = requests.request("GET", url, headers=headers, data=payload)
        print(response.text.encode('utf8'))

    def test_country_which_aggregate_groups_xml(self):
        specific_country_code = "BRA"
        url = "https://api.worldbank.org/v2/country/" + specific_country_code
        payload = {}
        headers = {}
        response = requests.request("GET", url, headers=headers, data=payload)
        print(response.text.encode('utf8'))

    def test_filter_to_see_all_countries_in_a_specified_region_xml(self):
        specific_region = "LCN"
        url = "https://api.worldbank.org/v2/country?region=" + specific_region
        payload = {}
        headers = {}
        response = requests.request("GET", url, headers=headers, data=payload)
        print(response.text.encode('utf8'))

    def test_filter_to_see_all_countries_in_a_specified_income_level_xml(self):
        specific_icome_level = "UMC"
        url = "https://api.worldbank.org/v2/country?incomelevel=" + specific_icome_level
        payload = {}
        headers = {}
        response = requests.request("GET", url, headers=headers, data=payload)
        print(response.text.encode('utf8'))

    def test_filter_to_see_all_countries_in_a_specified_lendingtype_xml(self):
        specific_lending_type = "IBD"
        url = "https://api.worldbank.org/v2/country?lendingtype=" + specific_lending_type
        payload = {}
        headers = {}
        response = requests.request("GET", url, headers=headers, data=payload)
        print(response.text.encode('utf8'))
    # XML

    # JSON
    def test_list_for_all_region_codes_json(self):
        url = "https://api.worldbank.org/v2/region?format=json"
        payload = {}
        headers = {}
        response = requests.request("GET", url, headers=headers, data=payload)
        print(response.text.encode('utf8'))

    def test_list_of_all_income_level_code_json(self):
        url = "https://api.worldbank.org/v2/incomelevel?format=json"
        payload = {}
        headers = {}
        response = requests.request("GET", url, headers=headers, data=payload)
        print(response.text.encode('utf8'))

    def test_list_of_all_lending_type_code_json(self):
        url = "https://api.worldbank.org/v2/lendingtypes?format=json"
        payload = {}
        headers = {}
        response = requests.request("GET", url, headers=headers, data=payload)
        print(response.text.encode('utf8'))

    def test_list_of_definitions_for_specific_region_json(self):
        specific_region_code = "LCN"
        url = "https://api.worldbank.org/v2/region/" + specific_region_code + "?format=json"
        payload = {}
        headers = {}
        response = requests.request("GET", url, headers=headers, data=payload)
        print(response.text.encode('utf8'))

    def test_list_of_definitions_for_income_levels_json(self):
        specific_income_level = "UMC"
        url = "https://api.worldbank.org/v2/incomelevel/" + specific_income_level + "?format=json"
        payload = {}
        headers = {}
        response = requests.request("GET", url, headers=headers, data=payload)
        print(response.text.encode('utf8'))

    def test_list_of_definitions_for_lending_types_json(self):
        specific_lending_types = "IBD;IDB"
        url = "https://api.worldbank.org/v2/lendingtype/" + specific_lending_types + "?format=json"
        payload = {}
        headers = {}
        response = requests.request("GET", url, headers=headers, data=payload)
        print(response.text.encode('utf8'))

    def test_country_which_aggregate_groups_json(self):
        specific_country_code = "BRA"
        url = "https://api.worldbank.org/v2/country/" + specific_country_code + "?format=json"
        payload = {}
        headers = {}
        response = requests.request("GET", url, headers=headers, data=payload)
        print(response.text.encode('utf8'))

    def test_filter_to_see_all_countries_in_a_specified_region_json(self):
        specific_region = "LCN"
        url = "https://api.worldbank.org/v2/country?region=" + specific_region + "&format=json"
        payload = {}
        headers = {}
        response = requests.request("GET", url, headers=headers, data=payload)
        print(response.text.encode('utf8'))

    def test_filter_to_see_all_countries_in_a_specified_income_level_json(self):
        specific_icome_level = "UMC"
        url = "https://api.worldbank.org/v2/country?incomelevel=" + specific_icome_level + "&format=json"
        payload = {}
        headers = {}
        response = requests.request("GET", url, headers=headers, data=payload)
        print(response.text.encode('utf8'))

    def test_filter_to_see_all_countries_in_a_specified_lendingtype_json(self):
        specific_lending_type = "IBD"
        url = "https://api.worldbank.org/v2/country?lendingtype=" + specific_lending_type + "&format=json"
        payload = {}
        headers = {}
        response = requests.request("GET", url, headers=headers, data=payload)
        print(response.text.encode('utf8'))
    # JSON
    # Aggregate API Queries


class UnitTestsWorldBankIndicatorAPIQueries(unittest.TestCase):
    # Indicator API Queries
    # XML
    def test_indicator_xml(self):
        url = "http://api.worldbank.org/v2/indicator"
        payload = {}
        headers = {}
        response = requests.request("GET", url, headers=headers, data=payload)
        print(response.text.encode('utf8'))

    def test_indicators_xml(self):
        url = "http://api.worldbank.org/v2/indicators"
        payload = {}
        headers = {}
        response = requests.request("GET", url, headers=headers, data=payload)
        print(response.text.encode('utf8'))

    def test_specific_indicator_xml(self):
        url = "http://api.worldbank.org/v2/indicator/NY.GDP.MKTP.CD"
        payload = {}
        headers = {}
        response = requests.request("GET", url, headers=headers, data=payload)
        print(response.text.encode('utf8'))

    def test_indicator_with_source_xml(self):
        source = "11"
        url = "http://api.worldbank.org/v2/indicator/NY.GDP.MKTP.CD?source=" + source
        payload = {}
        headers = {}
        response = requests.request("GET", url, headers=headers, data=payload)
        print(response.text.encode('utf8'))
    # XML

    # JSON
    def test_indicator_json(self):
        url = "http://api.worldbank.org/v2/indicator?format=json"
        payload = {}
        headers = {}
        response = requests.request("GET", url, headers=headers, data=payload)
        print(response.text.encode('utf8'))

    def test_specific_indicator_json(self):
        url = "http://api.worldbank.org/v2/indicator/NY.GDP.MKTP.CD?format=json"
        payload = {}
        headers = {}
        response = requests.request("GET", url, headers=headers, data=payload)
        print(response.text.encode('utf8'))

    def test_specific_indicators_json(self):
        url = "http://api.worldbank.org/v2/indicators/NY.GDP.MKTP.CD?format=json"
        payload = {}
        headers = {}
        response = requests.request("GET", url, headers=headers, data=payload)
        print(response.text.encode('utf8'))
    # JSON
    # Indicator API Queries


class UnitTestsWorldBankTopicAPIQueries(unittest.TestCase):
    # Topic API Queries
    # XML
    def test_topics_xml(self):
        url = "http://api.worldbank.org/v2/topics"
        payload = {}
        headers = {}
        response = requests.request("GET", url, headers=headers, data=payload)
        print(response.text.encode('utf8'))

    def test_specific_topic_xml(self):
        topic = "5"
        url = "http://api.worldbank.org/v2/topic/" + topic
        payload = {}
        headers = {}
        response = requests.request("GET", url, headers=headers, data=payload)
        print(response.text.encode('utf8'))

    def test_multiple_specific_topics_xml(self):
        topics = "5;11"
        url = "http://api.worldbank.org/v2/topic/" + topics
        payload = {}
        headers = {}
        response = requests.request("GET", url, headers=headers, data=payload)
        print(response.text.encode('utf8'))

    def test_indicator_with_specific_topic_xml(self):
        url = "http://api.worldbank.org/v2/indicator?topic=5"
        payload = {}
        headers = {}
        response = requests.request("GET", url, headers=headers, data=payload)
        print(response.text.encode('utf8'))
    # XML

    # JSON
    def test_topics_json(self):
        url = "http://api.worldbank.org/v2/topic?format=json"
        payload = {}
        headers = {}
        response = requests.request("GET", url, headers=headers, data=payload)
        print(response.text.encode('utf8'))
    # JSON
    # Topic API Queries


class UnitTestsWorldBankAdvancedDataAPIQueries(unittest.TestCase):
    # Advanced Data API Queries
    # Source Queries
    # XML
    def test_source_xml(self):
        url = "http://api.worldbank.org/v2/source"
        payload = {}
        headers = {}
        response = requests.request("GET", url, headers=headers, data=payload)
        print(response.text.encode('utf8'))

    def test_specific_source_xml(self):
        source = "2"
        url = "http://api.worldbank.org/v2/source/" + source
        payload = {}
        headers = {}
        response = requests.request("GET", url, headers=headers, data=payload)
        print(response.text.encode('utf8'))
    # XML
    # Source Queries

    # Concept Variables Queries
    # JSON
    def test_concept_specific_source_country_data_json(self):
        source = "2"
        url = "http://api.worldbank.org/v2/sources/" + source + "/country/data?format=json"
        payload = {}
        headers = {}
        response = requests.request("GET", url, headers=headers, data=payload)
        print(response.text.encode('utf8'))
    # JSON
    # Concept Variables Queries

    # Advanced Data Queries
    # XML
    def test_advanced_data_queries_source_country_series_time_version_xml(self):
        source = "57"
        country = "ALB"
        series = "AG"
        time = "yr1975"
        version = "199704"
        url = "http://api.worldbank.org/v2" + \
              "/sources/" + source \
              + "/country/" + country \
              + "/series/" + series \
              + "/time/" + time \
              + "/version/" + version + "/data?format=xml"
        payload = {}
        headers = {}
        response = requests.request("GET", url, headers=headers, data=payload)
        print(response.text.encode('utf8'))
    # XML

    # JSON
    def test_advanced_data_queries_source_country_series_time_version_json(self):
        url = "http://api.worldbank.org/v2/sources/57/country/ALB/series/AG.AGR.TRAC.NO" \
              "/time/all/version/199704/data?format=json"
        payload = {}
        headers = {}
        response = requests.request("GET", url, headers=headers, data=payload)
        print(response.text.encode('utf8'))
    # JSON
    # Advanced Data Queries

    # JSON-stat Queries (BETA)
    def test_json_stat_queries_json(self):
        url = "http://api.worldbank.org/v2/sources/57/country/ALB/series/AG.AGR.TRAC.NO" \
              "/time/all/version/199704/data?format=jsonstat"
        payload = {}
        headers = {}
        response = requests.request("GET", url, headers=headers, data=payload)
        print(response.text.encode('utf8'))
    # JSON-stat Queries (BETA)
    # Advanced Data API Queries

    # Metadata API Queries
    # About Metadata Queries
    # XML
    def test_metadata_api_queries_about_metadata_queries_sources_search_xml(self):
        url = "http://api.worldbank.org/v2/sources/2/search/solid%20fuel"
        payload = {}
        headers = {}
        response = requests.request("GET", url, headers=headers, data=payload)
        print(response.text.encode('utf8'))
    # XML

    # JSON
    def test_metadata_api_queries_about_metadata_queries_sources_search_json(self):
        url = "http://api.worldbank.org/v2/sources/2/search/solid%20fuel?format=json"
        payload = {}
        headers = {}
        response = requests.request("GET", url, headers=headers, data=payload)
        print(response.text.encode('utf8'))
    # JSON
    # About Metadata Queries

    # Source Queries
    # XML
    def test_metadata_api_queries_source_queries_sources_xml(self):
        url = "http://api.worldbank.org/v2/sources"
        payload = {}
        headers = {}
        response = requests.request("GET", url, headers=headers, data=payload)
        print(response.text.encode('utf8'))

    def test_metadata_api_queries_source_queries_sources_id_xml(self):
        url = "http://api.worldbank.org/v2/sources/2"
        payload = {}
        headers = {}
        response = requests.request("GET", url, headers=headers, data=payload)
        print(response.text.encode('utf8'))
    # XML

    # JSON
    def test_metadata_api_queries_source_queries_sources_json(self):
        url = "http://api.worldbank.org/v2/sources?format=json"
        payload = {}
        headers = {}
        response = requests.request("GET", url, headers=headers, data=payload)
        print(response.text.encode('utf8'))

    def test_metadata_api_queries_source_queries_sources_id_json(self):
        url = "http://api.worldbank.org/v2/sources/2?format=json"
        payload = {}
        headers = {}
        response = requests.request("GET", url, headers=headers, data=payload)
        print(response.text.encode('utf8'))
    # JSON
    # Source Queries

    # Concept Queries
    # XML
    def test__metadata_api_queries__concept_queries__source_id_concepts_xml(self):
        url = "http://api.worldbank.org/v2/sources/2/concepts"
        payload = {}
        headers = {}
        response = requests.request("GET", url, headers=headers, data=payload)
        print(response.text.encode('utf8'))

    def test__metadata_api_queries__concept_queries__source_id_concepts_metadata_xml(self):
        url = "http://api.worldbank.org/v2/sources/2/concepts/metadata"
        payload = {}
        headers = {}
        response = requests.request("GET", url, headers=headers, data=payload)
        print(response.text.encode('utf8'))

    def test__metadata_api_queries__concept_queries__source_id_concepts_country_metadata_xml(self):
        url = "http://api.worldbank.org/v2/sources/2/concepts/country/metadata"
        payload = {}
        headers = {}
        response = requests.request("GET", url, headers=headers, data=payload)
        print(response.text.encode('utf8'))
    # XML

    # JSON
    def test__metadata_api_queries__concept_queries__source_id_concepts_json(self):
        url = "http://api.worldbank.org/v2/sources/2/concepts?format=json"
        payload = {}
        headers = {}
        response = requests.request("GET", url, headers=headers, data=payload)
        print(response.text.encode('utf8'))

    def test__metadata_api_queries__concept_queries__source_id_concepts_metadata_json(self):
        url = "http://api.worldbank.org/v2/sources/2/concepts/metadata?format=json"
        payload = {}
        headers = {}
        response = requests.request("GET", url, headers=headers, data=payload)
        print(response.text.encode('utf8'))

    def test__metadata_api_queries__concept_queries__source_id_concepts_country_metadata_json(self):
        url = "http://api.worldbank.org/v2/sources/2/concepts/country/metadata?format=json"
        payload = {}
        headers = {}
        response = requests.request("GET", url, headers=headers, data=payload)
        print(response.text.encode('utf8'))
    # JSON
    # Concept Queries

    # Metatype Queries
    # XML
    def test__metadata_api_queries__metatype_queries__source_id_metatypes_xml(self):
        url = "http://api.worldbank.org/v2/sources/2/metatypes"
        payload = {}
        headers = {}
        response = requests.request("GET", url, headers=headers, data=payload)
        print(response.text.encode('utf8'))
    # XML

    # JSON
    def test__metadata_api_queries__metatype_queries__source_id_metatypes_json(self):
        url = "http://api.worldbank.org/v2/sources/2/metatypes?format=json"
        payload = {}
        headers = {}
        response = requests.request("GET", url, headers=headers, data=payload)
        print(response.text.encode('utf8'))
    # JSON
    # Metatype Queries

    # Metadata Queries
    # XML
    def test__metadata_api_queries__metadata_queries__source_country_metatypes_metadata_xml(self):
        url = "http://api.worldbank.org/v2/sources/2/country/usa;jpn/metatypes/incomegroup/metadata"
        payload = {}
        headers = {}
        response = requests.request("GET", url, headers=headers, data=payload)
        print(response.text.encode('utf8'))

    def test__metadata_api_queries__metadata_queries__source_country_metadata_xml(self):
        url = "http://api.worldbank.org/v2/sources/2/country/jpn/metadata"
        payload = {}
        headers = {}
        response = requests.request("GET", url, headers=headers, data=payload)
        print(response.text.encode('utf8'))

    def test__metadata_api_queries__metadata_queries__source_country_series_metadata_xml(self):
        url = "http://api.worldbank.org/v2/sources/2/country/usa;jpn/series/SP.POP.TOTL/metadata"
        payload = {}
        headers = {}
        response = requests.request("GET", url, headers=headers, data=payload)
        print(response.text.encode('utf8'))
    # XML

    # JSON
    def test__metadata_api_queries__metadata_queries__source_country_metatypes_metadata_json(self):
        url = "http://api.worldbank.org/v2/sources/2/country/usa;jpn/metatypes/incomegroup/metadata?format=json"
        payload = {}
        headers = {}
        response = requests.request("GET", url, headers=headers, data=payload)
        print(response.text.encode('utf8'))

    def test__metadata_api_queries__metadata_queries__source_country_metadata_json(self):
        url = "http://api.worldbank.org/v2/sources/2/country/jpn/metadata?format=json"
        payload = {}
        headers = {}
        response = requests.request("GET", url, headers=headers, data=payload)
        print(response.text.encode('utf8'))

    def test__metadata_api_queries__metadata_queries__source_country_series_metadata_json(self):
        url = "http://api.worldbank.org/v2/sources/2/country/usa;jpn/series/SP.POP.TOTL/metadata?format=json"
        payload = {}
        headers = {}
        response = requests.request("GET", url, headers=headers, data=payload)
        print(response.text.encode('utf8'))
    # JSON
    # Metadata Queries

    # Search Queries
    # XML
    def test__metadata_api_queries__search_queries__source_id_search_xml(self):
        url = "http://api.worldbank.org/v2/sources/2/search/solid%20fuel"
        payload = {}
        headers = {}
        response = requests.request("GET", url, headers=headers, data=payload)
        print(response.text.encode('utf8'))

    def test__metadata_api_queries__search_queries__source_id_concepts_country_search_xml(self):
        url = "http://api.worldbank.org/v2/sources/2/concepts/country/search/united"
        payload = {}
        headers = {}
        response = requests.request("GET", url, headers=headers, data=payload)
        print(response.text.encode('utf8'))

    def test__metadata_api_queries__search_queries__source_id_metatypes_region_search_xml(self):
        url = "http://api.worldbank.org/v2/sources/2/metatypes/region/search/south"
        payload = {}
        headers = {}
        response = requests.request("GET", url, headers=headers, data=payload)
        print(response.text.encode('utf8'))
    # XML

    # JSON
    def test__metadata_api_queries__search_queries__source_id_search_json(self):
        url = "http://api.worldbank.org/v2/sources/2/search/solid%20fuel?format=json"
        payload = {}
        headers = {}
        response = requests.request("GET", url, headers=headers, data=payload)
        print(response.text.encode('utf8'))

    def test__metadata_api_queries__search_queries__source_id_concepts_country_search_json(self):
        url = "http://api.worldbank.org/v2/sources/2/concepts/country/search/united?format=json"
        payload = {}
        headers = {}
        response = requests.request("GET", url, headers=headers, data=payload)
        print(response.text.encode('utf8'))

    def test__metadata_api_queries__search_queries__source_id_metatypes_region_search_json(self):
        url = "http://api.worldbank.org/v2/sources/2/metatypes/region/search/south?format=json"
        payload = {}
        headers = {}
        response = requests.request("GET", url, headers=headers, data=payload)
        print(response.text.encode('utf8'))
    # JSON
    # Search Queries

    # Download Queries
    # Excel
    def test__metadata_api_queries__download_queries__excel(self):
        url = "http://api.worldbank.org/v2/sources/2/country/usa;jpn/series/" \
              "SP.POP.TOTL/metadata?downloadformat=excel"
        payload = {}
        headers = {}
        response = requests.request("GET", url, headers=headers, data=payload)
        print(response.text.encode('utf8'))
    # Excel

    # CSV
    def test__metadata_api_queries__download_queries__csv(self):
        url = "http://api.worldbank.org/v2/sources/2/country/usa;jpn/series/SP.POP.TOTL" \
              "/metadata?downloadformat=csv"
        payload = {}
        headers = {}
        response = requests.request("GET", url, headers=headers, data=payload)
        print(response.text.encode('utf8'))
    # CSV
    # Download Queries

    # Metadata API Queries

    # SDMX API Queries

    # Metadata request

    # Data Flow
    # XML
    def test__sdmx_api_queries__metadata_request__data_flow__xml(self):
        url = "http://api.worldbank.org/v2/sdmx/rest/dataflow"
        payload = {}
        headers = {}
        response = requests.request("GET", url, headers=headers, data=payload)
        print(response.text.encode('utf8'))
    # XML

    # JSON
    def test__sdmx_api_queries__metadata_request__data_flow__json(self):
        url = "http://api.worldbank.org/v2/sdmx/rest/dataflow?format=json"
        payload = {}
        headers = {}
        response = requests.request("GET", url, headers=headers, data=payload)
        print(response.text.encode('utf8'))
    # JSON
    # Data Flow

    # Code List
    # XML
    def test__sdmx_api_queries__metadata_request__code_list__xml(self):
        url = "http://api.worldbank.org/v2/sdmx/rest/codelist/wb"
        payload = {}
        headers = {}
        response = requests.request("GET", url, headers=headers, data=payload)
        print(response.text.encode('utf8'))
    # XML

    # JSON
    def test__sdmx_api_queries__metadata_request__code_list__json(self):
        url = "http://api.worldbank.org/v2/sdmx/rest/codelist/wb?format=json"
        payload = {}
        headers = {}
        response = requests.request("GET", url, headers=headers, data=payload)
        print(response.text.encode('utf8'))
    # JSON
    # Code List

    # Data Structure Definition
    # XML
    def test__sdmx_api_queries__metadata_request__data_structure_definition__xml(self):
        url = "http://api.worldbank.org/v2/sdmx/rest/datastructure/wb"
        payload = {}
        headers = {}
        response = requests.request("GET", url, headers=headers, data=payload)
        print(response.text.encode('utf8'))
    # XML

    # JSON
    def test__sdmx_api_queries__metadata_request__data_structure_definition__json(self):
        url = "http://api.worldbank.org/v2/sdmx/rest/datastructure/wb/?format=json"
        payload = {}
        headers = {}
        response = requests.request("GET", url, headers=headers, data=payload)
        print(response.text.encode('utf8'))
    # JSON
    # Data Structure Definition

    # Metadata request

    # Data Request
    # XML
    def test__sdmx_api_queries__data_request__1_xml(self):
        url = "http://api.worldbank.org/v2/sdmx/rest/data/WDI/A.SP_POP_TOTL.AFG/?startperiod=2011&endPeriod=2011"
        payload = {}
        headers = {}
        response = requests.request("GET", url, headers=headers, data=payload)
        print(response.text.encode('utf8'))

    def test__sdmx_api_queries__data_request__2_xml(self):
        url = "http://api.worldbank.org/v2/sdmx/rest/data/WDI/A.SP_POP_TOTL./?startperiod=2011&endPeriod=2011"
        payload = {}
        headers = {}
        response = requests.request("GET", url, headers=headers, data=payload)
        print(response.text.encode('utf8'))

    def test__sdmx_api_queries__data_request__3_xml(self):
        url = "http://api.worldbank.org/v2/sdmx/rest/data/WDI/A..AFG/?startperiod=2011&endPeriod=2011"
        payload = {}
        headers = {}
        response = requests.request("GET", url, headers=headers, data=payload)
        print(response.text.encode('utf8'))

    def test__sdmx_api_queries__data_request__4_xml(self):
        url = "http://api.worldbank.org/v2/sdmx/rest/data/WDI/A.SP_POP_TOTL.AFG/?startperiod=2010&endPeriod=2015"
        payload = {}
        headers = {}
        response = requests.request("GET", url, headers=headers, data=payload)
        print(response.text.encode('utf8'))
    # XML

    # JSON
    def test__sdmx_api_queries__data_request__1_json(self):
        url = "http://api.worldbank.org/v2/sdmx/rest/data/WDI/A.SP_POP_TOTL.AFG/" \
              "?startperiod=2011&endPeriod=2011&format=json"
        payload = {}
        headers = {}
        response = requests.request("GET", url, headers=headers, data=payload)
        print(response.text.encode('utf8'))

    def test__sdmx_api_queries__data_request__2_json(self):
        url = "http://api.worldbank.org/v2/sdmx/rest/data/WDI/A.SP_POP_TOTL./" \
              "?startperiod=2011&endPeriod=2011&format=json"
        payload = {}
        headers = {}
        response = requests.request("GET", url, headers=headers, data=payload)
        print(response.text.encode('utf8'))

    def test__sdmx_api_queries__data_request__3_json(self):
        url = "http://api.worldbank.org/v2/sdmx/rest/data/WDI/A..AFG/?startperiod" \
              "=2011&endPeriod=2011&format=json"
        payload = {}
        headers = {}
        response = requests.request("GET", url, headers=headers, data=payload)
        print(response.text.encode('utf8'))

    def test__sdmx_api_queries__data_request__4_json(self):
        url = "http://api.worldbank.org/v2/sdmx/rest/data/WDI/A.SP_POP_TOTL.AFG" \
              "/?startperiod=2010&endPeriod=2015&format=json"
        payload = {}
        headers = {}
        response = requests.request("GET", url, headers=headers, data=payload)
        print(response.text.encode('utf8'))
    # JSON
    # Data Request

    # SDMX API Queries

    # Climate Data API

    # The Basic Request
    def test__climate_data_api__climateweb_xml(self):
        type = "mavg"
        var = "tas"
        start = "1920"
        end = "1939"
        iso = "710"
        ext = "json"
        url = "http://climatedataapi.worldbank.org/climateweb/rest/v1/country/" \
              + type + "/" \
              + var + "/" \
              + start + "/" \
              + end + "/" \
              + iso + "[." \
              + ext + "]"
        payload = {}
        headers = {}
        response = requests.request("GET", url, headers=headers, data=payload)
        print(response.text.encode('utf8'))
    # The Basic Request

    # Basin-level Requests

    # Basin-level Requests

    # Historical Data

    # Historical Data

    # KML Output

    # KML Output

    # Climate Data API


if __name__ == '__main__':
    unittest.main()
