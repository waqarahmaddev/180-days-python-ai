# Day 6: Dictionaries - Waqar - 10 Aug 2026

student = {"name": "Waqar", "age": 25, "city": "Faisalabad", "marks": 85}

print(f"Name: {student['name']}")
print(f"City: {student.get('city')}")

# Update
student["marks"] = 90
student["grade"] = "A"

# Loop
for key, value in student.items():
    print(f"{key}: {value}")

# List of Dicts - REAL PROJECT!
students = [
    {"name": "Waqar", "marks": 90},
    {"name": "Ali", "marks": 78},
    {"name": "Ahmed", "marks": 92}
]

# Find topper using Day 5 logic!
max_marks = students[0]["marks"]
topper = students[0]["name"]
for s in students:
    if s["marks"] > max_marks:
        max_marks = s["marks"]
        topper = s["name"]

print(f"\nTopper: {topper} with {max_marks} marks")
