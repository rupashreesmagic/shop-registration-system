
from .views import RegisterShopViewset,ShopViewSet
from rest_framework.routers import DefaultRouter
from django.urls import path, include
# from django.contrib import admin



router = DefaultRouter()
router.register('register_shop',RegisterShopViewset ,basename='register_shop')
router.register('search_shop',ShopViewSet ,basename='search_shop')


urlpatterns = [
    path('', include(router.urls)),
    ]


