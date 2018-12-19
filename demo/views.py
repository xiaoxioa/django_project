#-*- coding: utf-8 -*-
# from django.shortcuts import render, render_to_response
# from django.http import HttpResponse
# # from django.contrib.auth.models import User
# from demo.models import User
# from demo.form import UserForm
#
#
# # Create your views here.
#
# def register(request):
#     if request.method == 'POST':
#         userform = UserForm(request.POST)
#         if userform.is_valid():
#             username = userform.cleaned_data['username']
#             password = userform.cleaned_data['password']
#             email = userform.cleaned_data['email']
#
#             User.objects.create(username=username,password=password,email=email)
#             User.save()
#
#             return HttpResponse('User registration is successful!')
#     else:
#         userform = UserForm()
#     return render_to_response('register.html',{'userform':userform})
#
# def login(request):
#     if request.method == 'POST':
#         userform = UserForm(request.POST)
#         if userform.is_valid():
#             username = userform.cleaned_data['username']
#             password = userform.cleaned_data['password']
#
#             user = User.objects.filter(username__exact=username,password__exact=password)
#
#             if user:
#                 return render_to_response('../home/templates/index.html',{'userform':userform})
#             else:
#                 return HttpResponse('Username or password is invalid!')
#     else:
#         userform = UserForm()
#     return render_to_response('login.html',{'userform':userform})


from demo.form import *
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout,login
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from django.views.decorators.csrf import csrf_protect
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.template import RequestContext


@csrf_protect
def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = User.objects.create_user(
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password1'],
                email=form.cleaned_data['email']
            )
            user.save()

            return HttpResponseRedirect('./success/')
    else:
        form = RegistrationForm()

    return render(request, 'registration/register.html', {'form': form})


def register_success(request):
    return render(
        request,
        'registration/success.html'
    )


def logout_page(request):
    logout(request)
    return HttpResponseRedirect('/')


# @csrf_protect
# def login_page(request):
#     errors = []
#     authentication_form = AuthenticationForm
#     if request.method == "POST":
#         form = authentication_form(request, data=request.POST)
#         if form.is_valid():
#             try:
#                 username=User.objects.get(username=form.cleaned_data['username'])
#             except User.DoesNotExist:
#                 errors.append('Username invalid!')
#             else:
#                 user = authenticate(username=username, password=form.cleaned_data['password'])
#                 if user is not None:
#                     if user.is_active:
#                         login(request, user)
#                         return HttpResponseRedirect('/')
#                     else:
#                         errors.append('User not activated')
#                 else:
#                     errors.append('Username and password didn\'t match ')
#
#     else:
#         form = AuthenticationForm()
#     variables = {
#         'form': form,
#         'errors': errors
#     }
#     return render(
#         request,
#         'registration/login.html',
#         variables
#     )

@login_required
def home(request):
    return render(
        request,
        'home.html',
        {'user': request.user},
    )
