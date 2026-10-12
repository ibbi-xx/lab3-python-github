def add(num1, num2):
    return num1 + num2

def subtract(num1, num2):
    return num1 - num2

def multiply(num1, num2):
    return num1 * num2

def division(num1, num2):
    if num2 == 0:
        return "Number cannot be divided by 0"
    return num1 / num2

def even_or_odd(num1):
    if num1 % 2 == 0:
        return f"The number {int(num1)} is even"
    else:
        return f"The number {int(num1)} is odd"

def percentage(num1, num2):
    if num2 == 0:
        return "Cannot calculate percentage with base zero."
    perc = (num1 / num2) * 100
    return f"{num1} is {perc:.2f}% of {num2}"

continue_calculation = True

while continue_calculation:
    print("\n1. Addition\n2. Subtraction\n3. Multiplication\n4. Division\n5. Check Even/Odd\n6. Calculate Percentage\n7. Exit")
    userinput = input("Choose the option number (1-7): ")

    if userinput in ["1", "2", "3", "4", "6"]:
        try:
            num1 = float(input("Input a number: "))
            num2 = float(input("Input a second number: "))
            
            if userinput == "1":
                print("Result:", add(num1, num2))
            elif userinput == "2":
                print("Result:", subtract(num1, num2))
            elif userinput == "3":
                print("Result:", multiply(num1, num2))
            elif userinput == "4":
                print("Result:", division(num1, num2))
            elif userinput == "6":
                print(percentage(num1, num2))
        except ValueError:
            print("Invalid input! Please enter valid numbers.")

    elif userinput == "5":
        try:
            num1 = float(input("Input a number: "))
            print(even_or_odd(num1))
        except ValueError:
            print("Invalid input! Please enter a valid number.")

    elif userinput == "7":
        continue_calculation = False
        print("Have a nice day!")

    else:
        print("Invalid Choice! Please enter a number between 1 and 7.")
