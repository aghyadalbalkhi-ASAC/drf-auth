from django.shortcuts import render
from rest_framework.generics import ListAPIView, RetrieveAPIView, RetrieveDestroyAPIView, RetrieveUpdateDestroyAPIView,CreateAPIView

from .models import Device
from .serializer import DeviceSerializer
from .permissions import PermissionsClass

from rest_framework.permissions import IsAuthenticated

# Create your views here.


class DeviceGet(ListAPIView):
    queryset = Device.objects.all()
    serializer_class = DeviceSerializer
    permission_classes=(PermissionsClass,IsAuthenticated)


class DeviceGetInfo(RetrieveUpdateDestroyAPIView):
    queryset = Device.objects.all()
    serializer_class = DeviceSerializer
    permission_classes=(PermissionsClass,IsAuthenticated)
