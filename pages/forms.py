from django import forms
from .models import Feedback


class HomeForm(forms.ModelForm):
    post=forms.CharField()

    class Meta:
        model = Feedback
        fields = ('first_name', 'message', 'city', 'mobile_no', 'email_id')