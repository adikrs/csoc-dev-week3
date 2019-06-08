from django.shortcuts import render
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.forms import UserCreationForm


# Create your views here.


def loginView(request):
    pass

    form = UserCreationForm()
    return render(request, 'registration/login.html',{'form':form})


def logoutView(request):
    pass

def registerView(request):
    pass
    return render(request, 'registration/logout.html')