# try_except_explained.py
# A complete explanation of try-except blocks in Python

# ===========================
# 🧠 What is try-except for?
# ===========================
# It is used for *handling errors* (also called exceptions) in Python.
# Instead of crashing your program, it lets you react to the error gracefully.

# ===========================
# 📌 Basic Structure
# ===========================
# try:
#     code that might raise an error
# except SomeError:
#     code that runs if that error occurs

print("===== Example 1: Basic try-except =====")
try:
    print("Before error")
    result = 10 / 0  # This line will raise ZeroDivisionError
    print("This won't be printed")
except ZeroDivisionError:
    print("You tried to divide by zero!")

# ===========================
# 📌 Catching any error (not recommended, but sometimes useful)
# ===========================
print("\n===== Example 2: Catching any exception =====")
try:
    x = int("hello")  # Will raise ValueError
except Exception as e:  # Catch *any* error
    print("An error occurred:", e)

# ===========================
# 📌 Catching multiple specific exceptions
# ===========================
print("\n===== Example 3: Catching multiple exceptions =====")
try:
    lst = [1, 2, 3]
    print(lst[5])  # IndexError
except ValueError:
    print("Value error occurred.")
except IndexError:
    print("You tried to access an invalid list index.")

# ===========================
# 📌 Using 'else' block (runs only if no exception occurs)
# ===========================
print("\n===== Example 4: try-except-else =====")
try:
    x = int("42")
except ValueError:
    print("Could not convert to integer.")
else:
    print("Conversion successful! x =", x)

# ===========================
# 📌 Using 'finally' block (always runs, error or not)
# ===========================
print("\n===== Example 5: try-finally =====")
try:
    print("Trying something risky...")
    y = 1 / 1
except ZeroDivisionError:
    print("Divide by zero!")
finally:
    print("This code runs no matter what.")

# ===========================
# 📌 Raising your own exceptions (for custom logic)
# ===========================
print("\n===== Example 6: Raising exceptions manually =====")
def withdraw_money(balance, amount):
    if amount > balance:
        raise ValueError("Insufficient funds.")
    return balance - amount

try:
    new_balance = withdraw_money(100, 150)
except ValueError as err:
    print("Error:", err)

# ===========================
# ✅ Summary
# ===========================
# - Use try-except to catch and handle runtime errors.
# - Always catch specific exceptions where possible.
# - Use 'else' for code that should run only if no error occurs.
# - Use 'finally' for cleanup actions (e.g. closing files or network connections).
# - You can raise your own errors using 'raise'.

print("\nAll examples complete.")
