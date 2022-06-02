from django.contrib.auth import get_user_model
from django.db import models


class Dog(models.Model):
    objects = models.Manager()  # Fixes the unresolved reference
    coat_colors = [('BLK', 'Black'), ('BLK & CREAM', 'Black & Cream'), ('BLK & Red', 'Black & Red'),
                    ('BLK & SILVER', 'Black & Silver'), ('BLK & TAN', 'Black & Tan'), ('BLUE', 'Blue'),
                    ('GRAY', 'Gray'), ('LIVER', 'Liver'), ('SABLE', 'Sable'), ('WHITE', 'White'),
                    ('BI-COLOR', 'Bi-Color')]
    genders = [('M', 'Male'), ('F', 'Female')]
    name = models.CharField(max_length=256)
    owner = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    coat = models.CharField(max_length=64, choices=coat_colors)
    gender = models.CharField(max_length=1, choices=genders)
    description = models.TextField()
    date_entered = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'Dog\'s name: {self.name} --> Owner: {self.owner}'
