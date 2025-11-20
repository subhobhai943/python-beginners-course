# Lesson 11 Projects — Code Templates

# Number Guessing Game
import random
number = random.randint(1, 50)
for guess in range(6):
    user = int(input("Guess the number (1-50): "))
    if user == number:
        print("Congratulations!")
        break
    elif user < number:
        print("Too low!")
    else:
        print("Too high!")
else:
    print(f"Sorry, the number was {number}")

# To-Do List App

tasks = []
while True:
    action = input("Add / Remove / Show / Exit: ").lower()
    if action == "add":
        tasks.append(input("Task to add: "))
    elif action == "remove":
        try:
            tasks.remove(input("Task to remove: "))
        except ValueError:
            print("Task not found.")
    elif action == "show":
        print(tasks)
    elif action == "exit":
        break
    else:
        print("Unknown command.")

# Simple Calculator
while True:
    print("1. Add 2. Subtract 3. Multiply 4. Divide 5. Exit")
    choice = input("Choose: ")
    if choice == "5":
        break
    a = float(input("First number: "))
    b = float(input("Second number: "))
    if choice == "1":
        print(a + b)
    elif choice == "2":
        print(a - b)
    elif choice == "3":
        print(a * b)
    elif choice == "4":
        try:
            print(a / b)
        except ZeroDivisionError:
            print("Cannot divide by zero!")

# Password Generator
import random
import string
length = int(input("Password length: "))
chars = string.ascii_letters + string.digits + string.punctuation
password = "".join(random.choice(chars) for _ in range(length))
print("Generated password:", password)
---