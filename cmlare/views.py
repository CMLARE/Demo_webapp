from django.shortcuts import render

import pandas as pd
from cmlare.processData.processFile import process_file
from cmlare.ml_models.xgboostModel import wetDryWithB
# Create your views here.
from django.http import HttpResponse
import os
from demo.settings import BASE_DIR
import json

def index(request):
    return render(request= request,template_name="cmlare/index.html")

def testMap(request):
    return render(request= request,template_name="cmlare/map.html")
def xgboost(request):
    # file_path = os.path.join(BASE_DIR, "cmlare/master_files/PM_IG30028_15_201808151345_01.csv")

    # file = pd.read_csv(file_path, skiprows=1)
    file = pd.read_csv(request.FILES["files"], skiprows=1)
    file = process_file(file)

    from cmlare.ml_models.neuralNetwork import wetClassification

    wetDryClassified = wetDryWithB(file)
    predictions = wetClassification(wetDryClassified)
    predictions["predictions"] = predictions["predictions"].map(
        {"DRY": "1", "B": "2", "C": "3", "D": "4", "E": "5", "F": "6", "G": "7", "H": "8"})

    from cmlare.processData.processResult import addMipoint

    predictions = addMipoint(predictions)
    result = json.dumps(json.loads(predictions.to_json(orient='records')))

    return render(request=request,template_name="cmlare/map.html",context={"results":result})

    # return HttpResponse(result)

# def