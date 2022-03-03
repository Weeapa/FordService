from django.shortcuts import render
from django.http import HttpResponse
from team.models import Worker


def index(request):
    return HttpResponse("Work!")

def team_list(request):
    all_names = Worker.objects.all()
    return render(request, "team/list.html", {"names":all_names})