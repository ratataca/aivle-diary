from django.urls import path
from . import views

urlpatterns = [
<<<<<<< HEAD
    # client -> server
    # 1. html 파일줘
    path('main/', views.main),

    # ratataca.html로 가는 경로
=======
    path('login/', views.login),
    path('main/', views.main),
    path('diary/', views.dairy),
    path('lecture/', views.lecture),
    path('news/', views.news),
    path('hire/', views.hire),
    
>>>>>>> e9bcac001f8ff46ceb448c4c5fe283e5d3444c58
    path('main/test', views.test),

    # 2. 이벤트 -> 디비 줘봐( 조회 )
    #    이벤트 -> 업데이트(수정), 삭제, 입력(create)
    path('api/news/readAll', views.read_all_news),
    path('api/recruit/readAll', views.read_all_recruit),
]
