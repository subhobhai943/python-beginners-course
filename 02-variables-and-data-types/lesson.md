# Lesson 2: Variables and Data Types 📦

Welcome to Lesson 2! Now we'll learn how to store and work with data in Python.

## 🎯 What is a Variable?

A variable is like a labeled box where you can store information. You can put something in, look at what's inside, or change it later.

```python
name = "Alice"
age = 15
```

Think of it this way:
- `name` is a box labeled "name" containing "Alice"
- `age` is a box labeled "age" containing 15

## 📝 Creating Variables

Creating a variable is super easy:

```python
message = "Hello, Python!"
print(message)  # Prints: Hello, Python!

score = 100
print(score)  # Prints: 100
```

### Variable Naming Rules

✅ **Good variable names:**
```python
player_name = "Alex"
total_score = 500
is_game_over = False
```

❌ **Bad variable names:**
```python
2players = "Wrong"  # Can't start with a number
player-name = "Wrong"  # Can't use hyphens
my name = "Wrong"  # Can't have spaces
```

### Naming Conventions

- Use lowercase letters
- Use underscores to separate words (`my_variable`)
- Make names descriptive (`score` not `s`)
- Avoid Python keywords (like `print`, `if`, `for`)

## 🎨 Data Types in Python

Python has different types of data. Let's explore them!

### 1. Strings (Text) 📝

Strings are text wrapped in quotes:

```python
name = "Alice"
greeting = 'Hello!'  # Single or double quotes work
multiline = """This is
a longer
message"""

print(name)  # Prints: Alice
```

**String Operations:**
```python
first_name = "John"
last_name = "Doe"

# Combining strings (concatenation)
full_name = first_name + " " + last_name
print(full_name)  # Prints: John Doe

# Repeating strings
laugh = "ha" * 3
print(laugh)  # Prints: hahaha
```

### 2. Integers (Whole Numbers) 🔢

Integers are whole numbers:

```python
age = 15
score = 1000
temperature = -5

print(age + 5)  # Prints: 20
print(score * 2)  # Prints: 2000
```

### 3. Floats (Decimal Numbers) 🎯

Floats are numbers with decimal points:

```python
price = 19.99
temperature = 98.6
pi = 3.14159

print(price * 2)  # Prints: 39.98
```

### 4. Booleans (True/False) ✓✗

Booleans represent True or False:

```python
is_raining = True
has_homework = False
game_over = True

print(is_raining)  # Prints: True
```

## 🔄 Type Conversion

You can convert between different types:

```python
# String to Integer
age_text = "15"
age_number = int(age_text)
print(age_number + 5)  # Prints: 20

# Integer to String
score = 100
score_text = str(score)
print("Your score is: " + score_text)  # Prints: Your score is: 100

# String to Float
price = "19.99"
price_number = float(price)
print(price_number * 2)  # Prints: 39.98
```

## 🎮 Getting User Input

You can ask users for information:

```python
name = input("What's your name? ")
print("Hello, " + name + "!")

# For numbers, convert the input
age = input("How old are you? ")
age = int(age)  # Convert string to integer
print("Next year you'll be", age + 1)
```

## 🔍 Checking Data Types

```python
name = "Alice"
age = 15
price = 19.99
is_student = True

print(type(name))       # Prints: <class 'str'>
print(type(age))        # Prints: <class 'int'>
print(type(price))      # Prints: <class 'float'>
print(type(is_student)) # Prints: <class 'bool'>
```

## 💡 F-Strings (Modern String Formatting)

The easiest way to combine variables and text:

```python
name = "Alice"
age = 15
score = 95.5

# Put 'f' before the string and use {variable} inside
message = f"Hi, I'm {name}. I'm {age} years old and scored {score}%!"
print(message)
# Prints: Hi, I'm Alice. I'm 15 years old and scored 95.5%!

# You can do math inside f-strings
print(f"Next year I'll be {age + 1} years old")
# Prints: Next year I'll be 16 years old
```

## 🎯 Key Takeaways

✅ Variables store data for later use
✅ Use descriptive names with underscores
✅ Main data types: strings, integers, floats, booleans
✅ Use `input()` to get user input
✅ Use `int()`, `str()`, `float()` to convert types
✅ F-strings make string formatting easy

## 🏋️ Practice Time!

Head over to [exercises.py](exercises.py) to practice working with variables and data types!

## 🏆 Challenge (Optional)

Create a simple profile program that:
1. Asks for the user's name
2. Asks for their age
3. Asks for their favorite hobby
4. Prints a nice message using all this information

Example:
```
What's your name? Alex
How old are you? 14
What's your favorite hobby? gaming

Nice to meet you, Alex!
You're 14 years old and you love gaming.
That's awesome! 🎉
```

---

**Previous Lesson:** [⬅️ Introduction to Python](../01-getting-started/lesson.md)  
**Next Lesson:** [Operators](../03-operators/lesson.md) ➡️
