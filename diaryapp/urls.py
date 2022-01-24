from django.urls import path
from . import views

app_name = 'diaryapp'

urlpatterns = [
    
    # 1. html 파일줘
    path('login/', views.login, name='login'),
    path('main/', views.main, name='main'),
    path('diary/', views.dairy, name='diary'),
    path('lecture/', views.lecture, name='lecture'),
    path('news/', views.news, name='news'),
    path('hire/', views.hire, name='recruit'),
    
    path('main/test', views.test, name='test'),

    # 2. 이벤트 -> 디비 줘봐( 조회 )
    #    이벤트 -> 업데이트(수정), 삭제, 입력(create)
    path('api/news/readAll', views.read_all_news, name='news_read_all'),
    path('api/recruit/readAll', views.read_all_recruit, name='recruit_read_all'),

    # # 회원가입 등록 요청
    # path('api/user/signup', views.signup_user, name='signup_user'),

    # # 로그인 확인 요청
    # path('api/user/login', views.login_user, name='login_user'),
]
