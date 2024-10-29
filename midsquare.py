def mid_square(seed, n):
    random_numbers = []
    for _ in range(n):
        square = str(seed ** 2).zfill(8)   
        middle_digits = int(square[2:6])  
        seed = middle_digits               
        random_numbers.append(seed)    
    return random_numbers

seed = int(input("Enter the seed value (a positive integer): "))
n = int(input("Enter the number of random numbers to generate: "))
print("\nGenerated Random Numbers using Mid-Square Method:")
print(mid_square(seed, n))