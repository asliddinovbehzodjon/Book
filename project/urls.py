from django.contrib import admin
from django.urls import path,include
from django.conf import  settings
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from django.conf.urls.static import static

admin.site.site_header = "BigBook"
admin.site.site_title = "BigBook"
admin.site.site_url = "BigBook"
urlpatterns = [
    path('crazy/api/owner/', admin.site.urls),
    path('api/v1/',include('books.urls')),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    
]
urlpatterns +=static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)