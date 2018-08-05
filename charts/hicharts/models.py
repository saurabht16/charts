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

    def __str__(self):
        return self.name

class emp(models.Model):
    empno = models.IntegerField(primary_key=True)
    ename = models.CharField(max_length=10)
    job = models.CharField(max_length=100)
    mgr = models.IntegerField()
    hiredate = models.DateField()
    sal = models.FloatField()
    comm = models.FloatField()

    class Meta:
        db_table = 'emp'
        managed = False

    def __str__(self):
        return self.ename