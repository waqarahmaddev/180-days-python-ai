# Day 8 - File Handling: Read, Write, Append - Real Backend Skill
# Date: 12 Aug 2026 | Time: 11:07 PM | Waqar Ahmad
import os
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
def get_path(name): return os.path.join(BASE_DIR, name)

print("=== Day 8: File Handling Project ===\n")

print("1. Write File:")
with open(get_path("notes.txt"), "w") as f:
    f.write("Day 8 - Learning File Handling\n")
    f.write("Python is powerful!\n")
print("✅ notes.txt created!")

print("\n2. Read File:")
with open(get_path("notes.txt"), "r") as f:
    print(f.read())

print("3. Append File:")
with open(get_path("notes.txt"), "a") as f:
    f.write("Added at 11 PM - Day 8 streak!\n")
print("✅ Line appended!")

print("\n4. Read Line by Line:")
with open(get_path("notes.txt"), "r") as f:
    for line in f:
        print(f"-> {line.strip()}")

print("\n5. PROJECT: Save Student Marks")
with open(get_path("students.txt"), "w") as f:
    f.write(f"Waqar - 95 marks\nAli - 88 marks\nAhmed - 92 marks\n")

print("\nFind Topper from File:")
with open(get_path("students.txt"), "r") as f:
    topper = ""; max_marks = 0
    for line in f:
        parts = line.split(" - "); marks = int(parts[1].split()[0])
        if marks > max_marks: max_marks = marks; topper = parts[0]
    print(f"Topper: {topper} with {max_marks} marks")

print("\n6. PROJECT: To-Do List App")
with open(get_path("todo.txt"), "w") as f:
    f.write("1. Complete Day 8\n2. Push to GitHub\n3. LinkedIn post\n")
print("Your To-Do List:")
with open(get_path("todo.txt"), "r") as f: print(f.read())

print("7. PROJECT: Word Counter")
with open(get_path("notes.txt"), "r") as f:
    words = f.read().split()
    print(f"Total words: {len(words)}")

print("\n=== Day 8 Done - File Handling Mastered! ===")
