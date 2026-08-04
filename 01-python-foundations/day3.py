# Day 3 - Loops - Waqar Ahmad - 4 Aug 2026
# 180 Days Python AI Challenge

print("--- Project 1: Multiplication Table ---")
num = int(input("Enter number for table: "))

for i in range(1, 11):  # 1 to 10
    result = num * i
    print(f"{num} x {i} = {result}")

print("\n--- Project 2: Sum & Average with Loop ---")
n = int(input("How many numbers? "))
total = 0

for i in range(1, n+1):
    num2 = int(input(f"Enter number {i}: "))
    total = total + num2

average = total / n
print(f"Sum = {total}, Average = {average}")

print("\n--- Project 3a: Star Pattern ---")
rows = int(input("Enter rows for pattern: "))

for i in range(1, rows+1):
    for j in range(i):
        print("*", end=" ")
    print()

print("\n--- Project 3b: Guessing Game (while loop) ---")
secret = 7
guess = 0

while guess != secret:
    guess = int(input("Guess the number (1-10): "))
    if guess == secret:
        print("Correct! You guessed it!")
    else:
        print("Wrong, try again!")
