from django.urls import reverse_lazy
from django.shortcuts import render
from django.views import generic
from .models import Day
from .forms import DayCreateForm


class AddView(generic.CreateView):
    model = Day
    template_name = 'blog/day_formset.html'
    form_class = DayCreateForm
    uccess_url = reverse_lazy('blog:index')

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        if 'form' in kwargs:
            # form_invalidでのget_context_data呼び出しはこっち
            kwargs['formset'] = kwargs['form']
        else:
            # getからのget_context_data呼び出しはこっち
            kwargs['formset'] = self.get_form()
        return super().get_context_data(**kwargs)

