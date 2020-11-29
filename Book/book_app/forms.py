from django import forms
from django.core.exceptions import ValidationError

from book_app.models import Book



class BookForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.add_form_control_class_to_all()

    def add_form_control_class_to_all(self):
        for (_, field) in self.fields.items():
            field.widget.attrs['class'] = 'form-control'

    def clean_pages(self):
        pages = self.cleaned_data['pages']
        if pages <= 0:
            raise ValidationError('Pages should > 0')
        return pages

    class Meta:
        model = Book
        fields = '__all__'
        # widgets = {
        #     'title': forms.TextInput(
        #         attrs={
        #             'class': 'form-control',
        #         },
        #     ),
        #     'pages': forms.NumberInput(
        #         attrs={
        #             'class': 'form-control',
        #         }
        #     ),
        #     'author': forms.TextInput(
        #         attrs={
        #             'class': 'form-control',
        #         }
        #     ),
        #     'description': forms.Textarea(
        #         attrs={
        #             'class': 'form-control'
        #         }
        #     ),
        # }



