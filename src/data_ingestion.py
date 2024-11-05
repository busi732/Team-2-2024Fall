import pandas as pd

DATA_PATH = 'data/raw/'

# Read fault data
def read_fault():
    '''Function to process the fault data'''
    path = DATA_PATH + 'fault_data.csv'
    data = pd.read_csv(path)
    data['DateTime'] = pd.to_datetime(data['DateTime'])
    # print(data)
    return data

# Read scada data
def read_scada():
    '''Function to process the scada data'''
    path = DATA_PATH + 'scada_data.csv'
    data = pd.read_csv(path)
    data['DateTime'] = pd.to_datetime(data['DateTime'])
    return data

# Read status data
def read_status():
    '''Function to process the status data'''
    path = DATA_PATH + 'status_data.csv'
    data = pd.read_csv(path)
    data['Time'] = pd.to_datetime(data['Time'])
    return data