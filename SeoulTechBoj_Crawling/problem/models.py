from django.db import models
from tag.models import Tag


class Problem(models.Model):
    problemId = models.IntegerField(primary_key=True, unique=True)
    titleKo = models.CharField(max_length=200)
    isSolvable = models.BooleanField()
    acceptedUserCount = models.IntegerField()
    level = models.IntegerField()
    averageTries = models.DecimalField(max_digits=10, decimal_places=5)
    solved = models.BooleanField(default=False)

    tag = models.ManyToManyField('tag.Tag')



class SolvedProblem(models.Model):
    problemId = models.IntegerField(primary_key=True, unique=True)