#-*- coding: utf-8 -*-
# from django import forms
# from django.contrib.auth.models import User
# import re
#
# class LoginForm(forms.Form):
#    email = forms.EmailField(
#       label='email',
#       required=True,
#       error_messages={'required':'Please enter a correct Email'},
#       widget=forms.EmailInput(attrs={"class":'form-control',"value":'Registered Email','style':'color:#ADADAD'})
#    )
#    password = forms.CharField(
#       label='password',
#       required=True,
#       error_messages={'required':'Please enter correct password'},
#       widget=forms.PasswordInput(attrs={"class": 'form-control', "value": "Password", 'style': 'color:#ADADAD'})
#    )
#
# class RegisterForm(forms.Form):
#    name = forms.CharField(
#       label='name',
#       max_length=50,
#       required=True,
#       error_messages={'required': 'Please enter your username'},
#       widget=forms.TextInput(attrs={'class':"form-control","value":"Write an English name",'style':'color:#ADADAD'}),
#    )
#    email = forms.EmailField(
#       label='email',
#       required=True,
#       error_messages={'required':'Please enter a correct Email'},
#       widget=forms.EmailInput(attrs={"class":'form-control',"value":'Email used for login','style':'color:#ADADAD'})
#    )
#    password1 = forms.CharField(
#       label='password',
#       required=True,
#       error_messages={'required':'Please enter your password'},
#       widget=forms.PasswordInput(attrs={"class": 'form-control', "value": "Please enter your password"})
#    )
#    password2 = forms.CharField(
#       label='password',
#       required=True,
#       error_messages={'required':'Please check your password'},
#       widget=forms.PasswordInput(attrs={"class":'form-control', "value":"Please check password"})
#    )
#    def clean_name(self):
#       name = self.cleaned_data['name']
#       #check illegal name
#       if ' ' in name:
#          raise forms.ValidationError('No blanks')
#       if not re.search(r'^\w+$', name):
#          raise forms.ValidationError('Only letters or numbers')
#       try:
#          the_name = User.objects.get(username=name)
#       except User.DoesNotExist:
#          return name
#       raise forms.ValidationError('This name has been registered!')
#
#
#    def clean_email(self):
#       email = self.cleaned_data['email']
#       try:
#          user = User.objects.get(email=email)
#       except User.DoesNotExist:
#          return email
#       raise forms.ValidationError('This email has been registered')
#
#    def clean_password1(self):
#       password = self.cleaned_data['password1']
#       pwd_num = len(password)
#       if pwd_num < 6:
#          raise forms.ValidationError('Password should be longer than 6 digits')
#       if not re.search(r'^\w+$', password):
#          raise forms.ValidationError('Only letters or numbers')
#       return password
#
#    def clean_password2(self):
#       if 'password1' in self.cleaned_data:
#          password1 = self.cleaned_data['password1']
#          password2 = self.cleaned_data['password2']
#          if password1 == password2:
#             return password2
#          raise forms.ValidationError('Please Check Your Password Again!')
#

# class UserForm(forms.Form):
#     username = forms.CharField(label='用户名', max_length=50)
#     password = forms.CharField(label='密码', widget=forms.PasswordInput())
#     email = forms.EmailField(label='邮箱')


from django import forms
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _


class RegistrationForm(forms.Form):
    username = forms.RegexField(regex=r'^\w+$', widget=forms.TextInput(attrs=dict(required=True, max_length=30)),
                                label=_("Username"), error_messages={
            'invalid': _("This value must contain only letters, numbers and underscores.")})
    email = forms.EmailField(widget=forms.TextInput(attrs=dict(required=True, max_length=30)), label=_("Email address"))
    password1 = forms.CharField(
        widget=forms.PasswordInput(attrs=dict(required=True, max_length=30, render_value=False)), label=_("Password"))
    password2 = forms.CharField(
        widget=forms.PasswordInput(attrs=dict(required=True, max_length=30, render_value=False)),
        label=_("Password (again)"))

    def clean_username(self):
        username = self.cleaned_data['username']
        try:
            user = User.objects.get(username__iexact=self.cleaned_data['username'])
        except User.DoesNotExist:
            return username
        raise forms.ValidationError(_("The username already exists. Please try another one."))

    def clean(self):
        if 'password1' in self.cleaned_data and 'password2' in self.cleaned_data:
            if self.cleaned_data['password1'] != self.cleaned_data['password2']:
                raise forms.ValidationError(_("The two password fields did not match."))
        return self.cleaned_data




