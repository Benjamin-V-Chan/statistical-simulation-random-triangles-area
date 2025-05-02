import argparse, os
import numpy as np
import pandas as pd

def shoelace_area(pts):
    x1, y1 = pts[0]
    x2, y2 = pts[1]
    x3, y3 = pts[2]
    return abs(x1*(y2-y3) + x2*(y3-y1) + x3*(y1-y2)) * 0.5

def generate_areas(n_samples, seed=None):
    if seed is not None:
        np.random.seed(seed)
    areas = []
    for i in range(n_samples):
        pts = np.random.rand(3, 2)
        areas.append(shoelace_area(pts))
    return areas

def main():
    p = argparse.ArgumentParser(description="Generate random triangle areas")
    p.add_argument("-n", "--n_samples", type=int, default=100000, help="number of triangles")
    p.add_argument("--seed", type=int, default=None, help="random seed")
    p.add_argument("-o", "--output", default="../outputs/triangle_areas.csv", help="output CSV path")
    args = p.parse_args()

    outdir = os.path.dirname(os.path.abspath(args.output))
    os.makedirs(outdir, exist_ok=True)

    areas = generate_areas(args.n_samples, args.seed)
    df = pd.DataFrame({"id": range(1, len(areas)+1), "area": areas})
    df.to_csv(args.output, index=False)

if __name__ == "__main__":
    main()
