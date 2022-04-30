from django.shortcuts import render

# Create your views here.
from rest_framework import  viewsets
from django.contrib.auth.models import User
from .serializer import KitobxonSerializer, UserSerializer
from .models import Kitobxon
from rest_framework.generics import ListCreateAPIView

class KitobxonAll(viewsets.ModelViewSet):
    queryset = Kitobxon.objects.all()
    serializer_class = KitobxonSerializer
class UserAll(ListCreateAPIView):
        queryset = User.objects.all()
        serializer_class = UserSerializer

# class UserAll(viewsets.ModelViewSet):
#         queryset = User.objects.all()
#         serializer_class = UserSerializer
         
