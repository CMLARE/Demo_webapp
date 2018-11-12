import pandas


def midpointX(row):
    x1 = row["XStart"]
    # y1 = row["YStart"]
    x2 = row["XEnd"]
    # y2 = row["YEnd"]
#Input values as degrees

#Convert to radians
    # lat1 = math.radians(x1)
    # lon1 = math.radians(x2)
    # lat2 = math.radians(y1)
    # lon2 = math.radians(y2)


    # bx = math.cos(lat2) * math.cos(lon2 - lon1)
    # by = math.cos(lat2) * math.sin(lon2 - lon1)
    # lat3 = math.atan2(math.sin(lat1) + math.sin(lat2),
    #        math.sqrt((math.cos(lat1) + bx) * (math.cos(lat1)
    #        + bx) + by**2))
    # lon3 = lon1 + math.atan2(by, math.cos(lat1) + bx)
    #
    # return [round(math.degrees(lat3), 4), round(math.degrees(lon3), 4)]
    return (x1+x2)/2
def midpointY(row):
    # x1 = row["XStart"]
    y1 = row["YStart"]
    # x2 = row["XEnd"]
    y2 = row["YEnd"]

    return (y1+y2)/2

def addMipoint(predictions : pandas) -> pandas:
    predictions["midLat"] = predictions.apply(lambda row: midpointX(row),axis=1)
    predictions["midLong"] = predictions.apply(lambda row: midpointY(row),axis=1)

    return predictions[["predictions", "midLat", "midLong"]]