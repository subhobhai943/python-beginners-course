# Lesson 6: Lists and Tuples 📃

Welcome to Lesson 6! You'll learn how to store groups of items and work with collections.

## 📋 Lists

Lists are ordered collections that can hold any type of data. Think of them as containers:

```python
fruits = ["apple", "banana", "cherry"]
print(fruits)  # Prints: ['apple', 'banana', 'cherry']
```

You can access items using their index:

```python
print(fruits[0])  # 'apple'
print(fruits[1])  # 'banana'
```

Change items:
```python
fruits[1] = "blueberry"
print(fruits)
```

Lists can grow and shrink:
```python
fruits.append("orange")
fruits.remove("apple")
```

## 📃 Tuples

Tuples are like lists, but cannot change (immutable):

```python
colors = ("red", "green", "blue")
print(colors)
```

### Main list methods:
- `.append()` — add item
- `.remove()` — remove item
- `.pop()` — take item out
- `.sort()` — sort items
- `.reverse()` — reverse the order

## 🎯 Key Takeaways

✅ Lists are changeable
✅ Tuples are fixed
✅ Store many items in a single variable

---