# -*- coding: utf-8 -*-
from django import forms

class SelectFeatureForm(forms.Form):
    feature_num = forms.IntegerField(max_value=2000)