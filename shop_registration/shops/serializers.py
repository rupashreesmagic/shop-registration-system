# shops/serializers.py
from django.db import transaction
from rest_framework import serializers
from .models import Shop
import re

class ShopSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shop
        fields = ['id', 'name', 'latitude', 'longitude']
        extra_kwargs = {
            'name': {'required': True},
            'latitude': {'required': True},
            'longitude': {'required': True},
        }

LATITUDE_REGEX = r'^-?(90(\.0+)?|[1-8]?[0-9](\.[0-9]+)?)$'
LONGITUDE_REGEX = r'^-?(180(\.0+)?|1[0-7][0-9](\.[0-9]+)?|[1-9]?[0-9](\.[0-9]+)?)$'


class RegisterShopSerializer(serializers.ModelSerializer):
    name = serializers.CharField(required = True,error_messages={'invalid': 'Please enter a valid first name.'})
    latitude = serializers.CharField(required = True,error_messages={'invalid': 'Please enter a valid last name.'})
    longitude = serializers.CharField(required = False,error_messages={'invalid': 'Please enter a valid role.'})
    
    class Meta:
        model = Shop
        fields = ['id','name','latitude','longitude']

    def validate(self, attrs):
        # try:
            name = attrs.get('name')
            latitude = attrs.get('latitude')
            longitude = attrs.get('longitude')

            if not re.match(LATITUDE_REGEX, str(latitude)):
                raise serializers.ValidationError({'error':'Please provide valid latitude.'})
            
            if not re.match(LONGITUDE_REGEX, str(longitude)):
                raise serializers.ValidationError({'error':'Please provide valid longitude .'})

            obj = Shop()
            with transaction.atomic():
                obj.name=name
                obj.latitude=latitude
                obj.longitude=longitude

                obj.save()
            return attrs
        
class ShopSearchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shop
        fields = ['id', 'name', 'latitude', 'longitude']
