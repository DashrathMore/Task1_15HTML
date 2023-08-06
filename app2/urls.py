from django.urls import path
from app2.views import *
app_name='app2'
urlpatterns=[
    path('login1/', login1, name='login1'),
    path('login2/', login2, name='login2'),
    path('login3/', login3, name='login3'),
    path('card/', card, name='card'),

]