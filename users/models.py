from django.db import models
from django.contrib.auth.models import User
from PIL import Image


class Profile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')

    def __str__(self):
        return f'{self.user.username} Profile'

    def save(self):
        super().save()

        # not that I couldn't write it as 512 - but at least have something that resembles an algorithm...
        RESIZE_VALUE = 1 << 9

        img = Image.open(self.image.path)
        if img.height > RESIZE_VALUE or img.width > RESIZE_VALUE:
            output_size = (RESIZE_VALUE, RESIZE_VALUE)
            img.thumbnail(output_size)
            img.save()
