
from django.db import models
from django.contrib.auth.models import User


class Feedback(models.Model):
    first_name = models.CharField(max_length=30, unique=True)
    message = models.TextField(max_length=100)
    city = models.CharField(max_length=10)
    mobile_no = models.CharField(max_length=10)
    email_id = models.EmailField(unique=True)







