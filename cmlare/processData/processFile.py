import pandas as pd
import geopy.distance

import os
from demo.settings import BASE_DIR
links_path = "cmlare/master_files/mapped_links.csv"
links_path = os.path.join(BASE_DIR, links_path)

links = pd.read_csv(links_path)


def process_file(link_data_df):
    leftMerge = links.merge(link_data_df, left_on=links["source1_name"],right_on=link_data_df["ResourceName"],how="left")
    leftMerge = leftMerge.drop(columns = ["key_0"])
    rightMerge = leftMerge.merge(link_data_df, left_on=leftMerge["source2_name"],right_on=link_data_df["ResourceName"],how="left")
    rightMerge.dropna(subset=["ResourceName_x"])
    source1Data = rightMerge[["id_1","CollectionTime_x","latitude1","longitude1","RSL_MIN_x","RSL_MAX_x","RSL_AVG_x","TSL_MIN_y","TSL_MAX_y","TSL_AVG_y","latitude2","longitude2","frequency2","frequency_band"]]
    source2Data = rightMerge[["id_2","CollectionTime_y","latitude2","longitude2","RSL_MIN_y","RSL_MAX_y","RSL_AVG_y","TSL_MIN_x","TSL_MAX_x","TSL_AVG_x","latitude1","longitude1","frequency1","frequency_band"]]
    source1Data = source1Data.rename(columns={"id_1" : "ID","CollectionTime_x" : "DateTime","latitude1" : "XStart","longitude1" : "YStart","RSL_MIN_x":"RSL_MIN","RSL_MAX_x":"RSL_MAX","RSL_AVG_x":"RSL_AVG","TSL_MIN_y":"TSL_MIN","TSL_MAX_y":"TSL_MAX","TSL_AVG_y":"TSL_AVG","latitude2":"XEnd","longitude2": "YEnd","frequency2":"Frequency","frequency_band":"FrequencyBand"})
    source2Data = source2Data.rename(columns={"id_2" : "ID","CollectionTime_y" : "DateTime","latitude2" : "XStart","longitude2" : "YStart","RSL_MIN_y":"RSL_MIN","RSL_MAX_y":"RSL_MAX","RSL_AVG_y":"RSL_AVG","TSL_MIN_x":"TSL_MIN","TSL_MAX_x":"TSL_MAX","TSL_AVG_x":"TSL_AVG","latitude1":"XEnd","longitude1": "YEnd","frequency1":"Frequency","frequency_band":"FrequencyBand"})

    data = pd.concat([source1Data,source2Data])
    data = data.dropna()

    data["PathLength"] = data.apply(lambda row: calcPathLength(row), axis=1)

    return data

def calcPathLength(processed_data):
#     print(processed_data)
    start_cord = (processed_data["XStart"],processed_data["YStart"])
    end_cord = (processed_data["XEnd"],processed_data["YEnd"])
    return geopy.distance.vincenty(start_cord, end_cord).km

