from django.http import HttpResponseRedirect
from django.shortcuts import render,redirect
from .user_reg_forms import *
from django.contrib.auth.models import User
from django.contrib.auth.models import Group
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate,login



# # Create your views here.
def index(request):
    
    return render(request, 'app_users/index.html')

def admin_register(request):
    if request.method == 'POST':
        form = AdminRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successful Admin Registration')
            admin_group = Group.objects.get_or_create(name='HosAdmin')
            admin_group[0].user_set.add(form)
            return HttpResponseRedirect('/') 
            # return redirect('/')
        else:
            messages.error(request, 'Unable to register, try again please!')
            
    else:
        form = AdminRegisterForm()
    context = {
        'form':form
    }
    
    return render(request, 'register/admin_register.html', context)

def doctor_register(request):
    if request.method == 'GET':
        form = DoctorRegisterForm()
    else:
        if request.method == 'POST':
            form = DoctorRegisterForm(request.POST)
            if form.is_valid():
                form.save()
                messages.success(request, 'Successful Account Creation')
                # docs_group = Group.objects.get_or_create(name='HosDocs')
                # docs_group[0].user_set.add(form)
                # return HttpResponseRedirect('/')
            else:
                messages.error(request, 'Unable to register, Please try Again')
    
    return render(request, 'register/doctor_reg.html', {'form':form})

def biller_register(request):
    if request.method == 'POST':
        form = BillerRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successful Account Creation')
            billing_group = Group.objects.get_or_create(name='HosBilling')
            billing_group[0].user_set.add(form)
            return HttpResponseRedirect('app_users:index.html')
        else:
            messages.error(request, 'Unable to Register, Please Try Again')
    
    else:
        form = BillerRegisterForm()
    
    return render(request, 'register/biller_reg.html', {'form':form})

def admin_login(request):
    if request.method=='POST':
        form = AuthenticationForm(request,data=request.POST)
        if form.is_valid():
            username=form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username,password=password)
            if user is not None:
                login(request,user)
                if 'next' in request.POST:
                    return redirect(request.POST.get('next'))
                else:
                    messages.info(request, f"Successful Login {username}")
                    return redirect('/')
        else:
            messages.error(request, 'Invalid Credentials')
    else:
        form=AuthenticationForm()
    context = {
        'form':form 
    }
    return render(request, 'login/admin_log.html', context)
    

def doc_login(request):

    if request.method=='POST':
        form = AuthenticationForm(request,data=request.POST)
        if form.is_valid():
            username=form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username,password=password)
            if user is not None:
                login(request,user)
                if 'next' in request.POST:
                    return redirect(request.POST.get('next'))
                else:
                    messages.info(request, f"Successful Login {username}")
                    return redirect('/')
        else:
            messages.error(request, 'Invalid Credentials')
    else:
        form=AuthenticationForm()
    context = {
        'form':form 
    }
    return render(request, 'login/doc_log.html', context)
    

def biller_login(request):
    if request.method=='POST':
        form = AuthenticationForm(request,data=request.POST)
        if form.is_valid():
            username=form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username,password=password)
            if user is not None:
                login(request,user)
                if 'next' in request.POST:
                    return redirect(request.POST.get('next'))
                else:
                    messages.info(request, f"Successful Login {username}")
                    return redirect('/')
        else:
            messages.error(request, 'Invalid Credentials')
    else:
        form=AuthenticationForm()
    context = {
        'form':form 
    }
    return render(request, 'login/biller_log.html', context)
    

