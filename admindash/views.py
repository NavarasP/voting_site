from django.shortcuts import render

# Create your views here.
from .models import VotingSession, Vote, Voter, Candidate
from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator
from .forms import VoterForm, VotingSessionForm





def admin_dashboard(request):
    voters = Voter.objects.all()
    sessions = VotingSession.objects.all()

    session_data = []
    for session in sessions:
        candidates_data = []
        for candidate in session.candidates.all():
            vote_count = Vote.objects.filter(session=session, candidate=candidate).count()
            candidates_data.append({
                'candidate': candidate,
                'vote_count': vote_count,
            })
        session_data.append({
            'session': session,
            'candidates_data': candidates_data,
        })

    return render(request, 'admin_dashboard.html', {
        'voters': voters,
        'session_data': session_data,
    })






def add_voter(request):
    if request.method == 'POST':
        form = VoterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('admin_dashboard')
    else:
        form = VoterForm()
    return render(request, 'add_voter.html', {'form': form})

def edit_voter(request, voter_id):
    voter = get_object_or_404(Voter, id=voter_id)
    if request.method == 'POST':
        form = VoterForm(request.POST, instance=voter)
        if form.is_valid():
            form.save()
            return redirect('admin_dashboard')
    else:
        form = VoterForm(instance=voter)
    return render(request, 'edit_voter.html', {'form': form})

def delete_voter(request, voter_id):
    voter = get_object_or_404(Voter, id=voter_id)
    voter.delete()
    return redirect('admin_dashboard')

def create_session(request):
    if request.method == 'POST':
        form = VotingSessionForm(request.POST)
        if form.is_valid():
            session = form.save()
            return redirect('admin_dashboard')
        else:
            print("Form errors:", form.errors)
    else:
        form = VotingSessionForm()
    return render(request, 'create_session.html', {'form': form})

def edit_session(request, session_id):
    session = get_object_or_404(VotingSession, id=session_id)
    if request.method == 'POST':
        form = VotingSessionForm(request.POST, instance=session)
        if form.is_valid():
            form.save()
            return redirect('admin_dashboard')
    else:
        form = VotingSessionForm(instance=session)
    return render(request, 'edit_session.html', {'form': form})

def delete_session(request, session_id):
    session = get_object_or_404(VotingSession, id=session_id)
    session.delete()
    return redirect('admin_dashboard')