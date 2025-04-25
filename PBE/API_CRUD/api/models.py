from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField()
    age = models.PositiveIntegerField()
    phone = models.CharField(max_length=20)
    address = models.TextField()
    education = models.CharField(max_length=100)
    pets_count = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.user.username}'s profile"
