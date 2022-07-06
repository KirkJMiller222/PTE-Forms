from django.db import models
from django.urls import reverse
from django.conf import settings
from lots.models import Lot
from django.contrib.auth import get_user_model
User = get_user_model()

# Create your models here.

class GramStain(models.Model):
    lot_number = models.ForeignKey(Lot, related_name="gramstainform", on_delete=models.CASCADE)
    start_time = models.DateTimeField()
    completion_time = models.DateTimeField()
    email = models.EmailField()
    name = models.CharField(max_length=256)
    technician_name = models.CharField(max_length=256)
    colony_count = models.PositiveIntegerField()
    organism_discription = models.TextField(max_length=256)
    gram_stain_result = models.BooleanField()

    def __str__(self):
        return self.lot_number

    def save(self,*args,**kwargs):
        super().save(*args,**kwargs)

    def get_absolute_url(self):
        return reverse("pteforms:single",kwargs={'pk':self.pk})

    class Meta:
        ordering = ['-start_time']
