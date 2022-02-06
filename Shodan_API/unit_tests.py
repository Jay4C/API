import unittest
import requests


class UnitTestsShodanAPISearchMethods(unittest.TestCase):
    def test_shodan_host_ip(self):
        print('test_shodan_host_ip')

        params = (
            ('key', '{YOUR_API_KEY}'),
        )

        response = requests.get('https://api.shodan.io/shodan/host/8.8.8.8', params=params)

        print(response.text)

    def test_shodan_host_count(self):
        print('test_shodan_host_count')

        params = (
            ('key', '{YOUR_API_KEY}'),
            ('query', 'port:22'),
            ('facets', 'org,os'),
        )

        response = requests.get('https://api.shodan.io/shodan/host/count', params=params)

        print(response.text)

    def test_shodan_host_search(self):
        print('test_shodan_host_search')

        params = (
            ('key', '{YOUR_API_KEY}'),
            ('query', 'product:nginx'),
            ('facets', 'country'),
        )

        response = requests.get('https://api.shodan.io/shodan/host/search', params=params)

        print(response.text)

    def test_shodan_host_search_facets(self):
        print('test_shodan_host_search_facets')

        params = (
            ('key', '{YOUR_API_KEY}'),
        )

        response = requests.get('https://api.shodan.io/shodan/host/search/facets', params=params)

        print(response.text)

    def test_shodan_host_search_filters(self):
        print('test_shodan_host_search_filters')

        params = (
            ('key', '{YOUR_API_KEY}'),
        )

        response = requests.get('https://api.shodan.io/shodan/host/search/filters', params=params)

        print(response.text)

    def test_shodan_host_search_tokens(self):
        print('test_shodan_host_search_tokens')

        params = (
            ('key', '{YOUR_API_KEY}'),
            ('query', 'Raspbian port:22'),
        )

        response = requests.get('https://api.shodan.io/shodan/host/search/tokens', params=params)

        print(response.text)


class UnitTestsShodanAPIOnDemandScanning(unittest.TestCase):
    def test_shodan_ports(self):
        print('test_shodan_ports')

        params = (
            ('key', '{YOUR_API_KEY}'),
        )

        response = requests.get('https://api.shodan.io/shodan/ports', params=params)

        print(response.text)

    def test_shodan_protocols(self):
        print('test_shodan_protocols')

        params = (
            ('key', '{YOUR_API_KEY}'),
        )

        response = requests.get('https://api.shodan.io/shodan/protocols', params=params)

        print(response.text)

    def test_shodan_scan(self):
        print('test_shodan_scan')

        params = (
            ('key', '{YOUR_API_KEY}'),
        )

        data = {
            'ips': '8.8.8.8,1.1.1.1'
        }

        response = requests.post('https://api.shodan.io/shodan/scan', params=params, data=data)

        print(response.text)

    def test_shodan_scan_internet(self):
        print('test_shodan_scan_internet')

        params = (
            ('key', '{YOUR_API_KEY}'),
        )

        data = {
            'port': '80',
            'protocol': 'http'
        }

        response = requests.post('https://api.shodan.io/shodan/scan/internet', params=params, data=data)

        print(response.text)

    def test_shodan_scans(self):
        print('test_shodan_scans')

        params = (
            ('key', '{YOUR_API_KEY}'),
        )

        response = requests.get('https://api.shodan.io/shodan/scans', params=params)

        print(response.text)

    def test_shodan_scan_id(self):
        print('test_shodan_scan_id')

        params = (
            ('key', '{YOUR_API_KEY}'),
        )

        response = requests.get('https://api.shodan.io/shodan/scan/Mo8W7itcWumiy9Ay', params=params)

        print(response.text)


