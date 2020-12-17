from django.db import models
from django.contrib.auth.models import User
from PIL import Image
from .restaurants_names import RESTAURANT_NAMES


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')

    @property
    def is_restaurant_admin_profile(self):
        for item in RESTAURANT_NAMES:
            if not self.user.email.__str__().find(item) == -1:
                is_restaurant_admin_profile = item
                # print(self.user.email.__str__(), is_admin_profile)
                return is_restaurant_admin_profile
        return ''

    def __str__(self):
        return f'{self.user.username} Profile'

    def save(self, *args, **kwargs):
        super(Profile, self).save(*args, **kwargs)

        # not that I couldn't write it as 512 - but at least have something that resembles an algorithm...
        RESIZE_VALUE = 1 << 9
        IMG_PATH = self.image.path

        img = Image.open(IMG_PATH)
        if img.height > RESIZE_VALUE or img.width > RESIZE_VALUE:
            output_size = (RESIZE_VALUE, RESIZE_VALUE)
            img.thumbnail(output_size)
            img.save(IMG_PATH)
