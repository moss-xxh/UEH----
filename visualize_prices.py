import csv
from datetime import datetime
import statistics

# Read the data
data = {}
with open('aemo_prices_final.csv', 'r') as file:
    reader = csv.DictReader(file)
    for row in reader:
        region = row['REGIONID']
        if region not in data:
            data[region] = {'times': [], 'prices': []}
        data[region]['times'].append(datetime.strptime(row['SETTLEMENTDATE'], '%Y/%m/%d %H:%M:%S'))
        data[region]['prices'].append(float(row['RRP']))

# Create a simple text-based visualization for one region (SA1 - most interesting due to negative prices)
region = 'SA1'
prices = data[region]['prices']
times = data[region]['times']

print(f"\nPrice Timeline for {region} - Text Visualization")
print("=" * 80)
print("Time slots shown every 30 minutes, price ranges:")
print("  [-] = Negative price")
print("  [L] = Low (<$100)")
print("  [N] = Normal ($100-200)")
print("  [H] = High ($200-300)")
print("  [S] = Spike (>$300)")
print("=" * 80)

# Group by 30-minute intervals for visualization
current_hour = None
line = ""
for i, (time, price) in enumerate(zip(times, prices)):
    if i % 6 == 0:  # Every 30 minutes
        if current_hour != time.hour:
            if line:
                print(line)
            current_hour = time.hour
            line = f"{time.strftime('%H:%M')} |"
        
        if price < 0:
            symbol = "[-]"
        elif price < 100:
            symbol = "[L]"
        elif price < 200:
            symbol = "[N]"
        elif price < 300:
            symbol = "[H]"
        else:
            symbol = "[S]"
        
        line += f" {symbol}"

if line:
    print(line)

# Show specific examples of volatility
print(f"\n\nExamples of Extreme Volatility in {region}:")
print("=" * 60)

# Find largest price jumps
jumps = []
for i in range(1, len(prices)):
    jump = prices[i] - prices[i-1]
    jumps.append((times[i], prices[i-1], prices[i], jump))

# Sort by absolute jump size
jumps.sort(key=lambda x: abs(x[3]), reverse=True)

print("\nTop 5 Largest Price Changes (5-minute intervals):")
for i, (time, prev_price, curr_price, jump) in enumerate(jumps[:5]):
    print(f"{i+1}. {time.strftime('%H:%M')} | ${prev_price:.2f} → ${curr_price:.2f} | Change: ${jump:+.2f}")

# Find negative price periods
negative_periods = []
in_negative = False
start_time = None

for i, (time, price) in enumerate(zip(times, prices)):
    if price < 0 and not in_negative:
        in_negative = True
        start_time = time
    elif price >= 0 and in_negative:
        in_negative = False
        negative_periods.append((start_time, times[i-1], i - times.index(start_time)))

if negative_periods:
    print(f"\nNegative Price Periods in {region}:")
    for start, end, duration in negative_periods:
        print(f"  {start.strftime('%H:%M')} to {end.strftime('%H:%M')} ({duration*5} minutes)")

# Show all regions summary at specific times
print("\n\nSnapshot Comparison - All Regions at Key Times:")
print("=" * 80)
print("Time      | NSW1    | QLD1    | SA1     | TAS1    | VIC1")
print("-" * 80)

# Select key times: early morning, morning peak, midday, afternoon, evening peak
key_times = ['2025/06/30 03:00:00', '2025/06/30 07:30:00', '2025/06/30 12:00:00', 
             '2025/06/30 14:30:00', '2025/06/30 17:30:00']

for time_str in key_times:
    target_time = datetime.strptime(time_str, '%Y/%m/%d %H:%M:%S')
    row = f"{target_time.strftime('%H:%M')}  |"
    
    for region in ['NSW1', 'QLD1', 'SA1', 'TAS1', 'VIC1']:
        # Find closest time match
        region_times = data[region]['times']
        region_prices = data[region]['prices']
        
        for i, t in enumerate(region_times):
            if t >= target_time:
                price = region_prices[i]
                row += f" ${price:7.2f} |"
                break
    
    print(row)

print("\n" + "=" * 80)