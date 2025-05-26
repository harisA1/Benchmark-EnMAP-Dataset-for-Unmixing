# enmap-unmixing-benchmark

# Bare Soil Detection Benchmark from EnMAP Imagery

This repository provides a benchmark dataset for evaluating bare soil detection methods on EnMAP hyperspectral imagery. The dataset includes preprocessed spectral data and corresponding ground truth class labels derived from Sentinel-2 and land cover products.

📄 **Associated Paper**: _Spectral Unmixing for Bare Soil Detection: A Step Toward Hyperspectral Soil Organic Carbon Estimation_

📦 **Dataset Download**:  
[benchmark_dataset.npz (105 MB)](https://zenodo.org/record/XXXXXXX/files/benchmark_dataset.npz)  
*(Hosted on Zenodo — replace link with actual DOI)*

---

## 🔍 Dataset Description

The dataset consists of:

- `image`: Flat EnMAP hyperspectral image with shape `(N, B)`  
  where `N = height × width`, `B = 244 spectral bands` (covering 420–2450 nm)
- `ground_truth`: Flat array of class labels with shape `(N,)`  
  Ground truth is a categorical mask with the following classes:
  - `0`: Soil-dominant pixel  
  - `1`: Vegetation-dominant pixel  
  - `2`: Other (urban, forest, water, etc.)
- `height`, `width`: Original spatial dimensions of the EnMAP scene (e.g., 375 × 375)

The scene covers an agricultural region near **Lake Zazari in Western Macedonia, Greece**, and was acquired in **October 2023**.

---

## 📂 Folder Structure

