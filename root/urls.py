from django.urls import path
from .views import *

urlpatterns = [
    path('', home),
    path('#about',about),
    path('#features',about),
    path('#hero',about),
    path('#services',about),
    path('#pricing',about),
    path('#contact',about),
    

]