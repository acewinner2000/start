from django.urls import path
from .views import sp
from .views import home
urlpatterns = [
    
    path ('',home),
    path('',sp)
]
