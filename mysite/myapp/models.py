from django.utils import timezone
from django.db import models

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
    

