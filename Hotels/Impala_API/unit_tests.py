import unittest
from requests_tor import RequestsTor

endpoint = "https://api.getimpala.com"
api_key = ''


# https://docs.getimpala.com/#allocations
class UnitTestsImpalaAPIWithTorRequest(unittest.TestCase):
    def test_Authorization(self):
        print("test_Authorization")

        url = endpoint

        headers = {
            'Authorization': 'Bearer ' + api_key
        }

        rt = RequestsTor()

        r = rt.get(url, headers=headers)

        print(r.text)


class UnitTestsImpalaAPIAllocationsGroupBlocksWithTorRequest(unittest.TestCase):
    def test_Retrieve_an_Allocation(self):
        print("test_Retrieve_an_Allocation")

        hotelId = ""

        allocationId = ""

        url = endpoint + "/v2/hotel/" + hotelId + "/allocations/" + allocationId

        headers = {
            'Authorization': 'Bearer ' + api_key
        }

        rt = RequestsTor()

        r = rt.get(url, headers=headers)

        print(r.text)

    def test_Retrieve_all_Allocations(self):
        print("test_Retrieve_all_Allocations")

        hotelId = ""

        url = endpoint + "/v2/hotel/" + hotelId + "/allocations"

        headers = {
            'Authorization': 'Bearer ' + api_key
        }

        rt = RequestsTor()

        r = rt.get(url, headers=headers)

        print(r.text)


class UnitTestsImpalaAPIAreasRoomsBedsWithTorRequest(unittest.TestCase):
    def test_Retrieve_an_Area(self):
        print("test_Retrieve_an_Area")

        hotelId = ""

        areaId = ""

        url = endpoint + "/v2/hotel/" + hotelId + "/areas/" + areaId

        headers = {
            'Authorization': 'Bearer ' + api_key
        }

        rt = RequestsTor()

        r = rt.get(url, headers=headers)

        print(r.text)

    def test_Retrieve_all_Areas(self):
        print("test_Retrieve_all_Areas")

        hotelId = ""

        url = endpoint + "/v2/hotel/" + hotelId + "/areas"

        params = {
            'name': 'name'
        }

        headers = {
            'Authorization': 'Bearer ' + api_key
        }

        rt = RequestsTor()

        r = rt.get(url, headers=headers, params=params)

        print(r.text)


class UnitTestsImpalaAPIAreaTypesRoomTypesWithTorRequest(unittest.TestCase):
    def test_Retrieve_an_Area_Type(self):
        print("test_Retrieve_an_Area_Type")

        hotelId = ""

        areaTypeId = ""

        url = endpoint + "/v2/hotel/" + hotelId + "/area-types/" + areaTypeId

        headers = {
            'Authorization': 'Bearer ' + api_key
        }

        rt = RequestsTor()

        r = rt.get(url, headers=headers)

        print(r.text)

    def test_Retrieve_all_Area_Types(self):
        print("test_Retrieve_all_Area_Types")

        hotelId = ""

        url = endpoint + "/v2/hotel/" + hotelId + "/area-types"

        headers = {
            'Authorization': 'Bearer ' + api_key
        }

        rt = RequestsTor()

        r = rt.get(url, headers=headers)

        print(r.text)


class UnitTestsImpalaAPIBillsWithTorRequest(unittest.TestCase):
    def test_Retrieve_a_Bill(self):
        print("test_Retrieve_a_Bill")

        hotelId = ""

        billId = ""

        url = endpoint + "/v2/hotel/" + hotelId + "/bills/" + billId

        headers = {
            'Authorization': 'Bearer ' + api_key
        }

        rt = RequestsTor()

        r = rt.get(url, headers=headers)

        print(r.text)

    def test_Retrieve_Bills_for_a_Booking(self):
        print("test_Retrieve_Bills_for_a_Booking")

        hotelId = ""

        bookingId = ""

        url = endpoint + "/v2/hotel/" + hotelId + "/bookings/" + bookingId + "/bills"

        headers = {
            'Authorization': 'Bearer ' + api_key
        }

        rt = RequestsTor()

        r = rt.get(url, headers=headers)

        print(r.text)


