from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('list/', views.team_list, name="team_list")
]