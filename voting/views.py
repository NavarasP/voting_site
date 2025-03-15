from django.shortcuts import render
from ..admindash.models import VotingSession

def list_sessions(request):
    active_sessions = VotingSession.objects.filter(status='Active')
    return render(request, 'list_sessions.html', {'active_sessions': active_sessions})