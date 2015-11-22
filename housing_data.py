import numpy as np
from sklearn import preprocessing
import datetime
import warnings
import states

def analysis(data, period):
    # combine data based on the year

    data = np.array(data)
    data = np.delete(data,-1,1)
    data = np.delete(data,-1,1)

    warnings.filterwarnings("ignore")

    timestampToYear = np.array([datetime.datetime.fromtimestamp(value / 1e3).year for value in data[:,0]])

    data[:,0] = timestampToYear

    # sort data based on the year
    sortData = np.array(sorted(data, key = lambda x: int(x[0])))

    result = []
    # Year == 2013
    if period == 1:
        result = np.mean(sortData,axis=0)

    # Year == 2012
    elif period == 2:
        for value in sortData:
            if value[0] >= 1995 and value[0] <= 2000:
                result.append(value)

        result = np.mean(np.array(result),axis=0)

    # Year == 2011
    else:
        for value in sortData:
            if value[0] >= 1990 and value[0] <= 2000:
                result.append(value)

        result = np.mean(np.array(result),axis=0)

    output = []
    for value in xrange(1,len(result)):
        output.append(result[value])

    output = preprocessing.normalize(output)

    dictionaryOutput = dict(zip(sorted(states.states.values()),output[0]))

    return dictionaryOutput



