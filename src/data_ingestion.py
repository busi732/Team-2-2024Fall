import pandas as pd
import logging

# create an instance of the logger
logger = logging.getLogger()

# Define global variables
RAW_PATH = 'data/raw/'
PROCESSED_PATH = 'data/processed/'

def read_data(name: str) -> pd.DataFrame:
    '''
    Load shared data from the configured location.

    Parameters:
        name: {'fault', 'scada', 'status'}
            Specify the name of the dataset to load.

    Returns
        data: DataFrame
            The data loaded from the shared data file.
    '''
    # Create a path
    path = f'{RAW_PATH}{name}.csv'
    
    # Load data
    try:
        return pd.read_csv(path)
    except FileNotFoundError:
        logger.error(f'No such file or directory: {path}')

def merge_data(export: bool=False) -> pd.DataFrame:
    '''
    Merge fault, scada, and status data.
    
    Parameters
        export: bool
            Specify whether you want to save the merged dataset as a csv file.

    Returns:
        merged_data: DataFrame
            The merged dataset.
    '''
    
    # Read and preprocess each dataset
    fault_data = read_data('fault')
    scada_data = read_data('scada')
    status_data = read_data('status')

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
        path = PROCESSED_PATH + 'merged.csv'
        merged_data.to_csv(path, index=False)
        
    return merged_data