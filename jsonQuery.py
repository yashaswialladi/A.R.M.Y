import housing_data
import military_data
import queries
from runQueryRun import getDataFromQuery

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

    return finalOutput


analysis(['housing','military',1])