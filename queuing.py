import random
import numpy as np

def generate_exponential(rate):
    return np.random.exponential(1 / rate)

class Customer:
    def __init__(self, arrival_time, service_time):
        self.arrival_time = arrival_time
        self.service_time = service_time

def simulate_queue(arrival_rate, service_rate, num_customers):
    queue = [] 
    current_time = 0
    total_waiting_time = 0
    total_service_time = 0

    for _ in range(num_customers):
        inter_arrival_time = generate_exponential(arrival_rate)
        service_time = generate_exponential(service_rate)

        current_time += inter_arrival_time

        if queue and queue[0].arrival_time <= current_time:
            total_waiting_time += current_time - queue[0].arrival_time
            total_service_time += service_time
            queue.pop(0) 

        queue.append(Customer(current_time, service_time))

    print(f"Total Customers: {num_customers}")
    print(f"Average Waiting Time: {total_waiting_time / num_customers:.2f} units")
    print(f"Average Service Time: {total_service_time / num_customers:.2f} units")

if __name__ == "__main__":
    arrival_rate = float(input("Enter arrival rate (lambda): "))
    service_rate = float(input("Enter service rate (mu): "))
    num_customers = int(input("Enter number of customers to simulate: "))

    simulate_queue(arrival_rate, service_rate, num_customers)
