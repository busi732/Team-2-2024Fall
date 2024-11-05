import pandas as pd

RAW_PATH = 'data/raw/'
PROCESSED_PATH = 'data/processed/'

# Read fault data
def read_fault():
    '''Function to process the fault data'''
    path = RAW_PATH + 'fault_data.csv'
    data = pd.read_csv(path)
    return data

# Read scada data
def read_scada():
    '''Function to process the scada data'''
    path = RAW_PATH + 'scada_data.csv'
    data = pd.read_csv(path)
    return data

# Read status data
def read_status():
    '''Function to process the status data'''
    path = RAW_PATH + 'status_data.csv'
    data = pd.read_csv(path)
    return data

def merge_data(export=True):
    '''Function to merge fault, scada, and status data on DateTime with a Full Outer Join.'''
    
    # Read and preprocess each dataset
    fault_data = read_fault()
    scada_data = read_scada()
    status_data = read_status()

    # Ensure all DateTime columns are in pd.datetime format
    fault_data['DateTime'] = pd.to_datetime(fault_data['DateTime'])
    scada_data['DateTime'] = pd.to_datetime(scada_data['DateTime'])
    status_data['Time'] = pd.to_datetime(status_data['Time'])
    
    # Rename the Time column in each dataset for clarity
    fault_data.rename(columns={'Time': 'Time_fault'}, inplace=True)
    scada_data.rename(columns={'Time': 'Time_scada'}, inplace=True)
    status_data.rename(columns={'Time': 'DateTime'}, inplace=True)
    
    # Merge fault_data and scada_data on DateTime with a Full Outer Join
    merged_data = pd.merge(fault_data, scada_data, on='DateTime', how='outer')
    
    # Merge the result with status_data on DateTime with a Full Outer Join
    merged_data = pd.merge(merged_data, status_data, on='DateTime', how='outer')

    # Save the merged data to a CSV file
    if export:
        path = PROCESSED_PATH + 'merged_data.csv'
        merged_data.to_csv(path, index=False)
        
    return merged_data