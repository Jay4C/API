import unittest
from mollie.api.client import Client
import requests


# https://github.com/mollie/mollie-api-python
# https://docs.mollie.com/reference/v2/payments-api/create-payment
class UnitTestsPaymentsAPI(unittest.TestCase):
    # https://docs.mollie.com/reference/v2/payments-api/create-payment
    def test_create_payment(self):
        print('test_create_payment')

        mollie_client = Client()
        mollie_client.set_api_key('')
        payment = mollie_client.payments.create({
            'amount': {
                'currency': 'EUR',
                'value': '10.00'
            },
            'description': 'Order #12345',
            'redirectUrl': 'https://webshop.example.org/payments/webhook/',
            'webhookUrl': 'https://webshop.example.org/order/12345/',
            'locale': 'string optional',
            'method': 'string array optional',
            'metadata': {
                'order_id': '12345'
            },
            'sequenceType': 'string optional',
            'customerId': 'string optional',
            'mandateId': 'string optional',
            'restrictPaymentMethodsToCountry': 'string optional',
            # Payment method-specific parameters for Credit Card
            'billingAddress': {
                'streetAndNumber': 'string optional',
                'postalCode': 'string optional',
                'city': 'string optional',
                'region': 'string optional',
                'country': 'string optional'
            },
            'cardToken': 'string optional',
            'shippingAddress': {
                'streetAndNumber': 'string optional',
                'postalCode': 'string optional',
                'city': 'string optional',
                'region': 'string optional',
                'country': 'string optional'
            },
            # Access token parameters
            'profileId': 'string required',
            'testmode': 'boolean optional',
            # Mollie Connect parameters
            'applicationFee': {
                'amount': {
                    'currency': 'string required',
                    'value': 'string required'
                },
                'description': 'string required'
            },
            'routing': [
                {
                    'amount': {
                        'currency': 'string required',
                        'value': 'string required'
                    },
                    'destination': {
                        'type': 'string required',
                        'organizationId': 'string optional'
                    },
                    'releaseDate': 'date optional'
                }
            ]
        })

        response = payment.json()

        print(str(response))

    # https://docs.mollie.com/reference/v2/payments-api/get-payment
    def test_get_payment(self):
        print('test_get_payment')

        mollie_client = Client()
        mollie_client.set_api_key('')
        payment = mollie_client.payments.get('tr_WDqYK6vllg')

        response = payment.json()

        print(str(response))

    # https://docs.mollie.com/reference/v2/payments-api/update-payment
    def test_update_payment(self):
        print('test_update_payment')

        mollie_client = Client()
        mollie_client.set_api_key('')
        payment = mollie_client.payments.update("tr_7UhSN1zuXS", {
            'description': 'Order #98765',
            'webhookUrl': 'https://webshop.example.org/order/98765/',
            'redirectUrl': 'https://webshop.example.org/payments/webhook/',
            'metadata': {'order_id': '98765'}
        })

        response = payment.json()

        print(str(response))

    # https://docs.mollie.com/reference/v2/payments-api/cancel-payment
    def test_cancel_payment(self):
        print('test_cancel_payment')

        mollie_client = Client()
        mollie_client.set_api_key('')
        canceled_payment = mollie_client.payments.delete('tr_WDqYK6vllg')

        response = canceled_payment.json()

        print(str(response))

    # https://docs.mollie.com/reference/v2/payments-api/list-payments
    def test_list_payments(self):
        print('test_list_payments')

        mollie_client = Client()
        mollie_client.set_api_key('')

        # get the first page
        payments = mollie_client.payments.list()

        response = payments.json()

        print(str(response))


class UnitTestsMethodsAPI(unittest.TestCase):
    # https://docs.mollie.com/reference/v2/methods-api/list-methods
    def test_list_payment_methods(self):
        print('test_list_payment_methods')

        mollie_client = Client()
        mollie_client.set_api_key('')

        # Methods for the Payments API
        methods = mollie_client.methods.list()

        # Methods for the Orders API
        # methods = mollie_client.methods.list(resource='orders')

        response = methods.json()

        print(str(response))

    # https://docs.mollie.com/reference/v2/methods-api/list-all-methods
    def test_list_all_payment_methods(self):
        print('test_list_all_payment_methods')

        mollie_client = Client()
        mollie_client.set_api_key('')

        # Methods for the Payments API
        methods = mollie_client.methods.all()

        # Methods for the Orders API
        # methods = mollie_client.methods.list(resource='orders')

        response = methods.json()

        print(str(response))

    # https://docs.mollie.com/reference/v2/methods-api/get-method
    def test_get_payment_method(self):
        print('test_get_payment_method')

        mollie_client = Client()
        mollie_client.set_api_key('')
        payment_method = mollie_client.methods.get('ideal', include='issuers,pricing')

        response = payment_method.json()

        print(str(response))


