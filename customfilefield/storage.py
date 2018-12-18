# -*- coding:utf-8 -*-
'''
This file is to refactor storage function 
so that it can rename the file uploaded
'''

from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse
from django.conf import settings
import os, time, random


class FileStorage(FileSystemStorage):
    def __init__(self, location=settings.MEDIA_ROOT, base_url=settings.MEDIA_URL):
        # initialize
        super(FileStorage, self).__init__(location,base_url)

    # redefine _save()
    def _save(self, name, content):
        # file extension
        ext = os.path.splitext(name)[1]

        # file directory
        d = os.path.dirname(name)

        # define file name by YmdHMS
        fn = time.strftime("%Y%m%d%H%M%S")
        fn = fn + "_%d"%random.randint(0,100)

        # rename the file
        name = os.path.join(d, fn+ext)

        # Call the parent class method
        return super(FileStorage, self)._save(name, content)

