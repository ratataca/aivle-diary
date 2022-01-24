from django.urls import path
from . import views

urlpatterns = [
    
    # 1. html 파일줘
    path('main/', views.main),

    path('login/', views.login),
    path('main/', views.main),
    path('diary/', views.dairy),
    path('lecture/', views.lecture),
    path('news/', views.news),
    path('hire/', views.hire),
    
    path('main/test', views.test),

    # 2. 이벤트 -> 디비 줘봐( 조회 )
    #    이벤트 -> 업데이트(수정), 삭제, 입력(create)
    path('api/news/readAll', views.read_all_news),
    path('api/recruit/readAll', views.read_all_recruit),
]