class UnitTestsRefundsAPI(unittest.TestCase):
    # https://docs.mollie.com/reference/v2/refunds-api/create-refund
    def test_create_payment_refund(self):
        print('test_create_payment_refund')

        mollie_client = Client()
        mollie_client.set_api_key('')

        payment = mollie_client.payments.get('tr_WDqYK6vllg')
        refund = mollie_client.payment_refunds.on(payment).create({
            'amount': {
                'value': '5.95',
                'currency': 'EUR'
            }
        })

        response = refund.json()

        print(response)

    # https://docs.mollie.com/reference/v2/refunds-api/get-refund
    def test_get_payment_refund(self):
        print('test_get_payment_refund')

        mollie_client = Client()
        mollie_client.set_api_key('')

        payment = mollie_client.payments.get('tr_WDqYK6vllg')
        refund = mollie_client.payment_refunds.on(payment).get('re_4qqhO89gsT')

        response = refund.json()

        print(response)

    # https://docs.mollie.com/reference/v2/refunds-api/cancel-refund
    def test_cancel_payment_refund(self):
        print('test_cancel_payment_refund')

        mollie_client = Client()
        mollie_client.set_api_key('')

        payment = mollie_client.payments.get('tr_WDqYK6vllg')
        cancel_payment_refund = mollie_client.payment_refunds.on(payment).delete('re_4qqhO89gsT')

        response = cancel_payment_refund.json()

        print(response)

    # https://docs.mollie.com/reference/v2/refunds-api/list-refunds
    def test_list_refunds(self):
        print('test_list_refunds')

        mollie_client = Client()
        mollie_client.set_api_key('')
        refunds = mollie_client.payments.get('tr_WDqYK6vllg').refunds

        response = refunds.json()

        print(response)


class UnitTestsChargebacksAPI(unittest.TestCase):
    # https://docs.mollie.com/reference/v2/chargebacks-api/get-chargeback
    def test_get_chargeback(self):
        print('test_get_chargeback')

        mollie_client = Client()
        mollie_client.set_api_key('')

        payment = mollie_client.payments.get('tr_WDqYK6vllg')
        chargeback = mollie_client.payment_chargebacks.on(payment).get('chb_n9z0tp')

        response = chargeback.json()

        print(response)

    # https://docs.mollie.com/reference/v2/chargebacks-api/list-chargebacks
    def test_list_chargebacks(self):
        print('test_list_chargebacks')

        mollie_client = Client()
        mollie_client.set_api_key('')

        payment = mollie_client.payments.get('tr_WDqYK6vllg')
        chargebacks = payment.chargebacks

        response = chargebacks.json()

        print(response)


class UnitTestsCapturesAPI(unittest.TestCase):
    # https://docs.mollie.com/reference/v2/captures-api/get-capture
    def test_get_capture(self):
        print('test_get_capture')

        mollie_client = Client()
        mollie_client.set_api_key('')

        payment = mollie_client.payments.get('tr_WDqYK6vllg')
        capture = mollie_client.captures.on(payment).get('cpt_4qqhO89gsT')

        response = capture.json()

        print(response)

    # https://docs.mollie.com/reference/v2/captures-api/list-captures
    def test_list_captures(self):
        print('test_list_captures')

        mollie_client = Client()
        mollie_client.set_api_key('')

        payment = mollie_client.payments.get('tr_WDqYK6vllg')
        capture = mollie_client.captures.on(payment).list()

        response = capture.json()

        print(response)


class UnitTestsPaymentLinksAPI(unittest.TestCase):
    # https://docs.mollie.com/reference/v2/payment-links-api/create-payment-link
    def test_create_payment_link(self):
        print('test_create_payment_link')

        headers = {
            'Authorization': 'Bearer ',
        }

        data = {
          'amount[currency]': 'EUR',
          'amount[value]': '24.95',
          'description': 'Bicycle tires',
          'expiresAt': '2021-06-06T11:00:00 00:00',
          'redirectUrl': 'https://webshop.example.org/thanks',
          'webhookUrl': 'https://webshop.example.org/payment-links/webhook/'
        }

        response = requests.post('https://api.mollie.com/v2/payment-links', headers=headers, data=data)

        print(response)

    # https://docs.mollie.com/reference/v2/payment-links-api/get-payment-link
    def test_get_payment_link(self):
        print('test_get_payment_link')

        headers = {
            'Authorization': 'Bearer ',
        }

        response = requests.get('https://api.mollie.com/v2/payment-links/pl_4Y0eZitmBnQ6IDoMqZQKh', headers=headers)

        print(response)

    # https://docs.mollie.com/reference/v2/payment-links-api/list-payment-links
    def test_list_payment_links(self):
        print('test_list_payment_links')

        headers = {
            'Authorization': 'Bearer ',
        }

        params = (
            ('limit', '5'),
        )

        response = requests.get('https://api.mollie.com/v2/payment-links', headers=headers, params=params)

        print(response)


