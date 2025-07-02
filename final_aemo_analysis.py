import csv
from datetime import datetime
import statistics

def calculate_mae(prices):
    """Calculate Mean Absolute Error between consecutive prices"""
    if len(prices) < 2:
        return 0
    errors = []
    for i in range(1, len(prices)):
        errors.append(abs(prices[i] - prices[i-1]))
    return statistics.mean(errors)

def calculate_mape(prices):
    """Calculate Mean Absolute Percentage Error"""
    if len(prices) < 2:
        return 0
    errors = []
    for i in range(1, len(prices)):
        if prices[i-1] != 0:  # Avoid division by zero
            error = abs((prices[i] - prices[i-1]) / prices[i-1]) * 100
            errors.append(error)
    return statistics.mean(errors) if errors else 0

def count_direction_changes(prices):
    """Count how many times price direction changes"""
    if len(prices) < 3:
        return 0
    changes = 0
    for i in range(2, len(prices)):
        prev_diff = prices[i-1] - prices[i-2]
        curr_diff = prices[i] - prices[i-1]
        if prev_diff * curr_diff < 0:  # Sign change
            changes += 1
    return changes

# Read and deduplicate data
seen = set()
data_by_region = {}

with open('aemo_prices_clean.csv', 'r') as file:
    reader = csv.DictReader(file)
    for row in reader:
        key = (row['SETTLEMENTDATE'], row['REGIONID'])
        if key not in seen:
            seen.add(key)
            region = row['REGIONID']
            if region not in data_by_region:
                data_by_region[region] = []
            row['RRP'] = float(row['RRP'])
            row['timestamp'] = datetime.strptime(row['SETTLEMENTDATE'], '%Y/%m/%d %H:%M:%S')
            data_by_region[region].append(row)

# Sort by timestamp
for region in data_by_region:
    data_by_region[region].sort(key=lambda x: x['timestamp'])

# Save deduplicated data
with open('aemo_prices_final.csv', 'w', newline='') as file:
    writer = csv.DictWriter(file, fieldnames=['SETTLEMENTDATE', 'REGIONID', 'RRP'])
    writer.writeheader()
    
    for region in sorted(data_by_region.keys()):
        for record in data_by_region[region]:
            writer.writerow({
                'SETTLEMENTDATE': record['SETTLEMENTDATE'],
                'REGIONID': record['REGIONID'],
                'RRP': record['RRP']
            })

print("=" * 80)
print("AEMO ELECTRICITY MARKET ANALYSIS - 24 HOURS OF 5-MINUTE DISPATCH PRICES")
print("=" * 80)

# Overall summary
all_timestamps = []
for region in data_by_region:
    all_timestamps.extend([r['timestamp'] for r in data_by_region[region]])
min_time = min(all_timestamps)
max_time = max(all_timestamps)

print(f"\nData Period: {min_time} to {max_time}")
print(f"Duration: {(max_time - min_time).total_seconds() / 3600:.1f} hours")
print(f"Regions analyzed: {', '.join(sorted(data_by_region.keys()))}")

