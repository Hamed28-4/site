from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=40)
    description = models.TextField()
    date = models.DateField(auto_now_add=True)
    time = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title