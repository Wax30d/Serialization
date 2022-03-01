from rest_framework import serializers


# first style of serialization
# this class has the ability to serialize fields
class MerchantSerializer(serializers.Serializer):
    merchant_name = serializers.CharField()
    merchant_code = serializers.CharField()
    merchant_address = serializers.CharField()
