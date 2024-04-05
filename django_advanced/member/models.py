from django.db import models

class Member(models.Model):
    name = models.CharField(max_length=50, default="member")
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=50)
    is_leader = models.BooleanField(default=False)
    hearts = models.PositiveIntegerField(default=0)