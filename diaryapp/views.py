import datetime
import json
import os
from ssl import AlertDescription

from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse, response
#from sympy import re
from .models import Til, User
from django.utils import timezone
from .models import User, Lecture, News, Professor, Recruit, Til
from django.views.decorators.csrf import csrf_exempt
from django.core.paginator import Paginator
from config import settings
from django.conf import settings


app_name = 'diaryapp'
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
            return JsonResponse({'code': 500})
        return JsonResponse({'code': 200})
    else:
        return render(request, 'diaryapp/login.html')


def main(request):
    # 메인 페이지 초기 데이터 보내기.
    news = News.objects.order_by('?')
    p1 = Paginator(news,4)
    news_main = p1.page(1)
    lecture_today = Lecture.objects.filter(date=datetime.datetime.today())
    lecture_back = Lecture.objects.filter(date=datetime.datetime.today()-datetime.timedelta(1))
    lecture_front = Lecture.objects.filter(date=datetime.datetime.today()+datetime.timedelta(1))

    recruit = Recruit.objects.order_by('-date')
    p3 = Paginator(recruit,3)
    recruit = p3.page(1)
    return render(request,
    'diaryapp/index.html',{'recruit':recruit,'lecture':lecture_today,
    'lecture_f':lecture_front,'lecture_b':lecture_back,'news':news_main})
    

def diary(request):

    try:
        
        # 세션 만들기
        user_id = request.session["user_id"]

    except Exception as e:
        user_id = ""

    # diary 게시글 조회하는 부분        
    til = Til.objects.filter(user_id=user_id).order_by('-index')

    page = request.GET.get('page','1')
    p = Paginator(til,'1')
    til_list = p.page(page)
    print("til_list : ", til_list)

    #diary sidebar 부분
    lec1 = Lecture.objects.filter(professor_id=0)  
    lec2 = Lecture.objects.filter(professor_id=1)
    lec3 = Lecture.objects.filter(professor_id=2)
    lec4 = Lecture.objects.filter(professor_id=5)
    user_name=request.session["user_name"]
    return render(request, 'diaryapp/diary.html', 
        {'lec1':lec1, 'lec2':lec2,'lec3':lec3,'lec4':lec4,'til_list':til_list,'id1':user_id,'name1':user_name})



def lecture(request):
    lecture_list = Lecture.objects.all().order_by('-date')
    page = request.GET.get('page','1')
    p = Paginator(lecture_list,'7')
    lecture_data = p.page(page)
    return render(request, 'diaryapp/lecture.html', {'date' : lecture_data})

def news(request):
    news_list = News.objects.all()
    page=request.GET.get('page','1')
    p = Paginator(news_list,'5')
    news_data = p.page(page)
    return render(request, 'diaryapp/news.html', {'news_data' : news_data})


def hire(request):
    recruit_list=Recruit.objects.filter(date=datetime.datetime.today())[:48]
    page=request.GET.get('page','1')
    p=Paginator(recruit_list,'4')
    recruit=p.page(page)
    return render(request,
    'diaryapp/hire.html',{'recruit':recruit})


def team(request):
    return render(request, 'diaryapp/team.html')



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

@csrf_exempt
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
            return JsonResponse(data=data)
        else:
            data = {"result": False}
            return JsonResponse(data=data)

# 2. 3. 로그아웃
def logout(request):
    try:
        del request.session["user_id"]
        del request.session["user_name"]
    except KeyError:
        return redirect("diaryapp:login")    

    return redirect("diaryapp:login")

# 2. 4. 뉴스 
#    1) 뉴스 모든 데이터 조회
def read_all_news(request):
    data = News.objects.all()
    data=list(data.values())
    return JsonResponse(data,safe=False)

# 2. 5. 채용정보 read_all_recruit
# 2. 5. 1. 채용 모든 데이터 조회
def read_all_recruit(request):
    data = Recruit.objects.all()
    data=list(data.values())
    return JsonResponse(data, safe=False)


