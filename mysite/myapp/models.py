from django.utils import timezone
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Pslmatches(models.Model):
    PSL_CHOICE = [
        ('PZ', 'PESHAWAR ZALMI'),
        ('LQ', 'LAHORE QALANDARS'),
        ('KK', 'KARACHI KINGS'),
        ('QG', 'QUETTA GLADIATOR'),
        ('MS', 'MULTAN SULTAN'),

    ]
    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to='psl/')
    date_added = models.DateTimeField(default=timezone.now)
    type = models.CharField(max_length=2, choices=PSL_CHOICE)
    descriptions = models.TextField(default='')

    def __str__(self):
        return self.name
    
class TeamReview(models.Model):
    team = models.ForeignKey(Pslmatches, on_delete=models.CASCADE, related_name='reviews')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.IntegerField()
    comment = models.TextField()
    date_added = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f'{self.user.username} review for {self.team.name}'
    
class Player(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    team_players = models.ManyToManyField(Pslmatches, related_name='players')

    def __str__(self):
        return self.name
    
class PlayerCertificate(models.Model):
    team = models.OneToOneField(Pslmatches, on_delete=models.CASCADE, related_name='certificate')
    certificate_number = models.CharField(max_length=100)
    issued_date = models.DateTimeField(default=timezone.now)
    valid_until = models.DateTimeField()

    def __str__(self):
        return f'Certificate for {self.team.name}'
    

