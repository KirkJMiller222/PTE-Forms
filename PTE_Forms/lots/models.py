from django.db import models
from django.utils.text import slugify
from django.contrib.auth import get_user_model
User = get_user_model()
from django import template
register = template.Library()
from django.urls import reverse
# Create your models here.

class Lot(models.Model):
    lot_number = models.CharField(max_length=10, unique=True)
    slug = models.SlugField(allow_unicode=True, unique=True)
    harvest_size = models.DecimalField(max_digits=6, decimal_places=2)
    date_shipped = models.DateField()
    date_received = models.DateField()

    def __str__(self):
        return self.lot_number

    def save(self,*args,**kwargs):
        self.slug = slugify(self.lot_number)
        super().save(*args,**kwargs)

    def get_absolute_url(self):
        return reverse('lots:single',kwargs={'slug':self.slug})

    class Meta:
        ordering = ['lot_number']


    pass
