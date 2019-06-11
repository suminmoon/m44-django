# 내가 새로 생성하는 파일

from django.urls import path
from . import views

app_name = 'boards'

urlpatterns = [

    path('', views.index, name='index'),
    path('new/', views.new, name='new'),  # 사용자의 입력을 받아서 게시글을 작성하는 곳
    # path('create/', views.create, name='create'),  # 입력받는 데이터를 전송 받고 실제 DB에 작성 및 사용자에서 피드백
    path('<int:id>/', views.detail, name='detail'),  # 특정 게시글로 들어가기 /boards/<id>
    path('<int:id>/delete/', views.delete, name='delete'),
    path('<int:id>/edit/', views.edit, name='edit'),  # 게시글 수정 페이지 렌더링
    # path('<int:id>/update/', views.update, name='update'),  # 사용자가 입력한 수정 데이더를 전송받고 실제 DB에 수정 후 저장

]