# 2. 6. 강의
# 2. 6. 1. 강의 모든 데이터 조회
def read_all_lecture(request):
    data = Lecture.objects.all()
    data=list(data.values())
    return JsonResponse(data, safe=False)


# 3. 1. TIL관련
# 3. 1. 1. 게시글 업로드
@csrf_exempt
def upload(request):
    if request.method == 'POST':
        try:
            user_id = request.session["user_id"]
        except Exception as e:
            # session key 없을 떄
            return JsonResponse({'code': 500})
            
        # DB 들어가야할 정보
        title = request.POST["title"]
        content = request.POST["content"]
        now_date_time = datetime.datetime
        file_list = []

        # File
        current_time = now_date_time.utcnow().isoformat(sep='_', timespec='milliseconds').replace(":", "@")
        
        for image_name, image in request.FILES.items():
            image_buffer = image.read()
            
            # user 경로가 없을 때
            image_path_per_user = os.path.join(settings.BASE_DIR, settings.APP_NAME, settings.STATIC_URL[1:], settings.IMAGE_DIR, user_id)
            if not os.path.isdir(image_path_per_user):
                os.mkdir(image_path_per_user)  

            image_full_path = os.path.join(image_path_per_user, f"{current_time}@@@{image_name}")
            file_list.append(f"{current_time}@@@{image_name}")

            with open(image_full_path, "wb") as file:
                file.write(image_buffer)

            # DB 해당 컬럼 저장
            til = Til(date=current_time, title=title, content=content, img="***".join(file_list), user=User.objects.get(user_id=user_id))
            til.save()

        return JsonResponse({'code': 200})


# 3. 1. 2. 게시글 수정
@csrf_exempt
def update(request):
    if request.method == 'POST':
        try:
            user_id = request.session["user_id"]
        except Exception as e:
            # session key 없을 떄
            return JsonResponse({'code': 500})
        
        # DB Update를 위해 필요한 고유 키(id)
        idx = request.POST["idx"]

        # DB 들어가야할 정보
        title = request.POST["title"]
        content = request.POST["content"]
        
        now_date_time = datetime.datetime
        file_list = []

        # File
        current_time = now_date_time.utcnow().isoformat(sep='_', timespec='milliseconds').replace(":", "@")
        
        for image_name, image in request.FILES.items():
            image_buffer = image.read()
            print(">>> ", user_id)
            # user 경로가 없을 때
            image_path_per_user = os.path.join(settings.BASE_DIR, settings.APP_NAME, settings.STATIC_URL[1:], settings.IMAGE_DIR, user_id)
            if not os.path.isdir(image_path_per_user):
                os.mkdir(image_path_per_user)  

            image_full_path = os.path.join(image_path_per_user, f"{current_time}@@@{image_name}")
            file_list.append(f"{current_time}@@@{image_name}")

            with open(image_full_path, "wb") as file:
                file.write(image_buffer)

        # DB 해당 컬럼 저장
        til = Til.objects.get(index=idx)
        til.title = title
        til.content = content
        til.img = "***".join(file_list)
        # til = Til(date=current_time, title=title, content=content, img=str(file_list), user=User.objects.get(user_id=user_id))
        til.save()

        return JsonResponse({'code': 200})



# 3. 1. 3. 게시글 삭제
@csrf_exempt
def delete(request):
    if request.method == 'POST':
        
        # DB Update를 위해 필요한 고유 키(id)
        idx = request.POST["idx"]

        # DB 해당 컬럼 저장
        
        til = Til.objects.filter(index=idx).delete()
        # til = Til(date=current_time, title=title, content=content, img=str(file_list), user=User.objects.get(user_id=user_id))
        # til.save()

        return JsonResponse({'code': 200})


# 세션 유무 파악
def check_session(request):
    if "user_id" not in request.session:
        return JsonResponse({'code': 500})
    return JsonResponse({'code': 200})
