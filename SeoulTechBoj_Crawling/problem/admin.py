from django.contrib import admin
from problem.models import Problem, SolvedProblem, ProblemStatusByLevel
# Register your models here.
admin.site.register(Problem)
admin.site.register(SolvedProblem)
admin.site.register(ProblemStatusByLevel)