class UnitTestsOrdersAPI(unittest.TestCase):
    # https://docs.mollie.com/reference/v2/orders-api/create-order
    def test_create_order(self):
        print("test_create_order")

        headers = {
            'Content-Type': 'application/json',
            'Authorization': 'Bearer ',
        }

        data = '{ "amount": { "value": "1027.99", "currency": "EUR" }, "billingAddress": ' \
               '{ "organizationName": "Mollie B.V.", "streetAndNumber": "Keizersgracht 126", ' \
               '"city": "Amsterdam", "region": "Noord-Holland", "postalCode": "1234AB", ' \
               '"country": "NL", "title": "Dhr", "givenName": "Piet", "familyName": ' \
               '"Mondriaan", "email": "piet@mondriaan.com", "phone": "+31208202070" }, ' \
               '"shippingAddress": { "organizationName": "Mollie B.V.", "streetAndNumber": ' \
               '"Prinsengracht 126", "streetAdditional": "4th floor", "city": "Haarlem", ' \
               '"region": "Noord-Holland", "postalCode": "5678AB", "country": "NL", "title": ' \
               '"Mr", "givenName": "Chuck", "familyName": "Norris", "email": ' \
               '"norris@chucknorrisfacts.net" }, "metadata": { "order_id": "1337", ' \
               '"description": "Lego cars" }, "consumerDateOfBirth": "1958-01-31", "locale": ' \
               '"nl_NL", "orderNumber": "1337", "redirectUrl": "https://example.org/redirect", ' \
               '"webhookUrl": "https://example.org/webhook", "method": "klarnapaylater", ' \
               '"lines": [ { "type": "physical", "category": "gift", "sku": "5702016116977", ' \
               '"name": "LEGO 42083 Bugatti Chiron", "productUrl": ' \
               '"https://shop.lego.com/nl-NL/Bugatti-Chiron-42083", "imageUrl": ' \
               '"https://sh-s7-live-s.legocdn.com/is/image//LEGO/42083_alt1?$main$", ' \
               '"metadata": { "order_id": "1337", "description": "Bugatti Chiron" }, ' \
               '"quantity": 2, "vatRate": "21.00", "unitPrice": { "currency": "EUR", "value": ' \
               '"399.00" }, "totalAmount": { "currency": "EUR", "value": "698.00" }, ' \
               '"discountAmount": { "currency": "EUR", "value": "100.00" }, "vatAmount": ' \
               '{ "currency": "EUR", "value": "121.14" } }, { "type": "physical", "category": ' \
               '"gift", "sku": "5702015594028", "name": "LEGO 42056 Porsche 911 GT3 RS", ' \
               '"productUrl": "https://shop.lego.com/nl-NL/Porsche-911-GT3-RS-42056", "imageUrl": ' \
               '"https://sh-s7-live-s.legocdn.com/is/image/LEGO/42056?$PDPDefault$", "quantity": 1, ' \
               '"vatRate": "21.00", "unitPrice": { "currency": "EUR", "value": "329.99" }, "totalAmount": ' \
               '{ "currency": "EUR", "value": "329.99" }, "vatAmount": { "currency": "EUR", ' \
               '"value": "57.27" } } ] }'

        response = requests.post('https://api.mollie.com/v2/orders', headers=headers, data=data)

        print(response)

    # https://docs.mollie.com/reference/v2/orders-api/get-order
    def test_get_order(self):
        print('test_get_order')

        headers = {
            'Authorization': 'Bearer ',
        }

        params = (
            ('embed', 'payments,refunds'),
        )

        response = requests.get('https://api.mollie.com/v2/orders'
                                '/ord_kEn1PlbGa', headers=headers, params=params)

        print(response)

    # https://docs.mollie.com/reference/v2/orders-api/update-order
    def test_update_order(self):
        print('test_update_order')

        headers = {
            'Content-Type': 'application/json',
            'Authorization': 'Bearer ',
        }

        data = '{ "billingAddress": { "organizationName": "Mollie B.V.", "streetAndNumber": ' \
               '"Keizersgracht 126", "city": "Amsterdam", "region": "Noord-Holland", ' \
               '"postalCode": "1234AB", "country": "NL", "title": "Dhr", "givenName": ' \
               '"Piet", "familyName": "Mondriaan", "email": "piet@mondriaan.com", "phone": ' \
               '"+31208202070" } }'

        response = requests.patch('https://api.mollie.com/v2/orders/ord_kEn1PlbGa', headers=headers, data=data)

        print(response)

    # https://docs.mollie.com/reference/v2/orders-api/update-orderline
    def test_update_order_line(self):
        print('test_update_order_line')

        headers = {
            'Content-Type': 'application/json',
            'Authorization': 'Bearer ',
        }

        data = '{ "name": "LEGO 71043 Hogwarts\u2122 Castle", "productUrl": ' \
               '"https://shop.lego.com/en-GB/product/Hogwarts-Castle-71043", ' \
               '"imageUrl": "https://sh-s7-live-s.legocdn.com/is/image//LEGO/71043_alt1?$main$",' \
               ' "quantity": 2, "vatRate": "21.00", "unitPrice": { "currency": "EUR", "value": "349.00" }, ' \
               '"totalAmount": { "currency": "EUR", "value": "598.00" }, "discountAmount": ' \
               '{ "currency": "EUR", "value": "100.00" }, "vatAmount": { "currency": "EUR", ' \
               '"value": "103.79" } }'

        response = requests.patch('https://api.mollie.com/v2/orders/ord_pbjz8x/lines/odl_dgtxyl', headers=headers,
                                  data=data)

        print(response)

    # https://docs.mollie.com/reference/v2/orders-api/cancel-order
    def test_cancel_order(self):
        print('test_cancel_order')

        headers = {
            'Authorization': 'Bearer ',
        }

        response = requests.delete('https://api.mollie.com/v2/orders/ord_8wmqcHMN4U', headers=headers)

        print(response)

    # https://docs.mollie.com/reference/v2/orders-api/list-orders
    def test_list_orders(self):
        print('test_list_orders')

        headers = {
            'Authorization': 'Bearer ',
        }

        response = requests.get('https://api.mollie.com/v2/orders', headers=headers)

        print(response)

    # https://docs.mollie.com/reference/v2/orders-api/cancel-order-lines
    def test_cancel_order_lines(self):
        print('test_cancel_order_lines')

        headers = {
            'Content-Type': 'application/json',
            'Authorization': 'Bearer ',
        }

        data = '{ "lines": [ { "id": "odl_dgtxyl", "quantity": 1 }, { "id": "odl_jp31jz" } ] }'

        response = requests.delete('https://api.mollie.com/v2/orders/ord_8wmqcHMN4U'
                                   '/lines', headers=headers, data=data)

        print(response)

    # https://docs.mollie.com/reference/v2/orders-api/create-order-payment
    def test_create_order_payment(self):
        print('test_create_order_payment')

        headers = {
            'Content-Type': 'application/json',
            'Authorization': 'Bearer ',
        }

        data = '{ "method": "banktransfer" }'

        response = requests.post('https://api.mollie.com/v2/orders/ord_stTC2WHAuS'
                                 '/payments', headers=headers, data=data)

        print(response)

    # https://docs.mollie.com/reference/v2/orders-api/create-order-refund
    def test_create_order_refund(self):
        print('test_create_order_refund')

        headers = {
            'Content-Type': 'application/json',
            'Authorization': 'Bearer ',
        }

        data = '{ "lines": [ { "id": "odl_dgtxyl", "quantity": 1 } ], ' \
               '"description": "Required quantity not in stock, refunding one photo book.", ' \
               '"metadata": { "bookkeeping_id": 12345 } }'

        response = requests.post('https://api.mollie.com/v2/orders/ord_stTC2WHAuS'
                                 '/refunds', headers=headers, data=data)

        print(response)

    # https://docs.mollie.com/reference/v2/orders-api/list-order-refunds
    def test_list_order_refunds(self):
        print('test_list_order_refunds')

        headers = {
            'Authorization': 'Bearer ',
        }

        response = requests.get('https://api.mollie.com/v2/orders/ord_pbjz8x/refunds', headers=headers)

        print(response)


