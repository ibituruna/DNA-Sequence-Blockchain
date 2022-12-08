'''

'''
from FitDataSet import *
from storeDataJson import *
from Experiment import *

def main():

    fitData()
    data = storeData()

    print('Enter with an option: \n'
          '1 - Experiment I\n2 - Experiment II\n'
          '3 - Experiment III')
    option = int(input('Number: '))
    out = 0

    while(out != 1):
        if (option ==  1):
            ExperimentNumberOne(data)
        elif (option == 2):
            ExperimentNumberTwo(data)
        elif (option == 3):
            ExperimentNumberThree(data)
        else:
            print('Invalid Number')
        # asking for a new experiment 
        out = int(input('Press 1 to finish and 0 to continue: '))

if __name__ == '__main__':
    main()
