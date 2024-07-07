from django.db import models

class Profile(models.Model):
  first_name = models.CharField(max_length=255)
  last_name = models.CharField(max_length=255)
  email = models.CharField(max_length=255)
  image = models.ImageField 
  def __str__(self):
    return f"{self.first_name} {self.last_name}"
 