from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import User
from django.utils import timezone
from .models import News, Recruit, User,Lecture
from .models import News, User

###########
# Front   #
###########
# 1. HTML 파일 경로 지정 및 초기 세팅
def login(request):
    return render(request, 'diaryapp/login.html')

def main(request):
    my_id = User.objects.all()

    # 메인 페이지 초기 데이터 보내기..
    
    return render(
        request,
        'diaryapp/index.html',
        {"my_id" : my_id}
    )
    

def dairy(request):
    return render(request, 'diaryapp/diary.html')


def lecture(request):
    return render(request, 'diaryapp/lecture.html')

def news(request):
    news_data = News.objects.all()
    return render(request, 'diaryapp/news.html', {'date' : news_data})


def hire(request):
    return render(request, 'diaryapp/hire.html')


###########
# Back   #
###########
# API 코드
# 2. 이벤트 

# 2. 1. 로그인
# path('api/user/login', views.login_user, name='login_user'),


# 2. 2. 회원가입
# path('api/user/signup', views.signup_user, name='signup_user'),

# 2. 3. 로그아웃

# 2. 4. 뉴스 
# 2. 4. 1. 뉴스 모든 데이터 조회
def read_all_news(request):
    news_data = News.objects.all()
    return render(request, 'diaryapp/news.html', {'date' : news_data})

# 2. 5. 채용정보 

# 2. 6. 강의

# 2. 7. TIL관련


# 2. recruit 관련
def read_all_recruit(request):
    data = {}
    return JsonResponse(data)


def read_all_lecture(request):
    data = {}
    return JsonResponse(data)


def test(request):
    pass