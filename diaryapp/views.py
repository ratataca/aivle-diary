from django.shortcuts import render
from django.http import HttpResponse
from .models import User

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