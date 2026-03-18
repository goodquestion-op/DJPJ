from dataclasses import field
from django import forms
from .models import teacher

FRUIT_CHOICES= [
    ('orange', 'Oranges'),
    ('cantaloupe', 'Cantaloupes'),
    ('mango', 'Mangoes'),
    ('honeydew', 'Honeydews'),
    ]

class CarForm(forms.ModelForm):
    class Meta:
        model = teacher
        fields = ['Name','Area']


    def __int__(self, *args, **kwargs):
        super().__init__(*args,**kwargs)
        self.fields['Name'].widget.attrs.update({"class": "form-control"})
        for fields in self.fields:
            self.fields[field].widget.attrs.update({'class':"form-control"})

        

class InputForm(forms.ModelForm):
    class Meta:
        model = teacher
        fields = ['Name', 'Area']

 

class UserForm(forms.Form):
    first_name= forms.CharField(max_length=100)
    last_name= forms.CharField(max_length=100)
    email= forms.EmailField()
    age= forms.IntegerField()
    favorite_fruit= forms.CharField(label='What is your favorite fruit?', widget=forms.Select(choices=FRUIT_CHOICES))

class test(forms.Form):
    class Meta:
        model = teacher
        fields = ['Name']



