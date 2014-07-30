from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return HttpResponse("Eedith - Work hour automation system")


def detail(request, session_id):
    return HttpResponse("You're looking at session %s." % session_id)
