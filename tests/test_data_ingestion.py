from src.data_ingestion import *

print('Reading fault data...')
df_fault = read_fault()
print(df_fault.head())
print(f'Fault data shape: {df_fault.shape}')
print()

print('Reading scada data...')
df_scada = read_scada()
print(df_scada.head())
print(f'Scada data shape: {df_scada.shape}')
print()

print('Reading status data')
df_status = read_status()
print(df_status.head())
print(f'Status data shape: {df_status.shape}')
print()

print('Creating merged data')
df_merged = merge_data(export=False)
print(df_merged.head())
print(f'Merged data shape: {df_merged.shape}')
