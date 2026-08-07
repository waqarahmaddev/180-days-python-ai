# === FULL REWIND DAY 0 TO DAY 5 - WAQAR - 7 AUG 2026 ===

print("=== Day 1: Variables + Input ===", end="\n\n")

# Day 1: Variables - Boxes
name = "Waqar"
age = 25
height = 5.9
is_ready = True

# Day 1: f-string + sep + end
print(f"Name: {name}", f"Age: {age}", sep=" | ", end="\n\n")

# Day 5: List - Many boxes in one!
marks = [85, 90, 78, 92, 88]
print(f"Original marks: {marks}")
print(
    f"First mark: {marks[0]}, Last mark: {marks[-1]}, Total subjects: {len(marks)}",
    end="\n\n",
)


# Day 4: Function - Reusable Machine
def analyze_marks(marks):
    total = 0  # Day 1: Variable
    max_m = marks[0]  # Day 5: Index 0 - Assume first is max
    passed = []  # Day 5: Empty list for filter pattern

    # Day 3: For Loop + Day 5: Loop with list
    for m in marks:
        total = total + m  # Day 2: + operator

        # Day 2: If-Else - Comparison
        if m > max_m:
            max_m = m

        # Day 2: If logic
        if m >= 33:
            passed.append(m)  # Day 5: append - Build new list!

    # Day 2: Operators
    avg = total / len(marks)  # / always float

    # Day 2: Grade logic - If-Elif-Else
    if avg >= 90:
        grade = "A+"
    elif avg >= 80:
        grade = "A"
    elif avg >= 70:
        grade = "B"
    else:
        grade = "C"

    return total, max_m, avg, grade, passed  # Day 4: Return multiple!


# Day 4: Call function
total, max_m, avg, grade, passed = analyze_marks(marks)  # Day 1: Multiple assignment

print("=== Day 2 + Day 3 + Day 4 + Day 5 Combined ===")
print(f"Total: {total} | Max: {max_m} | Avg: {avg:.2f} | Grade: {grade}", sep=" | ")
print(f"Passed subjects: {passed} - Count: {len(passed)}")

# Day 2: % - Even/Odd + Day 3: Break/Continue idea
print("\n=== Extra: Even marks filter ===")


def filter_even(nums):
    evens = []
    for n in nums:
        if n % 2 == 0:  # Day 2: % remainder
            evens.append(n)
    return evens


print(f"Even marks: {filter_even(marks)}")

# Day 1: Input + int() - Uncomment to test live!
# new_mark = int(input("\nEnter new mark to add: "))
# marks.append(new_mark)
# print(f"Updated list: {marks}")

print("\n=== Rewind Done - Ready for Day 6 Dictionaries! ===", end=" - InshaAllah!\n")
