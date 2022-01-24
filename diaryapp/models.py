from django.db import models

class User(models.Model):
    user_id = models.CharField(primary_key=True, max_length=50)
    user_pw = models.CharField(max_length=20)
    user_name = models.CharField(max_length=10)
    date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'user'

class Diary(models.Model):
    index = models.AutoField(primary_key=True)
    date = models.DateTimeField()
    title = models.CharField(max_length=30)
    content = models.CharField(max_length=700)
    img = models.CharField(max_length=700,null=True,blank=True)
    user_id = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'diary'


class Lecture(models.Model):
    index = models.AutoField(primary_key=True)
    date = models.DateField()
    topic = models.CharField(max_length=50)
    detail = models.CharField(max_length=500)
    professor_id = models.ForeignKey('Professor',on_delete=models.DO_NOTHING,db_column='professor_id')
    professor_name = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'lecture'

class Professor(models.Model):
    id = models.AutoField(primary_key= True)
    name = models.CharField(max_length=15)

    class Meta:
        managed = False
        db_table = 'professor'

class News(models.Model):
    index = models.AutoField(primary_key=True)
    date = models.DateField()
    title = models.CharField(max_length=30)
    content = models.CharField(max_length=120)
    company = models.CharField(max_length=50)
    link = models.CharField(max_length=800)

    class Meta:
        managed = False
        db_table = 'news'


class Recruit(models.Model):
    index = models.AutoField(primary_key=True)
    date = models.DateField()
    company_name = models.CharField(max_length=50)
    job_title = models.CharField(max_length=150)
    job_fields = models.CharField(max_length=200)
    required_career = models.CharField(max_length=200)
    required_education = models.CharField(max_length=100)
    employment_type = models.CharField(max_length=50)
    work_place = models.CharField(max_length=200)
    deadlines = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'recruit'

