from django.urls import path
from . import views


app_name = 'movies'

urlpatterns = [

    path('', views.index, name = 'index'),  # 목록
    path('create/', views.create, name='create'),  # method 분기
    path('<int:movie_id>/', views.detail, name='detail'),
    path('<int:movie_id>/update/', views.update, name='update'),
    path('<int:movie_id>/delete/', views.delete, name='delete'),

    ]