class UnitTestsShodanAPINetworkAlerts(unittest.TestCase):
    def test_shodan_alert(self):
        print('test_shodan_alert')

        headers = {
            'Content-Type': 'application/json',
        }

        params = (
            ('key', '{YOUR_API_KEY}'),
        )

        data = ' { "name": "DNS Alert", "filters": { "ip": [ "8.8.8.8", "1.1.1.1" ] }, "expires": 0 } '

        response = requests.post('https://api.shodan.io/shodan/alert', headers=headers, params=params, data=data)

        print(response.text)

    def test_shodan_alert_id_info(self):
        print('test_shodan_alert_id_info')

        params = (
            ('key', '{YOUR_API_KEY}'),
        )

        response = requests.get('https://api.shodan.io/shodan/alert/67UQ4JM3NGJKROR9/info', params=params)

        print(response.text)

    def test_shodan_alert_id_delete(self):
        print('test_shodan_alert_id_delete')

        params = (
            ('key', '{YOUR_API_KEY}'),
        )

        response = requests.delete('https://api.shodan.io/shodan/alert/67UQ4JM3NGJKROR9', params=params)

        print(response.text)

    def test_shodan_alert_id_post(self):
        print('test_shodan_alert_id_post')

        headers = {
            'Content-Type': 'application/json',
        }

        params = (
            ('key', '{YOUR_API_KEY}'),
        )

        data = ' { "filters": { "ip": [ "8.8.8.8", "1.1.1.1" ] }, "expires": 0 } '

        response = requests.post('https://api.shodan.io/shodan/alert/67UQ4JM3NGJKROR9',
                                 headers=headers, params=params,
                                 data=data)

        print(response.text)

    def test_shodan_alert_info(self):
        print('test_shodan_alert_info')

        params = (
            ('key', '{YOUR_API_KEY}'),
        )

        response = requests.get('https://api.shodan.io/shodan/alert/info', params=params)

        print(response.text)

    def test_shodan_alert_triggers(self):
        print('test_shodan_alert_triggers')

        params = (
            ('key', '{YOUR_API_KEY}'),
        )

        response = requests.get('https://api.shodan.io/shodan/alert/triggers', params=params)

        print(response.text)

    def test_shodan_alert_id_trigger_trigger_put(self):
        print('test_shodan_alert_id_trigger_trigger_put')

        params = (
            ('key', '{YOUR_API_KEY}'),
        )

        response = requests.put('https://api.shodan.io/shodan/alert/OYPRB8IR9Z35AZPR/trigger'
                                '/new_service,vulnerable',
                                params=params)

        print(response.text)

    def test_shodan_alert_id_trigger_trigger_delete(self):
        print('test_shodan_alert_id_trigger_trigger_delete')

        params = (
            ('key', '{YOUR_API_KEY}'),
        )

        response = requests.delete('https://api.shodan.io/shodan/alert/OYPRB8IR9Z35AZPR'
                                   '/trigger/new_service,vulnerable',
                                   params=params)

        print(response.text)

    def test_shodan_alert_id_trigger_trigger_ignore_service_put(self):
        print('test_shodan_alert_id_trigger_trigger_ignore_service_put')

        params = (
            ('key', '{YOUR_API_KEY}'),
        )

        response = requests.put(
            'https://api.shodan.io/shodan/alert/OYPRB8IR9Z35AZPR/trigger/new_service'
            '/ignore/1.1.1.1:53', params=params)

        print(response.text)

    def test_shodan_alert_id_trigger_trigger_ignore_service_delete(self):
        print('test_shodan_alert_id_trigger_trigger_ignore_service_delete')

        params = (
            ('key', '{YOUR_API_KEY}'),
        )

        response = requests.delete(
            'https://api.shodan.io/shodan/alert/OYPRB8IR9Z35AZPR/trigger'
            '/new_service/ignore/1.1.1.1:53', params=params)

        print(response.text)

    def test_shodan_alert_id_notifier_notifier_id_put(self):
        print('test_shodan_alert_id_notifier_notifier_id_put')

        params = (
            ('key', '{YOUR_API_KEY}'),
        )

        response = requests.put('https://api.shodan.io/shodan/alert/OYPRB8IR9Z35AZPR'
                                '/notifier/default', params=params)

        print(response.text)

    def test_shodan_alert_id_notifier_notifier_id_delete(self):
        print('test_shodan_alert_id_notifier_notifier_id_delete')

        params = (
            ('key', '{YOUR_API_KEY}'),
        )

        response = requests.delete('https://api.shodan.io/shodan/alert/OYPRB8IR9Z35AZPR/notifier/default',
                                   params=params)

        print(response.text)


