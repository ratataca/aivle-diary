from django.urls import path
from . import views

urlpatterns = [
    # client -> server
    # 1. html 파일줘
    path('main/', views.main),

    # ratataca.html로 가는 경로
    path('main/test', views.test),

    # 2. 이벤트 -> 디비 줘봐( 조회 )
    #    이벤트 -> 업데이트(수정), 삭제, 입력(create)
    path('api/news/readAll', views.read_all_news),
    path('api/recruit/readAll', views.read_all_recruit),
]
