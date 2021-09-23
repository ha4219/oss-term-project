from django.shortcuts import render
from rest_framework import viewsets
from .models import Problem
from .serializers import ProblemSerializer


class ProblemView(viewsets.ModelViewSet):
    queryset = Problem.objects.all()
    serializer_class = ProblemSerializer
    