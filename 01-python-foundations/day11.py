# Day 11: Inheritance & Polymorphism
# Waqar Ahmad - 4 Oct 2026
# 180 Days Python to AI Challenge

print("=" * 50)
print("DAY 11: INHERITANCE & POLYMORPHISM")
print("=" * 50)


# ============================================================
# PROJECT 1: BankAccount -> SavingsAccount
# ============================================================

print("\n--- PROJECT 1: BankAccount -> SavingsAccount ---")

class BankAccount:
    """Parent class. Basic bank account."""

    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance
        print(f"[BankAccount] Created account for {owner} with balance {balance}")

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Deposit amount must be positive")
        self.balance += amount
        print(f"[BankAccount] Deposited {amount}. New balance: {self.balance}")

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Withdraw amount must be positive")
        if amount > self.balance:
            raise ValueError(f"Insufficient funds! Balance: {self.balance}, Tried: {amount}")
        self.balance -= amount
        print(f"[BankAccount] Withdrew {amount}. New balance: {self.balance}")

    def show_balance(self):
        print(f"[BankAccount] {self.owner} balance: {self.balance}")


class SavingsAccount(BankAccount):
    """Child class. Inherits from BankAccount. Adds interest."""

    def __init__(self, owner, balance, interest_rate):
        # Call parent __init__ first
        super().__init__(owner, balance)
        # Then add child-specific stuff
        self.interest_rate = interest_rate
        print(f"[SavingsAccount] Interest rate set to {interest_rate}")

    def add_interest(self):
        """Child-specific method. Parent does not have this."""
        interest = self.balance * self.interest_rate
        self.balance += interest
        print(f"[SavingsAccount] Interest added: {interest}. New balance: {self.balance}")


# Test Project 1
print("\nTesting SavingsAccount:")
savings = SavingsAccount("Waqar", 1000, 0.05)
savings.show_balance()
savings.deposit(500)
savings.withdraw(200)
savings.add_interest()
savings.show_balance()

print("\nTesting error handling:")
try:
    savings.withdraw(5000)
except ValueError as e:
    print(f"Error caught: {e}")


# ============================================================
# PROJECT 2: Person -> Student -> Teacher (Polymorphism)
# ============================================================

print("\n--- PROJECT 2: Person -> Student -> Teacher (Polymorphism) ---")

class Person:
    """Parent class."""

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def get_role(self):
        return "Person"

    def introduce(self):
        return f"Hi, I am {self.name}, age {self.age}. Role: {self.get_role()}"


class Student(Person):
    """Child class. Inherits from Person."""

    def __init__(self, name, age, student_id):
        super().__init__(name, age)
        self.student_id = student_id

    def get_role(self):
        # Override parent method
        return "Student"


class Teacher(Person):
    """Child class. Inherits from Person."""

    def __init__(self, name, age, subject):
        super().__init__(name, age)
        self.subject = subject

    def get_role(self):
        # Override parent method
        return "Teacher"


# Test Project 2
print("\nPolymorphism in action:")
people = [
    Person("Ali", 30),
    Student("Waqar", 25, "S123"),
    Teacher("Ahmed", 40, "Python")
]

for person in people:
    print(person.introduce())


# ============================================================
# PROJECT 3: Shape -> Circle, Rectangle (Polymorphism)
# ============================================================

print("\n--- PROJECT 3: Shape -> Circle, Rectangle (Polymorphism) ---")

class Shape:
    """Parent class."""

    def area(self):
        return 0

    def name(self):
        return "Shape"


class Circle(Shape):
    """Child class. Inherits from Shape."""

    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14159 * self.radius * self.radius

    def name(self):
        return "Circle"


class Rectangle(Shape):
    """Child class. Inherits from Shape."""

    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def name(self):
        return "Rectangle"


# Test Project 3
print("\nSame method 'area'. Different behavior:")
shapes = [
    Circle(5),
    Rectangle(4, 6),
    Circle(2),
    Rectangle(10, 3)
]

for shape in shapes:
    print(f"{shape.name()} area: {shape.area()}")


print("\n" + "=" * 50)
print("Day 11 Complete - Inheritance & Polymorphism")
print("=" * 50)
