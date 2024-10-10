import math
from rest_framework.response import Response
from rest_framework import status


def haversine(lat1, lon1, lat2, lon2):
    #print("ggggggggggggggggggggggggg")
    R = 6371  # Earth radius in kilometers
    dlat = math.radians(lat2 - lat1)
    dlon = math.radians(lon2 - lon1)
    a = math.sin(dlat / 2) ** 2 + math.cos(math.radians(lat1)) * math.cos(math.radians(lat2)) * math.sin(dlon / 2) ** 2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    return R * c

def http_200_response(message,error="",data=""):
    context={
        "status":True,
        "status_code":200,
        "message":message,
        "error":error,
        'data':data
        }
    
    return Response(context,status=status.HTTP_200_OK)

def http_400_response(message,error="",data=""):
    context={
        "status":False,
        "status_code":400,
        "message":message,
        "error":error,
        "data":data
        }
    return Response(context,status=status.HTTP_400_BAD_REQUEST)

def http_500_response(error,message="",data=""):
    context={
        "status":False,
        "status_code":500,
        "message":"Something Went Wrong!",
        "error":error,
        "data":data
        }
    return Response(context,status=status.HTTP_500_INTERNAL_SERVER_ERROR)