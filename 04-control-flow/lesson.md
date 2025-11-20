# Lesson 4: Control Flow - Making Decisions 🚦

Welcome to Lesson 4! Now we'll learn how to make our programs smart by making decisions and repeating tasks.

## 🤔 What is Control Flow?

Control flow determines which parts of your code run and when. It's like a roadmap for your program!

## 🔀 If Statements

If statements let your program make decisions:

```python
age = 16

if age >= 18:
    print("You can vote!")
```

**How it works:**
- Python checks if the condition (`age >= 18`) is True
- If True, it runs the indented code
- If False, it skips that code

### If-Else Statements

Provide an alternative when the condition is False:

```python
age = 15

if age >= 18:
    print("You can vote!")
else:
    print("You're too young to vote.")
    print(f"Wait {18 - age} more years!")
```

### If-Elif-Else Statements

Check multiple conditions:

```python
score = 85

if score >= 90:
    print("Grade: A - Excellent!")
elif score >= 80:
    print("Grade: B - Great job!")
elif score >= 70:
    print("Grade: C - Good work!")
elif score >= 60:
    print("Grade: D - You passed!")
else:
    print("Grade: F - Keep studying!")
```

## 🎯 Important: Indentation!

Python uses indentation (spaces) to group code:

```python
# ✅ Correct
if age >= 18:
    print("You can vote!")  # 4 spaces indent
    print("Register today!")  # 4 spaces indent

# ❌ Wrong - will cause an error
if age >= 18:
print("You can vote!")  # No indent - ERROR!
```

## 🔁 For Loops

Repeat code a specific number of times:

### Looping Through Numbers

```python
# Print numbers 0 to 4
for i in range(5):
    print(i)
# Output: 0, 1, 2, 3, 4

# Print numbers 1 to 5
for i in range(1, 6):
    print(i)
# Output: 1, 2, 3, 4, 5

# Count by 2s
for i in range(0, 11, 2):
    print(i)
# Output: 0, 2, 4, 6, 8, 10
```

### Looping Through Strings

```python
name = "Python"

for letter in name:
    print(letter)
# Output:
# P
# y
# t
# h
# o
# n
```

### Fun Example: Countdown

```python
print("Rocket launch countdown:")
for i in range(10, 0, -1):
    print(i)
print("Blast off! 🚀")
```

## ♾️ While Loops

Repeat code while a condition is True:

```python
count = 1

while count <= 5:
    print(f"Count: {count}")
    count += 1

print("Done!")
# Output:
# Count: 1
# Count: 2
# Count: 3
# Count: 4
# Count: 5
# Done!
```

### Real-World Example: Password Checker

```python
password = ""

while password != "python123":
    password = input("Enter password: ")
    if password != "python123":
        print("Wrong password! Try again.")

print("Access granted! ✅")
```

⚠️ **Warning:** Make sure your while loop has a way to stop, or it will run forever!

## 🛑 Break Statement

Exit a loop early:

```python
# Find the first number divisible by 7
for i in range(1, 100):
    if i % 7 == 0:
        print(f"Found it! {i}")
        break  # Exit the loop
# Output: Found it! 7
```

## ⏭️ Continue Statement

Skip to the next iteration:

```python
# Print only odd numbers
for i in range(10):
    if i % 2 == 0:
        continue  # Skip even numbers
    print(i)
# Output: 1, 3, 5, 7, 9
```

## 🎮 Fun Examples

### Example 1: Multiplication Table

```python
number = 5

print(f"Multiplication table for {number}:")
for i in range(1, 11):
    result = number * i
    print(f"{number} × {i} = {result}")
```

### Example 2: Password Strength Checker

```python
password = input("Create a password: ")

if len(password) < 6:
    print("❌ Too short! Use at least 6 characters.")
elif len(password) < 10:
    print("⚠️ Okay, but could be stronger.")
else:
    print("✅ Strong password!")
```

### Example 3: Number Guessing Game

```python
secret_number = 7
guesses = 3

for attempt in range(guesses):
    guess = int(input(f"Guess the number (Attempt {attempt + 1}/{guesses}): "))
    
    if guess == secret_number:
        print("🎉 Correct! You win!")
        break
    elif guess < secret_number:
        print("📈 Too low!")
    else:
        print("📉 Too high!")
else:
    print(f"😢 Game over! The number was {secret_number}")
```

## 🔗 Nested Loops and Conditions

You can put loops inside loops:

```python
# Print a pattern
for row in range(5):
    for col in range(row + 1):
        print("*", end="")
    print()  # New line
# Output:
# *
# **
# ***
# ****
# *****
```

## 🎯 Key Takeaways

✅ `if` makes decisions based on conditions
✅ `elif` checks additional conditions
✅ `else` handles all other cases
✅ `for` loops repeat a specific number of times
✅ `while` loops repeat while a condition is True
✅ `break` exits a loop early
✅ `continue` skips to the next iteration
✅ Indentation is crucial in Python!

## 🏋️ Practice Time!

Head over to [exercises.py](exercises.py) to practice control flow!

## 🏆 Challenge (Optional)

Create a simple menu-driven calculator:
1. Show a menu with options: Add, Subtract, Multiply, Divide, Exit
2. Ask the user to choose an option
3. If they choose a math operation, ask for two numbers and perform it
4. Keep showing the menu until they choose Exit
5. Use if-elif-else and a while loop

---

**Previous Lesson:** [⬅️ Operators](../03-operators/lesson.md)  
**Next Lesson:** [Functions](../05-functions/lesson.md) ➡️
