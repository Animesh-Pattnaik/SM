import numpy as np

def calculate_d_statistic(sample):
    n = len(sample)
    sorted_sample = np.sort(sample)
    
    D = 0.0
    for i in range(n):
        F_obs = (i + 1) / n
        F_exp = sorted_sample[i]
        D = max(D, abs(F_obs - F_exp))
    
    return D

if __name__ == "__main__":
    n = int(input("Enter the number of sample values: "))
    
    sample = []
    print("Enter sample values (between 0 and 1):")
    for _ in range(n):
        value = float(input())
        sample.append(value)

    alpha = float(input("Enter significance level (e.g., 0.05 for 5%): "))
    critical_value = float(input("Enter the critical value for the K-S test: "))

    D_statistic = calculate_d_statistic(sample)

    print(f"D-statistic: {D_statistic}")
    print(f"Critical value: {critical_value}")

    if D_statistic < critical_value:
        print("The null hypothesis is accepted. The sample follows the uniform distribution.")
    else:
        print("The null hypothesis is rejected. The sample does not follow the uniform distribution.")