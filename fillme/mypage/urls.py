from django.urls import path
from .views import *

app_name="mypage"
urlpatterns = [
   path('',my_profile,name='my_profile'),
   path('profile_update/',profile_update,name='profile_update'),
   path('<int:id>/',user_profile,name='user_profile'),
]