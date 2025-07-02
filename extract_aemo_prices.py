import csv
import pandas as pd
from datetime import datetime

# Read the CSV file
data = []
with open('PUBLIC_PRICES_202506300000_20250701040507.CSV', 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        if row[0] == 'D' and row[1] == 'DREGION':
            # Extract relevant fields
            timestamp = row[4].strip('"')
            region = row[6]
            price = float(row[8])
            
            data.append({
                'SETTLEMENTDATE': timestamp,
                'REGIONID': region,
                'RRP': price
            })

# Convert to DataFrame
df = pd.DataFrame(data)
df['SETTLEMENTDATE'] = pd.to_datetime(df['SETTLEMENTDATE'])

# Sort by region and timestamp
df = df.sort_values(['REGIONID', 'SETTLEMENTDATE'])

# Save to CSV
df.to_csv('aemo_prices_clean.csv', index=False)

# Print summary
print(f"Total records: {len(df)}")
print(f"Date range: {df['SETTLEMENTDATE'].min()} to {df['SETTLEMENTDATE'].max()}")
print(f"Regions: {df['REGIONID'].unique()}")
print(f"\nPrice summary by region:")
print(df.groupby('REGIONID')['RRP'].describe())