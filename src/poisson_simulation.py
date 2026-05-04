import numpy as np
import matplotlib.pyplot as plt
import time

# =========================
# PARAMETERS
# =========================
lam = 4
n = 1000


# =========================
# METHOD 1: NumPy (baseline)
# =========================
def poisson_numpy(lam, n):
    return np.random.poisson(lam, n)


# =========================
# METHOD 2: Exponential method
# =========================
def poisson_exponential(lam, n):
    samples = []

    for _ in range(n):
        t = 0
        count = 0

        while True:
            t += np.random.exponential(1 / lam)

            if t > 1:
                break

            count += 1

        samples.append(count)

    return np.array(samples)


# =========================
# METHOD 3: Inversion method
# =========================
def poisson_inversion(lam, n):
    samples = []

    for _ in range(n):
        u = np.random.uniform(0, 1)

        f = np.exp(-lam)
        F = f
        k = 1

        while F < u:
            f = (lam / k) * f
            F += f
            k += 1

        samples.append(k - 1)

    return np.array(samples)


# =========================
# METHOD 4: Fast approximation
# =========================
def poisson_fast(lam, n):
    samples = []

    for _ in range(n):
        u = np.random.uniform(0, 1)

        # Normal approximation
        z = np.random.normal(0, 1)
        k_guess = int(lam + np.sqrt(lam) * z)

        k = max(0, k_guess)

        # Refinement (inversion idea)
        f = np.exp(-lam)
        F = f
        i = 1

        while F < u:
            f = (lam / i) * f
            F += f
            i += 1

        samples.append(i - 1)

    return np.array(samples)


# =========================
# GENERATE DATA
# =========================
data_numpy = poisson_numpy(lam, n)
data_exp = poisson_exponential(lam, n)
data_inv = poisson_inversion(lam, n)
data_fast = poisson_fast(lam, n)


# =========================
# PRINT RESULTS
# =========================
print("=== MEANS ===")
print("NumPy:", np.mean(data_numpy))
print("Exponential:", np.mean(data_exp))
print("Inversion:", np.mean(data_inv))
print("Fast:", np.mean(data_fast))

print("\n=== VARIANCES ===")
print("NumPy:", np.var(data_numpy))
print("Exponential:", np.var(data_exp))
print("Inversion:", np.var(data_inv))
print("Fast:", np.var(data_fast))


# =========================
# PLOT (clean version)
# =========================
bins = np.arange(0, 15)

plt.hist(data_numpy, bins=bins, histtype='step', linewidth=2, label="NumPy")
plt.hist(data_exp, bins=bins, histtype='step', linewidth=2, label="Exponential")
plt.hist(data_inv, bins=bins, histtype='step', linewidth=2, label="Inversion")
plt.hist(data_fast, bins=bins, histtype='step', linewidth=2, label="Fast Approx")

plt.title("Poisson Simulation Methods Comparison (λ = 4)")
plt.xlabel("Values")
plt.ylabel("Frequency")
plt.legend()
plt.savefig("results/figures/poisson_comparison.png")
plt.show()


# =========================
# PERFORMANCE TEST
# =========================
print("\n=== PERFORMANCE ===")

lam_values = [2, 5, 10, 20]

for lam_test in lam_values:

    start = time.time()
    poisson_inversion(lam_test, 500)
    t_inv = time.time() - start

    start = time.time()
    poisson_exponential(lam_test, 500)
    t_exp = time.time() - start

    start = time.time()
    poisson_fast(lam_test, 500)
    t_fast = time.time() - start

    start = time.time()
    poisson_numpy(lam_test, 500)
    t_np = time.time() - start

    print(f"λ={lam_test} | Inversion={t_inv:.4f}s | Exponential={t_exp:.4f}s | Fast={t_fast:.4f}s | NumPy={t_np:.4f}s")