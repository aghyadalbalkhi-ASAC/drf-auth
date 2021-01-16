from rest_framework import serializers

from .models import Device

class DeviceSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('id', 'device_name','device_type', 'device_company', 'device_price')
        model = Device