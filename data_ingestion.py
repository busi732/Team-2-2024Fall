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
        data = pd.read_csv(path)
        
        # Ensure DateTime columns are in pd.datetime format
        if name == 'status':
            data['Time'] = pd.to_datetime(data['Time'])
            data.rename(columns={'Time': 'DateTime'}, inplace=True)
        else:
            data['DateTime'] = pd.to_datetime(data['DateTime'])
            
        return data
    except FileNotFoundError:
        logger.error(f'No such file or directory: {path}')

def merge_fault_scada(export: bool=False) -> pd.DataFrame:
    '''
    Merge fault and scada data.
    
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
    
    # Merge fault_data and scada_data on DateTime with a Full Outer Join
    merged_data = pd.merge(fault_data, scada_data, on=['DateTime', 'Time'], how='outer', suffixes=('_fault', '_scada'))

    # Save the merged data to a CSV file
    if export:
        path = f'{PROCESSED_PATH}merged.csv'
        merged_data.to_csv(path, index=False)
        
    return merged_data