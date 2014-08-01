from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from eedith.models import Session
from django.template import RequestContext, loader
from django.http import Http404
from django.core.urlresolvers import reverse
from django.utils import timezone
import math

# Create your views here.

def index(request):
    sessions_list = Session.objects.all()
    try:
        latest = Session.objects.all()[Session.objects.count()-1]
    except AssertionError:
        latest = Session(description="Default description", start_date=timezone.now(), end_date=timezone.now(), ended=False)
        latest.save()
    context = {'sessions_list': sessions_list, 'latest': latest}
    return render(request, 'sessions/index.html', context)


def detail(request, session_id):
    session = get_object_or_404(Session, pk=session_id)
    difference = session.end_date - session.start_date
    d = math.floor(((difference).seconds) / 3600)
    return render(request, 'sessions/detail.html', {'session': session, 'd': d})

def update_description(request, session_id):
    p = get_object_or_404(Session, pk=session_id)
    text = request.POST['description']
    p.description = text
    p.save()
    latest = Session.objects.all()[Session.objects.count()-1]
    return redirect('/eedith')

def create_session(request):
	new = Session(description="Default description", start_date=timezone.now(), end_date=timezone.now(), ended=False)
	text = request.GET['des']
	new.description = text
	new.save()
	latest = Session.objects.all()[Session.objects.count()-1]

	return redirect('/eedith')
	# return render(request, 'sessions/index.html', {
    #    'sessions_list': Session.objects.all(),
    #    'latest': latest,
    # })

def end_session(request, session_id):
	session = get_object_or_404(Session, pk=session_id)
	session.ended = True
	session.end_date = timezone.now()
	session.save()
	latest = Session.objects.all()[Session.objects.count()-1]

	return redirect('/eedith')

def all_sessions(request): 
    sessions_list = Session.objects.all()
    context = {'sessions_list': sessions_list}
    return render(request, 'sessions/all_sessions.html', context)

