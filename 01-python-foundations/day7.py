# Day 7: Tuples & Sets - 11 Aug 2026 - Waqar Ahmad

# --- TUPLE PROJECTS ---

# Project 1: Faisalabad Coordinates (Immutable!)
faisalabad_coords = (31.4187, 73.0791)
print(f"Faisalabad: {faisalabad_coords}")
lat, long = faisalabad_coords
print(f"Lat: {lat}, Long: {long}")

# Project 2: Student Record as Tuple (Cannot be changed by mistake)
student = ("Waqar", 25, 85) # name, age, marks
name, age, marks = student
print(f"{name} is {age} years, marks {marks}")

# --- SET PROJECTS ---

# Project 3: Remove Duplicates — Real use case!
skills_list = ["Python", "Git", "Python", "GitHub", "Python", "LinkedIn"]
print(f"Before: {skills_list} — {len(skills_list)} skills")
unique_skills = set(skills_list)
print(f"After: {unique_skills} — {len(unique_skills)} unique skills")
unique_list = list(unique_skills)
print(f"As list: {unique_list}")

# Project 4: Find Common Skills — Interview Q!
waqar_skills = {"Python", "Git", "GitHub", "FastAPI"}
ali_skills = {"Python", "Java", "Git", "Docker"}

common = waqar_skills & ali_skills
print(f"Common skills: {common}") # {Python, Git}

only_waqar = waqar_skills - ali_skills
print(f"Only Waqar: {only_waqar}")

all_skills = waqar_skills | ali_skills
print(f"All skills combined: {all_skills}")

# Project 5: Voting — Unique voters!
voters = ["Waqar", "Ali", "Waqar", "Ahmed", "Ali", "Waqar"]
unique_voters = set(voters)
print(f"Total votes: {len(voters)}, Unique voters: {len(unique_voters)} — {unique_voters}")
