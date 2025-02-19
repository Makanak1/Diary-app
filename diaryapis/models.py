from django.db import models
from django.contrib.auth.models import User

# Create your models here.
GENDER = ( 
    ("M", "MALE"),
    ("F", "FEMALE"),
)
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    fullname = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    gender = models.CharField(max_length=6, choices=GENDER)
    image = models.ImageField(upload_to="profile/",blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username

class Diary(models.Model):
    title = models.CharField(max_length=200)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title