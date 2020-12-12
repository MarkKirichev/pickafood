from django.db import models
from django.utils.translation import ugettext_lazy as _

# WEEKDAYS = [
#     (1, _("Monday")),
#     (2, _("Tuesday")),
#     (3, _("Wednesday")),
#     (4, _("Thursday")),
#     (5, _("Friday")),
#     (6, _("Saturday")),
#     (7, _("Sunday")),
# ]

WEEKDAYS = [
    (1, "Monday"),
    (2, "Tuesday"),
    (3, "Wednesday"),
    (4, "Thursday"),
    (5, "Friday"),
    (6, "Saturday"),
    (7, "Sunday"),
]


class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Location(models.Model):
    latitude = models.DecimalField(max_digits=22, decimal_places=16)
    longitude = models.DecimalField(max_digits=22, decimal_places=16)

    def __str__(self):
        return "lat:{}, lng: {}".format(self.latitude, self.longitude)


class PaymentMethod(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class OpeningHours(models.Model):
    weekday = models.IntegerField(choices=WEEKDAYS)
    from_hour = models.TimeField()
    to_hour = models.TimeField()
    restaurant = models.ForeignKey('app.Restaurant', on_delete=models.DO_NOTHING)

    class Meta:
        ordering = ('weekday', 'from_hour')
        unique_together = ('weekday', 'from_hour', 'to_hour')


def upload_menu_image_destination(instance, filename):
    return f'{instance.restaurant.name}/menu_images/{filename}'


def upload_cover_image_to(instance, filename):
    return f'{instance.name}/menu_images/{filename}'


class Restaurant(models.Model):
    name = models.CharField(max_length=60)
    slogan = models.CharField(max_length=150, blank=True, null=True)
    description = models.TextField()
    address = models.TextField()
    city = models.CharField(max_length=60)
    location = models.OneToOneField(Location, on_delete=models.DO_NOTHING)
    payment_methods = models.ManyToManyField(PaymentMethod)
    cover_image = models.ImageField(
        upload_to=upload_cover_image_to,
        blank=True,
        null=True
    )

    def __str__(self):
        return self.name

    @property
    def categories(self):
        cat_ids = self.menuitem_set.all().values_list('category').distinct()
        return Category.objects.filter(pk__in=cat_ids)


# TODO: Add options like (big pizza) +2.34, (whole grain) +1.22
class MenuItem(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.DO_NOTHING)
    restaurant = models.ForeignKey(Restaurant, on_delete=models.DO_NOTHING)
    image = models.ImageField(upload_to=upload_menu_image_destination, blank=True, null=True)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    is_active = models.BooleanField(default=False)

    def __str__(self):
        return self.name
