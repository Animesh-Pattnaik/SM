def linear_congruential_generator(seed, a, c, m):
    seed = (a * seed + c) % m
    return seed

def main():
    seed = int(input("Enter the seed value (a positive integer): "))
    a = int(input("Enter the multiplier (a): "))
    c = int(input("Enter the increment (c): "))
    m = int(input("Enter the modulus (m): "))
    n = int(input("Enter the number of random numbers to generate: "))

    print("\nGenerated Random Numbers using Linear Congruential Method:")
    for _ in range(n):
        seed = linear_congruential_generator(seed, a, c, m)
        print(seed)

if __name__ == "__main__":
    main()
