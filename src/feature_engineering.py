import pandas as pd
import os

# Get the absolute path of the current script
script_dir = os.path.dirname(os.path.abspath(__file__))

# Change to the parent directory of the script's location
parent_dir = os.path.abspath(os.path.join(script_dir, ".."))
os.chdir(parent_dir)

print("Current working directory:", os.getcwd())

#Getting the 2014 Market Data
# Define global variables
RAW_PATH_MARKET_2014 = 'data/raw/ERCOT_Market_Data_2014.xlsx'

# Attempt to load the file with a try-except block
try:
    # Check if the file exists
    if os.path.exists(RAW_PATH_MARKET_2014):
        # Load the Excel file
        market_data_2014 = pd.ExcelFile(RAW_PATH_MARKET_2014)
        print("File loaded successfully.")
    else:
        raise FileNotFoundError(f"File not found: {RAW_PATH_MARKET_2014}")
except FileNotFoundError as fnf_error:
    print(fnf_error)
except Exception as e:
    print(f"An error occurred while reading the file: {e}")


#Getting the 2015 Market Data
# Define global variables
RAW_PATH_MARKET_2015 = 'data/raw/ERCOT_Market_Data_2015.xlsx'

# Attempt to load the file with a try-except block
try:
    # Check if the file exists
    if os.path.exists(RAW_PATH_MARKET_2015):
        # Load the Excel file
        market_data_2015 = pd.ExcelFile(RAW_PATH_MARKET_2015)
        print("File loaded successfully.")
    else:
        raise FileNotFoundError(f"File not found: {RAW_PATH_MARKET_2015}")
except FileNotFoundError as fnf_error:
    print(fnf_error)
except Exception as e:
    print(f"An error occurred while reading the file: {e}")

# Define global variables
RAW_SCADA_DATA = 'data/raw/scada.csv'

#Getting the SCADA DATA

# Attempt to load the file with a try-except block
try:
    # Check if the file exists
    if os.path.exists(RAW_SCADA_DATA):
        # Load the Excel file
        scada_data= pd.read_csv(RAW_SCADA_DATA)
        print("File loaded successfully.")
    else:
        raise FileNotFoundError(f"File not found: {RAW_SCADA_DATA}")
except FileNotFoundError as fnf_error:
    print(fnf_error)
except Exception as e:
    print(f"An error occurred while reading the file: {e}")

#Adding Change in Energy as Feature for Renveue
# Ensure the 'WEC: Production kWh' column exists
if 'WEC: Production kWh' in scada_data.columns:
    # Calculate the energy change while handling nulls
    scada_data['Energy Change'] = scada_data['WEC: Production kWh'].fillna(method='ffill').diff()

    # Retain nulls in the new column where the original column had nulls
    scada_data.loc[scada_data['WEC: Production kWh'].isnull(), 'Energy Change'] = None
else:
    logger.error("'WEC: Production kWh' column is missing from the dataset.")


# Enhanced processing function to handle single 'Settlement Point Price' column per 'DateTime'
def process_market_data_grouped(market_data):
    processed_sheets = []
    for sheet in market_data.sheet_names:
        try:
            df = market_data.parse(sheet)
            # Check for required columns
            if {'Delivery Date', 'Hour Ending', 'Settlement Point Price'}.issubset(df.columns):
                # Convert Delivery Date to datetime
                df['Delivery Date'] = pd.to_datetime(df['Delivery Date'], errors='coerce')
                # Parse Hour Ending and calculate hours
                df['Hour Ending'] = df['Hour Ending'].str.extract(r'(\d+)').astype(float) - 1
                # Create complete DateTime column
                df['DateTime'] = df['Delivery Date'] + pd.to_timedelta(df['Hour Ending'], unit='h')
                # Group by DateTime and average the settlement point prices
                grouped = df.groupby('DateTime')['Settlement Point Price'].mean().reset_index()
                processed_sheets.append(grouped)
            else:
                print(f"Missing required columns in sheet: {sheet}")
        except Exception as e:
            print(f"Error processing sheet {sheet}: {e}")
    return pd.concat(processed_sheets, ignore_index=True) if processed_sheets else pd.DataFrame()

# Reprocess ERCOT 2014 and 2015 market data with the updated function
market_2014_grouped = process_market_data_grouped(market_data_2014)
market_2015_grouped = process_market_data_grouped(market_data_2015)

# Combine the processed data for both years
market_combined_grouped = pd.concat([market_2014_grouped, market_2015_grouped])



# Adding Change in Energy as Feature for Renveue
# Ensure the 'Settlement Point Price' column exists
if 'Settlement Point Price' in market_combined_grouped.columns:
    # Ensure both datasets have DateTime as the index for merging
    market_combined_grouped.set_index('DateTime', inplace=True)
    scada_data['DateTime'] = pd.to_datetime(scada_data['DateTime'])
    scada_data['Datetime Hour'] = scada_data['DateTime'].dt.floor('H')  # Ensure SCADA DateTime is rounded to the hour
    scada_with_prices=pd.merge(scada_data, market_combined_grouped, left_on='Datetime Hour', right_index=True, how='inner')
else:
    logger.error("'Settlement Point Price' column is missing from the dataset.")



# Adding Feature Renveue suing 'Settlement Point Price' and 'Energy Change'
# Ensure the 'Settlement Point Price' column exists
if 'Settlement Point Price' in scada_with_prices.columns:
    # Calculate revenue
    scada_with_prices['Revenue'] = scada_with_prices['Energy Change'] * scada_with_prices['Settlement Point Price']
else:
    logger.error("'Settlement Point Price' column is missing from the dataset.")


# # Saving the Features Paths
# Define the output file path
PROCESSED_DATA_DIR = "data/processed"
os.makedirs(PROCESSED_DATA_DIR, exist_ok=True)  # Ensure the directory exists

# Define the full path for the output file
processed_file_path = os.path.join(PROCESSED_DATA_DIR, "scada_with_features.csv")

# Save the processed data
scada_with_prices.to_csv(processed_file_path, index=False)
print(f"Processed data saved to {processed_file_path}")

