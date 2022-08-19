from django.urls import path
from .views import *
from . import views

app_name = "post"
urlpatterns = [
    path('', post_list_create, name = 'post_list_create'), # 모든 게시물 가져 오기 및 사진 게시물 작성
    path('<int:post_pk>/', post_detail_update_delete, name = 'post_detail_update_delete'), # 사진 - 특정 게시물 가져 오기 / 수정 / 삭제
    path('video_post_create/', video_post_create, name = 'video_post_create'),# 영상 - 특정 게시물 작성하기
    path('<int:post_pk>/video_post_update_delete/', video_post_update_delete, name = 'video_post_update_delete'), # 영상 - 특정 게시물 가져 오기 / 수정 / 삭제
    path('myfollow/', following_post_list, name = 'following_post_list'), # 내가 팔로우한 유저의 게시글만 조회가능한 api
    path('mypost/', my_post_list, name = 'my_post_list'), # 내가 작성한 게시글 목록을 조회하는 api
    path('mypost/<int:persona_id>/', my_persona_post_list, name = 'my_persona_post_list'), # 나의 특정 페르소나가 작성한 게시글 목록을 조회하는 api
    path('user_post/<int:user_id>/', user_post_list, name = 'user_post_list'), # 내가 아닌 특정 유저가 작성한 게시글만 조회하는 api
    path('user_post/<int:user_id>/<int:persona_id>/', user_persona_post_list, name = 'user_persona_post_list'), # 내가 아닌 특정 유저의 특정 페르소나가 작성한 게시글만 조회하는 api
    path('follow_persona/', subfollowing_post_list, name = 'subfollowing_post_list'), # 내가 소식받기한 페르소나의 게시글만 조회하는 api
    path('<int:post_id>/comments/', post_comment_list, name = 'post_comment_list'), # 특정 게시물의 댓글 보기 / 작성하기
    path('<int:post_pk>/comments/<int:comment_pk>/', post_comment_detail_update_delete, name = 'post_comment_detail_update_delete'), # 특정 게시물의 특정 댓글 보기 / 수정 / 삭제
    path('<int:post_pk>/post_likes/', post_likes, name = 'post_likes'), # 해당 게시물 좋아요 수 보기
    path('<int:post_pk>/send_like/', send_like, name = 'send_like') # 해당 게시물 속 좋아요 누르기 / 취소하기
]