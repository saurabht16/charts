from django.db import models

# Create your models here.

class Passenger(models.Model):
    MALE = 'M'
    FEMALE = 'F'


    SEX_CHOICES = (
        (MALE, 'male'),
        (FEMALE, 'female')
        )

    CHERBOURG = 'C'
    QUEENSTOWN = 'Q'
    SOUTHAMPTON = 'S'

    PORT_CHOICES = (
        (CHERBOURG, 'Cherbourg'),
        (QUEENSTOWN, 'Queenstown'),
        (SOUTHAMPTON, 'Southampton'),
        )
    name = models.CharField(max_length=100)
    sex = models.CharField(max_length=10)
    survived = models.BooleanField()
    age = models.FloatField()
    ticket_class = models.PositiveSmallIntegerField()
    embarked = models.CharField(max_length=100)