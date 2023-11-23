from django.urls import path
from .views import *

urlpatterns = [
    path('signup/', signup, name='signup'),
    path('login/', login, name='login'),
    path('cuslogin/', cuslogin, name='cuslogin'),
    path('index/', index, name='index'),
    path('tables/', tables, name='tables'),
    path('beds/', beds, name='beds'),
    path('chairs/', chairs, name='chairs'),
    path('cabinets/', cabinets, name='cabinets'),
    path('budget1/', budget1, name='budget1'),
    path('budget2/', budget2, name='budget2'),
    path('budget3/', budget3, name='budget3'),
    path('insert/', insertproduct, name='insertproduct'),
    path('submit/', submit_order, name='submit_order'),
    path('index/edit/<int:product>/', edit, name='edit'),
    path('index/edit/editprod/<int:product>/', editprod, name='editprod'),
    path('index/delete/<int:product>/', delete, name='delete'),
    path('transaction/', transaction, name='transaction'),
]
