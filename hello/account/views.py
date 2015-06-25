from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from forms import LoginForm
from django.contrib import messages
import hello
# Create your views here.


def index(request):
    return HttpResponse("Hello, world. You're at the BoordComputer index.")

def inloggen(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            next = request.POST.get('next', None);
            user = authenticate(username=username, password=password)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    redirect_url = next if next is not None else BITBV.settings.LOGIN_REDIRECT_URL
                    return HttpResponseRedirect(redirect_url)
                else:
                    messages.add_message(request, messages.ERROR, "Gebruiker niet actief")
            else:
                messages.add_message(request, messages.ERROR, "Gebruikersnaam en/of wachtwoord is onjuist")
    else:
        form = LoginForm()

    return render(request, 'account/login.html', {
        'form': form,
        })

def uitloggen(request):
    form = LoginForm()
    if request.user.is_authenticated():
            logout(request)
            messages.add_message(request, messages.SUCCESS, 'Succesvol uitgelogd!')
    else:
            messages.add_message(request, messages.INFO, 'Er was geen gebruiker ingelogd.')

    return HttpResponseRedirect('/account/inloggen')
