from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login),
    path('main/', views.main),
    path('diary/', views.dairy),
    path('lecture/', views.lecture),
    path('news/', views.news),
    path('hire/', views.hire),
    
    path('main/test', views.test),

    path('/api/news/readAll', views.read_all_news),
    path('/api/recruit/readAll', views.read_all_recruit),
]
