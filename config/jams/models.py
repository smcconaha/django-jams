from django.db import models
from django.core.validators import MinValueValidator

class Song(models.Model):
    title = models.CharField(max_length=255)
    duration = models.FloatField(null=False, default=.01, validators=[MinValueValidator(.01)])
    num_plays = models.BigIntegerField(default=0, validators=[MinValueValidator(0)])
    explicit = models.BooleanField()
