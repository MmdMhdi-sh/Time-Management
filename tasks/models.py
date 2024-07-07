from django.db import models

from profiles.models import Profile

class Task(models.Model):
  name = models.CharField(max_length=255)
  description = models.CharField(max_length=31)
  add_date = models.DateField(auto_now=False, auto_now_add=False)
  anticipated_duration = models.IntegerField()
  profile_id = models.ForeignKey(Profile, on_delete=models.CASCADE)
  def __str__(self):
    return f"{self.profile_id} {self.name} {self.add_date}"
