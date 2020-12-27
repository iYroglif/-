from django.shortcuts import render
from django.http import HttpResponse
from .models import Team


def master(request):
    teams = Team.objects.order_by('id')
    return render(request, 'master.html', {'teams': teams})


def detail(request):
    c_id = request.GET['id']
    team = Team.objects.get(id=c_id)
    return render(request, 'detail.html', {'team': team})
