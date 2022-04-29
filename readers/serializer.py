from rest_framework import  serializers
from .models import Kitobxon
from django.contrib.auth.models import User
from books.serializer import KitoblarSerializer
class KitobxonSerializer(serializers.HyperlinkedModelSerializer):
    books = KitoblarSerializer(many=True,read_only=True)
    class Meta:
        model = Kitobxon
        fields = ['id','url', 'name','starred','books']

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['username','email','password']