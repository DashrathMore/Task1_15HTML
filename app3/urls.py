from django.urls import path
from app3.views import *
app_name='app3'
urlpatterns=[
    path('animation/', animation, name='animation'),
    path('animation2/', animation2, name='animation2'),
    path('animation3/', animation3, name='animation3'),
]