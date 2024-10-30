import math
import random
from collections import deque

def exponential_random(rate):
    U = random.random()
    return -math.log(1 - U) / rate

def finite_queue_model(max_queue_size, arrival_rate, service_rate, total_customers):
    queue = deque()
    rejected_customers = 0
    current_time = 0

    print(f"Simulating Finite Queue Model (M/M/1/{max_queue_size} Queue)")

    for i in range(1, total_customers + 1):
        arrival_time = current_time + exponential_random(arrival_rate)
        service_time = exponential_random(service_rate)

        print(f"Customer {i} arrives at {arrival_time:.2f}", end="")

        if len(queue) >= max_queue_size:
            print(" but is rejected (queue full).")
            rejected_customers += 1
        else:
            queue.append(service_time)
            print(" and joins the queue.")

        if queue and current_time <= arrival_time:
            current_time = arrival_time + queue.popleft()
            print(f"Customer is served and departs at {current_time:.2f}.")
        elif queue:
            current_time += queue.popleft()
            print(f"Customer is served and departs at {current_time:.2f}.")

    print(f"\nTotal Customers: {total_customers}")
    print(f"Rejected Customers (Queue Full): {rejected_customers}")
    print(f"Rejection Probability: {rejected_customers / total_customers:.2f}")

if __name__ == "__main__":
    max_queue_size = int(input("Enter maximum queue size: "))
    arrival_rate = float(input("Enter arrival rate (lambda): "))
    service_rate = float(input("Enter service rate (mu): "))
    total_customers = int(input("Enter total number of customers to simulate: "))

    finite_queue_model(max_queue_size, arrival_rate, service_rate, total_customers)