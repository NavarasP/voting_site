from django import forms
from .models import Voter, VotingSession, Candidate

class VoterForm(forms.ModelForm):
    class Meta:
        model = Voter
        fields = ['name', 'fingerprint_data', 'retina_data']



class VotingSessionForm(forms.ModelForm):
    candidates = forms.ModelMultipleChoiceField(
        queryset=Candidate.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=True
    )

    class Meta:
        model = VotingSession
        fields = ['name', 'start_time', 'end_time', 'status', 'candidates']
        widgets = {
            'start_time': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
            'end_time': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        }