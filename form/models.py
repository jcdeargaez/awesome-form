from django.db import models


class Entry(models.Model):
    CATS = 1
    DOGS = 2
    pet_choices = [
        (CATS, 'Cats'),
        (DOGS, 'Dogs'),
    ]
    name = models.CharField(max_length=50, unique=True)
    color = models.CharField(max_length=7)
    pet = models.PositiveSmallIntegerField(choices=pet_choices, default=CATS)
