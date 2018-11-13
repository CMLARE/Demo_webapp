import pickle
from sklearn.preprocessing import StandardScaler

import pandas as pd
# from xgboost import XGBClassifier
import os
from demo.settings import BASE_DIR
neuralWetModel13LayerPath = "cmlare/trained_models/mlp_ANN_rainy_only_h-13-500.sav"
neuralWetModel13LayerPath = os.path.join(BASE_DIR, neuralWetModel13LayerPath)

neuralWetModel13Layer = pickle.load(open(neuralWetModel13LayerPath, "rb"))
selected_feature_types = ["FrequencyBand","PathLength","RSL_AVG","RSL_MIN","RSL_MAX","TSL_MAX"]


def wetClassification(dataframe):
    wetLinks = dataframe.loc[dataframe["predictions"] != "DRY"]
    X = wetLinks[selected_feature_types]
    scaler = StandardScaler()
    # Fit only to the training data
    print("Fitting data..")
    scaler.fit(X)
    print("Data fitting finished.")
    StandardScaler(copy=True, with_mean=True, with_std=True)
    X = scaler.transform(X)
    predictions = neuralWetModel13Layer.predict(X)
    wetLinks["predictions"] = predictions

    dryLinks = dataframe.loc[dataframe["predictions"] == "DRY"]

    for index,row in wetLinks.iterrows():
        try:
            dryLinks.loc[index]
            dryLinks.drop(index,inplace=True)
        except KeyError:
            continue
    dataframe = pd.concat([dryLinks,wetLinks])
    # print(dataframe)
    return dataframe

