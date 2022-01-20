from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('pop',views.pop,name='pop'),
    path('search',views.search,name='search')
]