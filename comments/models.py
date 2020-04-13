from django.db import models

class Comment(models.Model):
    name            = models.CharField(max_length = 50)
    content         = models.TextField()
    created_time    = models.DateTimeField(auto_now_add = True)
    updated_time    = models.DateTimeField(auto_now = True)



