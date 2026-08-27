from django.contrib import messages
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from .models import *

# Create your views here.
def login(request):
    if request.user.is_authenticated:
        return redirect("home")
    
    if request.method == "POST":

        username=request.POST['username']
        password=request.POST['password']
        utilisateur = authenticate(request, username = username, password = password)

        if utilisateur:
            auth_login(request, utilisateur)
            return redirect("home")
        else:
            return render (request, "login.html", {'message': 'Les réponses ne correspondent pas. Réessaie, en minuscule et sans émojis.'})
    else:
        try:
            message=request.POST.get('message', '')
        except:
            message=''
            

        return render(request, "login.html", {'message': message})


def logout(request):
    auth_logout(request)
    return redirect("login")


@login_required
def home(request):
    return render(request, "index.html")


@login_required
def message(request):

    if request.method == "POST":

        titre=request.POST['titre']
        message=request.POST['message']
        Message.objects.create(titre=titre, contenu=message, auteur=request.user)

        message='Ton message a bien été envoyé avec succès Bolingo. Je le lirais dès que possible.'
        return redirect(f'/message/?notification={message}')

    else:
        try:
            message=request.GET.get('notification', '')
        except:
            message=''
    
        return render(request, "message.html", {'message': message})

@login_required
def poeme1(request):
    return render(request, "poeme-1.html")


@login_required
def poeme2(request):
    return render(request, "poeme-2.html")


@login_required
def poeme3(request):
    return render(request, "poeme-3.html")


@login_required
def poeme4(request):
    return render(request, "poeme-4.html")


@login_required
def poeme5(request):
    return render(request, "poeme-5.html")

@login_required
def poeme6(request):
    return render(request, "poeme-6.html")

