from django.db import models

# Create your models here.
from django.db.models import CASCADE

from django.contrib.auth.models import User
class Serie(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()

    def __str__(self):
        return self.title


class Score(models.Model):
    score = models.IntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    serie = models.ForeignKey(Serie, on_delete=models.CASCADE)

    def __str__(self):
        return F'{self.user}, {self.serie}, {self.score}'


class Episode(models.Model):
    number = models.IntegerField()
    name = models.CharField(max_length=50)
    serie = models.ForeignKey(Serie, on_delete=CASCADE)

    def __str__(self):
        return f'{self.name} - {self.number}'
