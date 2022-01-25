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
            user = User.objects.get(user_id=user_id, user_pw=user_pw)
        except Exception as e:
            print(e)
            # TODO : Error 처리
            raise NotImplementedError()
        

        request.session["user_id"] = user.user_id
        request.session["user_name"] = user.user_name

        return redirect("diaryapp:main")
        # return render_to_response('diaryapp/index.html')
    else:
        return render(request, 'diaryapp/login.html')

def main(request):
    # 메인 페이지 초기 데이터 보내기..

    return render(
        request,
        'diaryapp/index.html',
        
    )
    

def dairy(request):
    return render(request, 'diaryapp/diary.html')


def lecture(request):
    lecture_data = Lecture.objects.all()
    return render(request, 'diaryapp/lecture.html', {'date' : lecture_data})

def news(request):
    news_data = News.objects.all()
    return render(request, 'diaryapp/news.html', {'date' : news_data})


def hire(request):
    return render(request, 'diaryapp/hire.html')


def team(request):
    return render(request, 'diaryapp/team.html')


def temp(request):
    return render(request, 'diaryapp/temp.html')


###########
# Back   #
###########
# API 코드
# 2. 이벤트 

# 2. 1. 로그인



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


# 2. 3. 로그아웃
def logout(request):
    print("logout")
    del request.session["user_id"]
    del request.session["user_name"]

    return redirect("login")

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