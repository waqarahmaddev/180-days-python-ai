# Day 5 - Lists & Loops - 6 Aug 2026
# Waqar Ahmad - 180 Days AI Challenge

# --- Learning: Lists Basics ---
fruits = ["apple", "banana", "mango", "orange"]
print(f"My fruits: {fruits}")
print(f"First fruit: {fruits[0]}")
print(f"Total fruits: {len(fruits)}")

# List operations
fruits.append("kiwi")
print(f"After append: {fruits}")

fruits[1] = "pineapple"
print(f"After update: {fruits}")

# --- Function 1: Sum of List ---
def sum_list(nums):
    total = 0
    for n in nums:
        total += n
    return total

# --- Function 2: Find Max (without using max()) ---
def find_max(nums):
    if len(nums) == 0:
        return "list is empty"
    biggest = nums[0]
    for n in nums:
        if n > biggest:
            biggest = n
    return biggest

# --- Function 3: Search Item ---
def search_item(my_list, item):
    if item in my_list:
        return f"{item} found!"
    else:
        return f"{item} not found"

# --- Function 4: Filter Even Numbers ---
def filter_even(nums):
    even_list = []
    for n in nums:
        if n % 2 == 0:
            even_list.append(n)
    return even_list

# --- Function 5: Count Occurrences ---
def count_item(my_list, item):
    count = 0
    for x in my_list:
        if x == item:
            count += 1
    return count

# --- Testing All Functions ---
print("\n--- Day 5 Tests ---")
numbers = [5, 10, 15, 20, 25, 30, 10]
print(f"Numbers: {numbers}")

print(f"Sum: {sum_list(numbers)}")
print(f"Max: {find_max(numbers)}")
print(f"Search 20: {search_item(numbers, 20)}")
print(f"Search 99: {search_item(numbers, 99)}")
print(f"Even only: {filter_even(numbers)}")
print(f"Count of 10: {count_item(numbers, 10)}")

print("\nDay 5 Done!")
