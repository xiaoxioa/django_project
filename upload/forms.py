# -*- coding: utf-8 -*-
from django import forms

class UploadFileForm(forms.Form):
    datafile = forms.FileField(
        label='Select a data file',
        help_text='Hello'
    )