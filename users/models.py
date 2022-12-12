from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class UserModel(models.Model):
    user = models.OneToOneField(User, primary_key=True, on_delete=models.CASCADE)
    lat = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)
    long = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)

    def __str__(self):
        return self.user.username