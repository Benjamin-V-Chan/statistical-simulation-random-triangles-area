# 1. Parse command-line arguments: input CSV path, output directory.
# 2. Read the CSV of areas.
# 3. Plot a histogram of “area”:
#      a. Choose an appropriate number of bins.
#      b. Label axes, title.
#      c. Draw a vertical line at the sample mean and theoretical mean.
#      d. Save as histogram.png.
# 4. Plot the empirical CDF of “area”:
#      a. Sort areas.
#      b. Plot sorted areas vs. (i+1)/n.
#      c. Label axes, title.
#      d. Save as cdf.png.