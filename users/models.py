from django.db import models

# Create your models here.


class UserProfile(models.Model):
    username = models.CharField(max_length=100, unique=True)
    email = models.EmailField(unique=True)
    bio = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.username
