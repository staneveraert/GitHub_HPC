import time
from multiprocessing import Pool

def partial_sum(start, end):
    return sum(i * i for i in range(start, end))

def long_calculation():
    print("Starting parallel calculation...")
    start = time.time()

    total_range = int(1e10)
    num_chunks = 36
    chunk_size = total_range // num_chunks

    # Create ranges for each chunk
    ranges = [(i * chunk_size, (i + 1) * chunk_size) for i in range(num_chunks)]

    with Pool(processes=num_chunks) as pool:
        results = pool.starmap(partial_sum, ranges)

    result = sum(results)
    end = time.time()

    print(f"Calculation result: {result}")
    print(f"Time taken: {end - start:.2f} seconds")

if __name__ == "__main__":
    long_calculation()