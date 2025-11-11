# buggy_script.py

def divide_numbers(a, b):
    # BUG: division by zero not handled
    return a / b

def main():
    x = 10
    y = 0   # BUG: this will cause ZeroDivisionError
    result = divide_numbers(x, y)
    print("Result is: " + result)  # BUG: string concatenation with number
    print("Script finished")

if __name__ == "__main__":
    main()
