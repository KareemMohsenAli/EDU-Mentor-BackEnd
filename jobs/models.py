from django.db import models

# Create your models here.
class GmailAccount(models.Model):
    email = models.EmailField(unique=True)