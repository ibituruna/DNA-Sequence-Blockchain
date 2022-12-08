'''
ARQUIVO PARA ARMAZENAR OS

'''

import json
from LoadDataSet import *

def storeData():

    dataDna = []
    numberPair = 0

    datasetOpening()
    data = open('dnaDATA.txt', 'r')

    for element in data:
        if(element != '\n'):
            dataTem = {
                'pair': element,
                'numberPair': numberPair,
            }
            dataDna.append(dataTem)
            numberPair = numberPair + 1

    print('\nBegin DNA sequence in vector')
    print(dataDna, '\n')

    data.close()

    return dataDna
