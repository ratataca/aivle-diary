from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import News, Recruit, User,Lecture



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
# 1. lecture 관련

#패키지 설치: djangorestframework, django-filter

from rest_framework.views import APIView
from .serializers import LectureSerializer,NewsSerializer,RecruitSerializer


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
