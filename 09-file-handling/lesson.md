# Lesson 9: File Handling 📂

Welcome to Lesson 9! You'll learn how to read and write files — a super power in programming.

## 📖 Reading Files

```python
with open('hello.txt', 'r') as file:
    contents = file.read()
    print(contents)
```

## ✍️ Writing Files

```python
with open('hello.txt', 'w') as file:
    file.write("Hello, world!")
```

## 📦 Working with CSV and JSON

CSV:
```python
import csv
with open('data.csv', newline='') as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)
```

JSON:
```python
import json
with open('user.json') as f:
    data = json.load(f)
    print(data)
```

## 🎯 Key Takeaways
✅ Files store data outside code
✅ Can read/write text, CSV, JSON
✅ Always close files ("with" does this for you)
---