class UnitTestsShipmentsAPI(unittest.TestCase):
    # https://docs.mollie.com/reference/v2/shipments-api/create-shipment
    def test_create_shipment(self):
        print('test_create_shipment')

        headers = {
            'Content-Type': 'application/json',
            'Authorization': 'Bearer ',
        }

        data = {
            '{ "lines": [ { "id": "odl_dgtxyl", "quantity": 1 }, { "id": "odl_jp31jz" } ], '
            '"tracking": { "carrier": "PostNL", "code": "3SKABA000000000", '
            '"url": "http://postnl.nl/tracktrace/?B': '3SKABA000000000',
            'P': '1015CW',
            'D': 'NL',
            'T': 'C" } }'
        }

        response = requests.post('https://api.mollie.com/v2/orders'
                                 '/ord_kEn1PlbGa/shipments', headers=headers, data=data)

        print(response)

    # https://docs.mollie.com/reference/v2/shipments-api/get-shipment
    def test_get_shipment(self):
        print('test_get_shipment')

        headers = {
            'Authorization': 'Bearer ',
        }

        response = requests.get('https://api.mollie.com/v2/orders/ord_kEn1PlbGa/shipments/shp_3wmsgCJN4U',
                                headers=headers)

        print(response)

    # https://docs.mollie.com/reference/v2/shipments-api/list-shipments
    def test_list_shipments(self):
        print('test_list_shipments')

        headers = {
            'Authorization': 'Bearer ',
        }

        response = requests.get('https://api.mollie.com/v2/order/ord_kEn1PlbGa/shipments', headers=headers)

        print(response)

    # https://docs.mollie.com/reference/v2/shipments-api/update-shipment
    def test_update_shipment(self):
        print('test_update_shipment')

        headers = {
            'Content-Type': 'application/json',
            'Authorization': 'Bearer ',
        }

        data = {
            '{ "tracking": { "carrier": "PostNL", "code": "3SKABA000000000", '
            '"url": "http://postnl.nl/tracktrace/?B': '3SKABA000000000',
            'P': '1015CW',
            'D': 'NL',
            'T': 'C" } }'
        }

        response = requests.post('https://api.mollie.com/v2/orders/ord_kEn1PlbGa/shipments/shp_3wmsgCJN4U',
                                 headers=headers, data=data)

        print(response)


