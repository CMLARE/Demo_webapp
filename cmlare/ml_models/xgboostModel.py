import pickle
from sklearn.preprocessing import StandardScaler
import math
import pandas as pd
# from xgboost import XGBClassifier

xgboostWetDryWithBModelPath = "../trained_models/XGBOOST_2_layer_classification_with_B_as_dry.sav"

xgboostWetDryWithBModel = pickle.load(open(xgboostWetDryWithBModelPath, "rb"))
selected_feature_types = ["FrequencyBand","PathLength","RSL_AVG","RSL_MIN","RSL_MAX","TSL_MAX"]


def wetDryWithB(dataframe):
    print(dataframe.columns)
    X = dataframe[selected_feature_types]
    scaler = StandardScaler()
    # Fit only to the training data
    print("Fitting data..")
    scaler.fit(X)
    print("Data fitting finished.")
    StandardScaler(copy=True, with_mean=True, with_std=True)
    X = scaler.transform(X)
    predictions = xgboostWetDryWithBModel.predict(X)
    dataframe["predictions"] = predictions

    return dataframe

# from sklearn.metrics import classification_report,confusion_matrix
# print(classification_report(predictions["class"],predictions["predictions"]))
# print(confusion_matrix(predictions["class"],predictions["predictions"]))
