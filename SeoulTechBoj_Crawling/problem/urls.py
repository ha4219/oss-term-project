from django.urls import path, include
from rest_framework.urlpatterns import format_suffix_patterns
from .views import ProblemView

problem_list = ProblemView.as_view({
    'get': 'list'
})

problem_detail = ProblemView.as_view({
    'get': 'retrieve',
})

urlpatterns = format_suffix_patterns([
    path('problems/', problem_list, name='problem_list'),
    path('problem/<int:pk>/', problem_detail, name='problem_detail'),
])