class UnitTestsCustomersAPI(unittest.TestCase):
    # https://docs.mollie.com/reference/v2/customers-api/create-customer
    def test_create_customer(self):
        print('test_create_customer')

        headers = {
            'Authorization': 'Bearer ',
        }

        data = {
            'name': 'Customer A',
            'email': 'customer@example.org'
        }

        response = requests.post('https://api.mollie.com/v2/customers', headers=headers, data=data)

        print(response)

    # https://docs.mollie.com/reference/v2/customers-api/get-customer
    def test_get_customer(self):
        print('test_get_customer')

        headers = {
            'Authorization': 'Bearer ',
        }

        response = requests.get('https://api.mollie.com/v2/customers/cst_kEn1PlbGa', headers=headers)

        print(response)

    # https://docs.mollie.com/reference/v2/customers-api/update-customer
    def test_update_customer(self):
        print('test_update_customer')

        headers = {
            'Authorization': 'Bearer ',
        }

        data = {
            'name': 'Updated Customer A',
            'email': 'updated-customer@example.org'
        }

        response = requests.patch('https://api.mollie.com/v2/customers'
                                  '/cst_8wmqcHMN4U', headers=headers, data=data)

        print(response)

    # https://docs.mollie.com/reference/v2/customers-api/delete-customer
    def test_delete_customer(self):
        print('test_delete_customer')

        headers = {
            'Authorization': 'Bearer ',
        }

        response = requests.delete('https://api.mollie.com/v2/customers/cst_8wmqcHMN4U', headers=headers)

        print(response)

    # https://docs.mollie.com/reference/v2/customers-api/list-customers
    def test_list_customers(self):
        print('test_list_customers')

        headers = {
            'Authorization': 'Bearer ',
        }

        response = requests.get('https://api.mollie.com/v2/customers', headers=headers)

        print(response)

    # https://docs.mollie.com/reference/v2/customers-api/create-customer-payment
    def test_create_customer_payment(self):
        print('test_create_customer_payment')

        headers = {
            'Authorization': 'Bearer ',
        }

        data = {
            'amount[currency]': 'EUR',
            'amount[value]': '10.00',
            'description': 'Order #12345',
            'sequenceType': 'first',
            'redirectUrl': 'https://webshop.example.org/order/12345/',
            'webhookUrl': 'https://webshop.example.org/payments/webhook/'
        }

        response = requests.post('https://api.mollie.com/v2/customers/cst_8wmqcHMN4U/payments', headers=headers,
                                 data=data)

        print(response)

    # https://docs.mollie.com/reference/v2/customers-api/list-customer-payments
    def test_list_customer_payments(self):
        print('test_list_customer_payments')

        headers = {
            'Authorization': 'Bearer ',
        }

        response = requests.get('https://api.mollie.com/v2/customers/cst_8wmqcHMN4U/payments', headers=headers)

        print(response)


class UnitTestsMandatesAPI(unittest.TestCase):
    # https://docs.mollie.com/reference/v2/mandates-api/create-mandate
    def test_create_mandate(self):
        print('test_create_mandate')

        mollie_client = Client()
        mollie_client.set_api_key('')

        mandate = mollie_client.customer_mandates.with_parent_id('cst_4qqhO89gsT').create({
            'method': 'directdebit',
            'consumerName': '',
            'consumerAccount': '',
            'consumerBic': '',
            'signatureDate': '',
            'mandateReference': ''
        })

        response = mandate.json()

        print(response)

    # https://docs.mollie.com/reference/v2/mandates-api/get-mandate
    def test_get_mandate(self):
        print('test_get_mandate')

        headers = {
            'Authorization': 'Bearer ',
        }

        response = requests.get('https://api.mollie.com/v2/customers/cst_4qqhO89gsT/mandates/mdt_h3gAaD5zP',
                                headers=headers)

        print(response)

    # https://docs.mollie.com/reference/v2/mandates-api/revoke-mandate
    def test_revoke_mandate(self):
        print('test_revoke_mandate')

        headers = {
            'Authorization': 'Bearer ',
        }

        response = requests.delete('https://api.mollie.com/v2/customers/cst_stTC2WHAuS/mandates/mdt_pWUnw6pkBN',
                                   headers=headers)

        print(response)

    # https://docs.mollie.com/reference/v2/mandates-api/list-mandates
    def test_list_mandates(self):
        print('test_list_mandates')

        headers = {
            'Authorization': 'Bearer ',
        }

        response = requests.get('https://api.mollie.com/v2/customers/cst_8wmqcHMN4U/mandates', headers=headers)

        print(response)


