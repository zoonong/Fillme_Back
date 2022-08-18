from django.urls import path
from .views import *

app_name="notice"
urlpatterns = [
   path('',my_notice,name='my_notice'),
]