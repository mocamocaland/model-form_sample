from django.shortcuts import render
from django.views import generic
from .models import Day
from .forms import DayCreateForm


class AddView(generic.CreateView):
    model = Day
    form_class = DayCreateForm
    #success_url = reverse_lazy('diary:index')

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

