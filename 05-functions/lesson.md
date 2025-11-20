# Lesson 5: Functions - Reusable Code Blocks 🔧

Welcome to Lesson 5! Functions are one of the most important concepts in programming. They help you organize and reuse your code.

## 🤔 What is a Function?

A function is a reusable block of code that performs a specific task. Think of it like a recipe - you write it once and use it many times!

## 📝 Creating Your First Function

```python
def greet():
    print("Hello, World!")
    print("Welcome to Python!")

# Call the function
greet()
# Output:
# Hello, World!
# Welcome to Python!
```

**Anatomy of a function:**
- `def` - keyword to define a function
- `greet` - function name (use descriptive names!)
- `()` - parentheses (parameters go here)
- `:` - colon to start the function block
- Indented code - the function body

## 🎁 Functions with Parameters

Parameters let you pass information to functions:

```python
def greet(name):
    print(f"Hello, {name}!")
    print("Nice to meet you!")

greet("Alice")   # Hello, Alice!
greet("Bob")     # Hello, Bob!
greet("Charlie") # Hello, Charlie!
```

### Multiple Parameters

```python
def introduce(name, age, city):
    print(f"Hi! I'm {name}.")
    print(f"I'm {age} years old.")
    print(f"I live in {city}.")

introduce("Alex", 15, "New York")
# Output:
# Hi! I'm Alex.
# I'm 15 years old.
# I live in New York.
```

### Default Parameters

```python
def greet(name="Friend"):
    print(f"Hello, {name}!")

greet("Alice")  # Hello, Alice!
greet()         # Hello, Friend! (uses default)
```

## 🔙 Return Values

Functions can return values back to you:

```python
def add(a, b):
    result = a + b
    return result

total = add(5, 3)
print(total)  # 8

# You can use the return value directly
print(add(10, 20))  # 30
```

### Multiple Return Values

```python
def calculate(a, b):
    sum_result = a + b
    diff_result = a - b
    prod_result = a * b
    return sum_result, diff_result, prod_result

sum_val, diff_val, prod_val = calculate(10, 5)
print(f"Sum: {sum_val}")    # Sum: 15
print(f"Diff: {diff_val}")   # Diff: 5
print(f"Product: {prod_val}") # Product: 50
```

## 🎯 Real-World Examples

### Example 1: Temperature Converter

```python
def celsius_to_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

def fahrenheit_to_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * 5/9
    return celsius

temp_c = 25
temp_f = celsius_to_fahrenheit(temp_c)
print(f"{temp_c}°C = {temp_f}°F")  # 25°C = 77.0°F
```

### Example 2: Grade Calculator

```python
def get_grade(score):
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"

student_score = 85
grade = get_grade(student_score)
print(f"Score: {student_score} = Grade: {grade}")  # Score: 85 = Grade: B
```

### Example 3: Password Validator

```python
def is_strong_password(password):
    if len(password) < 8:
        return False
    
    has_number = False
    for char in password:
        if char.isdigit():
            has_number = True
            break
    
    return has_number

password1 = "abc123"
password2 = "secure2024"

print(is_strong_password(password1))  # False (too short)
print(is_strong_password(password2))  # True
```

## 🌐 Variable Scope

Variables have different "scopes" - where they can be used:

### Local Scope

```python
def my_function():
    x = 10  # Local variable - only exists inside the function
    print(x)

my_function()  # Prints: 10
# print(x)  # Error! x doesn't exist outside the function
```

### Global Scope

```python
x = 10  # Global variable

def my_function():
    print(x)  # Can access global variable

my_function()  # Prints: 10
print(x)       # Prints: 10
```

### Modifying Global Variables

```python
count = 0  # Global variable

def increment():
    global count  # Tell Python we want to use the global variable
    count += 1

increment()
print(count)  # 1
increment()
print(count)  # 2
```

## 📚 Function Documentation

Good practice: document your functions!

```python
def calculate_area(length, width):
    """
    Calculate the area of a rectangle.
    
    Parameters:
    length (float): The length of the rectangle
    width (float): The width of the rectangle
    
    Returns:
    float: The area of the rectangle
    """
    return length * width

area = calculate_area(5, 3)
print(f"Area: {area}")  # Area: 15
```

## 🎮 Fun Examples

### Example 1: Dice Roll Simulator

```python
import random

def roll_dice():
    return random.randint(1, 6)

def roll_two_dice():
    dice1 = roll_dice()
    dice2 = roll_dice()
    total = dice1 + dice2
    print(f"🎲 Dice 1: {dice1}")
    print(f"🎲 Dice 2: {dice2}")
    print(f"Total: {total}")
    return total

roll_two_dice()
```

### Example 2: Text Art Generator

```python
def create_border(text, char="*"):
    border = char * (len(text) + 4)
    print(border)
    print(f"{char} {text} {char}")
    print(border)

create_border("Hello, Python!")
# Output:
# *******************
# * Hello, Python! *
# *******************

create_border("Welcome!", "=")
# Output:
# ==============
# = Welcome! =
# ==============
```

## 🎯 Key Takeaways

✅ Functions make code reusable and organized
✅ Use `def` to define functions
✅ Parameters let you pass data to functions
✅ `return` sends data back from functions
✅ Default parameters provide fallback values
✅ Local variables exist only inside functions
✅ Global variables exist everywhere
✅ Document your functions with docstrings

## 🏋️ Practice Time!

Head over to [exercises.py](exercises.py) to practice creating functions!

## 🏆 Challenge (Optional)

Create a simple text-based game with functions:
1. `start_game()` - Welcomes the player
2. `get_player_choice()` - Asks player to choose rock, paper, or scissors
3. `get_computer_choice()` - Randomly chooses for computer
4. `determine_winner(player, computer)` - Determines who won
5. `play_again()` - Asks if player wants another round

Use all these functions together to create a complete Rock, Paper, Scissors game!

---

**Previous Lesson:** [⬅️ Control Flow](../04-control-flow/lesson.md)  
**Next Lesson:** Coming soon! ➡️
