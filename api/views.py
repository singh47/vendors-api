from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework.views import APIView
from api.models import Vendors
from api.serializers import VendorSerializer, ExpiredCount, CategoryCount
from api.utils import load_execl_data
from api.utils import string_to_date
# Create your views here.


# returns all vendors data
class index(APIView):

    def get(self, request):
        vendors = Vendors.objects.all()[:50]
        vendor_serializer = VendorSerializer(vendors, many=True)
        return Response(vendor_serializer.data)


class load_data(APIView):

    def get(self, request):
        if Vendors.objects.exists():
            return HttpResponse("Data Already Exists")
        else:
            data = load_execl_data()
            for dataset in data:
                contract_date = string_to_date(dataset[6])
                contract_expiry = string_to_date(dataset[7])
                try:
                    Vendors(vendor_name=dataset[1], vendor_number=dataset[2],
                        agreement_number=dataset[3], contract_status=dataset[4],
                        contract_category=dataset[5], contract_date=dataset[6],
                        contract_expiry=string_to_date(dataset[7])).save()
                except:
                    print(f"Error importing agreement number: {dataset[3]}")
            return HttpResponse("Imported successfully")


# returns total expired contracts
class get_expired(APIView):

    def get(self, request):
        vendors_count = Vendors.objects.filter(contract_status='Expired').count()
        total_count = Vendors.objects.count()
        valid_count = total_count - vendors_count
        vendor_serializer = ExpiredCount(data={'expired':vendors_count, 'active':valid_count })
        if vendor_serializer.is_valid():
            return Response(vendor_serializer.data)
        return Response(vendor_serializer.errors)


# Categories percentage
class get_categories(APIView):

    def get(self, request):
        it_count = Vendors.objects.filter(contract_category='IT').count()
        build_count = Vendors.objects.filter(contract_category='Build Services').count()
        fleet_count = Vendors.objects.filter(contract_category='Fleet').count()
        mobile_count = Vendors.objects.filter(contract_category='Mobile Technology').count()
        network_count = Vendors.objects.filter(contract_category='Network').count()
        fiber_count = Vendors.objects.filter(contract_category='Fiber').count()
        power_count = Vendors.objects.filter(contract_category='Power, Space & HVAC ').count()
        category_serializer = CategoryCount(data={'IT':it_count, 'Build_Service':build_count,
                                                'Fleet': fleet_count, 'Mobile_Technology': mobile_count,
                                                'Network': network_count, 'Power': power_count,
                                                'Fiber': fiber_count })
        if category_serializer.is_valid():
            return Response(category_serializer.data)
        else:
            return Response(category_serializer.errors)