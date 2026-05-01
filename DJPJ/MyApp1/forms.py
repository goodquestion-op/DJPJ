from dataclasses import field
from django import forms
from .models import teacher
from .models import teacher_name







        

class InputForm(forms.ModelForm):
    class Meta:
        model = teacher
        fields = ['Name', 'Area']

 


class Mydropdownform(forms.Form):
    selection = forms.ModelChoiceField(
        queryset = teacher.objects.all(),
        empty_label="(Select an option)"
    )

