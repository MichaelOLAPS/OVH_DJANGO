from django import forms
from .models import Image


class ImageForm(forms.ModelForm):
    """Form for the image model"""
    class Meta:
        model = Image
        fields = ('title', 'image')

class Formulaire(forms.Form):
    Societe = forms.CharField(widget=forms.TextInput(attrs={'placeholder':"Société",'class':'input-expand1'}), label=False)
    Nom = forms.CharField(widget=forms.TextInput(attrs={'placeholder':"Nom",'class':'input-expand2'}), label=False, required=True)
    Prenom = forms.CharField(widget=forms.TextInput(attrs={'placeholder':"Prénom",'class':'input-expand3'}), label=False, required=True)
    Email = forms.CharField(widget=forms.TextInput(attrs={'placeholder': "Email",'class':'input-expand4'}), label=False,required=True)
    Tel = forms.CharField(widget=forms.TextInput(attrs={'placeholder':"Tel",'class':'input-expand5'}), label=False)
    Sujet = forms.CharField(widget=forms.Textarea(attrs={'placeholder':"Ce que j'ai à dire",'class':'input-expand6'}),label=False,required=True)

