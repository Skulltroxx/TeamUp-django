import datetime
from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

class Arena(models.Model):
    title = models.CharField(max_length=15)
    lat = models.DecimalField(max_digits=9, decimal_places=6)
    long = models.DecimalField(max_digits=9, decimal_places=6)

    def __str__(self):
        return self.title

class Event(models.Model):
    date = models.DateField() #default=datetime.date.today() + datetime.timedelta(days=7)
    datetime_created = models.DateTimeField(default=datetime.datetime.now)
    arena = models.ForeignKey(Arena, blank=True, null=True, on_delete=models.DO_NOTHING)
    sport = models.CharField(max_length=25)
    players = models.ManyToManyField(User)

    def __str__(self):
        return self.sport + " on " + str(self.date)

    def get_absolute_url(self):
        return reverse("event-detail", kwargs={"pk": self.pk})
    
