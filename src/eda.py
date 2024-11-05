from src.data_ingestion import *
from dataprep.eda import create_report

# Load the data
df_fault = read_fault()
df_scada = read_scada()
df_status = read_status()

# Generate a profile report
fault_report = create_report(df_fault)
scada_report = create_report(df_scada)
status_report = create_report(df_status)

# Save the report
EDA_PATH = 'data/eda_reports/'
fault_report.save(EDA_PATH + 'fault_report.html')
status_report.save(EDA_PATH + 'scada_report.html') 
status_report.save(EDA_PATH + 'status_report.html') 