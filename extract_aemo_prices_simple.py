import csv
from datetime import datetime
import statistics

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

# Group by region
regions = {}
for record in data:
    region = record['REGIONID']
    if region not in regions:
        regions[region] = []
    regions[region].append(record)

# Sort data by timestamp for each region
for region in regions:
    regions[region].sort(key=lambda x: x['SETTLEMENTDATE'])

# Save to CSV
with open('aemo_prices_clean.csv', 'w', newline='') as file:
    writer = csv.DictWriter(file, fieldnames=['SETTLEMENTDATE', 'REGIONID', 'RRP'])
    writer.writeheader()
    
    for region in sorted(regions.keys()):
        for record in regions[region]:
            writer.writerow(record)

# Print summary
print(f"Total records: {len(data)}")
print(f"\nRecords by region:")
for region in sorted(regions.keys()):
    prices = [r['RRP'] for r in regions[region]]
    print(f"\n{region}:")
    print(f"  Count: {len(prices)}")
    print(f"  Min price: ${min(prices):.2f}")
    print(f"  Max price: ${max(prices):.2f}")
    print(f"  Mean price: ${statistics.mean(prices):.2f}")
    print(f"  Median price: ${statistics.median(prices):.2f}")
    if len(prices) > 1:
        print(f"  Std dev: ${statistics.stdev(prices):.2f}")
    
    # Count price spikes and negative prices
    spikes = sum(1 for p in prices if p > 300)
    negative = sum(1 for p in prices if p < 0)
    print(f"  Price spikes (>$300): {spikes}")
    print(f"  Negative prices: {negative}")

print("\nData saved to aemo_prices_clean.csv")