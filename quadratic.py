def quadratic_congruential(seed, a, b, m):
    """Generates the next random number using the quadratic congruential method."""
    return (a * seed * seed + b) % m

def main():
    seed = int(input("Enter the seed value (a positive integer): "))
    a = int(input("Enter the coefficients (a): "))
    b = int(input("Enter the coefficient (b): "))
    m = int(input("Enter the modulus (m): "))
    n = int(input("Enter the number of random numbers to generate: "))

    print("\nGenerated Random Numbers using Quadratic Congruential Method:")
    for _ in range(n):
        seed = quadratic_congruential(seed, a, b, m)  # Generate the next random number
        print(seed)

if __name__ == "__main__":
    main()