# Poisson Simulation

Simulation and analysis of the Poisson distribution using multiple methods in Python.

## Objective

This project simulates random samples from a Poisson distribution using four different methods and compares their empirical distributions, sample moments, and computational performance.

## Methods Used

- NumPy built-in Poisson generator
- Exponential inter-arrival method
- Inversion method
- Fast approximation method

## Data

This project uses simulated data generated from a Poisson distribution. No external datasets are required.

## Validation

The simulation results were validated by comparing:
- Sample means to the theoretical value λ
- Sample variances to the theoretical value λ
- Histogram overlap across methods

All methods produced results consistent with the theoretical Poisson distribution.

## Files

- `src/poisson_simulation.py` — main simulation script
- `results/figures/` — saved plots and figures

## How to Run
Run in the terminal: 
py src/poisson_simulation.py

Install the required packages:

```bash
pip install -r requirements.txt


