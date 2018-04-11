from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.views import generic
from .forms import DayInlineFormSet, DayCreateForm
from .models import Category, Day



class IndexView(generic.ListView):
    model = Day


class AddView(generic.CreateView):
    model = Day
    form_class = DayCreateForm
    success_url = reverse_lazy('diary:index')


class CategoryCreateView(generic.CreateView):
    model = Category
    fields = '__all__'
    success_url = reverse_lazy('diary:index')

    def form_valid(self, form):
        self.object = form.save(commit=False)

        formset = DayInlineFormSet(self.request.POST, instance=self.object)

        if formset.is_valid():
            self.object.save()
            formset.save()
            return HttpResponseRedirect(self.get_success_usl())
        else:
            return self.render_to_response(self.get_context_data(form=form, formset=formset))

        def get_context_data(self, **kwargs):
            if 'formset' not in kwargs:
                kwargs['formset'] = DayInlineFormSet(self.request.POST or None)
            return super().get_context_data(**kwargs)
