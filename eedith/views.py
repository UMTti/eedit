from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from eedith.models import Session
from django.template import RequestContext, loader
from django.http import Http404
from django.core.urlresolvers import reverse

# Create your views here.

def index(request):
    sessions_list = Session.objects.all()
    context = {'sessions_list': sessions_list}
    return render(request, 'sessions/index.html', context)


def detail(request, session_id):
    session = get_object_or_404(Session, pk=session_id)
    return render(request, 'sessions/detail.html', {'session': session})

def update_description(request, session_id):
    p = get_object_or_404(Session, pk=session_id)
    text = request.POST['description']
    p.description = text
    p.save()
    return render(request, 'sessions/index.html', {
        'sessions_list': Session.objects.all(),
    })
