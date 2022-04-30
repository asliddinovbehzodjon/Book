from django.contrib import admin
from django.urls import path,include
from django.conf import  settings
from django.conf.urls.static import static

admin.site.site_header = "BigBook"
admin.site.site_title = "BigBook"
admin.site.site_url = "BigBook"
urlpatterns = [
    path('api/owner/', admin.site.urls),
    path('api/v1/',include('books.urls')),
  
    
]
urlpatterns +=static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)