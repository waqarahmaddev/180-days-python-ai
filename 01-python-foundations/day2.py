# Day 2 - Operators and If Else
# Waqar Ahmad - 1 Aug 2026

# Even Odd Checker
age = int(input("Enter your age: "))
if age % 2 == 0:
    print("Your age is even.")
else:
    print("Your age is odd.")

# Grade Checker
marks = int(input("Enter your marks (0-100): "))
if marks >= 90:
    print("Grade: A+")
elif marks >= 80:
    print("Grade: A")
elif marks >= 70:
    print("Grade: B")
elif marks >= 60:
    print("Grade: C")
else:
    print("Grade: F")

# Voting Check
v_age = int(input("Enter age for voting: "))
if v_age >= 18:
    print("You can vote")
else:
    print("You cannot vote")

# Bill Split
bill = float(input("Enter bill: "))
friends = int(input("Enter friends: "))
each = bill / friends
print(f"Each pays: ${each:.2f}")
