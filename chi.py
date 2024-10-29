def main():
    n = int(input("Enter the number of categories: "))
    if n <= 0:
        print("Error: Number of categories must be positive!")
        return

    observed = [int(input(f"Observed frequency for category {i + 1}: ")) for i in range(n)]
    total_observed = sum(observed)
    expected = total_observed / n

    chi_square = sum((obs - expected) ** 2 / expected for obs in observed)
    
    print(f"\nExpected frequency for each category: {expected}")
    print(f"Chi-Square Statistic: {chi_square}")
    print(f"Degrees of Freedom: {n - 1}")

if __name__ == "__main__":
    main()