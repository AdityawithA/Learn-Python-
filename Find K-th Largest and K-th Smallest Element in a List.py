def find_kth_largest_smallest(numbers, k):
    unique_numbers = sorted(set(numbers))
    if k <= 0 or k > len(unique_numbers):
        raise ValueError("k is out of the valid range.")
    kth_smallest = unique_numbers[k - 1]
    kth_largest = unique_numbers[-k]
    return kth_smallest, kth_largest

def main():
    numbers_input = input("Enter a list of integers separated by spaces: ")
    numbers = list(map(int, numbers_input.split()))
    k = int(input("Enter the value of k: "))
    smallest, largest = find_kth_largest_smallest(numbers, k)
    print(f"{k}-th Smallest: {smallest}")
    print(f"{k}-th Largest: {largest}")

main()
