#from django.http import HttpResponse
from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import ImageForm
from .forms import Formulaire
from django.core.mail import send_mail
from django.template.loader import render_to_string
#from django.core import mail
#from .models import Person
#from django.core.cache import cache
#import json
#import requests

def index(request):
    return render(request,'myapp/index.html')

def image_upload_view(request):
    """Process images uploaded by users"""
    if request.method == 'post':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            # Get the current instance object to display in the template
            img_obj = form.instance
            send_mail("Sujet pour le test","test",'w.zenaidi@olaps.fr','m.lapeyrere@olaps.fr')
            return render(request, 'myapp/index.html', {'form': form, 'img_obj': img_obj})
    else:
        form = ImageForm()
    return render(request, 'myapp/index.html', {'form': form})

def get_name(request):
    if request.method == 'POST':
        form = Formulaire(request.POST)
        
        if form.is_valid():
            email = form.cleaned_data['Email']
            Nom = form.cleaned_data['Nom']
            Societe = form.cleaned_data['Societe']
            Prenom = form.cleaned_data['Prenom']
            Tel = form.cleaned_data['Tel']
            Sujet = form.cleaned_data['Sujet']
            html = render_to_string('myapp/emails/contactform.html',{
                'Email':email,
                'Nom':Nom,
                'Societe':Societe,
                'Prenom':Prenom,
                'Tel':Tel,
                'Sujet':Sujet
            })
            send_mail('Demande de contact',Sujet,email,['m.lapeyrere@olaps.fr'],html_message=html)    
            return HttpResponseRedirect('/myapp')
    else :
        form = Formulaire()
   
    return render(request, 'myapp/Form.html',{'form': form})