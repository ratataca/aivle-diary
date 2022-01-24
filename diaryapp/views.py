from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import User


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

#프로그램 업로드/다운로드 추가 예정 --