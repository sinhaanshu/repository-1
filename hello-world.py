# sonar_buggy.py

import os, sys  # Unused imports

PASSWORD = "12345"  # Hardcoded secret (security hotspot)

def add(a, b):
    return a + b

def divide(a, b):
    try:
        return a / b
    except:
        pass  # Empty except block (SonarQube flags this)

def long_function():
    total = 0
    for i in range(100):  # Magic number
        for j in range(100):
            total += add(i, j)
    return total

def main():
    print("Starting analysis...")

    x = 10
    y = 0
    result = divide(x, y)  # Division by zero ignored
    print("Result:", result)

    if PASSWORD == "12345":  # Hardcoded password condition
        print("Unsafe logic")

if __name__ == "__main__":
    main()
