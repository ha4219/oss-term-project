from django.db import models


class User(models.Model):
    userId = models.CharField(max_length=200, primary_key=True)
    solvedProblems = models.ManyToManyField('problem.Problem')


class TagScore(models.Model):
    tag = models.ForeignKey('tag.Tag', on_delete=models.CASCADE)
    user = models.ForeignKey('user.User', on_delete=models.CASCADE)
    level0 = models.IntegerField(default=0)
    cnt0 = models.IntegerField()
    level1 = models.IntegerField(default=0)
    cnt1 = models.IntegerField()
