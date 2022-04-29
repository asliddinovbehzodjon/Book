from django.contrib import admin
from django.urls import reverse
from django.utils.safestring import mark_safe
# Register your models here.
from .models import Kitoblar,Category
@admin.register(Kitoblar)
class KitoblarAdmin(admin.ModelAdmin):
     list_display = ['name','author','downloaded','uploader','filesize']
     list_per_page = 10
     search_fields= ['name','description','author','user__name']
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
     list_display = ('name',)
     list_per_page = 5
     search_fields = ('name',)


     
     
     
     
          