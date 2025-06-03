# Biomedical Data Analysis

This project contains a simple Python script to analyze and visualize biomedical data.

## Setup

Install dependencies:

```bash
pip install -r requirements.txt
```

## Usage

Run the analysis script:

```bash
python biomed/analyze.py
```

The script loads the UCI Heart Disease dataset from `biomed/data/heart_disease.csv`.
It prints summary statistics and saves a scatter plot showing patient cholesterol
versus age colored by the diagnosis value.
