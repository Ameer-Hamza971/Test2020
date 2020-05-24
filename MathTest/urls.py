from django.urls import path
from . import views

urlpatterns = [
    path('mathtest', views.mathtest, name='mathtest'),
    path('teacherDisplay', views.teacherDisplay, name='teacherDisplay'),
]
