from django.urls import path,include
from rest_framework import routers
from .views import *
from readers.views import *


router = routers.DefaultRouter()
router.register('books',KitoblarAll)
router.register('readers',KitobxonAll)
router.register('search',KitobSearch,basename='search')
router.register('category',Categories)
router.register('users',UserAll)
router.register('channels',ReklamaAll)
router.register('upload',BookUpload)

urlpatterns =[
    path('',include(router.urls)),

]