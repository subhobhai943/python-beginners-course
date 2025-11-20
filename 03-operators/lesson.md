# Lesson 3: Operators ⚙️

Welcome to Lesson 3! Let's learn how to perform operations and make comparisons in Python.

## 🧮 Arithmetic Operators

These operators help you do math:

```python
# Basic Math
print(10 + 5)    # Addition: 15
print(10 - 5)    # Subtraction: 5
print(10 * 5)    # Multiplication: 50
print(10 / 5)    # Division: 2.0 (always returns a float)
```

### More Math Operators

```python
print(10 // 3)   # Floor division: 3 (rounds down)
print(10 % 3)    # Modulus (remainder): 1
print(2 ** 3)    # Power (exponent): 8 (2 to the power of 3)
```

**Real-World Example:**
```python
# Is a number even or odd?
number = 7
remainder = number % 2
print(remainder)  # 1 means odd, 0 means even

# Calculate total cost
price = 19.99
quantity = 3
total = price * quantity
print(f"Total cost: ${total}")  # Total cost: $59.97
```

## 📊 Comparison Operators

These compare values and return True or False:

```python
print(5 == 5)    # Equal to: True
print(5 != 3)    # Not equal to: True
print(5 > 3)     # Greater than: True
print(5 < 3)     # Less than: False
print(5 >= 5)    # Greater than or equal: True
print(5 <= 4)    # Less than or equal: False
```

**Real-World Example:**
```python
age = 16
can_drive = age >= 16
print(can_drive)  # True

score = 85
passed = score >= 60
print(f"Did you pass? {passed}")  # Did you pass? True
```

## 🔗 Logical Operators

Combine multiple conditions:

### AND Operator
Both conditions must be True:

```python
age = 16
has_license = True

can_drive = age >= 16 and has_license
print(can_drive)  # True (both conditions are True)

# Another example
is_weekend = True
has_homework = False
can_play = is_weekend and not has_homework
print(can_play)  # True
```

### OR Operator
At least one condition must be True:

```python
is_raining = False
is_snowing = True

need_jacket = is_raining or is_snowing
print(need_jacket)  # True (one condition is True)

# Another example
has_cash = False
has_card = True
can_buy = has_cash or has_card
print(can_buy)  # True
```

### NOT Operator
Reverses the condition:

```python
is_tired = False
print(not is_tired)  # True

is_sunny = True
is_cloudy = not is_sunny
print(is_cloudy)  # False
```

## 🎯 Assignment Operators

Shortcuts for updating variables:

```python
score = 10

# Long way
score = score + 5
print(score)  # 15

# Short way (same result)
score += 5    # Same as: score = score + 5
print(score)  # 20
```

**All Assignment Operators:**
```python
x = 10

x += 5   # x = x + 5  → 15
x -= 3   # x = x - 3  → 12
x *= 2   # x = x * 2  → 24
x /= 4   # x = x / 4  → 6.0
x //= 2  # x = x // 2 → 3.0
x %= 2   # x = x % 2  → 1.0
x **= 3  # x = x ** 3 → 1.0
```

## 🎮 Operator Priority (Order of Operations)

Just like in math, Python follows an order:

```python
result = 5 + 3 * 2
print(result)  # 11 (multiplication happens first)

# Use parentheses to change order
result = (5 + 3) * 2
print(result)  # 16 (addition happens first)
```

**Priority Order (highest to lowest):**
1. `()` Parentheses
2. `**` Exponent
3. `*`, `/`, `//`, `%` Multiplication, Division
4. `+`, `-` Addition, Subtraction
5. `==`, `!=`, `>`, `<`, `>=`, `<=` Comparisons
6. `not` Logical NOT
7. `and` Logical AND
8. `or` Logical OR

## 🎪 Fun Examples

### Example 1: Gaming Score System
```python
base_score = 100
bonus_points = 50
multiplier = 2

final_score = (base_score + bonus_points) * multiplier
print(f"Your final score: {final_score}")  # 300

high_score = 500
is_new_record = final_score > high_score
print(f"New record? {is_new_record}")  # False
```

### Example 2: Age Checker
```python
age = 15
is_teenager = age >= 13 and age <= 19
print(f"Are you a teenager? {is_teenager}")  # True
```

### Example 3: Temperature Converter
```python
celsius = 25
fahrenheit = (celsius * 9/5) + 32
print(f"{celsius}°C is {fahrenheit}°F")  # 25°C is 77.0°F
```

## 🎯 Key Takeaways

✅ Arithmetic operators: `+`, `-`, `*`, `/`, `//`, `%`, `**`
✅ Comparison operators return True or False
✅ `and` requires both conditions True
✅ `or` requires at least one condition True
✅ `not` reverses the condition
✅ Use `+=`, `-=`, etc. as shortcuts
✅ Parentheses control operation order

## 🏋️ Practice Time!

Head over to [exercises.py](exercises.py) to practice operators!

## 🏆 Challenge (Optional)

Create a program that:
1. Asks for the user's test score (0-100)
2. Determines if they passed (score >= 60)
3. Determines their grade:
   - 90-100: A
   - 80-89: B
   - 70-79: C
   - 60-69: D
   - Below 60: F
4. Prints whether they passed and their grade

Hint: You'll use multiple comparison operators!

---

**Previous Lesson:** [⬅️ Variables and Data Types](../02-variables-and-data-types/lesson.md)  
**Next Lesson:** [Control Flow](../04-control-flow/lesson.md) ➡️