class UnitTestsShodanAPINotifiers(unittest.TestCase):
    def test_notifier_get(self):
        print('test_notifier_get')

        params = (
            ('key', '{YOUR_API_KEY}'),
        )

        response = requests.get('https://api.shodan.io/notifier', params=params)

        print(response.text)

    def test_notifier_provider(self):
        print('test_notifier_provider')

        params = (
            ('key', '{YOUR_API_KEY}'),
        )

        response = requests.get('https://api.shodan.io/notifier/provider', params=params)

        print(response.text)

    def test_notifier_put(self):
        print('test_notifier_put')

        params = (
            ('key', '{YOUR_API_KEY}'),
        )

        data = {
            'provider': 'email',
            'description': 'Email notifier',
            'to': 'jmath@shodan.io'
        }

        response = requests.post('https://api.shodan.io/notifier', params=params, data=data)

        print(response.text)

    def test_notifier_id_delete(self):
        print('test_notifier_id_delete')

        params = (
            ('key', '{YOUR_API_KEY}'),
        )

        response = requests.delete('https://api.shodan.io/notifier/1VxiaJb93Gn8TUnM', params=params)

        print(response.text)

    def test_notifier_id_get(self):
        print('test_notifier_id_get')

        params = (
            ('key', '{YOUR_API_KEY}'),
        )

        response = requests.get('https://api.shodan.io/notifier/1VxiaJb93Gn8TUnM', params=params)

        print(response.text)

    def test_notifier_id_put(self):
        print('test_notifier_id_put')

        params = (
            ('key', '{YOUR_API_KEY}'),
        )

        data = {
            'to': 'jmath@gmail.com'
        }

        response = requests.put('https://api.shodan.io/notifier/1VxiaJb93Gn8TUnM', params=params, data=data)

        print(response.text)


class UnitTestsShodanAPIDirectoryMethods(unittest.TestCase):
    def test_shodan_query(self):
        print('test_shodan_query')

        params = (
            ('key', '{YOUR_API_KEY}'),
        )

        response = requests.get('https://api.shodan.io/shodan/query', params=params)

        print(response.text)

    def test_shodan_query_search(self):
        print('test_shodan_query_search')

        params = (
            ('query', 'webcam'),
            ('key', '{YOUR_API_KEY}'),
        )

        response = requests.get('https://api.shodan.io/shodan/query/search', params=params)

        print(response.text)

    def test_shodan_query_tags(self):
        print('test_shodan_query_tags')

        params = (
            ('key', '{YOUR_API_KEY}'),
        )

        response = requests.get('https://api.shodan.io/shodan/query/tags', params=params)

        print(response.text)


class UnitTestsShodanAPIBulkData(unittest.TestCase):
    def test_shodan_data(self):
        print('test_shodan_data')

        params = (
            ('key', '{YOUR_API_KEY}'),
        )

        response = requests.get('https://api.shodan.io/shodan/data', params=params)

        print(response.text)

    def test_shodan_data_dataset(self):
        print('test_shodan_data_dataset')

        params = (
            ('key', '{YOUR_API_KEY}'),
        )

        response = requests.get('https://api.shodan.io/shodan/data/raw-daily', params=params)

        print(response.text)


class UnitTestsShodanAPIManageOrganization(unittest.TestCase):
    def test_org(self):
        print('test_org')

        params = (
            ('key', '{YOUR_API_KEY}'),
        )

        response = requests.get('https://api.shodan.io/org', params=params)

        print(response.text)

    def test_org_member_user_put(self):
        print('test_org_member_user_put')

        params = (
            ('key', '{YOUR_API_KEY}'),
        )

        response = requests.put('https://api.shodan.io/org/member/new-member@shodan.io', params=params)

        print(response.text)

    def test_org_member_user_delete(self):
        print('test_org_member_user_delete')

        params = (
            ('key', '{YOUR_API_KEY}'),
        )

        response = requests.delete('https://api.shodan.io/org/member/new-member@shodan.io', params=params)

        print(response.text)


