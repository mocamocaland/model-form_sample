from django import forms
from  .models import Day


class DayCreateForm(forms.ModelForm):

    class Meta:
        model = Day
        fields = '__all__'


DayCreateFormSet = forms.modelformset_factory(
    Day, form=DayCreateForm, extra=3, can_delete=True
)
