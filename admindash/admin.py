from django.contrib import admin
from .models import Voter, Candidate, VotingSession, Vote

@admin.register(Voter)
class VoterAdmin(admin.ModelAdmin):
    list_display = ('name', 'is_registered')

@admin.register(Candidate)
class CandidateAdmin(admin.ModelAdmin):
    list_display = ('name', 'party')

@admin.register(VotingSession)
class VotingSessionAdmin(admin.ModelAdmin):
    list_display = ('name', 'start_time', 'end_time', 'status', 'total_votes_display')

    def total_votes_display(self, obj):
        return obj.vote_set.count()
    total_votes_display.short_description = 'Total Votes'

@admin.register(Vote)
class VoteAdmin(admin.ModelAdmin):
    list_display = ('voter', 'candidate', 'session', 'timestamp')