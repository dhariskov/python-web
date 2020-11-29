from django import forms

from app.models import Profile, Expense


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'


class ExpenseForm(forms.ModelForm):
    class Meta:
        model = Expense
        fields = '__all__'
