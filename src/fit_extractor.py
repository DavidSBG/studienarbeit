from asyncio.windows_events import NULL

def semiCirclesToDegrees(semicircles):
    if semicircles == None:
        return None
    else:
        return semicircles * (180 / (2^31))

def extract_day(fitfile):
    for record in fitfile.get_messages("record"):
        for data in record:
            if data.name == 'timestamp':
                return data.value

def extract_coordinates(fitfile):
    lat = []
    long = []
    for record in fitfile.get_messages("record"):
        for data in record:
            if data.name == 'position_lat' and data.value != None:
                lat.append(semiCirclesToDegrees(data.value))
            if data.name == 'position_long' and data.value != None:
                long.append(semiCirclesToDegrees(data.value))
    return (lat, long)

def extract_distance(fitfile):
    for record in fitfile.get_messages("record"):
        distance = 0
        for data in record:
            if data.name == 'distance':
                if data.value >= distance:
                    distance=data.value
    return int(distance)

def extract_avg_speed(fitfile):
    avg_speed = 0
    for record in fitfile.get_messages("record"):
        for data in record:
            if data.name == 'speed' and data.value != 0:
                avg_speed = avg_speed+(data.value-avg_speed)/1
                #print("new value:{}, new avg:{}{}".format(data.value, avg_speed, data.units))
    #print("Calcualted avg speed:{}".format(avg_speed*3.6))
    return avg_speed*3.6

def extract_avg_hf(fitfile):
    avg_hf = 0
    for record in fitfile.get_messages("record"):
        for data in record:
            if data.name == 'heart_rate' and data.value != 0:
                avg_hf = avg_hf+(data.value-avg_hf)/1
                #print("new value:{}, new avg:{}{}".format(data.value, avg_speed, data.units))
    #print("Calcualted avg hf:{}".format(avg_hf))
    return avg_hf

def groupInBins(dfRow, value, binCount):
    maxDistanz = dfRow.max()
    minDistanz = dfRow.min()
    distanzBinSize = (maxDistanz-minDistanz)/binCount
    
    for i in range(0, binCount):
        lowerBorder = minDistanz+distanzBinSize*i
        upperBorder = minDistanz+distanzBinSize*(i+1)
        if value>=lowerBorder and value<=upperBorder:
            return "{} - {}".format(int(lowerBorder), int(upperBorder))