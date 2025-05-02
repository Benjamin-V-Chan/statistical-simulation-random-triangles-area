# 1. Parse command-line arguments: number of samples (n), random seed, output CSV path.
# 2. (Re)create outputs directory if needed.
# 3. For i in 1..n:
#      a. Sample three points (x1,y1), (x2,y2), (x3,y3) uniformly in [0,1]×[0,1].
#      b. Compute triangle area via the shoelace formula:
#           area = abs(x1(y2−y3) + x2(y3−y1) + x3(y1−y2)) / 2.
#      c. Record area.
# 4. Save all areas to a CSV with columns ["id","area"].