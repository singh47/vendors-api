from rest_framework import serializers
from api.models import Vendors

class VendorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vendors
        fields = ['vendor_name', 'vendor_number', 'agreement_number',
                  'contract_status', 'contract_category', 'contract_date',
                  'contract_expiry']


class ExpiredCount(serializers.Serializer):
    expired = serializers.IntegerField()
    active = serializers.IntegerField()


class CategoryCount(serializers.Serializer):
    IT = serializers.IntegerField()
    Build_Service = serializers.IntegerField()
    Fleet = serializers.IntegerField()
    Mobile_Technology = serializers.IntegerField()
    Network = serializers.IntegerField()
    Power = serializers.IntegerField()
    Fiber = serializers.IntegerField()