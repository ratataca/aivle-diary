from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
<<<<<<< HEAD
from .models import User
from django.utils import timezone
=======
from .models import News, Recruit, User,Lecture

>>>>>>> origin/server2


def login(request):
    return render(request, 'diaryapp/login.html')


# html 경로 코드
def main(request):
    my_id = User.objects.all()
    print(my_id)
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
    return render(request, 'diaryapp/news.html')


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


# API 코드
# 1. news 관련
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


# 회원가입 관련
# def signup_user(request):
#     if request.method == 'POST':
#         user_id = request.POST.get('user_id')
#         user_pw = request.POST.get('user_pw')
#         user_name = request.POST.get('user_name')

#         print(">> ", user_id, user_pw, user_name)

#         m = User(
#             user_id=user_id, user_pw=user_pw, user_name=user_name)
#         m.date_joined = timezone.now()
#         m.save()

#         data = {"msg" : '%s님 반갑습니다!' % (user_name)}
#         return render(request, 'diaryapp/login.html')

#     else:
#         data = {"msg" : '회원가입에 실패하셨습니다.'}
#         return render(request, 'diaryapp/login.html')

# def login_user(request):
#     if request.method == 'POST':
#         user_id = request.POST.get('user_id')
#         user_pw = requesst.POST.get('user_pw')
#         m = User.objects.get(user_id=user_id, user_pw=user_pw)

#         # 회원정보 조회 실패 시 예외 발생
#         data = {"msg" : '회원가입에 실패하셨습니다.'}
#         return HttpResponse(data)
#     else:
#         return render(request, 'member/login_custom.html')

# 1. lecture 관련

#패키지 설치: djangorestframework, django-filter
from rest_framework.views import APIView
from .serializers import LectureSerializer, NewsSerializer, RecruitSerializer


class read_all_lecture(APIView):
    def get(self, request):
        queryset = Lecture.objects.all()
        print(queryset)
        serializer = LectureSerializer(queryset, many=True)
        return JsonResponse(serializer.data,safe=False)

# 2. news관련 

# class read_all_news(APIView):
#     def get(self, request):
#         queryset = News.objects.all()
#         print(queryset)
#         serializer = NewsSerializer(queryset, many=True)
#         return JsonResponse(serializer.data,safe=False)

# # 3. recruit 관련
# class read_all_recruit(APIView):
#     def get(self, request):
#         queryset = Recruit.objects.all()
#         print(queryset)
#         serializer = RecruitSerializer(queryset, many=True)
#         return JsonResponse(serializer.data,safe=False)
