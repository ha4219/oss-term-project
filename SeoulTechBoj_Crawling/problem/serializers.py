from rest_framework import serializers
from .models import Problem, ProblemStatusByLevel
import django_filters
from django_filters import FilterSet


class ProblemSerializer(serializers.ModelSerializer):
    level = django_filters.NumberFilter(name="level")

    class Meta:
        model = Problem
        fields = ('problemId', 'titleKo', 'acceptedUserCount', 'averageTries', 'level')


class LevelStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProblemStatusByLevel
        fields = ('level', 'total', 'solved', 'notSolved', )