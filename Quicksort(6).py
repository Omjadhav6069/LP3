import random
import time

def partition(arr, low, high, is_random):
    pivot_index = random.randint(low, high) if is_random else high
    arr[pivot_index], arr[high] = arr[high], arr[pivot_index]
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

def quick_sort(arr, low, high, is_random):
    if low < high:
        pi = partition(arr, low, high, is_random)
        quick_sort(arr, low, pi - 1, is_random)
        quick_sort(arr, pi + 1, high, is_random)

def analyze_quick_sort(arr):
    for is_random in [False, True]:
        arr_copy = arr[:]
        start_time = time.time()
        quick_sort(arr_copy, 0, len(arr_copy) - 1, is_random)
        method = "Randomized" if is_random else "Deterministic"
        print(f"{method} QuickSort - Time: {time.time() - start_time:.5f}s")

# User input
n = int(input("Enter the number of elements: "))
arr = [random.randint(1, 1000) for _ in range(n)]
analyze_quick_sort(arr)
