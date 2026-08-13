# Day 9 - Exception Handling: Try/Except/Finally - Crash-Proof Apps
# Date: 13 Aug 2026 | Waqar Ahmad - Day 9/180
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))


def get_path(name):
    return os.path.join(BASE_DIR, name)


print("=== Day 9: Exception Handling Project ===\n")

# 1. BASIC try/except - Division by zero
print("1. Zero Division Handler:")
try:
    num = int(input("Enter number to divide 100: "))
    result = 100 / num
    print(f"Result: {result}")
except ZeroDivisionError:
    print("❌ Cannot divide by zero! Enter non-zero!")
except ValueError:
    print("❌ Please enter a number, not text!")

# 2. File Not Found - Real backend bug!
print("\n2. File Not Found Handler:")
try:
    with open(get_path("no_file.txt"), "r") as f:
        print(f.read())
except FileNotFoundError:
    print("❌ File not found! Creating it now...")
    with open(get_path("no_file.txt"), "w") as f:
        f.write("This file was auto-created by Day 9 handler!\n")
    print("✅ File created!")

# 3. Multiple except - Pro pattern
print("\n3. Multiple Exceptions - Student Marks:")
try:
    with open(get_path("students.txt"), "r") as f:
        for line in f:
            name, marks_part = line.split(" - ")
            marks = int(marks_part.split()[0])
            print(f"{name}: {marks} - Grade: {'A' if marks>=90 else 'B'}")
except FileNotFoundError:
    print("❌ students.txt not found - Run Day 8 first!")
except ValueError:
    print("❌ Marks format error in file!")
except Exception as e:
    print(f"❌ Unexpected error: {e}")

# 4. finally - Always runs - Real world: close DB connection
print("\n4. finally - Always runs:")
try:
    with open(get_path("notes.txt"), "r") as f:
        print(f.read(50))
except FileNotFoundError:
    print("❌ notes.txt missing")
finally:
    print("✅ Cleanup done - finally always runs!")

# 5. PROJECT 1: Crash-Proof Calculator
print("\n5. PROJECT: Crash-Proof Calculator")


def safe_calculator():
    while True:
        try:
            a = float(input("Enter first number (or q to quit): "))
            op = input("Enter operator + - * / : ")
            b = float(input("Enter second number: "))
            if op == "+":
                print(f"Result: {a+b}")
            elif op == "-":
                print(f"Result: {a-b}")
            elif op == "*":
                print(f"Result: {a*b}")
            elif op == "/":
                print(f"Result: {a/b}")
            else:
                print("❌ Invalid operator!")
            break
        except ZeroDivisionError:
            print("❌ Cannot divide by zero! Try again!")
        except ValueError:
            print("❌ Invalid number! Try again!")
        except Exception as e:
            print(f"❌ Error: {e}")


# safe_calculator() # Uncomment to test interactive

# 6. PROJECT 2: Safe File Reader with Loop
print("\n6. PROJECT: Safe File Reader (Loop until success)")
attempts = 0
while attempts < 3:
    try:
        filename = input(f"Enter file to read (attempt {attempts+1}/3): ").strip()
        if not filename:
            filename = "notes.txt"
        with open(get_path(filename), "r") as f:
            print(f"✅ File content:\n{f.read()}")
            break
    except FileNotFoundError:
        print(f"❌ {filename} not found! Try notes.txt, students.txt, todo.txt")
        attempts += 1
    except Exception as e:
        print(f"❌ Error: {e}")
        attempts += 1
else:
    print("❌ 3 attempts failed - Exiting!")

# 7. PROJECT 3: Age Validator with Custom Raise
print("\n7. PROJECT: Age Validator with raise")


def validate_age(age):
    if age < 0:
        raise ValueError("Age cannot be negative!")
    if age > 120:
        raise ValueError("Age too high! Are you human?")
    return True


try:
    age = int(input("Enter your age: "))
    validate_age(age)
    print(
        f"✅ Valid age: {age} - You can vote!"
        if age >= 18
        else f"✅ Valid age: {age} - Cannot vote yet!"
    )
except ValueError as ve:
    print(f"❌ Validation Error: {ve}")

print("\n=== Day 9 Done - Crash-Proof Apps Mastered! ===")
