from django.contrib.auth.forms import forms
from .models import Reader


class UpdateProfileForm(forms.ModelForm):
    class Meta:
        model = Reader
        exclude = ('is_author',)