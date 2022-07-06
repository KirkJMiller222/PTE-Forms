from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.urls import reverse
from django.views import generic
from lots.models import Lot

# Create your views here.
class CreateLot(LoginRequiredMixin, generic.CreateView):
    fields = ('lot_number','harvest_size','date_shipped','date_received')
    model = Lot

class SingleLot(generic.DetailView):
    model = Lot

class ListLot(generic.ListView):
    model = Lot 