class UnitTestsSubscriptionsAPI(unittest.TestCase):
    # https://docs.mollie.com/reference/v2/subscriptions-api/create-subscription
    def test_create_subscription(self):
        print('test_create_subscription')

        headers = {
            'Authorization': 'Bearer ',
        }

        data = {
            'amount[currency]': 'EUR',
            'amount[value]': '25.00',
            'times': '4',
            'interval': '3 months',
            'description': 'Quarterly payment',
            'webhookUrl': 'https://webshop.example.org/subscriptions/webhook/'
        }

        response = requests.post('https://api.mollie.com/v2/customers/cst_stTC2WHAuS'
                                 '/subscriptions', headers=headers,
                                 data=data)

        print(response)

    # https://docs.mollie.com/reference/v2/subscriptions-api/get-subscription
    def test_get_subscription(self):
        print('test_get_subscription')

        headers = {
            'Authorization': 'Bearer ',
        }

        response = requests.get('https://api.mollie.com/v2/customers/cst_stTC2WHAuS/subscriptions'
                                '/sub_rVKGtNd6s3',
                                headers=headers)

        print(response)

    # https://docs.mollie.com/reference/v2/subscriptions-api/cancel-subscription
    def test_cancel_subscription(self):
        print('test_cancel_subscription')

        headers = {
            'Authorization': 'Bearer ',
        }

        response = requests.delete('https://api.mollie.com/v2/customers/cst_stTC2WHAuS'
                                   '/subscriptions/sub_rVKGtNd6s3',
                                   headers=headers)

        print(response)

    # https://docs.mollie.com/reference/v2/subscriptions-api/list-subscriptions
    def test_list_subscriptions(self):
        print('test_list_subscriptions')

        headers = {
            'Authorization': 'Bearer ',
        }

        response = requests.get('https://api.mollie.com/v2/customers/cst_8wmqcHMN4U'
                                '/subscriptions', headers=headers)

        print(response)

    # https://docs.mollie.com/reference/v2/subscriptions-api/list-all-subscriptions
    def test_list_all_subscriptions(self):
        print('test_list_all_subscriptions')

        headers = {
            'Authorization': 'Bearer ',
        }

        response = requests.get('https://api.mollie.com/v2/subscriptions', headers=headers)

        print(response)

    # https://docs.mollie.com/reference/v2/subscriptions-api/list-subscriptions-payments
    def test_list_subscription_payments(self):
        print('test_list_subscription_payments')

        headers = {
            'Authorization': 'Bearer ',
        }

        response = requests.get(
            'https://api.mollie.com/v2/customers/cst_8wmqcHMN4U/subscriptions'
            '/sub_8JfGzs6v3K/payments', headers=headers)

        print(response)

    # https://docs.mollie.com/reference/v2/subscriptions-api/update-subscription
    def test_update_subscription(self):
        print('test_update_subscription')

        headers = {
            'Authorization': 'Bearer ',
        }

        data = {
            'amount[currency]': 'EUR',
            'amount[value]': '10.00',
            'times': '42',
            'startDate': '2018-12-12',
            'description': 'Mollie Recurring subscription',
            'webhookUrl': 'https://example.org/webhook'
        }

        response = requests.patch('https://api.mollie.com/v2/customers/cst_5a2pPrwaWy'
                                  '/subscriptions/sub_8EjeBVgtEn',
                                  headers=headers, data=data)

        print(response)


class UnitTestsConnectAPI(unittest.TestCase):
    # https://docs.mollie.com/reference/oauth2/authorize
    def test_authorize(self):
        print('test_authorize')

        headers = {
            'Authorization': 'Bearer ',
        }

        data = {
            'client_id': 'string required',
            'redirect_uri': 'string optional',
            'state': 'string required',
            'scope': 'string required',
            'response_type': 'string required',
            'approval_prompt': 'string required',
            'locale': 'string optional'
        }

        response = requests.get('https://www.mollie.com/oauth2/authorize', headers=headers,
                                 data=data)

        print(response)

    # https://docs.mollie.com/reference/oauth2/tokens
    def test_generate_tokens_initial_request(self):
        print('test_generate_tokens')

        data = {
            'grant_type': 'authorization_code',
            'code': ''
        }

        response = requests.post('https://api.mollie.com/oauth2/tokens', data=data,
                                 auth=('', ''))

        print(response)

    # https://docs.mollie.com/reference/oauth2/tokens
    def test_generate_tokens_refresh_request(self):
        print('test_generate_tokens')

        data = {
            'grant_type': 'refresh_token',
            'refresh_token': ''
        }

        response = requests.post('https://api.mollie.com/oauth2/tokens', data=data,
                                 auth=('app_j9Pakf56Ajta6Y65AkdTtAv', 'S5lTvMDTjl95HGnwYmsszDtbMp8QBE2lLcRJbD7I'))

        print(response)

    # https://docs.mollie.com/reference/oauth2/revoke-token
    def test_revoke_token(self):
        print('test_revoke_token')

        data = {
            'token_type_hint': 'refresh_token',
            'token': ''
        }

        response = requests.delete('https://api.mollie.com/oauth2/tokens', data=data,
                                   auth=('client_id', 'client_secret'))

        print(response)


class UnitTestsPermissionsAPI(unittest.TestCase):
    # https://docs.mollie.com/reference/v2/permissions-api/get-permission
    def test_get_permission(self):
        print('test_get_permission')

        headers = {
            'Authorization': 'Bearer ',
        }

        response = requests.get('https://api.mollie.com/v2/permissions/payments.read', headers=headers)

        print(response)

    # https://docs.mollie.com/reference/v2/permissions-api/list-permissions
    def test_list_permissions(self):
        print('test_list_permissions')

        headers = {
            'Authorization': 'Bearer ',
        }

        response = requests.get('https://api.mollie.com/v2/permissions', headers=headers)

        print(response)


class UnitTestOrganizationsAPI(unittest.TestCase):
    # https://docs.mollie.com/reference/v2/organizations-api/current-organization
    def test_get_current_organization(self):
        print('test_get_current_organization')

        headers = {
            'Authorization': 'Bearer ',
        }

        response = requests.get('https://api.mollie.com/v2/organizations/me', headers=headers)

        print(response)

    # https://docs.mollie.com/reference/v2/organizations-api/get-organization
    def test_get_organization(self):
        print('test_get_organization')

        headers = {
            'Authorization': 'Bearer ',
        }

        response = requests.get('https://api.mollie.com/v2/organizations/org_12345678', headers=headers)

        print(response)


