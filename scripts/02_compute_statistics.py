# 1. Parse command-line arguments: input CSV path, output JSON path.
# 2. Read the CSV of areas.
# 3. Compute descriptive statistics:
#      mean, median, variance, std, min, max,
#      5th/25th/75th/95th percentiles,
#      theoretical mean (1/6) for reference.
# 4. Assemble into a dict and write out as JSON.