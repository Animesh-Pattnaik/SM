import numpy as np
from scipy import stats

n = int(input("Enter the number of random numbers to generate: "))
distribution = input("Enter the distribution to test (e.g., 'uniform', 'norm'): ")


if distribution == 'uniform':
    random_numbers = np.random.uniform(0, 1, n)
elif distribution == 'norm':
    random_numbers = np.random.normal(0, 1, n)
else:
    print("Unsupported distribution")
    exit()

random_numbers.sort()
ecdf = np.arange(1, n+1) / n

if distribution == 'uniform':
    cdf = random_numbers  
elif distribution == 'norm':
    cdf = stats.norm.cdf(random_numbers)


d_max = np.max(ecdf - cdf)
d_min = np.max(cdf - ecdf)


ks_statistic = max(d_max, d_min)


print(f"D_max: {d_max}")
print(f"D_min: {d_min}")
print(f"KS Statistic (D): {ks_statistic}")


ks_statistic_scipy, p_value = stats.kstest(random_numbers, distribution)

print(f"KS Statistic from scipy: {ks_statistic_scipy}")
print(f"P-value: {p_value}")


alpha = 0.05  
if p_value > alpha:
    print(f"The sample follows a {distribution} distribution (fail to reject H0).")
else:
    print(f"The sample does not follow a {distribution} distribution (reject H0).")