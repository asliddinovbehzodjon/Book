from django.contrib import admin
from django.utils.html import format_html
# Register your models here.
from .models import Kitobxon
@admin.register(Kitobxon)
class KitobxonAdmin(admin.ModelAdmin):
    
     list_display = ('image','name','starred','name_colored',)
     search_fields = ['name','starred']
     list_per_page = 10
     def name_colored(self, obj):
          html =''
          if obj.starred>10:
               color_code = '00FF00'
               html = '<span style="color: #{};">{}</span>'.format(color_code, "Faol")
          else:
               color_code = 'FF0000'
               
               html = '<span style="color: #{};">{}</span>'.format(color_code, "Hali ko'p kitob yuklashiz kerak")
          return format_html(html)
     name_colored.admin_order_field = 'Status'
     name_colored.short_description = 'Status'