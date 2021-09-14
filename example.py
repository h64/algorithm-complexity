import time

start_time = time.time()

def print_time_elapsed():
    time_elapsed = round(time.time() - start_time, 2)
    print(f"{time_elapsed} seconds have passed")

#################################
# Time Complexity! Big-O Notation
huge_haystack = ['hay'] * 20000000
huge_haystack.append('needle')

# Constant O(1)
# number of operations stays constant as input increases
def find_needle_in_haystack(arr):
    needle_from_the_sewing_kit = "needle" # O(1)
    return needle_from_the_sewing_kit

# find_needle_in_haystack(huge_haystack)
# print_time_elapsed()

# Linear O(n)
# number of operations increases linearly as input increases
def find_needle_in_haystack(arr):
    for i in range(len(huge_haystack)):
        if huge_haystack[i] == 'needle':
            return i # loop 10 million and 1 times, or `n` times


# find_needle_in_haystack(huge_haystack)
# print_time_elapsed()

# Quadratic O(n^2)
# number of operations increases by power of two as input increases
def find_needle_in_haystack(arr):
    num_operations = 0
    for i in range(len(arr)):
        for j in range(len(arr)):
            num_operations += 1
            print(num_operations)

# find_needle_in_haystack(huge_haystack)
# print_time_elapsed()

# Factorial O(n^2)
# adding a nested loop for every item

# Logarithmic O(log(n))
# Halving the problem space (input) with each operation - phonebook!