class UnitTestsProfilesAPI(unittest.TestCase):
    # https://docs.mollie.com/reference/v2/profiles-api/create-profile
    def test_create_profile(self):
        print('test_create_profile')

        headers = {
            'Authorization': 'Bearer ',
        }

        data = {
            'name': 'My website name',
            'website': 'https://www.mywebsite.com',
            'email': 'info@mywebsite.com',
            'phone': ' 31208202070',
            'categoryCode': '5399',
            'mode': 'live'
        }

        response = requests.post('https://api.mollie.com/v2/profiles', headers=headers, data=data)

        print(response)

    # https://docs.mollie.com/reference/v2/profiles-api/get-profile
    def test_get_profile(self):
        print('test_get_profile')

        headers = {
            'Authorization': 'Bearer ',
        }

        response = requests.get('https://api.mollie.com/v2/profiles/pfl_v9hTwCvYqw', headers=headers)

        print(response)

    # https://docs.mollie.com/reference/v2/profiles-api/get-profile-me
    def test_get_current_profile(self):
        print('test_get_current_profile')

        headers = {
            'Authorization': 'Bearer ',
        }

        response = requests.get('https://api.mollie.com/v2/profiles/me', headers=headers)

        print(response)

    # https://docs.mollie.com/reference/v2/profiles-api/update-profile
    def test_update_profile(self):
        print('test_update_profile')

        headers = {
            'Authorization': 'Bearer ',
        }

        data = {
            'name': 'My website name - Update 1',
            'website': 'https://www.mywebsite2.com',
            'email': 'info@mywebsite2.com',
            'phone': ' 31208202070',
            'categoryCode': '5399'
        }

        response = requests.patch('https://api.mollie.com/v2/profiles'
                                  '/pfl_v9hTwCvYqw', headers=headers, data=data)

        print(response)

    # https://docs.mollie.com/reference/v2/profiles-api/delete-profile
    def test_delete_profile(self):
        print('test_delete_profile')

        headers = {
            'Authorization': 'Bearer ',
        }

        response = requests.delete('https://api.mollie.com/v2/profiles/pfl_v9hTwCvYqw', headers=headers)

        print(response)

    # https://docs.mollie.com/reference/v2/profiles-api/enable-method
    def test_enable_payment_method(self):
        print('test_enable_payment_method')

        headers = {
            'Authorization': 'Bearer ',
        }

        response = requests.post('https://api.mollie.com/v2/profiles/pfl_v9hTwCvYqw'
                                 '/methods/ideal', headers=headers)

        print(response)

    # https://docs.mollie.com/reference/v2/profiles-api/disable-method
    def test_disable_payment_method(self):
        print('test_disable_payment_method')

        headers = {
            'Authorization': 'Bearer ',
        }

        response = requests.delete('https://api.mollie.com/v2/profiles/pfl_v9hTwCvYqw'
                                   '/methods/ideal', headers=headers)

        print(response)

    # https://docs.mollie.com/reference/v2/profiles-api/enable-gift-card-issuer
    def test_enable_gift_card_issuer(self):
        print('test_enable_gift_card_issuer')

        headers = {
            'Authorization': 'Bearer ',
        }

        response = requests.post(
            'https://api.mollie.com/v2/profiles/pfl_v9hTwCvYqw/methods/giftcard/issuers/festivalcadeau',
            headers=headers)

        print(response)

    # https://docs.mollie.com/reference/v2/profiles-api/disable-gift-card-issuer
    def test_disable_gift_card_issuer(self):
        print('test_disable_gift_card_issuer')

        headers = {
            'Authorization': 'Bearer ',
        }

        response = requests.delete(
            'https://api.mollie.com/v2/profiles/pfl_v9hTwCvYqw/methods/giftcard/issuers/festivalcadeau',
            headers=headers)

        print(response)

    # https://docs.mollie.com/reference/v2/profiles-api/enable-voucher-issuer
    def test_enable_voucher_issuer(self):
        print('test_enable_voucher_issuer')

        headers = {
            'Authorization': 'Bearer ',
            'Content-Type': 'application/json',
        }

        data = '{ "contractId": "abc123" }'

        response = requests.post('https://api.mollie.com/v2/profiles/pfl_v9hTwCvYqw/methods'
                                 '/voucher/issuers/appetiz',
                                 headers=headers, data=data)

        print(response)

    # https://docs.mollie.com/reference/v2/profiles-api/disable-voucher-issuer
    def test_disable_voucher_issuer(self):
        print('test_disable_voucher_issuer')

        headers = {
            'Authorization': 'Bearer ',
        }

        response = requests.delete('https://api.mollie.com/v2/profiles/pfl_v9hTwCvYqw/methods/voucher'
                                   '/issuers/appetiz',
                                   headers=headers)

        print(response)

    # https://docs.mollie.com/reference/v2/profiles-api/list-profiles
    def test_list_profiles(self):
        print('test_list_profiles')

        headers = {
            'Authorization': 'Bearer ',
        }

        params = (
            ('limit', '5'),
        )

        response = requests.get('https://api.mollie.com/v2/profiles', headers=headers, params=params)

        print(response)


