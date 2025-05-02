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

