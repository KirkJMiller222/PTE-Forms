from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views import generic
from django.http import Http404
from . import models
from . import forms
from braces.views import SelectRelatedMixin
from django.contrib.auth import get_user_model
User = get_user_model()

# Create your views here.

class GramStainList(SelectRelatedMixin, generic.ListView):
     model = models.GramStain
     select_related = ('lot')

class LotGramStain(generic.ListView):
    model = models.GramStain
    template_name = 'pteforms/pteforms_list.html'

    def get_queryset(self):
        try:
            return self.gramstain.all()
        except GramStain.DoesNotExist:
            raise Http404
        else:
            return self.gramstain.all()

    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        context['lot_number'] = self.lot_number
        return context

class GramStainDetail(SelectRelatedMixin, generic.DetailView):
    model = models.GramStain
    select_related = ('lot_number')

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(lot__lot_number__iexact=self.kwargs.get('lot_number'))

class CreateGramStain(LoginRequiredMixin,SelectRelatedMixin,generic.CreateView):
    fields = ('__all__')
    model = models.GramStain

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return super().form_valid(form)

class DeleteGramStain(LoginRequiredMixin,SelectRelatedMixin,generic.DeleteView):
    model = models.GramStain
    select_related = ('lot_number')
    success_url = reverse_lazy ('lots:all')

    def get_queryset(self):
        queryset = super().get.queryset()
        return queryset.filter(user_id = self.request.user.id)

    def delete(self,*args,**kwargs):
        messages.success(self.request, 'Gram Stain Deleted')
        return super().delete(*args,**kwargs)
