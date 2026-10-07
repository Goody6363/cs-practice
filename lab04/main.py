import sys 
from stats import average_by_city, read_valid, warmest_city

lines = sys.stdin.read().splitlines()

records = read_valid(lines)

averages = average_by_city(records)
city = warmest_city(records)

print(len(records))
print(len(lines) - len(records))
print(f"{averages[city]: 1}")