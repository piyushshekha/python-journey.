# ==============================================================================
# 🐍 PYTHON MASTER CHEATSHEET (LECTURES 1, 2, 3)
# ==============================================================================

# ------------------------------------------------------------------------------
# 📌 LECTURE 1: VARIABLES, DATA TYPES, OPERATORS & INPUT
# ------------------------------------------------------------------------------

# 1. Primitive Data Types
age = 21                  # int (Integer)
price = 99.50             # float (Decimal number)
name = "Piyush"           # str (String / Text)
is_active = True          # bool (Boolean: True / False - First letter Capital!)
data = None               # NoneType (Absence of value)

# Check Data Type
print(type(age))          # <class 'int'>

# 2. Type Casting (Explicit Conversion)
num_str = "100"
num_int = int(num_str)    # String -> Int
float_val = float(5)      # 5 -> 5.0

# 3. User Input (Golden Rule: input() ALWAYS returns str!)
# user_name = input("Enter name: ")
# user_age = int(input("Enter age: "))

# 4. Arithmetic Operators
a, b = 7, 2
print(a + b)              # 9 (Addition)
print(a - b)              # 5 (Subtraction)
print(a * b)              # 14 (Multiplication)
print(a / b)              # 3.5 (Normal Division -> ALWAYS returns float)
print(a // b)             # 3 (Floor Division -> Discards decimal part)
print(a % b)              # 1 (Modulo -> Returns remainder)
print(a ** b)             # 49 (Power -> 7^2)

# 5. Relational / Comparison Operators (Always return True / False)
print(a == b)             # False (Equal to)
print(a != b)             # True (Not equal to)
print(a >= b)             # True (Greater than or equal to)

# 6. Logical Operators
print(True and False)     # False (Both must be True)
print(True or False)      # True (At least one must be True)
print(not True)           # False (Inverts boolean)


# ------------------------------------------------------------------------------
# 📌 LECTURE 2: STRINGS, SLICING & CONDITIONAL STATEMENTS
# ------------------------------------------------------------------------------

s = "  Python Developer  "

# 1. String Methods (Do NOT change original string, return NEW string!)
clean_s = s.strip()       # Removes extra spaces from start & end: "Python Developer"
print(clean_s.lower())    # "python developer"
print(clean_s.upper())    # "PYTHON DEVELOPER"
print(clean_s.capitalize()) # "Python developer" (Only 1st char capital)
print(clean_s.count("e")) # 3 (Counts total occurrences)
print(clean_s.find("Dev"))# 7 (Returns first starting index, -1 if not found)
print(clean_s.replace("Python", "Backend")) # "Backend Developer"
print(clean_s.endswith("per")) # True

# 2. Indexing & Slicing: [start : stop : step] (stop index is EXCLUDED)
word = "DEVELOPER"
print(word[0])            # 'D' (First character)
print(word[-1])           # 'R' (Last character)
print(word[0:4])          # 'DEVE' (Indices 0, 1, 2, 3)
print(word[::2])          # 'DVLPR' (Step of 2: alternate letters)
print(word[::-1])         # 'REPOLEVED' (Negative step reverses string!)

# 3. Immutability
# word[0] = 'X'           # ❌ TypeError! Strings cannot be modified in-place

# 4. Conditionals (Indentation = 4 Spaces)
score = 85
if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
else:
    grade = "C"


# ------------------------------------------------------------------------------
# 📌 LECTURE 3: LISTS & TUPLES (DATA STRUCTURES)
# ------------------------------------------------------------------------------

# 1. Lists (MUTABLE: Original data can change in memory)
marks = [75, 90, 82, 60]
marks[0] = 99             # ✔️ Allowed! marks is now [99, 90, 82, 60]

# List Methods (In-place modification: return None!)
marks.append(100)         # Adds at the very end
marks.insert(1, 45)       # Inserts value 45 at index 1
marks.sort()              # Sorts ascending
marks.sort(reverse=True)  # Sorts descending
marks.reverse()           # Reverses list in-place

# Removing Elements:
popped_item = marks.pop() # Removes last item and RETURNS it
marks.remove(45)          # Removes first matching value 45 (returns None)

# The Copy Rule:
# copy_list = marks       # ❌ Alias trap: changing copy_list will change marks!
real_copy = marks.copy()  # ✔️ Real duplicate list in new memory location

# 2. Tuples (IMMUTABLE: Read-only, cannot be changed)
tup = (10, 20, 30, 20)
print(tup[0])             # 10 (Indexing allowed)
# tup[0] = 99             # ❌ TypeError! Cannot change tuple values

# Single Element Tuple Trap:
single_fake = (5)         # ❌ Integer, not tuple!
single_real = (5,)        # ✔️ Tuple (comma is mandatory!)

# Tuple Methods (Only 2 methods exist):
print(tup.count(20))      # 2 (Counts occurrences)
print(tup.index(30))      # 2 (First index of value)

# 3. Conversion between List & Tuple
tup_to_list = list(tup)   # Converts tuple to list
list_to_tup = tuple(marks)# Converts list to tuple