from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from .models import Problem, ProblemStatusByLevel
from .serializers import ProblemSerializer, LevelStatusSerializer
from rest_framework import generics


class ProblemView(viewsets.ModelViewSet):
    serializer_class = ProblemSerializer
    queryset = Problem.objects.all()


class ProblemViewNotSolvedAndLevel(generics.ListAPIView):
    serializer_class = ProblemSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ('level', )

    def get_queryset(self):
        level = self.kwargs["level"]
        query_set = Problem.objects.filter(solved=False, level=level, isSolvable=True)
        return query_set


class LevelStatus(generics.ListAPIView):
    serializer_class = LevelStatusSerializer
    queryset = ProblemStatusByLevel.objects.all()