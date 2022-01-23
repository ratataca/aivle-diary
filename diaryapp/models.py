from django.db import models


# TODO - 1. 모델 속성 및 이름 작성하기
class User(models.Model):
    user_id = models.CharField(max_length=50)
    user_pw = models.CharField(max_length=20)
    user_name = models.CharField(max_length=10)


class News(models.Model):
    pass

class recruit(models.Model):
    pass

class professor(models.Model):
    pass

class lecture(models.Model):
    pass

