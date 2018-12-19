#!/usr/bin/python
# -*- coding: utf-8 -*-
import time
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required

# Create your views here.

import pandas as pd
import numpy as np
from sklearn.decomposition import PCA
from sklearn.lda import LDA


@login_required
def feature_select_index(request):
    if request.method == 'POST':

        path = request.session.get("uploadDataFilePath", default=None)
        method = request.POST['feature_selection_method']
        if method == "PCA":
            #result[0] PCA值  #result[1] target/regression
            newData = pca(path)
        elif method == "LDA":
            newData = lda(path)
        else:
            print 1
            #reuslt = LDA(path)
        # 经过PCA处理过后的数据转换为DataFrame

        newDataFilePath = "C:/Users/XXXX/Desktop/Dj_pro/Dj_pro/DATA/temp/feature_selected.csv"
        newData.to_csv(newDataFilePath, index=False)
        request.session['newDataFilePath'] = newDataFilePath
        return render(
            request,
            'success.html',
            {
                'newdata' : np.array(newData)
            }
        )
    return render(
        request,
        'feature_select_index.html',
    )

@login_required
def feature_success(request):
    return render(
        request,
        'success.html'
    )

def success(request):
    print 2;

def pca(path):

    data = pd.read_csv(path)

    data_train = data.drop(data.columns[len(data.columns)-1],axis = 1)
    data_target = data.iloc[:, len(data.columns) - 1]

    pca = PCA(n_components=0.999)

    newData = pca.fit_transform(data_train)

    datas_train = np.array(newData)
    datas_target = np.array(data_target)

    newData = pd.DataFrame(newData, columns=range(newData.shape[1]))
    newData.insert(len(newData.columns), 'target', datas_target)
    return newData

def lda(path):

    data = pd.read_csv(path)

    data_train = data.drop(data.columns[len(data.columns)-1],axis = 1)
    data_target = data.iloc[:, len(data.columns) - 1]

    pca = PCA(n_components=0.999)

    newData = pca.fit_transform(data_train)

    datas_train = np.array(newData)
    datas_target = np.array(data_target)

    newData = pd.DataFrame(newData, columns=range(newData.shape[1]))
    newData.insert(len(newData.columns), 'target', datas_target)
    return newData

