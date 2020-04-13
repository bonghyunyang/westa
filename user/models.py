from django.db import models

class User(models.Model):
    name     = models.CharField(max_length = 50)
    email    = models.CharField(max_length = 100)
    password = models.CharField(max_length = 200)
    created  = models.DateTimeField(auto_now_add = True)
    updated  = models.DateTimeField(auto_now = True) 

    class Meta:
        db_table = "users" #테이블 명칭은 복수로 할 것
