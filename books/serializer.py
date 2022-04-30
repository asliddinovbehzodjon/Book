from rest_framework import serializers
from .models import Category, Kitoblar, Reklama
class KitoblarSerializer(serializers.HyperlinkedModelSerializer):

     class Meta:
          model = Kitoblar
          fields = ['id','url','category','name','description','author','user','image','file','size','uploaded','downloaded']

class CategorySerializer(serializers.HyperlinkedModelSerializer):
     kitoblar = KitoblarSerializer(read_only = True,many=True)
     class Meta:
          model = Category
          fields = ('id','url','name', 'kitoblar',)
class ReklamaSerializer(serializers.ModelSerializer):
     class Meta:
          model = Reklama
          fields = "__all__"