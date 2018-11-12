import pandas as pd
from cmlare.processData.processFile import process_file
from cmlare.ml_models.xgboostModel import wetDryWithB

file = pd.read_csv("../master_files/PM_IG30028_15_201808151345_01.csv",skiprows =1)
file = process_file(file)
from cmlare.ml_models.neuralNetwork import wetClassification

print(file)
wetDryClassified = wetDryWithB(file)
predictions = wetClassification(wetDryClassified)
predictions["predictions"] = predictions["predictions"].map({"DRY":"A","B":"B","C":"C","D":"D","E":"E","F":"F","G":"G","H":"H"})


from cmlare.processData.processResult import addMipoint

predictions = addMipoint(predictions)
# print(predictions.loc[predictions["predictions"]!="A"])
print(predictions)
print(predictions.loc[73])