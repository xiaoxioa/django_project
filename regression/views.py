#!/usr/bin/python2.7
# -*- coding: utf-8 -*-
import time
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
# Create your views here.
import pandas as pd
from sklearn.cross_validation import train_test_split
from sklearn.tree import DecisionTreeRegressor
from sklearn import linear_model
from sklearn import neighbors
from sklearn.svm import SVR
import numpy as np
import scipy


@login_required
def regression_index(request):
    if request.method == 'POST':
        DataFilePath = request.session.get('newDataFilePath', default=None)
        regression_method = request.POST['regression_method']
        #数据预处理
        data = pd.read_csv(DataFilePath)
        # 交叉验证,拆分数据集和验证集
        data_train = data.drop(data.columns[len(data.columns) - 1], axis=1)
        data_target = data.iloc[:, len(data.columns) - 1]
        X_train, X_test, y_train, y_test = train_test_split(data_train, data_target, test_size=0.33, random_state=42)
        #保存真实值
        targetDataFilePath = "C:\Users\XXXX\Desktop\Dj_pro\Dj_pro/DATA/temp/regression_target.csv"


        if regression_method == "clf":
            result = clfRegression(X_train, X_test, y_train, y_test)
        elif regression_method == "svr":
            result = svRegression(X_train, X_test, y_train, y_test)
        elif regression_method == "KNN":
            result = knnRegression(X_train, X_test, y_train, y_test)
        elif regression_method == "line":
            result = lineRegression(X_train, X_test, y_train, y_test)
            print 1
        y_test = np.array(y_test)
        y_test = pd.DataFrame(y_test, columns=[1])
        y_test.to_csv(targetDataFilePath, index=False)
        request.session['targetResultPath'] = targetDataFilePath
        # 保存地址空间
        request.session['regressionResultPath'] = result[0]
        # 得分
        request.session['regressionScore'] = result[1]
        return render(
            request,
            'finish.html'
        )
    return render(
        request,
        'regression_index.html',
    )


def clfRegression(X_train, X_test, y_train, y_test):

    clf = DecisionTreeRegressor()
    clf.fit(X_train, y_train)
    result = clf.predict(X_test)
    score = clf.score(X_test, y_test)
    # 保存
    result = pd.DataFrame(result, columns=[1])
    regressionDataFilePath = "C:\Users\XXXX\Desktop\Dj_pro\Dj_pro/DATA/temp/regression.csv"
    result.to_csv(regressionDataFilePath, index=False)

    return [regressionDataFilePath, score]


def lineRegression(X_train, X_test, y_train, y_test):

    line = linear_model.LinearRegression()
    line.fit(X_train, y_train)
    result = line.predict(X_test)
    score = line.score(X_test, y_test)
    # 保存
    result = pd.DataFrame(result, columns=[1])
    regressionDataFilePath = "C:\Users\XXXX\Desktop\Dj_pro\Dj_pro/DATA/temp/regression.csv"
    result.to_csv(regressionDataFilePath, index=False)

    return [regressionDataFilePath, score]


def knnRegression(X_train, X_test, y_train, y_test):

    knn = neighbors.KNeighborsRegressor()
    knn.fit(X_train, y_train)
    result = knn.predict(X_test)
    score = knn.score(X_test, y_test)
    # 保存
    result = pd.DataFrame(result, columns=[1])
    regressionDataFilePath = "C:\Users\XXXX\Desktop\Dj_pro\Dj_pro/DATA/temp/regression.csv"
    result.to_csv(regressionDataFilePath, index=False)

    return [regressionDataFilePath, score]


def svRegression(X_train, X_test, y_train, y_test):

    svr = SVR()
    svr.fit(X_train, y_train)
    result = svr.predict(X_test)
    score = svr.score(X_test, y_test)
    # 保存
    result = pd.DataFrame(result, columns=[1])
    regressionDataFilePath = "C:\Users\XXXX\Desktop\Dj_pro\Dj_pro/DATA/temp/regression.csv"
    result.to_csv(regressionDataFilePath, index=False)

    return [regressionDataFilePath, score]