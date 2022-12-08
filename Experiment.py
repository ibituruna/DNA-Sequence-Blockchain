
from bigchaindb_driver import BigchainDB
from bigchaindb_driver.crypto import generate_keypair
import datetime

''' EXPERIMENT 1 - SEDING 40 TRANSACTION '''
def ExperimentNumberOne(data):
    with open('experimento_1_1.txt', 'w') as arquivo:
        if (arquivo == None):
            print('Error: archive not loaded ... ')
            exit(-1)
        else:
            print(' #### START EXPERIMENT 1.1 #### ')
            print('storing data in archive ... ')
            data_start = datetime.datetime.now()
            arquivo.write('Begin in: ' + str(data_start) + '\n')

            IP_PORT = str(input('Enter with IP:PORT : '))
            bdb = BigchainDB(IP_PORT)
            #bdb = BigchainDB('10.102.22.142:9984')
            if (bdb == None):
                print('Error: not possible to reach this IP - PORT!')
                exit(-1)
            else:
                print('Start the process to send transactions ... ')
                for transaction in range(40):
                    key = generate_keypair()
                    tx = bdb.transactions.prepare(
                        operation = 'CREATE',
                        signers = key.public_key,
                        asset = {'data': {'message': str(data[transaction])}}
                    )
                    signed_tx = bdb.transactions.fulfill(
                        tx,
                        private_keys=key.private_key
                    )
                    bdb.transactions.send_sync(signed_tx)

            print('Finish the process')
            data_finish = datetime.datetime.now()
            arquivo.write('Finish in: ' + str(data_finish) + '\n')
            result_time = data_finish - data_start
            arquivo.write('Delta Time: ' + str(result_time) + '\n')
            # recording the data sending in the experiment
            arquivo.write(' Data seding to BigchainDB: ')
            for i in range(40):
                arquivo.write(str(data[i]))
            arquivo.write(' === Finish data === ')
            # closing archive
            arquivo.close()


''' EXPERIMENT 1 - SEDING 80 TRANSACTION '''
def ExperimentNumberTwo(data):
    with open('experimento_1_2.txt', 'w') as arquivo:
        if (arquivo == None):
            print('Error: archive not loaded ... ')
            exit(-1)
        else:
            print(' #### START EXPERIMENT 1.2 #### ')
            print('storing data in archive ... ')
            data_start = datetime.datetime.now()
            arquivo.write('Begin in: ' + str(data_start) + '\n')

            IP_PORT = str(input('Enter with IP:PORT : '))
            bdb = BigchainDB(IP_PORT)
            #bdb = BigchainDB('10.102.22.142:9984')
            if (bdb == None):
                print('Error: not possible to reach this IP - PORT!')
                exit(-1)
            else:
                print('Start the process to send transactions ... ')
                for transaction in range(80):
                    key = generate_keypair()
                    tx = bdb.transactions.prepare(
                        operation = 'CREATE',
                        signers = key.public_key,
                        asset = {'data': {'message': str(data[transaction])}}
                    )
                    signed_tx = bdb.transactions.fulfill(
                        tx,
                        private_keys=key.private_key
                    )
                    bdb.transactions.send_sync(signed_tx)

            print('Finish the process')
            data_finish = datetime.datetime.now()
            arquivo.write('Finish in: ' + str(data_finish) + '\n')
            result_time = data_finish - data_start
            arquivo.write('Delta Time: ' + str(result_time) + '\n')
            # recording the data sending in the experiment
            arquivo.write(' Data seding to BigchainDB: ')
            for i in range(80):
                arquivo.write(str(data[i]))
            arquivo.write(' === Finish data === ')
            # closing archive
            arquivo.close()


''' EXPERIMENT 1 - SEDING 105 TRANSACTION '''
def ExperimentNumberThree(data):
    with open('experimento_1_3.txt', 'w') as arquivo:
        if (arquivo == None):
            print('Error: archive not loaded ... ')
            exit(-1)
        else:
            print(' #### START EXPERIMENT 1.3 #### ')
            print('storing data in archive ... ')
            data_start = datetime.datetime.now()
            arquivo.write('Begin in: ' + str(data_start) + '\n')

            IP_PORT = str(input('Enter with IP:PORT : '))
            bdb = BigchainDB(IP_PORT)
            #bdb = BigchainDB('10.102.22.142:9984')
            if (bdb == None):
                print('Error: not possible to reach this IP - PORT!')
                exit(-1)
            else:
                print('Start the process to send transactions ... ')
                for transaction in range(105):
                    key = generate_keypair()
                    tx = bdb.transactions.prepare(
                        operation = 'CREATE',
                        signers = key.public_key,
                        asset = {'data': {'message': str(data[transaction])}}
                    )
                    signed_tx = bdb.transactions.fulfill(
                        tx,
                        private_keys=key.private_key
                    )
                    bdb.transactions.send_sync(signed_tx)

            print('Finish the process')
            data_finish = datetime.datetime.now()
            arquivo.write('Finish in: ' + str(data_finish) + '\n')
            result_time = data_finish - data_start
            arquivo.write('Delta Time: ' + str(result_time) + '\n')
            # recording the data sending in the experiment
            arquivo.write(' Data seding to BigchainDB: ')
            for i in range(105):
                arquivo.write(str(data[i]))
            arquivo.write(' === Finish data === ')
            # closing archive
            arquivo.close()
