from django.urls import path
from . import views

urlpatterns = [
    path('main/', views.main),
    path('main/test', views.test),

    path('/api/news/readAll', views.read_all_news),
    path('/api/recruit/readAll', views.read_all_recruit),
]
