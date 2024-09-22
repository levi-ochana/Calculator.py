def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error! Division by zero."
    else:
        return x / y

def power_of(x, y):
    return x ** y

def modulos(x, y):
    return x % y

def is_prime(z):
    if z <= 1:
        return False
    for i in range(2, int(z**0.5) + 1):
        if z % i == 0:
            return False
    return True

def odd_or_even(z):
    return "even" if z % 2 == 0 else "odd"

def check_is_divided_by_five(z):
    return z % 5 == 0

def display_menu():
    print("Please choose an option from the menu:")
    print("1. Add numbers")
    print("2. Subtract numbers")
    print("3. Multiply numbers")
    print("4. Divide numbers")
    print("5. Power of numbers")
    print("6. Modulus of numbers")
    print("7. Exit")

def get_choice():
    while True:
        try:
            choice = int(input("Enter your choice between 1-7: "))
            if 1 <= choice <= 7:
                return choice
            else:
                print("Invalid choice, please enter a number between 1 and 7.")
        except ValueError:
            print("Invalid input, please enter a valid integer.")

def get_numbers():
    while True:
        try:
            numbers_input = input("Enter two integers separated by a space or comma: ")
            numbers = numbers_input.replace(",", " ").split()

            if len(numbers) != 2:
                print("Please enter exactly two integers.")
                continue

            num1 = int(numbers[0])
            num2 = int(numbers[1])
            return num1, num2
        except ValueError:
            print("Invalid input. Please enter valid integers.")

def perform_operation(choice):
    if choice == 7:
        print("Exiting the program")
        return False

    x, y = get_numbers()


    if choice == 1:
        result = add(x, y)
    elif choice == 2:
        result = subtract(x, y)
    elif choice == 3:
        result = multiply(x, y)
    elif choice == 4:
        result = divide(x, y)
    elif choice == 5:
        result = power_of(x, y)
    elif choice == 6:
        result = modulos(x, y)
    print("\n" * 2)
    print(f"Result: {result}")

    if isinstance(result, (int, float)):
        print(f"{result} is {'prime' if is_prime(result) else 'not prime'}")
        print(f"{result} is {odd_or_even(result)}")
        print(f"{result} is {'divided by five without a remainder' if check_is_divided_by_five(result) else 'not divided by five without a remainder'}")
    else:
        print("Cannot perform additional checks on the result.")
    print("\n" * 2)
    return True

def main():
    while True:
        display_menu()
        choice = get_choice()
        if not perform_operation(choice):
            break

main()
