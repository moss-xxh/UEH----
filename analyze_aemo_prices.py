import csv
from datetime import datetime
import statistics
import math

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
        if prev_diff * curr_diff < 0:  # Sign change indicates direction change
            changes += 1
    return changes

def identify_peak_offpeak(data):
    """Identify peak and off-peak patterns"""
    hourly_prices = {}
    for record in data:
        dt = datetime.strptime(record['SETTLEMENTDATE'], '%Y/%m/%d %H:%M:%S')
        hour = dt.hour
        if hour not in hourly_prices:
            hourly_prices[hour] = []
        hourly_prices[hour].append(record['RRP'])
    
    # Calculate average price by hour
    hourly_avg = {}
    for hour, prices in hourly_prices.items():
        hourly_avg[hour] = statistics.mean(prices)
    
    return hourly_avg

# Read the cleaned data
data_by_region = {}
with open('aemo_prices_clean.csv', 'r') as file:
    reader = csv.DictReader(file)
    for row in reader:
        region = row['REGIONID']
        if region not in data_by_region:
            data_by_region[region] = []
        row['RRP'] = float(row['RRP'])
        data_by_region[region].append(row)

# Analyze each region
print("=" * 80)
print("COMPREHENSIVE AEMO ELECTRICITY PRICE ANALYSIS")
print("=" * 80)

for region in sorted(data_by_region.keys()):
    data = data_by_region[region]
    prices = [r['RRP'] for r in data]
    
    print(f"\n{'='*60}")
    print(f"REGION: {region}")
    print(f"{'='*60}")
    
    # Basic statistics
    print(f"\nBasic Statistics:")
    print(f"  Total intervals: {len(prices)}")
    print(f"  Min price: ${min(prices):.2f}/MWh")
    print(f"  Max price: ${max(prices):.2f}/MWh")
    print(f"  Mean price: ${statistics.mean(prices):.2f}/MWh")
    print(f"  Median price: ${statistics.median(prices):.2f}/MWh")
    
    # Volatility measures
    print(f"\nVolatility Measures:")
    print(f"  Standard deviation: ${statistics.stdev(prices):.2f}")
    print(f"  Coefficient of variation: {(statistics.stdev(prices) / statistics.mean(prices)) * 100:.1f}%")
    print(f"  Price range: ${max(prices) - min(prices):.2f}")
    
    # Error metrics
    mae = calculate_mae(prices)
    mape = calculate_mape(prices)
    print(f"\nError Metrics (consecutive price changes):")
    print(f"  MAE (Mean Absolute Error): ${mae:.2f}/MWh")
    print(f"  MAPE (Mean Absolute Percentage Error): {mape:.1f}%")
    
    # Price events
    spikes = sum(1 for p in prices if p > 300)
    high_prices = sum(1 for p in prices if p > 200)
    negative = sum(1 for p in prices if p < 0)
    low_prices = sum(1 for p in prices if p < 100)
    
    print(f"\nPrice Events:")
    print(f"  Price spikes (>$300/MWh): {spikes} ({spikes/len(prices)*100:.1f}%)")
    print(f"  High prices (>$200/MWh): {high_prices} ({high_prices/len(prices)*100:.1f}%)")
    print(f"  Negative prices (<$0/MWh): {negative} ({negative/len(prices)*100:.1f}%)")
    print(f"  Low prices (<$100/MWh): {low_prices} ({low_prices/len(prices)*100:.1f}%)")
    
    # Direction changes
    changes = count_direction_changes(prices)
    print(f"\nPrice Movement:")
    print(f"  Direction changes: {changes} ({changes/(len(prices)-2)*100:.1f}% of intervals)")
    
    # Peak/off-peak analysis
    hourly_avg = identify_peak_offpeak(data)
    sorted_hours = sorted(hourly_avg.items(), key=lambda x: x[1], reverse=True)
    
    print(f"\nPeak/Off-Peak Analysis (average price by hour):")
    print(f"  Top 3 peak hours:")
    for hour, avg_price in sorted_hours[:3]:
        print(f"    Hour {hour:02d}:00 - ${avg_price:.2f}/MWh")
    print(f"  Bottom 3 off-peak hours:")
    for hour, avg_price in sorted_hours[-3:]:
        print(f"    Hour {hour:02d}:00 - ${avg_price:.2f}/MWh")
    
    # Price distribution
    print(f"\nPrice Distribution Percentiles:")
    percentiles = [10, 25, 50, 75, 90, 95, 99]
    for p in percentiles:
        value = sorted(prices)[int(len(prices) * p / 100)]
        print(f"  {p}th percentile: ${value:.2f}/MWh")

# Overall market summary
print(f"\n{'='*80}")
print("OVERALL MARKET SUMMARY")
print(f"{'='*80}")

all_prices = []
for region in data_by_region:
    all_prices.extend([r['RRP'] for r in data_by_region[region]])

print(f"\nAcross all regions:")
print(f"  Total data points: {len(all_prices)}")
print(f"  Market-wide average: ${statistics.mean(all_prices):.2f}/MWh")
print(f"  Market-wide volatility (std dev): ${statistics.stdev(all_prices):.2f}")
print(f"  Overall price spikes (>$300): {sum(1 for p in all_prices if p > 300)}")
print(f"  Overall negative prices: {sum(1 for p in all_prices if p < 0)}")

print("\nData source: AEMO NEMWEB Public Prices")
print("Analysis complete. Results saved to aemo_prices_clean.csv")