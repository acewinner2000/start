from django.urls import path
from .views import *

urlpatterns = [
    path('', home),
    path('#about',home),
    path('#features',home),
    path('#hero',home),
    path('#services',home),
    path('#pricing',home),
    path('#contact',home),
    path('login',login)
    

]