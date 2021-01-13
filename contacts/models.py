from django.db import models

# NOTE: when settings file has "USE_TZ=True", then need to use timezone code instead
# change datetime.datetime.now() to timezone.now()
#from datetime import datetime
from django.utils import timezone

# Create your models here.
# user_id only if user is logged in
class Contact(models.Model):
  listing = models.CharField(max_length=200)
  listing_id = models.IntegerField()
  name = models.CharField(max_length=200)
  email = models.CharField(max_length=100)
  phone = models.CharField(max_length=100)
  message = models.TextField(blank=True)
  #contact_date = models.DateTimeField(default=datetime.now, blank=True)
  contact_date = models.DateTimeField(default=timezone.now, blank=True)
  user_id = models.IntegerField(blank=True)
  
  def __str__(self):
    return self.name
