from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy 
from django.views import generic
from .forms import DayCreateForm
from .models import Day


class IndexView(generic.ListView):
    model = Day
    paginate_by = 3


class AddView(generic.CreateView):
    model = Day
    form_class = DayCreateForm
    success_url = reverse_lazy('blog:index')

    




