from django.shortcuts import render
from django.http import HttpResponse
from .models import Competitions

# Create your views here.
def post_list(request):
    competitions = Competitions.objects.all()
    return render(request, 'portal/index.html', context={'competitions': competitions})



def competition_detail(request, slug):
    competition = Competitions.objects.get(slug=slug)
    return render(request, 'portal/competition_detail.html', context={'competition': competition})