from django import forms
from  .models import Day, Category


class DayCreateForm(forms.ModelForm):

    class Meta:
        model = Day
        fields = '__all__'


DayInlineFormSet = forms.inlineformset_factory(
    Category, Day, fields=('title', 'text'), can_delete=False
)