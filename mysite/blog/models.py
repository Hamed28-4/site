from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=40)
    description = models.TextField()
    date = models.DateField(auto_now_add=True)
    time = models.TimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    
class Account(models.Model):
    phone = models.CharField(max_length=11)