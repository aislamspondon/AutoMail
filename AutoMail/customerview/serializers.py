from customerview.models import CustomerInfo, CustomerPreview
from rest_framework import serializers


class CustomerInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomerInfo
        fields = '__all__'


class CustomerPreviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomerPreview
        fields = '__all__'
