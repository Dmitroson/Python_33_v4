import numpy as np
import pandas as pd
import math

def average_harmonic(items: list):
    n = len(items)
    s = 0
    for i in items:
        j = str(i).replace(',', '.')
        if(math.isnan(float(j))):
            continue
        
        s += (1 / float(j))
    
    if(s == 0):
        return 0
    else:
        return n / s
    
def get_nan_indexes(items: list):
    indexes = []
    k = 0
    for i in items:
        j = str(i).replace(',', '.')
        if(math.isnan(float(j))):
            indexes.append(k)
        k += 1
        
    return indexes
    
def unique_elements(items: list):
    uniqueElements = set(items)
    return list(uniqueElements)

# main code

file = pd.read_csv('Base.txt', delimiter='\t')
skipColumn = True
indexes = []
table = {}
for columnName in file:
    if(skipColumn):
        table[''] = file[columnName].tolist()
        skipColumn = False
        continue
    
    columnValues = file[columnName].tolist()
    ah = "%.4f" % average_harmonic(columnValues)
    indexes = indexes + get_nan_indexes(columnValues)
    
    result = file[columnName].fillna(ah).tolist()
    table[columnName] = result

pd.DataFrame(table).to_csv('TabSH.txt', index=None, sep='\t')

newFile = pd.read_csv('TabSH.txt', delimiter='\t')
updatedRows = pd.DataFrame(newFile).loc[unique_elements(indexes)]
print(updatedRows)