from __future__ import unicode_literals
#storage function help to rename file
import time

from customfilefield.storage import FileStorage
from django.db import models


# Create your models here.

# def upload_to(instance, filename):
#     return '/'.join([DATA_ROOT, instance.user_name, filename])
#
# class UploadFile(models.Model):
#     datafile = models.FileField(upload_to=upload_to)

'''
Upload datafile with name changing
'''

# change file path by return an upload_to string
def get_file_path(instance, filename):
    username = instance.username
    dir_name = 'datasets'
    # print username, " ", filename
    # return '/datasets/'.join([username, filename])
    return '/'.join([dir_name, username, filename])


class UploadFile(models.Model):
    datafile = models.FileField('datafile', upload_to=get_file_path, storage=FileStorage())
    username = models.CharField('username', max_length=50, default="nobody")
    sourcefile = models.CharField('sourcefile', max_length=50, default="none")
    size = models.CharField('size', max_length=30, default="none")
    date = models.CharField('date', max_length=32, default=time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))

    def __str__(self):
        return self.username

    class Meta:
        ordering = ['username']

