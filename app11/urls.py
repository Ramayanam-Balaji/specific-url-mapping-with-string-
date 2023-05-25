from django.urls import path
app_name='anything'
from app11.views import *
urlpatterns=[
    path('virat/',virat,name='virat'),
    path('msd/',msd,name='msd')
]