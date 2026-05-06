from dataclasses import field
from django import forms
from .models import teacher



class CarForm(forms.ModelForm):
    class Meta:
        model = teacher
        fields = ['Name']
        #'Area'


    def __int__(self, *args, **kwargs):
        super().__init__(*args,**kwargs)
        self.fields['Name'].widget.attrs.update({"class": "form-control"})
        for fields in self.fields:
            self.fields[field].widget.attrs.update({'class':"form-control"})
#
        

class InputForm(forms.ModelForm):
    class Meta:
        model = teacher
        fields = ['Name' ]
        #'Area'

 


class test(forms.Form):
    class Meta:
        model = teacher
        fields = ['Name']

class Mydropdownform(forms.Form):
    selection = forms.ModelChoiceField(
        queryset = teacher.objects.all(),
        empty_label="(Select an option)"
    )

