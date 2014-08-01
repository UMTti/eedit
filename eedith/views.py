from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from eedith.models import Session
from django.template import RequestContext, loader
from django.http import Http404
from django.core.urlresolvers import reverse
from django.utils import timezone

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
    return render(request, 'sessions/detail.html', {'session': session})

def update_description(request, session_id):
    p = get_object_or_404(Session, pk=session_id)
    text = request.POST['description']
    p.description = text
    p.save()
    latest = Session.objects.all()[Session.objects.count()-1]
    return render(request, 'sessions/index.html', {
        'sessions_list': Session.objects.all(),
        'latest': latest,
    })

def create_session(request):
	new = Session(description="Default description", start_date=timezone.now(), end_date=timezone.now(), ended=False)
	new.save()
	latest = Session.objects.all()[Session.objects.count()-1]

	return render(request, 'sessions/index.html', {
        'sessions_list': Session.objects.all(),
        'latest': latest,
    })

def end_session(request, session_id):
	session = get_object_or_404(Session, pk=session_id)
	session.ended = True
	session.save()
	latest = Session.objects.all()[Session.objects.count()-1]

	return render(request, 'sessions/index.html', {
        'sessions_list': Session.objects.all(),
        'latest': latest,
    })


