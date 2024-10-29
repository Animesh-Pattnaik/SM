import random
import math

def main():
    mean = float(input("Enter the mean for Poisson distribution: "))
    n = int(input("Enter the number of random variables to generate: "))

    print("\nGenerated Poisson Random Variables:")
    for _ in range(n):
        L = math.exp(-mean)
        p = 1.0
        k = 0

        while p > L:
            k += 1
            p *= random.random()  # Generate uniform random number between 0 and 1

        print(k - 1)

if __name__ == "__main__":
    main()