class UnitTestsImpalaAPIBookingSetsWithTorRequest(unittest.TestCase):
    def test_Retrieve_all_Booking_Sets(self):
        print("test_Retrieve_all_Booking_Sets")

        hotelId = ""

        url = endpoint + "/v2/hotel/" + hotelId + "/booking-sets"

        headers = {
            'Authorization': 'Bearer ' + api_key
        }

        params = {
            'startDate': 'startDate',
            'endDate': 'endDate'
        }

        rt = RequestsTor()

        r = rt.get(url, headers=headers, params=params)

        print(r.text)

    def test_Retrieve_a_Booking_Set(self):
        print("test_Retrieve_a_Booking_Set")

        hotelId = ""

        bookingSetId = ""

        url = endpoint + "/v2/hotel/" + hotelId + "/booking-sets/" + bookingSetId

        headers = {
            'Authorization': 'Bearer ' + api_key
        }

        rt = RequestsTor()

        r = rt.get(url, headers=headers)

        print(r.text)


class UnitTestsImpalaAPIBookingsWithTorRequest(unittest.TestCase):
    def test_Retrieve_a_Booking(self):
        print("test_Retrieve_a_Booking")

        hotelId = ""

        bookingId = ""

        url = endpoint + "/v2/hotel/" + hotelId + "/bookings/" + bookingId

        headers = {
            'Authorization': 'Bearer ' + api_key
        }

        rt = RequestsTor()

        r = rt.get(url, headers=headers)

        print(r.text)

    def test_Retrieve_all_Bookings(self):
        print("test_Retrieve_all_Bookings")

        hotelId = ""

        url = endpoint + "/v2/hotel/" + hotelId + "/bookings"

        params = {
            'startDate': 'startDate',
            'endDate': 'endDate'
        }

        headers = {
            'Authorization': 'Bearer ' + api_key
        }

        rt = RequestsTor()

        r = rt.get(url, headers=headers, params=params)

        print(r.text)


class UnitTestsImpalaAPIChargesWithTorRequest(unittest.TestCase):
    def test_Retrieve_a_Charge(self):
        print("test_Retrieve_a_Charge")

        hotelId = ""

        billId = ""

        chargeId = ""

        url = endpoint + "/v2/hotel/" + hotelId + "/bill/" + billId + "/charge/" + chargeId

        headers = {
            'Authorization': 'Bearer ' + api_key
        }

        rt = RequestsTor()

        r = rt.get(url, headers=headers)

        print(r.text)

    def test_Retrieve_all_Charges_on_a_Bill(self):
        print("test_Retrieve_all_Charges_on_a_Bill")

        hotelId = ""

        billId = ""

        url = endpoint + "/v2/hotel/" + hotelId + "/bills/" + billId + "/charges"

        headers = {
            'Authorization': 'Bearer ' + api_key
        }

        rt = RequestsTor()

        r = rt.get(url, headers=headers)

        print(r.text)


class UnitTestsImpalaAPICompaniesWithTorRequest(unittest.TestCase):
    def test_Retrieve_a_Company(self):
        print("test_Retrieve_a_Company")

        hotelId = ""

        companyId = ""

        url = endpoint + "/v2/hotel/" + hotelId + "/companies/" + companyId

        headers = {
            'Authorization': 'Bearer ' + api_key
        }

        rt = RequestsTor()

        r = rt.get(url, headers=headers)

        print(r.text)


class UnitTestsImpalaAPIExtrasWithTorRequest(unittest.TestCase):
    def test_Retrieve_a_Extra(self):
        print("test_Retrieve_a_Extra")

        hotelId = ""

        extraId = ""

        url = endpoint + "/v2/hotel/" + hotelId + "/extras/" + extraId

        headers = {
            'Authorization': 'Bearer ' + api_key
        }

        rt = RequestsTor()

        r = rt.get(url, headers=headers)

        print(r.text)

    def test_Retrieve_all_Extras(self):
        print("test_Retrieve_all_Extras")

        hotelId = ""

        url = endpoint + "/v2/hotel/" + hotelId + "/extras"

        headers = {
            'Authorization': 'Bearer ' + api_key
        }

        rt = RequestsTor()

        r = rt.get(url, headers=headers)

        print(r.text)


