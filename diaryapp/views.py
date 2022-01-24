import json

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
    return render(request, 'diaryapp/login.html', {"isLogined": False})

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



# 2. 2. 회원가입

def signup_user(request):
    if request.method == 'POST':
        print("Hello")
        req = json.loads(request.body.decode('utf-8'))
        user_id = req["user_id"]#request.POST.get('user_id')
        user_pw = req["user_id"]#request.POST.get('user_pw')
        user_name = req["user_name"]#request.POST.get('user_name')
        
        print(user_id, user_pw, user_name)
        # print("=================" * 3)
        # print(">> ", user_id, user_pw, user_name)

        # 기존 사용자 동일한 id 있는지?
        try:
            m = User(
                user_id = user_id,
                user_pw = user_pw, 
                user_name = user_name
            )
            m.date = timezone.now()
            m.save()
        except Exception as e:
            print("Error : ", e)
            pass
    
        data = {
                "isLogined": True,
                "user_name" : user_name
                }
        # return render(request, 'diaryapp/login.html', data)
        return JsonResponse(data=data)
    else:
        return render(request, 'diaryapp/login.html')


# 2. 3. 로그아웃

# 2. 4. 뉴스 
#    1) 뉴스 모든 데이터 조회
def read_all_news(request):
    news_data = News.objects.all()
    return render(request, 'diaryapp/news.html', {'date' : news_data})

# 2. 5. 채용정보 

# 2. 6. 강의
def read_all_lecture(request):
    pass
# 2. 7. TIL관련


# 2. recruit 관련
def read_all_recruit(request):
    data = {}
    return JsonResponse(data)

def test(request):
    pass

#프로그램 업로드/다운로드 추가 예정 --
