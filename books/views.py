from django.shortcuts import render
from requests import Response
# Create your views here.
from django_filters import rest_framework as filters
from rest_framework import viewsets
from django.db.models import Q
from rest_framework.pagination import PageNumberPagination,LimitOffsetPagination
from .models import Category, Kitoblar
from rest_framework import status
from .serializer import CategorySerializer, KitoblarSerializer

from rest_framework.response import Response

class KitoblarAll(viewsets.ModelViewSet):
    queryset = Kitoblar.objects.all()
    serializer_class = KitoblarSerializer
    pagination_class = PageNumberPagination
class Categories(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    pagination_class = PageNumberPagination
class KitobSearch(viewsets.ModelViewSet):
      serializer_class = KitoblarSerializer
      pagination_class = PageNumberPagination
      def get_queryset(self):
          books = Kitoblar.objects.all()
          return  books
      def retrieve(self, request, *args, **kwargs):
          params = kwargs
          kitoblar = Kitoblar.objects.filter(Q(name__icontains=params['pk']) |Q(description__icontains=params['pk']) | Q(author__icontains=params['pk']) |  Q(janr__icontains=params['pk']))
          serializer = KitoblarSerializer(kitoblar,many=True,context={'request': request})
          return Response(serializer.data,status=status.HTTP_200_OK)




     