from django.shortcuts import render, redirect
from shops.serializers import RegisterShopSerializer,ShopSearchSerializer
from shops.utils import http_200_response, http_400_response, http_500_response,haversine
from .forms import ShopRegistrationForm
from .models import Shop
from rest_framework.viewsets import ModelViewSet
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema

class RegisterShopViewset(ModelViewSet):
    serializer_class = RegisterShopSerializer
    http_method_names = ["post"]

    def get_queryset(self):
        queryset = Shop.objects.all()
        return queryset
    
    def create(self, request, *args, **kwargs):
        try:
            serializer = self.serializer_class(data = request.data)
            if serializer.is_valid():
                data = Shop.objects.filter(name = serializer.data['name']).last()
                user_data = {'name':data.name, 'latitude':data.latitude, 'longitude':data.longitude}
                return http_200_response(message="Shop registered successfully.",data=user_data)
            else:
                if list(serializer.errors.keys())[0] != "error":
                    return http_400_response(message=f"{list(serializer.errors.keys())[0]} : {serializer.errors[list(serializer.errors.keys())[0]][0]}")
                else:
                    return http_400_response(message=serializer.errors[list(serializer.errors.keys())[0]][0])
        except Exception as e:
            return http_500_response(error=str(e))
        

class ShopViewSet(ModelViewSet):
    queryset = Shop.objects.all()
    serializer_class = ShopSearchSerializer
    http_method_names = ["get"]

    user_latitude = openapi.Parameter('user_latitude', in_=openapi.IN_QUERY, type=openapi.TYPE_NUMBER)
    user_longitude = openapi.Parameter('user_longitude', in_=openapi.IN_QUERY, type=openapi.TYPE_NUMBER)

    @swagger_auto_schema(manual_parameters=[user_latitude, user_longitude])
    def list(self, request, *args, **kwargs):
        user_latitude = request.query_params.get('user_latitude')
        user_longitude = request.query_params.get('user_longitude')

        # Validate latitude and longitude
        if user_latitude is None or user_longitude is None:
            return http_400_response(message="Latitude and longitude must be provided.")

        try:
            user_latitude = float(user_latitude)
            user_longitude = float(user_longitude)
        except ValueError:
            return http_400_response(message="Invalid latitude or longitude format.")

        shops = self.get_queryset()
        shop_distances = []

        for shop in shops:
            shop_latitude = float(shop.latitude)
            shop_longitude = float(shop.longitude)
            distance = haversine(user_latitude, user_longitude, shop_latitude, shop_longitude)
            shop_distances.append((shop, distance))

        sorted_shops = sorted(shop_distances, key=lambda x: x[1])
        sorted_shop_data = [
            {
                "id": shop[0].id,
                "name": shop[0].name,
                "latitude": shop[0].latitude,
                "longitude": shop[0].longitude,
                "distance": shop[1]
            } for shop in sorted_shops
        ]
        return http_200_response(message="Shops retrieved successfully.",data=sorted_shop_data)