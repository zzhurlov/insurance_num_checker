from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIRequestFactory
from rest_framework import status
from checker.models import InsuranceNumber
from checker.views import CheckInsuranceNumberView


class CheckInsuranceNumberViewTests(TestCase):
    def setUp(self):
        self.factory = APIRequestFactory()
        self.insurance_number = InsuranceNumber.objects.create(number="12602903624")
        self.view = CheckInsuranceNumberView.as_view()
        self.url = reverse("checker")

    def test_post_check_number_good_request(self):
        url = self.url

        data1 = {"number": "126-029-036 24"}
        data2 = {"number": "126-029-036 24"}

        request1 = self.factory.post(url, data1, format="json")
        request2 = self.factory.post(url, data2, format="json")

        response1 = self.view(request1)
        response2 = self.view(request2)

        self.assertEqual(response1.status_code, status.HTTP_200_OK)
        self.assertEqual(response2.status_code, status.HTTP_200_OK)

    def test_post_check_number_bad_request(self):
        url = reverse("checker")

        data1 = {"number": "abcdefghijk"}
        data2 = {"number": "!**343sdf#^^#$"}
        data3 = {"number": "32243305624"}
        data4 = {"number": "43-3106-455 65"}
        data5 = {"number": "000-000-000 00"}
        data6 = {"number": ""}

        request1 = self.factory.post(url, data1, format="json")
        request2 = self.factory.post(url, data2, format="json")
        request3 = self.factory.post(url, data3, format="json")
        request4 = self.factory.post(url, data4, format="json")
        request5 = self.factory.post(url, data5, format="json")
        request6 = self.factory.post(url, data6, format="json")

        response1 = self.view(request1)
        response2 = self.view(request2)
        response3 = self.view(request3)
        response4 = self.view(request4)
        response5 = self.view(request5)
        response6 = self.view(request6)

        self.assertEqual(response1.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response2.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response3.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response4.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response5.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response6.status_code, status.HTTP_400_BAD_REQUEST)
