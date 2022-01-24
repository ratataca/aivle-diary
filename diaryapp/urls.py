from django.urls import path
from . import views


app_name = 'diaryapp'

urlpatterns = [
    

    # 1. HTML 파일 경로 지정
    path('login/', views.login, name='login'),
    path('main/', views.main, name='main'),
    path('diary/', views.dairy, name='diary'),
    path('lecture/', views.lecture, name='lecture'),
    path('news/', views.news, name='news'),
    path('hire/', views.hire, name='recruit'),
    
    path('main/test', views.test, name='test'),

    # 2. 이벤트 

    # 2. 1. 로그인
    # path('api/user/login', views.login_user, name='login_user'),
    

    # 2. 2. 회원가입
    # path('api/user/signup', views.signup_user, name='signup_user'),

    # 2. 3. 로그아웃

    # 2. 4. 뉴스 
    path('api/news/readAll', views.read_all_news, name='news_read_all'),

    # 2. 5. 채용정보 
    path('api/recruit/readAll', views.read_all_recruit, name='recruit_read_all'),

    # 2. 6. 강의
    path('api/lecture/readAll', views.read_all_lecture, name='lecture_read_all'),

    # 2. 7. TIL관련

    # # 회원가입 등록 요청
    

    # # 로그인 확인 요청
    
]
