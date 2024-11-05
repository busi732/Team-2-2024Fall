from src.data_ingestion import *

print('Reading fault data...')
df_fault = read_fault()
print(df_fault.head())
print(df_fault.shape)
print()

print('Reading scada data...')
df_scada = read_scada()
print(df_scada.head())
print(df_scada.shape)
print()

print('Reading status data')
df_status = read_status()
print(df_status.head())
print(df_status.shape)