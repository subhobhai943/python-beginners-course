# Lesson 7: Dictionaries and Sets 🔑

Welcome to Lesson 7! Let's learn about dictionaries and sets — perfect for storing pairs and unique items.

## 📖 Dictionaries

Dictionaries hold data as key-value pairs. Think: word and meaning, name and phone number.

```python
student = {"name": "Alex", "age": 15, "grade": "A"}
print(student["name"])  # 'Alex'
```

Add or change:
```python
student["email"] = "alex@example.com"
student["age"] = 16
```

Loop with:
```python
for key in student:
    print(key, student[key])
```

## 🔢 Sets

Sets store unique items (no duplicates):

```python
colors = {"red", "blue", "green", "red"}
print(colors)  # {'red', 'green', 'blue'}
```

Add with `.add()`, remove with `.remove()`

## 🎯 Key Takeaways

✅ Dictionaries for key-value data
✅ Sets for unique items
✅ Fast lookup and filtering
---