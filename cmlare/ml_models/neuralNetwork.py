import pickle
from sklearn.preprocessing import StandardScaler

import pandas as pd
# from xgboost import XGBClassifier

neuralWetModel13LayerPath = "../trained_models/mlp_ANN_rainy_only_h-13-500.sav"

neuralWetModel13Layer = pickle.load(open(neuralWetModel13LayerPath, "rb"))
selected_feature_types = ["FrequencyBand","PathLength","RSL_AVG","RSL_MIN","RSL_MAX","TSL_MAX"]


def wetClassification(dataframe):
    wetLinks = dataframe.loc[dataframe["predictions"] != "DRY"]
    print(wetLinks.shape)
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

    dataframe = pd.concat([dryLinks,wetLinks])

    return dataframe
