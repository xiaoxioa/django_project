from __future__ import unicode_literals
import numpy as np
import pandas as pd
import time

from django.db import models

# change file path by return an upload_to string
from customfilefield.storage import FileStorage


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