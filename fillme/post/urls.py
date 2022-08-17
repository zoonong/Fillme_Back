from django.urls import path
from .views import *
from . import views

app_name = "post"
urlpatterns = [
    path('', post_list_create, name = 'post_list_create'), # 모든 게시물 가져 오기 및 사진 게시물 작성
    path('<int:post_pk>/', post_detail_update_delete, name = 'post_detail_update_delete'), # 사진 - 특정 게시물 가져 오기 / 수정 / 삭제
    path('video_post_create/', video_post_create, name = 'video_post_create'),# 영상 - 특정 게시물 작성하기
    path('<int:post_pk>/video_post_update_delete/', video_post_update_delete, name = 'video_post_update_delete'), # 영상 - 특정 게시물 가져 오기 / 수정 / 삭제
    path('mypost/', my_post_list, name = 'my_post_list'), # 내가 작성한 게시글 목록을 조회하는 api
    path('<int:post_id>/comments/', post_comment_list, name = 'post_comment_list'), # 특정 게시물의 댓글 보기 / 작성하기
    path('<int:post_pk>/comments/<int:comment_pk>/', post_comment_detail_update_delete, name = 'post_comment_detail_update_delete'), # 특정 게시물의 특정 댓글 보기 / 수정 / 삭제
    path('<int:post_pk>/post_likes/', post_likes, name = 'post_likes'), # 해당 게시물 좋아요 수 보기
    path('<int:post_pk>/send_like/', send_like, name = 'send_like') # 해당 게시물 속 좋아요 누르기 / 취소하기
]