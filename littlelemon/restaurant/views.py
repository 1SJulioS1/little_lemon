from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics
from rest_framework.viewsets import ModelViewSet
from rest_framework import permissions

from django.shortcuts import render
from django.contrib.auth.models import User

from .models import Menu, Booking
from .serializers import UserSerializer, BookingSerializer, MenuSerializer
# Create your views here.


# def menu(request):
#    menu_data = Menu.objects.all()
#    main_data = {'menu': menu_data}
#    return render(request, 'menu.html', {'menu': main_data})

def index(request):
    return render(request, 'index.html', {})


class BookingViewSet(ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer


class MenuItemsView(generics.ListCreateAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer


class SingleMenuItemView(generics.RetrieveUpdateAPIView, generics.DestroyAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer


class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]
