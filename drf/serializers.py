from rest_framework import serializers
from .models import Merchant

# first style of serialization
# this class has the ability to serialize fields

# class MerchantSerializer(serializers.Serializer):
#     merchant_name = serializers.CharField()
#     merchant_code = serializers.CharField()
#     merchant_address = serializers.CharField()


# second style of serialization is Model serializer
# this class has the ability to serialize model

class MerchantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Merchant
        fields = '__all__'
