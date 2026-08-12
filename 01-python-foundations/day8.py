# Day 8 - File Handling: Read, Write, Append - Real Backend Skill
# Date: 12 Aug 2026 | Time: 11:07 PM | Waqar Ahmad

print("=== Day 8: File Handling Project ===\n")

# 1. WRITE File - Create new file (w = write, overwrites)
print("1. Write File:")
with open("notes.txt", "w") as f:
    f.write("Day 8 - Learning File Handling\n")
    f.write("Python is powerful!\n")
print("✅ notes.txt created!")

# 2. READ File - Read full file (r = read)
print("\n2. Read File:")
with open("notes.txt", "r") as f:
    content = f.read()
    print(content)

# 3. APPEND File - Add without deleting (a = append)
print("3. Append File:")
with open("notes.txt", "a") as f:
    f.write("Added at 11 PM - Day 8 streak!\n")
print("✅ Line appended!")

# 4. Read Line by Line - Real world log reading
print("\n4. Read Line by Line:")
with open("notes.txt", "r") as f:
    for line in f:
        print(f"-> {line.strip()}")

# 5. PROJECT 1: Student Marks Saver
print("\n5. PROJECT: Save Student Marks")
name = "Waqar"
marks = 95
with open("students.txt", "w") as f:
    f.write(f"{name} - {marks} marks\n")
    f.write("Ali - 88 marks\n")
    f.write("Ahmed - 92 marks\n")
print("✅ students.txt saved!")

# Read back and find topper (Day 6 logic + File)
print("\nFind Topper from File:")
with open("students.txt", "r") as f:
    topper = ""
    max_marks = 0
    for line in f:
        # line = "Waqar - 95 marks"
        parts = line.split(" - ")
        student_name = parts[0]
        student_marks = int(parts[1].split()[0])
        if student_marks > max_marks:
            max_marks = student_marks
            topper = student_name
    print(f"Topper: {topper} with {max_marks} marks")

# 6. PROJECT 2: To-Do List App (Real App Logic)
print("\n6. PROJECT: To-Do List App")
# Add tasks
with open("todo.txt", "w") as f:
    f.write("1. Complete Day 8 File Handling\n")
    f.write("2. Push to GitHub\n")
    f.write("3. LinkedIn post\n")

# Read tasks
print("Your To-Do List:")
with open("todo.txt", "r") as f:
    print(f.read())

# 7. PROJECT 3: Count Words in File
print("7. PROJECT: Word Counter")
with open("notes.txt", "r") as f:
    text = f.read()
    words = text.split()
    print(f"Total words in notes.txt: {len(words)}")
    print(f"Words: {words}")

print("\n=== Day 8 Done - File Handling Mastered! ===")
