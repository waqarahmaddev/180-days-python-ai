# Day 1 - Part 2: Input, Casting, Print Tricks

# 1. Input + Casting
name = input("Enter your name: ")
age = int(input("Enter your age: "))
city = input("Enter your city: ")

# 2. Print with sep and end
print("\n--- Your Info ---")
print(name, age, city, sep=" | ")
print(f"Hello {name}, you are {age} years old and live in {city}", end="! \n" )

# 3. Multiple Assignment Demo
x, y, z = 5, 10, 15
print(f"x: {x}, y: {y}, z: {z}")

a = b = c = 0
print(f"a: {a}, b: {b}, c: {c}")

print("\n--- Projects ---")

# Project 1: Simple Calculator
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

print(f"Sum: {num1 + num2}")
print(f"Difference: {num1 - num2}")
print(f"Product: {num1 * num2}")
print(f"Divide: {num1 / num2 }")

# Project 2: Swap Trick (Multiple Assignment)
a = 10
b = 20
print(f"\n Before Swap: a={a}, b={b}", end=" -> ")
a, b = b, a
print(f"After Swap: a={a}, b={b}")

# Project 3: Intro Card
print("\n--- My AI Card ---")
print(f"Name: {name}, Age: {age}, City: {city}", sep=" ")
print("Goal: Aspiring AI Developer", end="! \n")
