from django.contrib.auth.forms import forms
from reader.models import Reader


class CreateProfileForm(forms.ModelForm):
    class Meta:
        model = Reader
        exclude = ('is_author', 'user')