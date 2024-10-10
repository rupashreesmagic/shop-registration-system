from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Shop
from .serializers import ShopSerializer
from .utils import haversine
from rest_framework import status

@api_view(['POST'])
def register_shop_api(request):
    serializer = ShopSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)

@api_view(['GET'])
def search_shops_api(request):
    # Get latitude and longitude from request and handle missing values
    user_lat = request.GET.get('latitude')
    user_lon = request.GET.get('longitude')
    
    # Check if both latitude and longitude are present
    if user_lat is None or user_lon is None:
        return Response({'error': 'Latitude and longitude are required'}, status=status.HTTP_400_BAD_REQUEST)
    
    try:
        # Convert to float and handle invalid values
        user_lat = float(user_lat)
        user_lon = float(user_lon)
    except ValueError:
        return Response({'error': 'Invalid latitude or longitude value'}, status=status.HTTP_400_BAD_REQUEST)
    
    # Get all shops and calculate distances
    shops = Shop.objects.all()
    shop_distances = []
    
    for shop in shops:
        distance = haversine(user_lat, user_lon, shop.latitude, shop.longitude)  # Make sure haversine is defined
        shop_distances.append({'shop': shop, 'distance': distance})

    # Sort shops by distance and prepare the response data
    sorted_shops = sorted(shop_distances, key=lambda x: x['distance'])
    sorted_shops_data = [{'name': s['shop'].name, 'distance': s['distance']} for s in sorted_shops]
    
    return Response(sorted_shops_data)
