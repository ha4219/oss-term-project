from django.conf.urls import url
from django.urls import path, include, re_path
from rest_framework.urlpatterns import format_suffix_patterns
from .views import ProblemView, ProblemViewNotSolvedAndLevel, LevelStatus


problem_detail = ProblemView.as_view({
    'get': 'retrieve',
})

urlpatterns = format_suffix_patterns([
    re_path('^notSolvedProblems/(?P<level>.+)/$', ProblemViewNotSolvedAndLevel.as_view(), name='problem_list'),
    path('problem/<int:pk>/', problem_detail, name='problem_detail'),
    path('level/', LevelStatus.as_view()),
])