from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from .forms import userUpdateForm

# Create your views here.

def signup(request):
    form=UserCreationForm()
    if request.method=="POST":
        form=UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    context={'form':form}
    return render(request,'users/signup.html',context)

def logoutconfirm(request):

    return render(request,'users/logoutconfirm.html')

def profile(request):

    form=userUpdateForm(instance=request.user)
    if (request.method=='POST'):
        form=userUpdateForm(request.POST,instance=request.user)
        if form.is_valid():
            form.save() 
            return redirect('home')

    context={'form':form}
    return render(request,'users/profile.html',context)