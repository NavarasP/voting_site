from django.db import models



class Voter(models.Model):
    name = models.CharField(max_length=100)
    fingerprint_data = models.TextField()  
    retina_data = models.TextField()  
    is_registered = models.BooleanField(default=False)

    def __str__(self):
        return self.name

class Candidate(models.Model):
    name = models.CharField(max_length=100)
    party = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.name} ({self.party})"
    

class VotingSession(models.Model):
    name = models.CharField(max_length=100)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    status = models.CharField(max_length=10, choices=[('Active', 'Active'), ('Inactive', 'Inactive')], default='Inactive')
    candidates = models.ManyToManyField('Candidate')

    def __str__(self):
        return self.name



class Vote(models.Model):
    voter = models.ForeignKey('Voter', on_delete=models.CASCADE)  
    candidate = models.ForeignKey('Candidate', on_delete=models.CASCADE)
    session = models.ForeignKey('VotingSession', on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.voter.name} voted for {self.candidate.name} in {self.session.name}"