from django import forms
from .models import Food

class FoodForm(forms.ModelForm):
    CHOICES=(
        ('Veg','veg'),
        ('Non-Veg','non-veg')
        )
    foodType = forms.ChoiceField(widget=forms.RadioSelect, choices=CHOICES)
    foodDescription=forms.CharField(widget=forms.Textarea(attrs={'class':'form-control','rows':3,'cols':25}))
    class Meta:
        model=Food
        fields="__all__"
        widgets={
            'foodName':forms.TextInput(attrs=
            {'class':'form-control'})
        }