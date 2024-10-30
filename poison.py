import math
import random

def poisson_random(avg_rate):
    events, threshold, product = 0, math.exp(-avg_rate), 1.0
    while product > threshold:
        events += 1
        product *= random.random()
    return events - 1

def main():
    avg_rate = float(input("Enter the average rate of occurrence (lambda): "))
    num_samples = int(input("Enter the number of Poisson-distributed samples to generate: "))

    print(f"\nPoisson-distributed random numbers (with λ = {avg_rate}):")
    for _ in range(num_samples):
        print(poisson_random(avg_rate), end=" ")
    print()

if __name__ == "__main__":
    main()