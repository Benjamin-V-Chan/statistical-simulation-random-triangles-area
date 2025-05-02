import argparse, os, json
import pandas as pd
import matplotlib.pyplot as plt

def plot_histogram(areas, stats, outpath):
    plt.figure()
    plt.hist(areas, bins=50, edgecolor="black")
    plt.axvline(stats["mean"], linestyle="--", label=f"Sample mean={stats['mean']:.3f}")
    plt.axvline(stats["theoretical_mean"], color="red", linestyle=":", label="Theoretical mean=0.1667")
    plt.xlabel("Triangle area")
    plt.ylabel("Frequency")
    plt.title("Histogram of Random Triangle Areas")
    plt.legend()
    plt.tight_layout()
    plt.savefig(outpath)
    plt.close()

def plot_cdf(areas, outpath):
    sorted_areas = sorted(areas)
    cumprob = [i/len(sorted_areas) for i in range(1, len(sorted_areas)+1)]
    plt.figure()
    plt.step(sorted_areas, cumprob, where="post")
    plt.xlabel("Triangle area")
    plt.ylabel("Empirical CDF")
    plt.title("Empirical CDF of Random Triangle Areas")
    plt.tight_layout()
    plt.savefig(outpath)
    plt.close()

