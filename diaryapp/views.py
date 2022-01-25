import datetime
import json

from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from sympy import re
from .models import User
from django.utils import timezone
from .models import News, Recruit, User,Lecture
from .models import News, User
from django.views.decorators.csrf import csrf_exempt
from .forms import UploadFileForm
from django.core.paginator import Paginator
###########
# Front   #
###########
# 1. HTML 파일 경로 지정 및 초기 세팅
@csrf_exempt
def login(request):
    if request.method == 'POST':
        
        user_id = request.POST.get("user_id")
        user_pw = request.POST.get("user_pw")

        try:
            # 데이터 조회를 성공했을 때
            user = User.objects.get(user_id=user_id, user_pw=user_pw)

            # 세션 만들기
            request.session["user_id"] = user.user_id
            request.session["user_name"] = user.user_name
        except Exception as e:
            print(e)
            # TODO : Error 처리
            raise NotImplementedError()
        

        return JsonResponse({'code': 200})
    else:
        return render(request, 'diaryapp/login.html')


def main(request):
    # 메인 페이지 초기 데이터 보내기.
    news=News.objects.order_by('-date')
    p1=Paginator(news,4)
    news_main=p1.page(1)
    lecture_today=Lecture.objects.filter(date=datetime.datetime.today())
    lecture_back=Lecture.objects.filter(date=datetime.datetime.today()-datetime.timedelta(1))
    lecture_front=Lecture.objects.filter(date=datetime.datetime.today()+datetime.timedelta(1))

    recruit=Recruit.objects.order_by('-date')
    p3=Paginator(recruit,1)
    recruit=p3.page(1)
    recruit_2=p3.page(2)
    recruit_3=p3.page(3)

    return render(request,
    'diaryapp/index.html',{'recruit_2':recruit_2,'recruit':recruit,
    'recruit_3':recruit_3,'lecture':lecture_today,
    'lecture_f':lecture_front,'lecture_b':lecture_back,'news':news_main})
    

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
#   위 Front쪽 추가 됨


# 2. 2. 회원가입
def signup_user(request):
    if request.method == 'POST':
        req = json.loads(request.body.decode('utf-8'))
        user_id = req["user_id"]#request.POST.get('user_id')
        user_pw = req["user_pw"]#request.POST.get('user_pw')
        user_name = req["user_name"]#request.POST.get('user_name')
        
        print(user_id, user_pw, user_name)
        # print("=================" * 3)
        # print(">> ", user_id, user_pw, user_name)

        # TODO 기존 사용자 동일한 id 있는지?
        # TODO 이메일 정규식 추가
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


def is_existed_user(request):
    if request.method == 'POST':
        req = json.loads(request.body.decode('utf-8'))
        user_id = req["user_id"]
        
        try:
            data = User.objects.filter(user_id=user_id)
            rep = list(data.values())
            
        except Exception as e:
            print("Error : ", e)
        
        if len(rep) > 0:
            data = {"result": True}
            print("해당 아이디가 동일하게 있슴!!!")
            return JsonResponse(data=data)
        else:
            data = {"result": False}
            return JsonResponse(data=data)

# 2. 3. 로그아웃
def logout(request):
    print("logout")
    del request.session["user_id"]
    del request.session["user_name"]

    return redirect("diaryapp:login")

# 2. 4. 뉴스 
#    1) 뉴스 모든 데이터 조회
def read_all_news(request):
    data = News.objects.all()
    data=list(data.values())
    return JsonResponse(data,safe=False)

# 2. 5. 채용정보 
# 2. 5. 1. 채용 모든 데이터 조회
def read_all_recruit(request):
    data = Recruit.objects.all()
    data=list(data.values())
    return JsonResponse(data,safe=False)


# 2. 6. 강의
# 2. 6. 1. 강의 모든 데이터 조회
def read_all_lecture(request):
    data = Lecture.objects.all()
    data=list(data.values())
    return JsonResponse(data,safe=False)


# 2. 7. TIL관련


# # 2. recruit 관련
# def read_all_recruit(request):
#     data = {}
#     return JsonResponse(data)

# 3. 파일 업로드 -- 프론트엔드에서 가져갈 때 주석 해제하고 사용


app_name = 'diaryapp'

def upload(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            uploadFile = form.save()
            # uploadFile = form.save(commit=False)
            name = uploadFile.file.name
            size = uploadFile.file.size
            return HttpResponse('%s<br>%s' % (name, size))
    else:
        form = UploadFileForm()
    return render(
        request, 'diaryapp/upload.html', {'form': form})


def test(request):
    pass