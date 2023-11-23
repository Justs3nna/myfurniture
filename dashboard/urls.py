from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name='homepage'),   
    path('aboutus/', aboutus, name='aboutus'),
]
