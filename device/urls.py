  
from .views import DeviceGet,DeviceGetInfo
from django.contrib import admin
from django.urls import path
urlpatterns = [
    path('',DeviceGet.as_view(),name = 'device_list'),
    path('<int:pk>/',DeviceGetInfo.as_view(),name='device_details')

]