class UnitTestsShodanAPIAccountMethods(unittest.TestCase):
    def test_account_profile(self):
        print('test_account_profile')

        params = (
            ('key', '{YOUR_API_KEY}'),
        )

        response = requests.get('https://api.shodan.io/account/profile', params=params)

        print(response.text)


class UnitTestsShodanAPIDNSMethods(unittest.TestCase):
    def test_dns_domain_domain(self):
        print('test_dns_domain_domain')

        params = (
            ('key', '{YOUR_API_KEY}'),
        )

        response = requests.get('https://api.shodan.io/dns/domain/google.com', params=params)

        print(response.text)

    def test_dns_resolve(self):
        print('test_dns_resolve')

        params = (
            ('hostnames', 'google.com,facebook.com'),
            ('key', '{YOUR_API_KEY}'),
        )

        response = requests.get('https://api.shodan.io/dns/resolve', params=params)

        print(response.text)

    def test_dns_reverse(self):
        print('test_dns_reverse')

        params = (
            ('ips', '8.8.8.8,1.1.1.1'),
            ('key', '{YOUR_API_KEY}'),
        )

        response = requests.get('https://api.shodan.io/dns/reverse', params=params)

        print(response.text)


class UnitTestsShodanAPIUtilityMethods(unittest.TestCase):
    def test_tools_httpheaders(self):
        print('test_tools_httpheaders')

        params = (
            ('key', '{YOUR_API_KEY}'),
        )

        response = requests.get('https://api.shodan.io/tools/httpheaders', params=params)

        print(response.text)

    def test_tools_myip(self):
        print('test_tools_myip')

        params = (
            ('key', '{YOUR_API_KEY}'),
        )

        response = requests.get('https://api.shodan.io/tools/myip', params=params)

        print(response.text)


class UnitTestsShodanAPIStatusMethods(unittest.TestCase):
    def test_api_info(self):
        print('test_api_info')

        params = (
            ('key', '{YOUR_API_KEY}'),
        )

        response = requests.get('https://api.shodan.io/api-info', params=params)

        print(response.text)


class UnitTestsShodanAPIDataStreams(unittest.TestCase):
    def test_shodan_banners(self):
        print('test_shodan_banners')

        params = (
            ('key', '{YOUR_API_KEY}'),
        )

        response = requests.get('https://stream.shodan.io/shodan/banners', params=params)

        print(response.text)

    def test_shodan_asn_asn(self):
        print('test_shodan_asn_asn')

        params = (
            ('key', '{YOUR_API_KEY}'),
        )

        response = requests.get('https://stream.shodan.io/shodan/asn/3303,32475', params=params)

        print(response.text)

    def test_shodan_countries_countries(self):
        print('test_shodan_countries_countries')

        params = (
            ('key', '{YOUR_API_KEY}'),
        )

        response = requests.get('https://stream.shodan.io/shodan/countries/DE,US', params=params)

        print(response.text)

    def test_shodan_ports_ports(self):
        print('test_shodan_ports_ports')

        params = (
            ('key', '{YOUR_API_KEY}'),
        )

        response = requests.get('https://stream.shodan.io/shodan/ports/22,443', params=params)

        print(response.text)


class UnitTestsShodanAPIStreamingNetworkAlerts(unittest.TestCase):
    def test_shodan_alert(self):
        print('test_shodan_alert')

        params = (
            ('key', '{YOUR_API_KEY}'),
        )

        response = requests.get('https://stream.shodan.io/shodan/alert', params=params)

        print(response.text)

    def test_shodan_alert_id(self):
        print('test_shodan_alert_id')

        params = (
            ('key', '{YOUR_API_KEY}'),
        )

        response = requests.get('https://stream.shodan.io/shodan/alert/OYPRB8IR9Z35AZPR', params=params)

        print(response.text)


if __name__ == '__main__':
    unittest.main()
