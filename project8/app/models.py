from django.db import models


# Create your models here.


class Ipl(models.Model):
    STATUS = [
        ('win', 'Win'),
        ('lose', 'Lose'),
    ]

    sl_no = models.DecimalField(max_digits=5, decimal_places=2, primary_key=True)
    year = models.CharField(max_length=4, unique=True)
    winner = models.CharField(max_length=4, choices=STATUS, default='lose')  # Added max_length




class Teams(models.Model):  # Capitalized model name for consistency
    ipl = models.ForeignKey(Ipl, on_delete=models.CASCADE)  # Renamed field
    team_name = models.CharField(max_length=50, unique=True)  # Increased max_length for team_name
    position = models.DecimalField(max_digits=2, decimal_places=0)  # Corrected typo and format


