from django.db import models
from django.contrib.auth.models import User 
from PIL import Image

# class means name of table || artibutes are fields of the table 
class Profile(models.Model):
# on_delete (argument) means what we will do with PROFILE if user is deleted
# | CASCADE is when USER is deleted also delete PROFILE

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default_IRIXFQA.jpg', upload_to='profile_pics')  #upload_to ---- mention dir. name

    def __str__(self):
        return f"{self.user.username} Profile"
    
    def save(self):
        super().save()

        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)

