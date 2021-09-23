from django.db import models


class Tag(models.Model):
    name = models.CharField(max_length=200, unique=True, primary_key=True)