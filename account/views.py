from django.contrib.auth import authenticate, login,logout
from django.shortcuts import render, redirect
# Create your views here.
from pyexpat.errors import messages
from django.contrib import messages


from .forms import  UserCreationForm


def acces(request):
    context = {}
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(request, email=email, password=password)
        if user is not None:
            login(request, user)
            if user.is_client:
                messages.success(request, 'Bienvenu')
                return redirect('acceuil')
            else:
                messages.success(request, "votre demande est en cour d'acceptation")
                return redirect('acces')
        else:
            messages.error(request, "error d'authentification")

    return render(request, 'account/Acces.html', context)
def acceuil(request):
    return render(request, 'societe/acceuil.html')


def inscription(request):

    form =UserCreationForm()
    if request.method=='POST':
        form=UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('email')
            messages.success(request, "Votre Demande est envoye."
                                      "Attendre une email pour la confirmation de l'acceptation" )
            return redirect('acces')
        else:
            messages.error(request, form.errors)


    context={'form': form}
    return render(request, 'account/inscription.html',context)

def logoutUser(request):
    logout(request)
    return redirect('index')