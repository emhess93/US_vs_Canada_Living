import pandas as pd

# Load CSV files
livingcosts_df = pd.read_csv("data/cost-of-living.csv")
headers_df = pd.read_csv("data/Cost_of_Living_Columns.csv",sep='\t')
headers_df.columns = headers_df.columns.str.strip().str.lower()

# Create dictionary to map the headers to the main data file
key_to_header = dict(zip(headers_df['column'], headers_df['description']))

# Replace the headers in the main data file with descriptions from the mapping
livingcosts_df.columns = [key_to_header.get(col, col) for col in livingcosts_df.columns]

# Filter the dataframe to only show US & Canada data
livingcosts_df = livingcosts_df[
    (livingcosts_df["Name of the country"] == "United States") |
    (livingcosts_df["Name of the country"] == "Canada")
    ]

# Save the updated DataFrame to new CSV file
livingcosts_df.to_csv('updated_living_costs', index=False)

print(livingcosts_df)