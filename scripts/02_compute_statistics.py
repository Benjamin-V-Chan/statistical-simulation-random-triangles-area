#!/usr/bin/env python3
import argparse, os, json
import pandas as pd
import numpy as np

def compute_stats(areas):
    stats = {
        "count": int(len(areas)),
        "mean": float(np.mean(areas)),
        "median": float(np.median(areas)),
        "variance": float(np.var(areas, ddof=1)),
        "std_dev": float(np.std(areas, ddof=1)),
        "min": float(np.min(areas)),
        "max": float(np.max(areas)),
        "percentiles": {
            "5th": float(np.percentile(areas, 5)),
            "25th": float(np.percentile(areas, 25)),
            "75th": float(np.percentile(areas, 75)),
            "95th": float(np.percentile(areas, 95))
        },
        "theoretical_mean": float(1/6)
    }
    return stats

def main():
    p = argparse.ArgumentParser(description="Compute summary stats for triangle areas")
    p.add_argument("-i", "--input", default="../outputs/triangle_areas.csv", help="input CSV path")
    p.add_argument("-o", "--output", default="../outputs/summary_stats.json", help="output JSON path")
    args = p.parse_args()

    os.makedirs(os.path.dirname(args.output), exist_ok=True)
    df = pd.read_csv(args.input)
    stats = compute_stats(df["area"].values)
    with open(args.output, "w") as f:
        json.dump(stats, f, indent=4)

if __name__ == "__main__":
    main()
