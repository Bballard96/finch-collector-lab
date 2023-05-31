from django.db import models
from django.urls import reverse

class Finch(models.Model):
  name = models.CharField(max_length=100)
  breed = models.CharField(max_length=100)
  description = models.TextField(max_length=250)
  age = models.IntegerField()

	# new code below
  def __str__(self):
    return self.name
  
  def get_absolute_url(self):
    return reverse('finch-detail', kwargs={'finch_id': self.id})