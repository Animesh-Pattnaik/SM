def multiplicative_congruential(seed, a, m):
    seed = (a * seed) % m
    return seed

def main():
    seed = int(input("Enter the seed value (a positive integer): "))
    a = int(input("Enter the multiplier (a): "))
    m = int(input("Enter the modulus (m): "))
    n = int(input("Enter the number of random numbers to generate: "))

    print("\nGenerated Random Numbers using Multiplicative Congruential Method:")
    for _ in range(n):
        seed = multiplicative_congruential(seed, a, m)
        print(seed)

if __name__ == "__main__":
    main()
