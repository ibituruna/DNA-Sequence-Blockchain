from LoadDataSet import *


def fitData():
    datasetOpening()
    arquivoDNA = open('dnaDATA.txt', 'r')
    for row in arquivoDNA:
       print(row)
    print('Number of elements: ' + str(len(row)))

    arquivoDNA.close()
