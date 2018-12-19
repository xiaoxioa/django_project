# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
import pandas as pd
import numpy as np

# Create your views here.
def result_index(request):
    DataFilePath = request.session.get('targetResultPath', default=None)
    result = pd.read_csv(DataFilePath)
    targetResultPath = request.session.get('regressionResultPath', default=None)
    target = pd.read_csv(targetResultPath)
    score = request.session.get('regressionScore', default=None)
    return render(
        request,
        'result_index.html',
        {'target': pd.json.dumps(np.ravel(np.array(result))), 'result_len': pd.json.dumps(np.arange(len(result))),
         'predict': pd.json.dumps(np.ravel(np.array(target))), 'score': pd.json.dumps(score)}
    )