class UnitTestsImpalaAPIGuestsWithTorRequest(unittest.TestCase):
    def test_Retrieve_a_Guest(self):
        print("test_Retrieve_a_Guest")

        hotelId = ""

        guestId = ""

        url = endpoint + "/v2/hotel/" + hotelId + "/guests/" + guestId

        headers = {
            'Authorization': 'Bearer ' + api_key
        }

        rt = RequestsTor()

        r = rt.get(url, headers=headers)

        print(r.text)

    def test_Retrieve_all_Guests(self):
        print("test_Retrieve_all_Guests")

        hotelId = ""

        url = endpoint + "/v2/hotel/" + hotelId + "/guests"

        params = {
            'startDate': 'startDate',
            'endDate': 'endDate'
        }

        headers = {
            'Authorization': 'Bearer ' + api_key
        }

        rt = RequestsTor()

        r = rt.get(url, headers=headers, params=params)

        print(r.text)


class UnitTestsImpalaAPIPaymentsWithTorRequest(unittest.TestCase):
    def test_Retrieve_a_Paymentt(self):
        print("test_Retrieve_a_Paymentt")

        hotelId = ""

        billId = ""

        paymentId = ""

        url = endpoint + "/v2/hotel/" + hotelId + "/bills/" + billId + "/payment/" + paymentId

        headers = {
            'Authorization': 'Bearer ' + api_key
        }

        rt = RequestsTor()

        r = rt.get(url, headers=headers)

        print(r.text)

    def test_Retrieve_all_Payments_on_a_Bill(self):
        print("test_Retrieve_all_Payments_on_a_Bill")

        hotelId = ""

        billId = ""

        url = endpoint + "/v2/hotel/" + hotelId + "/bills/" + billId + "/payments"

        headers = {
            'Authorization': 'Bearer ' + api_key
        }

        rt = RequestsTor()

        r = rt.get(url, headers=headers)

        print(r.text)


class UnitTestsImpalaAPIRatePlansWithTorRequest(unittest.TestCase):
    def test_Make_a_pricing_decision_for_a_Rate_Plan(self):
        print("test_Make_a_pricing_decision_for_a_Rate_Plan")

        hotelId = ""

        ratePlanId = ""

        url = endpoint + "/v2/hotel/" + hotelId + "/rate-plans/" + ratePlanId + "/price"

        payload = {
            'date': '',
            'amountDescription': {
                "type": "ABSOLUTE",
                "value": "5000"
            },
            'areaTypeId': 'areaTypeId'
        }

        headers = {
            'Authorization': 'Bearer ' + api_key
        }

        rt = RequestsTor()

        r = rt.put(url, headers=headers, data=payload)

        print(r.text)

    def test_Retrieve_a_Rate_Plan(self):
        print("test_Retrieve_a_Rate_Plan")

        hotelId = ""

        ratePlanId = ""

        url = endpoint + "/v2/hotel/" + hotelId + "/rate-plans/" + ratePlanId

        headers = {
            'Authorization': 'Bearer ' + api_key
        }

        rt = RequestsTor()

        r = rt.put(url, headers=headers)

        print(r.text)

    def test_Retrieve_all_Rate_Plans(self):
        print("test_Retrieve_all_Rate_Plans")

        hotelId = ""

        url = endpoint + "/v2/hotel/" + hotelId + "/rate-plans"

        params = {
            'accessCode': 'accessCode'
        }

        headers = {
            'Authorization': 'Bearer ' + api_key
        }

        rt = RequestsTor()

        r = rt.put(url, headers=headers, params=params)

        print(r.text)


if __name__ == '__main__':
    unittest.main()
