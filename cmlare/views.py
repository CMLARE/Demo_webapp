from django.shortcuts import render

import pandas as pd
from cmlare.processData.processFile import process_file
from cmlare.ml_models.xgboostModel import wetDryWithB
# Create your views here.
from django.http import HttpResponse
import os
from demo.settings import BASE_DIR


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def points(request):

    file_path = os.path.join(BASE_DIR, "cmlare/master_files/PM_IG30028_15_201808151345_01.csv")

    file = pd.read_csv(file_path, skiprows=1)

    file = process_file(file)

    from cmlare.ml_models.neuralNetwork import wetClassification

    wetDryClassified = wetDryWithB(file)
    predictions = wetClassification(wetDryClassified)
    predictions["predictions"] = predictions["predictions"].map(
        {"DRY": "A", "B": "B", "C": "C", "D": "D", "E": "E", "F": "F", "G": "G", "H": "H"})

    from cmlare.processData.processResult import addMipoint

    predictions = addMipoint(predictions)
    # print(predictions.loc[predictions["predictions"]!="A"])
    print(predictions)
    return HttpResponse(pd.DataFrame.to_json(predictions))