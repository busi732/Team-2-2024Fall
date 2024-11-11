from src.data_ingestion import *

# Test read_data function
for name in ['fault', 'scada', 'status', 'exception']:
    print(f'Reading {name} data...')
    df = read_data(name)
    if df is not None:
        print(f'Shape: {df.shape}')
    print()

# Test merge_data function
print('Merging data...')
df_merged = merge_data(export=False)
print(f'Shape: {df_merged.shape}')
