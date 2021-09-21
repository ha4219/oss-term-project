from django.db import models


class Problem(models.Model):
    problemId = models.IntegerField()
    titleKo = models.CharField(max_length=200)
