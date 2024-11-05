from src.data_ingestion import *
from dataprep.eda import create_report

# Load the data
df_merged = merge_data()

# Generate a profile report
fault_report = create_report(df_merged)

# Save the report
EDA_PATH = 'data/eda_report/'
fault_report.save(EDA_PATH + 'report.html')