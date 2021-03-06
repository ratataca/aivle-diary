from django.urls import path
from . import views

app_name = 'diaryapp'

urlpatterns = [
    ###########
    # Front   #
    ###########
    # 1. HTML 파일 경로 지정
    path('login/', views.login, name='login'),
    path('main/', views.main, name='main'),
    path('diary/', views.diary, name='diary'),
    path('lecture/', views.lecture, name='lecture'),
    path('news/', views.news, name='news'),
    path('hire/', views.hire, name='recruit'),
    path('team/', views.team, name='team'),

    
    ###########
    # Back   #
    ###########
    # 2. 이벤트 
    # 서버팀 오늘 작업

    # 2. 1. 세션 확인
    path('api/user/session', views.check_session, name='session'),
    

    # 2. 2. 회원가입
    path('api/user/signup', views.signup_user, name='signup_user'),
    path('api/user/signup/isUnique', views.is_existed_user, name='user_isUnique'),

    # 2. 3. 로그아웃
    path('api/user/logout', views.logout, name='logout'),

    # 2. 4. 메인페이지

    # 2. 5. 뉴스 
    path('api/news/readAll', views.read_all_news, name='news_read_all'),

    # 2. 6. 채용정보 
    path('api/recruit/readAll', views.read_all_recruit, name='recruit_read_all'),

    # 2. 7. 강의
    path('api/lecture/readAll', views.read_all_lecture, name='lecture_read_all'),

    # 2. 8. TIL
    # 2. 8. 1. 게시글 업로드
    path('diary/api/upload', views.upload, name='upload'),
    
    # 2. 8. 2. 게시글 수정
    path('diary/api/update', views.update, name='update'),
    
    # 2. 8. 3. 게시글 수정
    path('diary/api/delete', views.delete, name='delete'),
    
]
