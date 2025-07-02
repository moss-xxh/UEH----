import csv
from datetime import datetime

# Read the data
data = []
with open('aemo_prices_clean.csv', 'r') as file:
    reader = csv.DictReader(file)
    for row in reader:
        row['timestamp'] = datetime.strptime(row['SETTLEMENTDATE'], '%Y/%m/%d %H:%M:%S')
        data.append(row)

# Get unique timestamps and regions
timestamps = sorted(list(set(r['timestamp'] for r in data)))
regions = sorted(list(set(r['REGIONID'] for r in data)))

print(f"Data Coverage Analysis")
print(f"=" * 60)
print(f"Date range: {timestamps[0]} to {timestamps[-1]}")
print(f"Total unique timestamps: {len(timestamps)}")
print(f"Regions: {', '.join(regions)}")

# Calculate time span
time_span = timestamps[-1] - timestamps[0]
print(f"Time span: {time_span.total_seconds() / 3600:.1f} hours")

# Check interval consistency
intervals = []
for i in range(1, len(timestamps)):
    interval = (timestamps[i] - timestamps[i-1]).total_seconds() / 60
    intervals.append(interval)

unique_intervals = sorted(list(set(intervals)))
print(f"\nInterval analysis:")
print(f"Unique intervals found: {unique_intervals} minutes")

# Check for gaps
if max(intervals) > 5:
    print(f"\nGaps detected (intervals > 5 minutes):")
    for i in range(1, len(timestamps)):
        interval = (timestamps[i] - timestamps[i-1]).total_seconds() / 60
        if interval > 5:
            print(f"  {timestamps[i-1]} to {timestamps[i]} ({interval:.0f} minutes)")

# Count records per region per hour
hourly_counts = {}
for record in data:
    hour = record['timestamp'].replace(minute=0, second=0, microsecond=0)
    region = record['REGIONID']
    key = (hour, region)
    if key not in hourly_counts:
        hourly_counts[key] = 0
    hourly_counts[key] += 1

print(f"\nRecords per hour by region (expected 12 for 5-minute intervals):")
hours = sorted(list(set(h for h, r in hourly_counts.keys())))
for hour in hours[:5]:  # Show first 5 hours
    print(f"\n{hour}:")
    for region in regions:
        count = hourly_counts.get((hour, region), 0)
        print(f"  {region}: {count} records")