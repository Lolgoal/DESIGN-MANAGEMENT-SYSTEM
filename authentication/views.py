from django.shortcuts import render
from django.shortcuts import HttpResponse
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
# Create your views here.
from .forms import  UserRegistrationForm, UserEditForm
from .decorators import unauthenticated_member
from django.contrib.auth.models import User
from django.shortcuts import redirect
from django.urls import reverse
from django.http import JsonResponse
from django.contrib	import	messages
from django.views.generic import ListView

       
   
@unauthenticated_member           
def register(request):
    if request.method== 'POST':
        user_form= UserRegistrationForm(request.POST)
        
        if user_form.is_valid():
            new_user= user_form.save(commit=False)
            new_user.set_password(user_form.cleaned_data['password'])
            new_user.save()
            return render(request, 'account/register_done.html', {'new_user':new_user})
        
    else:
        user_form= UserRegistrationForm()
    return render(request, 'account/register.html', {'user_form':user_form})
    
        


@login_required 
def login_success(request): 
    return redirect("dashboard")





def main(request):
    return render(request,'main/index.html')
