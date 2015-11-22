import numpy as np
from sklearn import preprocessing
import warnings
import collections
from states import states

def analysis(data, period):
    warnings.filterwarnings("ignore")

    # Year == 2013
    if period == 1:
        result = [element for element in data if element[2] == 2013]

    # Year == 2012
    elif period == 2:
        result = [element for element in data if element[2] == 2012]
    # Year == 2011
    else:
        result = [element for element in data if element[2] == 2011]


    stateWiseResult = np.array(sorted(result, key = lambda x: (x[1])))
    stateCost =  preprocessing.normalize(stateWiseResult[:,0])
    statesName = stateWiseResult[:,1]

    # mapping cost with states

    dictionary = dict(zip(statesName,stateCost[0]))

    for value in states.values():
        if value not in dictionary.keys():
            dictionary[value] = 0

    output = dict(collections.OrderedDict(sorted(dictionary.items())))

    return output







