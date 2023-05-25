from django.urls import path
app_name='something'
from app12.views import *
urlpatterns=[
    path('abd/',abd,name='abd'),
    path('prabhas/',prabhas,name='prabhas')
]
