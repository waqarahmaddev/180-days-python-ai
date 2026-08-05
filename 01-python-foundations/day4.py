# Day 4 - Functions - 5 Aug 2026
# Waqar Ahmad

# function 1 - greeting
def greet(name):

    return f"Hello {name} Welcome to Day 4"

# function 2 - add
def add(a,b):
    return a+b

def sub(a,b):
    return a-b

def mul(a,b):
    return a*b

def div(a,b):
    if b==0:
        return "cannot divide by zero"
    return a/b

# function 3 - even odd
def even_odd(num):
    if num%2==0:
        return "Even"
    else:
        return "Odd"

# function 4 - grade
def grade(marks):
    if marks>=90:
        return "A+"
    elif marks>=80:
        return "A"
    elif marks>=70:
        return "B"
    else:
        return "F"

# function 5 - bill split
def bill_split(bill,friends):
    if friends==0:
        return "friends cannot be 0"
    return bill/friends

# testing my functions
print("Day 4 Functions Test")

print(greet("Waqar"))
print(greet("Ali"))

print("5 + 3 =", add(5,3))
print("10 - 3 =", sub(10,3))
print("5 * 3 =", mul(5,3))
print("10 / 2 =", div(10,2))
print("10 / 0 =", div(10,0))

print("25 is", even_odd(25))
print("10 is", even_odd(10))

print("94 marks grade is", grade(94))
print("75 marks grade is", grade(75))

print("Bill 4876 split 3 =", bill_split(4876,3))

print("Day 4 Done")
