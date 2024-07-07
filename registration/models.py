from django.db import models

from profiles.models import Profile

class User(models.Model):
  username = models.CharField(max_length=255)
  password = models.CharField(max_length=31)
  firstname = models.CharField(max_length=31)
  lastname = models.CharField(max_length=31)
  email = models.CharField(max_length=31)
  profile_id = models.ForeignKey(Profile, on_delete=models.CASCADE)
  def __str__(self):
    return f"{self.username} {self.password}"
  

