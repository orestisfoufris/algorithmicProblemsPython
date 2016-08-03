"""
Generate a power set from a give set
"""

def generatePowerSet(initialList):
    powerSet = []
    selectedSoFar = []
    directedPowerSet(initialList, 0, selectedSoFar, powerSet)
    
    return powerSet

def directedPowerSet(initialList, i, selectedSoFar, powerSet):
    if i == len(initialList):
        powerSet.append([x for x in selectedSoFar])
        return
    
    selectedSoFar.append(initialList[i])
    directedPowerSet(initialList, i+1, selectedSoFar, powerSet)
    del selectedSoFar[len(selectedSoFar) - 1]
    directedPowerSet(initialList, i+1, selectedSoFar, powerSet)    
    
    
print generatePowerSet([0, 1, 2])
