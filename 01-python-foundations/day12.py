# Day 12: Encapsulation & Abstraction
# Waqar Ahmad - 16 Oct 2026
# 180 Days Python to AI Challenge

print("=" * 50)
print("DAY 12: ENCAPSULATION & ABSTRACTION")
print("=" * 50)


# ============================================================
# PROJECT 1: BankAccount with Encapsulation
# ============================================================

print("\n--- PROJECT 1: BankAccount with Encapsulation ---")

class BankAccount:
    """Bank account with private balance and validation."""

    def __init__(self, owner, balance):
        self.owner = owner
        self.__balance = balance  # private

    @property
    def balance(self):
        """Getter. Read balance from outside."""
        return self.__balance

    @balance.setter
    def balance(self, amount):
        """Setter. Validate before setting."""
        if amount < 0:
            raise ValueError("Balance cannot be negative")
        self.__balance = amount

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Deposit must be positive")
        self.__balance += amount
        print(f"[BankAccount] Deposited {amount}. New balance: {self.__balance}")

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Withdraw must be positive")
        if amount > self.__balance:
            raise ValueError(f"Insufficient funds! Balance: {self.__balance}")
        self.__balance -= amount
        print(f"[BankAccount] Withdrew {amount}. New balance: {self.__balance}")


# Test Project 1
print("\nTesting BankAccount:")
account = BankAccount("Waqar", 1000)
print(f"Owner: {account.owner}")
print(f"Balance: {account.balance}")

account.deposit(500)
account.withdraw(200)
print(f"Final balance: {account.balance}")

print("\nTesting private access:")
try:
    print(account.__balance)
except AttributeError as e:
    print(f"Cannot access private: {e}")

print("\nTesting setter validation:")
try:
    account.balance = -100
except ValueError as e:
    print(f"Setter caught: {e}")


# ============================================================
# PROJECT 2: Student with Encapsulation and Validation
# ============================================================

print("\n--- PROJECT 2: Student with Encapsulation ---")

class Student:
    """Student with private marks and validation."""

    def __init__(self, name, marks):
        self.name = name
        self.__marks = marks  # private

    @property
    def marks(self):
        return self.__marks

    @marks.setter
    def marks(self, value):
        if value < 0 or value > 100:
            raise ValueError("Marks must be between 0 and 100")
        self.__marks = value

    def get_grade(self):
        if self.__marks >= 90:
            return "A+"
        elif self.__marks >= 80:
            return "A"
        elif self.__marks >= 70:
            return "B"
        elif self.__marks >= 60:
            return "C"
        else:
            return "F"

    def __str__(self):
        return f"{self.name}: marks = {self.__marks}, grade = {self.get_grade()}"


# Test Project 2
print("\nTesting Student:")
s1 = Student("Waqar", 85)
print(s1)

s1.marks = 95
print(f"After update: {s1}")

print("\nTesting marks validation:")
try:
    s1.marks = 150
except ValueError as e:
    print(f"Validation caught: {e}")


# ============================================================
# PROJECT 3: Shape with Abstraction
# ============================================================

print("\n--- PROJECT 3: Shape with Abstraction ---")

from abc import ABC, abstractmethod

class Shape(ABC):
    """Abstract base class. Cannot create object directly."""

    @abstractmethod
    def area(self):
        """Every shape must have area."""
        pass

    @abstractmethod
    def name(self):
        """Every shape must have name."""
        pass

    def describe(self):
        return f"{self.name()} has area {self.area()}"


class Circle(Shape):
    """Circle. Must implement area and name."""

    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14159 * self.radius * self.radius

    def name(self):
        return "Circle"


class Rectangle(Shape):
    """Rectangle. Must implement area and name."""

    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def name(self):
        return "Rectangle"


# Test Project 3
print("\nTesting Shape abstraction:")

shapes = [Circle(5), Rectangle(4, 6), Circle(2)]
for shape in shapes:
    print(shape.describe())

print("\nTesting cannot instantiate abstract class:")
try:
    s = Shape()
except TypeError as e:
    print(f"Cannot instantiate Shape: {e}")


print("\n" + "=" * 50)
print("Day 12 Complete - Encapsulation & Abstraction")
print("=" * 50)
