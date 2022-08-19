from django.urls import path
from .views import *

app_name="mypage"
urlpatterns = [
   path('',my_profile,name='my_profile'),
   path('profile_update/',profile_update,name='profile_update'),
   path('<int:user_id>/',user_profile,name='user_profile'),
   path('persona/',my_persona_list_create,name='my_persona_list_create'),
   path('persona/<int:persona_id>/',my_persona_rud,name='my_persona_rud'),
   path('persona/<int:persona_id>/openpublic/',persona_public,name='persona_public'),
   path('<int:user_id>/persona/',user_persona_list,name='user_persona_list'),
   path('<int:user_id>/persona/<int:persona_id>/',user_persona_detail,name='user_persona_detail'),
   path('profile_persona/',my_profile_persona,name='my_profile_persona'),
   path('profile_persona/<int:user_id>/',user_profile_persona,name='user_profile_persona'),
   path('random_profile/',random_user_list, name='random_user_list'),
   path('following_list/',my_following_list,name='my_following_list'),
   path('<int:user_id>/following_list/',user_following_list,name='user_following_list'),
   path('follow/<int:user_id>/',follow,name='follow'),
   path('persona_follow/<int:persona_id>/',persona_follow,name='persona_follow'),
   path('new_feelings/',new_feelings,name='new_feelings'),
]