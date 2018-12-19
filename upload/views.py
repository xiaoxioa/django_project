# -*- coding:utf-8 -*-
from django.shortcuts import render, render_to_response
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.template import RequestContext
from django.urls import reverse
from django.views.decorators.csrf import csrf_protect

from Dj_pro.settings import DATA_DIRS
from upload.models import UploadFile
from upload.forms import UploadFileForm
import numpy as np
import pandas as pd


# Create your views here.


@login_required
@csrf_protect
def upload_file(request):
    # Handle file upload
    if request.method == 'POST':
        if request.POST['type'] == u'1':
            form = UploadFileForm(request.POST, request.FILES)
            if form.is_valid():
                file = request.FILES['datafile']
                newdoc = UploadFile(datafile=file)
                user = request.user
                newdoc.username = user.username #
                newdoc.sourcefile = file.name
                newdoc.size = file.size
                newdoc.save()
                filelist = list(UploadFile.objects.filter(username=request.user.username).values())
                return render(request, 'upload_file.html', {'form': form, 'filelist': filelist}, RequestContext(request))
        elif request.POST['type'] == u'2':
            path = DATA_DIRS + "/" + request.POST['datefile_path']  # 获取保存数据文件的地址
            path.replace("/", "\\")
            data = pd.read_csv(path)
            datas = np.array(data)
            request.session['uploadDataFilePath'] = path  # 将数据文件地址保证至
            # Session，方便feature_select选用
            request.session['newDataFilePath'] = path
            return render(
                request,
                'data.html',
                {'datas': datas}
            )
    else:
        filelist = list(UploadFile.objects.filter(username=request.user.username).values())
        form = UploadFileForm()  # An empty,unbound form
    # #Load documents for the list page
    # documents = UploadFile.objects.all()
    return render(
        request,
        'upload_file.html',
        {'form': form,
         'filelist': filelist}
    )


@login_required
def upload_success(request):

    return render(
        request,
        'upload_success.html'
    )