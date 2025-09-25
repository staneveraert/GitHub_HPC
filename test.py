import time

def long_calculation():
    print("Starting long calculation...")
    start = time.time()
    result = sum(i*i for i in range(int(1e10)))
    end = time.time()
    print(f"Calculation result: {result}")
    print(f"Time taken: {end - start:.2f} seconds")

if __name__ == "__main__":
    long_calculation()