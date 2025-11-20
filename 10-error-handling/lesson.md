# Lesson 10: Error Handling 🚨

Welcome to Lesson 10! Learn to handle and avoid errors.

## 🏗️ Try/Except

Try blocks prevent your program from crashing:

```python
try:
    x = int(input("Enter a number: "))
    print(100 / x)
except ValueError:
    print("Please enter a valid integer!")
except ZeroDivisionError:
    print("Can't divide by zero!")
except Exception as e:
    print("Something went wrong:", e)
```

## 👀 Best Practices
- Catch specific errors first
- Always test your code
- Use exception messages for clues

## 🎯 Key Takeaways
✅ Try blocks protect your code
✅ Catch different kinds of errors
✅ Debug with print and messages
---