from django.urls import path
from . import views # 현재 디렉토리에서 views 가져오기

urlpatterns = [

    path('static_example', views.static_example),
    path('artii/', views.artii),
    path('result/', views.result),

    path('throw/', views.throw),
    path('catch/', views.catch),

    path('template_language', views.template_language),
    path('introduce/<str:name>/<int:age>/', views.introduce),
    path('greeting/<str:name>/', views.greeting),  # 정해진 주소가 아닌 string 으로 들어오는 모든 name에 대해
    path('dinner/', views.dinner),
    path('index/', views.index),  # index로 들어오면 views.index 를 실행


]