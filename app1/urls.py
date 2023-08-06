from django.urls import path
from app1.views import *

app_name='app1'

urlpatterns=[
    path('table/', table,name='table'),
    path('table1/', table1, name='table1'),
    path('table2/', table2, name='table2'),
    path('table3/', table3, name='table3'),
    path('table4/', table4, name='table4'),
    path('table5/', table5, name='table5'),
    path('home/', home, name='home'),
]