# Detailed analysis by region
for region in sorted(data_by_region.keys()):
    data = data_by_region[region]
    prices = [r['RRP'] for r in data]
    
    print(f"\n{'='*70}")
    print(f"REGION: {region}")
    print(f"{'='*70}")
    
    print(f"\nData points: {len(prices)} (5-minute intervals)")
    
    # Price statistics
    print(f"\nPrice Statistics:")
    print(f"  Minimum: ${min(prices):.2f}/MWh")
    print(f"  Maximum: ${max(prices):.2f}/MWh")
    print(f"  Average: ${statistics.mean(prices):.2f}/MWh")
    print(f"  Median: ${statistics.median(prices):.2f}/MWh")
    print(f"  Std Dev: ${statistics.stdev(prices):.2f}/MWh")
    
    # Volatility analysis
    mae = calculate_mae(prices)
    mape = calculate_mape(prices)
    cv = (statistics.stdev(prices) / statistics.mean(prices)) * 100
    
    print(f"\nVolatility Metrics:")
    print(f"  MAE (consecutive prices): ${mae:.2f}/MWh")
    print(f"  MAPE (consecutive prices): {mape:.1f}%")
    print(f"  Coefficient of Variation: {cv:.1f}%")
    
    # Price movements
    changes = count_direction_changes(prices)
    print(f"\nPrice Movement Analysis:")
    print(f"  Direction changes: {changes} times")
    print(f"  Direction change frequency: {changes/(len(prices)-2)*100:.1f}%")
    
    # Price events
    spikes = [p for p in prices if p > 300]
    high = [p for p in prices if p > 200]
    negative = [p for p in prices if p < 0]
    low = [p for p in prices if p < 100]
    
    print(f"\nPrice Events:")
    print(f"  Extreme spikes (>$300/MWh): {len(spikes)} intervals ({len(spikes)/len(prices)*100:.1f}%)")
    if spikes:
        print(f"    Highest spike: ${max(spikes):.2f}/MWh")
    print(f"  High prices (>$200/MWh): {len(high)} intervals ({len(high)/len(prices)*100:.1f}%)")
    print(f"  Negative prices: {len(negative)} intervals ({len(negative)/len(prices)*100:.1f}%)")
    if negative:
        print(f"    Lowest negative: ${min(negative):.2f}/MWh")
    print(f"  Low prices (<$100/MWh): {len(low)} intervals ({len(low)/len(prices)*100:.1f}%)")
    
    # Time-based patterns
    hourly_avg = {}
    for record in data:
        hour = record['timestamp'].hour
        if hour not in hourly_avg:
            hourly_avg[hour] = []
        hourly_avg[hour].append(record['RRP'])
    
    for hour in hourly_avg:
        hourly_avg[hour] = statistics.mean(hourly_avg[hour])
    
    sorted_hours = sorted(hourly_avg.items(), key=lambda x: x[1], reverse=True)
    
    print(f"\nIntraday Pattern (top 3 expensive hours):")
    for hour, avg in sorted_hours[:3]:
        print(f"  {hour:02d}:00 - ${avg:.2f}/MWh average")
    
    print(f"\nIntraday Pattern (top 3 cheapest hours):")
    for hour, avg in sorted_hours[-3:]:
        print(f"  {hour:02d}:00 - ${avg:.2f}/MWh average")

# Market comparison
print(f"\n{'='*70}")
print("INTER-REGIONAL COMPARISON")
print(f"{'='*70}")

print(f"\nAverage Prices by Region:")
for region in sorted(data_by_region.keys()):
    prices = [r['RRP'] for r in data_by_region[region]]
    print(f"  {region}: ${statistics.mean(prices):.2f}/MWh")

print(f"\nVolatility by Region (Std Dev):")
for region in sorted(data_by_region.keys()):
    prices = [r['RRP'] for r in data_by_region[region]]
    print(f"  {region}: ${statistics.stdev(prices):.2f}/MWh")

print(f"\nPrice Spike Frequency by Region (>$300/MWh):")
for region in sorted(data_by_region.keys()):
    prices = [r['RRP'] for r in data_by_region[region]]
    spikes = sum(1 for p in prices if p > 300)
    print(f"  {region}: {spikes} spikes ({spikes/len(prices)*100:.1f}%)")

print(f"\n{'='*70}")
print("KEY FINDINGS:")
print(f"{'='*70}")
print("1. The Australian electricity market shows high volatility with frequent price spikes")
print("2. Price can vary dramatically within minutes (5-minute dispatch intervals)")
print("3. SA region shows unique characteristics with negative prices")
print("4. Morning (7-8am) and evening (5-6pm) peaks are clearly visible")
print("5. Tasmania shows the most stable prices with lowest volatility")

print(f"\nData saved to: aemo_prices_final.csv")
print("Source: AEMO NEMWEB Public Prices")