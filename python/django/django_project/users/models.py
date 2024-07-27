from django.db import models
from django.contrib.auth.models import User 

# class means name of table || artibutes are fields of the table 
class Profile(models.Model):
# on_delete (argument) means what we will do with PROFILE if user is deleted
# | CASCADE is when USER is deleted also delete PROFILE

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')  #upload_to ---- mention dir. name

    def __str__(self):
        return f"{self.user.username} Profile"