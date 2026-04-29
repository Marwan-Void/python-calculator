print("Welcome To Marwan's Python Calculator\n")
while True:
    try:
        num1 = int(input("Enter The First Number: ").strip())
        op = input("Enter The Operator: ").lower().strip()
        num2 = int(input("Enter The Second Number: ").strip())

        print("\nThe Result:")
        if op == "+":
            print(num1 + num2)
        elif op == "-":
            print(num1 - num2)
        elif op == "*" or op == "x":
            print(num1 * num2)
        elif op == "/":
            print(num1 / num2)
        elif op == "**" or op == "^" or op == "pow" or op == "power":
            print(num1 ** num2)
        elif op == "%":
            print(num1 % num2)
        else:
            raise ValueError("Error: Unknown Operator!")
    except ValueError as e:
        error_message = str(e)
        if error_message != "Error: Unknown Operator!":
            error_message = "\nError: You Should Enter Numbers and an Operator Only!"
        print(f"{error_message}")
    except ZeroDivisionError:
        print("Error: You Can't Divide/Modulo By Zero")
    
    again = input("\nWanna Try Again?(y/n)\n").strip().lower()
    print()
    if again == "y" or again == "yes":
        print("------------------------------------------------------")
        continue
    else:
        print("K! Good Bye...")
        break