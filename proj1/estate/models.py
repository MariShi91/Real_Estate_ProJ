from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.
class Ad(models.Model):
    AD_TYPES = [('rent', 'for rent'), ('sale', 'for sale')]
    ACCOMODATION_TYPES = [('Flat', 'flat'), ('House', 'house')]

    ad_type = models.CharField(max_length=4, blank=False, choices=AD_TYPES)
    accomodation_type = models.CharField(max_length=5, blank=False, choices=ACCOMODATION_TYPES)
    address = models.CharField(max_length=200)
    rooms = models.IntegerField()
    area = models.DecimalField(max_digits=10,decimal_places=2)
    price = models.DecimalField(max_digits=10,decimal_places=2)
    phone = models.CharField(max_length=15)
    desc = models.TextField()
    image = models.ImageField(null=True, blank=True, default='house.jpg', upload_to='houses_pics')
    date_posted = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def get_price(self):
        if self.price - int(self.price) == 0:
            return int(self.price)
        return self.price

    def get_area(self):
        if self.area - int(self.area) == 0:
            return  int(self.area)
        return self.area
    

    def get_absolute_url(self):
        return reverse('ad-detail', kwargs={'pk': self.pk})

    