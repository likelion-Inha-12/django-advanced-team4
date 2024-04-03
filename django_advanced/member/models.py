from django.db import models

class Member(models.Model):
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=50)
    is_leader = models.BooleanField(default=False)
    hearts = models.PositiveIntegerField(default=0)