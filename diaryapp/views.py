from django.shortcuts import render
from django.http import HttpResponse
from .models import User

# html 경로 코드
def main(request):
    my_id = User.objects.all()
    print(my_id)
    return render(
        request,
        'diaryapp/index.html',
        {"my_id" : my_id}
    )

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
    pass


# 2. recruit 관련
def read_all_recruit(request):
    pass