class UnitTestsOnboardingAPI(unittest.TestCase):
    # https://docs.mollie.com/reference/v2/onboarding-api/get-onboarding-status
    def test_get_onboarding_status(self):
        print('test_get_onboarding_status')

        headers = {
            'Authorization': 'Bearer access_dHar4XY7LxsDOtmnkVtjNVWXLSlXsM',
        }

        response = requests.get('https://api.mollie.com/v2/onboarding/me', headers=headers)

        print(response)

    # https://docs.mollie.com/reference/v2/onboarding-api/submit-onboarding-data
    def test_submit_onboarding_data(self):
        print('test_submit_onboarding_data')

        headers = {
            'Content-Type': 'application/json',
            'Authorization': 'Bearer access_dHar4XY7LxsDOtmnkVtjNVWXLSlXsM',
        }

        data = '{ "organization": { "name": "Mollie B.V.", "address": { "streetAndNumber": ' \
               '"Keizersgracht 126", "postalCode": "1015 CW", "city": "Amsterdam", "country": ' \
               '"NL" }, "registrationNumber": "30204462", "vatNumber": "NL815839091B01" }, ' \
               '"profile": { "name": "Mollie", "url": "https://www.mollie.com", "email": ' \
               '"info@mollie.com", "phone": "+31208202070", "categoryCode": 6012 } }'

        response = requests.post('https://api.mollie.com/v2/onboarding/me', headers=headers, data=data)

        print(response)


class UnitTestsSettlementsAPI(unittest.TestCase):
    # https://docs.mollie.com/reference/v2/settlements-api/get-settlement
    def test_get_settlement(self):
        print('test_get_settlement')

        headers = {
            'Authorization': 'Bearer ',
        }

        response = requests.get('https://api.mollie.com/v2/settlements/stl_jDk30akdN', headers=headers)

        print(response)

    # https://docs.mollie.com/reference/v2/settlements-api/get-next-settlement
    def test_get_next_settlement(self):
        print('test_get_next_settlement')

        headers = {
            'Authorization': 'Bearer ',
        }

        response = requests.get('https://api.mollie.com/v2/settlements/next', headers=headers)

        print(response)

    # https://docs.mollie.com/reference/v2/settlements-api/get-open-settlement
    def test_get_open_settlement(self):
        print('test_get_open_settlement')

        headers = {
            'Authorization': 'Bearer ',
        }

        response = requests.get('https://api.mollie.com/v2/settlements/open', headers=headers)

        print(response)

    # https://docs.mollie.com/reference/v2/settlements-api/list-settlements
    def test_list_settlements(self):
        print('test_list_settlements')

        headers = {
            'Authorization': 'Bearer ',
        }

        params = (
            ('limit', '5'),
        )

        response = requests.get('https://api.mollie.com/v2/settlements', headers=headers, params=params)

        print(response)

    # https://docs.mollie.com/reference/v2/settlements-api/list-settlement-payments
    def test_list_settlement_payments(self):
        print('test_list_settlement_payments')

        headers = {
            'Authorization': 'Bearer ',
        }

        params = (
            ('limit', '5'),
        )

        response = requests.get('https://api.mollie.com/v2/settlements/stl_jDk30akdN/payments', headers=headers,
                                params=params)

        print(response)

    # https://docs.mollie.com/reference/v2/settlements-api/list-settlement-refunds
    def test_list_settlement_refunds(self):
        print('test_list_settlement_refunds')

        headers = {
            'Authorization': 'Bearer ',
        }

        response = requests.get('https://api.mollie.com/v2/settlements/stl_jDk30akdN/refunds', headers=headers)

        print(response)

    # https://docs.mollie.com/reference/v2/settlements-api/list-settlement-chargebacks
    def test_list_settlement_chargebacks(self):
        print('test_list_settlement_chargebacks')

        headers = {
            'Authorization': 'Bearer ',
        }

        response = requests.get('https://api.mollie.com/v2/settlements/stl_jDk30akdN/chargebacks', headers=headers)

        print(response)

    # https://docs.mollie.com/reference/v2/settlements-api/list-settlement-captures
    def test_list_settlement_captures(self):
        print('test_list_settlement_captures')

        headers = {
            'Authorization': 'Bearer ',
        }

        response = requests.get('https://api.mollie.com/v2/settlements/stl_jDk30akdN/captures', headers=headers)

        print(response)


class UnitTestsInvoicesAPI(unittest.TestCase):
    # https://docs.mollie.com/reference/v2/invoices-api/get-invoice
    def test_get_invoice(self):
        print('test_get_invoice')

        headers = {
            'Authorization': 'Bearer ',
        }

        response = requests.get('https://api.mollie.com/v2/invoices/inv_xBEbP9rvAq', headers=headers)

        print(response)

    # https://docs.mollie.com/reference/v2/invoices-api/list-invoices
    def test_list_invoices(self):
        print('test_list_invoices')

        headers = {
            'Authorization': 'Bearer ',
        }

        response = requests.get('https://api.mollie.com/v2/invoices', headers=headers)

        print(response)


class UnitTestsWalletsAPI(unittest.TestCase):
    # https://docs.mollie.com/reference/v2/wallets-api/request-apple-pay-payment-session
    def test_request_apple_pay_payment_session(self):
        print('test_request_apple_pay_payment_session')

        headers = {
            'Authorization': 'Bearer ',
            'Content-Type': 'application/json',
        }

        payload = {
            "domain": "pay.mywebshop.com",
            "validationUrl": "https://apple-pay-gateway-cert.apple.com/paymentservices/paymentSession",
        }

        response = requests.post('https://api.mollie.com/v2/wallets/applepay/sessions', headers=headers, data=payload)

        print(response)


if __name__ == '__main__':
    unittest.main()
