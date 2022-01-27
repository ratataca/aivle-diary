from django.contrib import admin
from .models import User,Diary,Lecture,Professor,Recruit,News,Til

# TODO - 2. 모델명칭 등록하기
admin.site.register(User)
admin.site.register(Diary)
admin.site.register(Lecture)
admin.site.register(Professor)
admin.site.register(Recruit)
admin.site.register(News)
admin.site.register(Til)