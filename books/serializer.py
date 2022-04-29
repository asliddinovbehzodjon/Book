from rest_framework import serializers
from .models import Category, Kitoblar
class KitoblarSerializer(serializers.HyperlinkedModelSerializer):

     class Meta:
          model = Kitoblar
          fields = ['id','url','category','name','description','author','user','image','file','size','uploaded','downloaded']

class CategorySerializer(serializers.HyperlinkedModelSerializer):
     kitoblar = KitoblarSerializer(read_only = True,many=True)
     class Meta:
          model = Category
          fields = ('id','url','name', 'kitoblar',)