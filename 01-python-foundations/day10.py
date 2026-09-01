# Day 10 - OOP Basics: Classes & Objects
# Date: 1 Sep 2026 - Resume Day
# Journey: Day 0-9 -> Day 10 | Python Foundations
# Topics: class, __init__, self, instance vs class variables, methods, __str__, raise, try/except

# PROJECT 1: Student Grade System (Day 2, 5, 6 logic -> Now OOP)
class Student:
    """Student with marks, grade and pass/fail logic - Real school system"""
    school_name = "GCUF"  # Class variable - same for all students

    def __init__(self, name: str, marks: int):
        if marks < 0 or marks > 100:
            raise ValueError("Marks must be between 0-100!")
        self.name = name
        self.marks = marks

    def get_grade(self):
        if self.marks >= 80: return "A+"
        elif self.marks >= 70: return "A"
        elif self.marks >= 60: return "B"
        elif self.marks >= 50: return "C"
        else: return "F"

    def is_pass(self):
        return self.marks >= 50

    def __str__(self):
        return f"{self.name} | Marks: {self.marks} | Grade: {self.get_grade()} | Pass: {self.is_pass()} | School: {self.school_name}"

# PROJECT 2: BankAccount (Day 9 Exception Handling + OOP = Crash-Proof Bank)
class BankAccount:
    """Bank Account with deposit/withdraw - Real app never crashes"""

    def __init__(self, holder_name: str, balance: float = 0):
        if balance < 0:
            raise ValueError("Initial balance cannot be negative!")
        self.holder_name = holder_name
        self.balance = balance
        self.history = []  # List of transactions (Day 5 Lists)

    def deposit(self, amount: float):
        if amount <= 0:
            raise ValueError("Deposit must be positive!")
        self.balance += amount
        self.history.append(f"Deposited {amount}")
        return f"✅ Deposited {amount}, New Balance: {self.balance}"

    def withdraw(self, amount: float):
        if amount <= 0:
            raise ValueError("Withdraw must be positive!")
        if amount > self.balance:
            raise ValueError(f"Insufficient funds! Balance: {self.balance}, Tried: {amount}")
        self.balance -= amount
        self.history.append(f"Withdrew {amount}")
        return f"✅ Withdrew {amount}, Balance: {self.balance}"

    def show_balance(self):
        return f"💰 {self.holder_name}'s Balance: {self.balance}"

    def show_history(self):
        if not self.history:
            return "No transactions yet"
        return "\n".join(self.history)

    def __str__(self):
        return f"{self.holder_name} - Balance: {self.balance}"

# PROJECT 3: To-Do App OOP Version (Day 8 File Handling -> Now OOP)
class TodoManager:
    """To-Do Manager - Day 8 project converted to OOP"""
    def __init__(self):
        self.tasks = []

    def add_task(self, task: str):
        self.tasks.append(task)
        return f"Added: {task}"

    def show_tasks(self):
        if not self.tasks:
            return "No tasks"
        result = ""
        for i, t in enumerate(self.tasks, 1):
            result += f"{i}. {t}\n"
        return result.strip()

# ===== DEMO - Real Usage =====
if __name__ == "__main__":
    print("="*50)
    print("PROJECT 1: Student System")
    print("="*50)
    try:
        s1 = Student("Waqar", 85)
        s2 = Student("Ali", 45)
        print(s1)
        print(s2)
    except ValueError as ve:
        print(f"❌ Validation Error: {ve}")

    print("\n" + "="*50)
    print("PROJECT 2: Crash-Proof BankAccount")
    print("="*50)
    try:
        acc = BankAccount("Waqar", 1000)
        print(acc.show_balance())
        print(acc.deposit(500))
        print(acc.withdraw(200))
        # This will fail safely - Day 9 logic
        print(acc.withdraw(5000))
    except ValueError as ve:
        print(f"❌ {ve}")
    finally:
        print(f"Final: {acc.show_balance()}")
        print("History:\n" + acc.show_history())

    print("\n" + "="*50)
    print("PROJECT 3: To-Do OOP")
    print("="*50)
    todo = TodoManager()
    print(todo.add_task("Learn OOP Basics"))
    print(todo.add_task("Build BankAccount"))
    print(todo.show_tasks())

    print("\n✅ Day 10 Done - OOP Basics Mastered! Student + BankAccount + ToDo OOP")
