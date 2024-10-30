import math
import random
from collections import deque

def exponential_random(rate):
    U = random.random()
    return -math.log(1 - U) / rate

def infinite_queue_model(arrival_rate, service_rate, total_customers):
    queue = deque()
    current_time = 0
    total_waiting_time = 0

    print("Simulating Infinite Queue Model (M/M/1 Queue)")

    for i in range(1, total_customers + 1):
        arrival_time = current_time + exponential_random(arrival_rate)
        service_time = exponential_random(service_rate)

        print(f"Customer {i} arrives at {arrival_time:.2f} and joins the queue.")

        queue.append(service_time)

        if current_time <= arrival_time:
            current_time = arrival_time + queue.popleft()
            print(f"Customer is served and departs at {current_time:.2f}.")
        else:
            current_time += queue.popleft()
            total_waiting_time += (current_time - arrival_time)
            print(f"Customer is served and departs at {current_time:.2f}.")

    print(f"\nTotal Customers: {total_customers}")
    print(f"Average Waiting Time: {total_waiting_time / total_customers:.2f}")

if __name__ == "__main__":
    arrival_rate = float(input("Enter arrival rate (lambda): "))
    service_rate = float(input("Enter service rate (mu): "))
    total_customers = int(input("Enter total number of customers to simulate: "))

    infinite_queue_model(arrival_rate, service_rate, total_customers)