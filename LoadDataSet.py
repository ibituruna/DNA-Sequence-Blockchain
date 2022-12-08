'''
CODIGO PARA CARREGAR O ARQUIVO DE DNA.
ARQUIVO ORIGINAL: https://archive.ics.uci.edu/ml/datasets/Molecular+Biology+(Promoter+Gene+Sequences)
'''

import csv

def datasetOpening():
    with open('DNAsequenceDATASET.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter = ';')
        cabecalho = True
        arquivo = open('dnaDATA.txt','w')
        for row in csv_reader:
            if cabecalho:
                print(f'Heads: {", ".join(row)}')
                cabecalho = False
            else:
               arquivo.write(row[2].strip() + '\n')
        arquivo.close()
