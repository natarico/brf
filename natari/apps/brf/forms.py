from django import forms
from .models import Profile

class ProfileForm(forms.ModelForm):
    CHOICES =(('1', "Rain"),
            ('2', "Sun"),
            ('3', "Snow"),
            ('4', "Clouds"),
            ('5', "Storms"))
    city = forms.CharField(label="What city are you located in?", max_length=20)
    weather = forms.ChoiceField(choices=CHOICES, label="Which do you prefer:", widget=forms.RadioSelect(), initial=1)
        
    class Meta:
        model = Profile
        fields = ('city', 'weather')
