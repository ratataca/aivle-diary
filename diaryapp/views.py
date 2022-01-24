from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import User
from django.utils import timezone
from .models import News, Recruit, User,Lecture
from .models import News, User

###########
# Front   #
###########
# 1. HTML 파일 경로 지정
def login(request):
    return render(request, 'diaryapp/login.html')

def main(request):
    my_id = User.objects.all()
    
    return render(
        request,
        'diaryapp/index.html',
        {"my_id" : my_id}
    )
    

def dairy(request):
    return render(request, 'diaryapp/diary.html')


def lecture(request):
    return render(request, 'diaryapp/lecture.html')


def hire(request):
    return render(request, 'diaryapp/hire.html')


def test(request):
    my_id = User.objects.all()
    print(my_id)

    return render(
        request,
        'diaryapp/ratataca.html',
        {"my_id" : my_id}
    )


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
def news(request):
    new = News.objects.all()
    return render(request, 'diaryapp/news.html', {'date' : new})

# 2. 5. 채용정보 

# 2. 6. 강의

# 2. 7. TIL관련

# # 회원가입 등록 요청


# # 로그인 확인 요청



def read_all_news(request):
    data =  {   'index' : 1,
                'data' : '2022-01-23',
                'title' : '오늘의 IT 뉴스', 
                'content' : '안녕하세요 오늘 급하게 전달해야할...', 
                'link' : "naver.com"
            }

    return JsonResponse(data)


# 2. recruit 관련
def read_all_recruit(request):
    data = {}
    return JsonResponse(data)


def read_all_lecture(request):
    data = {}
    return JsonResponse(data)