# statistical-simulation-random-triangles-area

## Project Overview

This project simulates the distribution of areas formed by triangles whose vertices are randomly sampled from a uniform distribution over the unit square $[0,1] \times [0,1]$. It conducts large-scale statistical experiments to explore the behavior and properties of random triangle areas.

### Mathematical Background

Given three random points $(x_1, y_1), (x_2, y_2), (x_3, y_3)$ independently sampled from the uniform distribution on $[0,1]^2$, the area $A$ of the triangle can be computed using the **Shoelace Formula**:

$$
A = \frac{1}{2} |x_1(y_2 - y_3) + x_2(y_3 - y_1) + x_3(y_1 - y_2)|
$$

This formula arises from the determinant of a matrix representing two vectors forming the sides of the triangle.

The expected value of the area can be derived using multivariate integration. Specifically, since the points are independent and identically distributed, the expected area $E[A]$ can be computed as:

$$
E[A] = \int_{0}^{1} \int_{0}^{1} \int_{0}^{1} \int_{0}^{1} \int_{0}^{1} \int_{0}^{1} \frac{1}{2} |x_1(y_2-y_3) + x_2(y_3-y_1) + x_3(y_1-y_2)| \, dx_1 \, dy_1 \, dx_2 \, dy_2 \, dx_3 \, dy_3
$$

Solving this yields:

$$
E[A] = \frac{1}{6}
$$

**Proof Sketch**:

* By symmetry and linearity of expectation, the computation simplifies considerably.
* The absolute value introduces complexity, but the positive and negative contributions symmetrically balance over the full domain.
* Utilizing properties of uniform random variables and independence, along with Fubini's Theorem, allows the decomposition into simpler expected value computations.
* Final integrations result in the clean fraction $1/6$.

Higher moments, such as variance and skewness, are much more difficult to compute exactly but can be approximated empirically via simulation.

Thus, this simulation seeks not only to verify $E[A] = 1/6$ empirically but also to explore the full distributional characteristics of random triangle areas.

---

## Folder Structure

```
project-root/
├── scripts/
│   ├── 01_generate_data.py
│   ├── 02_compute_statistics.py
│   └── 03_visualize_results.py
├── outputs/
│   ├── triangle_areas.csv
│   ├── summary_stats.json
│   ├── histogram.png
│   └── cdf.png
└── README.md
```

---

## Usage

### 1. Setup the Project:

Clone the repository.
Ensure you have Python installed.
Install required dependencies using the requirements.txt file.

```bash
pip install -r requirements.txt
```

### 2. Generate Random Triangle Data:

```bash
python3 scripts/01_generate_data.py -n 200000 --seed 42
```

* `-n`: Number of triangles to simulate (default 100000)
* `--seed`: Random seed for reproducibility (optional)
* `-o`: Output CSV path (optional)

### 3. Compute Summary Statistics:

```bash
python3 scripts/02_compute_statistics.py
```

* `-i`: Input CSV path (optional)
* `-o`: Output JSON path for summary statistics (optional)

### 4. Generate Visualizations:

```bash
python3 scripts/03_visualize_results.py
```

* `-i`: Input CSV path (optional)
* `-s`: Summary statistics JSON path (optional)
* `-o`: Output directory for images (optional)

All generated files (CSV, JSON, PNGs) will be saved into the `outputs/` folder.

---

## Requirements

* Python 3.8+
* numpy
* pandas
* matplotlib

Install all dependencies with:

```bash
pip install -r requirements.txt
```
