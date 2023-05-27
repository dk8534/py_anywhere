from django import forms
from .models import movie
from django.core import validators

class AddMoviePage(forms.ModelForm):
    # to add validation for any model form field then we required to define that before Meta class,like that: 
    # rating field validator
    def rating_validator(value):
        if value > 5:
            raise forms.ValidationError('Rating should be 0 to 5') 
    rating = forms.IntegerField(validators=[rating_validator])

    class Meta:
        model = movie
        fields = '__all__'