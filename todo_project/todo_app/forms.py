from django import forms

def max_len_validator(value):
    if not value or len(value) < 2:
        raise forms.ValidationError('Vnimavaj')

class TodoForm(forms.Form):
    title = forms.CharField(label='title', max_length=20, )
    description = forms.CharField(widget=forms.Textarea, validators=((max_len_validator),))
