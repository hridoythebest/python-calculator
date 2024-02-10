import math

# Arithmetic Functions
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Division by zero is not allowed!"
    else:
        return x / y

# Trigonometric Functions
def sine(x):
    return math.sin(math.radians(x))

def cosine(x):
    return math.cos(math.radians(x))

def tangent(x):
    return math.tan(math.radians(x))

# Exponential Function
def power(x, y):
    return x ** y

# Unit Conversion 
conversion_factors = {
    'length': {
        'm': 1,
        'cm': 0.01,
        'km': 1000,
        'ft': 0.3048,
        'in': 0.0254 
    },
    'weight': {
        'kg': 1,
        'g': 0.001,
        'lb': 0.453592,
        'oz': 0.0283495
    }
}

def convert_units(value, from_unit, to_unit):
    if from_unit not in conversion_factors or to_unit not in conversion_factors:
        return "Invalid units"

    try:
        # Find the categories first
        from_category = next((cat for cat in conversion_factors if from_unit in conversion_factors[cat]), None)
        to_category = next((cat for cat in conversion_factors if to_unit in conversion_factors[cat]), None)

        # Ensure units are in the same category
        if from_category != to_category: 
            return "Cannot convert between different categories"

        from_factor = conversion_factors[from_category][from_unit] 
        to_factor = conversion_factors[to_category][to_unit]
        result = value * from_factor / to_factor
        return result

    except ZeroDivisionError:
        return "Cannot convert to the same unit"

# Calculator Main Loop
while True:
    print("Select operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Sine")
    print("6. Cosine")
    print("7. Tangent")
    print("8. Exponential")
    print("9. Unit Conversion")

    choice = input("Enter choice(1/2/3/4/5/6/7/8/9): ")

    if choice in ('1', '2', '3', '4', '8'):
        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))

            if choice == '1':
                print(num1, "+", num2, "=", add(num1, num2))
            elif choice == '2':
                print(num1, "-", num2, "=", subtract(num1, num2))
            elif choice == '3':
                print(num1, "*", num2, "=", multiply(num1, num2))
            elif choice == '4':
                print(num1, "/", num2, "=", divide(num1, num2))
            elif choice == '8':
                print(num1, "^", num2, "=", power(num1, num2)) 

        except ValueError:
            print("Invalid input. Please enter numbers only.")

    elif choice in ('5', '6', '7'):
        try:
            num = float(input("Enter angle in degrees: "))
            if choice == '5':
                print("sin(", num, ") =", sine(num))
            elif choice == '6':
                print("cos(", num, ") =", cosine(num))
            elif choice == '7':
                print("tan(", num, ") =", tangent(num))
        except ValueError:
            print("Invalid input. Please enter a number.")

    elif choice == '9':
        try:
            value = float(input("Enter value to convert: "))

            print("Select type of conversion:")
            for key in conversion_factors:
                print(key)  # Print available categories (e.g., length, weight)

            category = input("Enter category: ").lower()

            if category in conversion_factors:
                from_unit = input("Enter original unit: ").lower()
                to_unit = input("Enter target unit: ").lower()

                result = convert_units(value, from_unit, to_unit)

                if result is not None: 
                    print(value, from_unit, "=", result, to_unit)
                else:
                    print(result)  # Print error message from convert_units
            else:
                print("Invalid category")

        except ValueError:
            print("Invalid input. Please enter a number.")

    else:
        print("Invalid Input")
