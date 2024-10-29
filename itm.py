import math
import random

def generate_exponential(rate):
    u = random.uniform(0, 1)
    return -math.log(1 - u) / rate

def main():
    rate = float(input("Enter the rate parameter for Exponential distribution: "))
    n = int(input("Enter the number of random variables to generate: "))

    print("\nGenerated Exponential Random Variables:")
    for _ in range(n):
        exp_rv = generate_exponential(rate)
        print(exp_rv)

if __name__ == "__main__":
    main()