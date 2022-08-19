from django.urls import path
from .views import *

app_name="usersearch"
urlpatterns = [
   path('',search_user,name='search_user'),
   path('history/',history_list_create,name='history_list_create'),
   path('history/<int:history_id>/',delete_history,name='delete_history'),
]