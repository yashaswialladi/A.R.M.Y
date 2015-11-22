import housing_data
import military_data
import queries
import numpy as np
from runQueryRun import getDataFromQuery
from sklearn import preprocessing


def analysis(inputQuery):

    if len(inputQuery) == 3:
        analyzeQueryH = queries.queries['housing']
        analyzeQueryM = queries.queries['military']
        house = (housing_data.analysis(getDataFromQuery(analyzeQueryH),inputQuery[2]))
        military = (military_data.analysis(getDataFromQuery(analyzeQueryM),inputQuery[2]))
        finalOutput = dict((k, v * military[k]) for k, v in house.items() if k in military)

    elif len(inputQuery) == 2:
        if inputQuery[0] == "housing":
            analyzeQueryH = queries.queries['housing']
            finalOutput = (housing_data.analysis(getDataFromQuery(analyzeQueryH),inputQuery[1]))
        elif inputQuery[0] == "military":
            analyzeQueryM = queries.queries['military']
            finalOutput = (military_data.analysis(getDataFromQuery(analyzeQueryM),inputQuery[1]))
        elif inputQuery[0] == "deathCountry":
            analyzeQueryD = queries.queries['deathCountry']
            output = getDataFromQuery(analyzeQueryD)
            value = []
            for v in output:
                value.append(v[1])
            value = preprocessing.normalize(value)
            finalOutput = []
            for v in xrange(len(value[0])):
                finalOutput.append([output[v][0],value[0][v]])
            finalOutput = dict(finalOutput)

    return finalOutput

#print analysis(['deathCountry',2])