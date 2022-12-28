from django.urls import path
from app2.views import *
app_name='something2'

urlpatterns=[
    path('one/',one,name='one'),
    path('two/',two,name='two'),
]