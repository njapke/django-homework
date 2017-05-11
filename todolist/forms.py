from django import forms
from django.core.validators import MaxValueValidator, MinValueValidator

class TodoForm(forms.Form):
    task = forms.CharField(label='Task', max_length=160,widget=forms.TextInput(attrs={'class' : 'form-control'}))
    date = forms.DateTimeField(label='Due',widget=forms.TextInput(attrs={'class' : 'form-control'}),input_formats=['%Y-%m-%d %H:%M'])
    completion = forms.IntegerField(label="Completion",widget=forms.NumberInput(attrs={'class' : 'form-control','min':'0','max':"100"}),validators=[MaxValueValidator(100),
                                                 MinValueValidator(0)])


class DeleteForm(forms.Form):
    delete = forms.IntegerField()
