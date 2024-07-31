import calculator

def main():
    try:
        a=int(input("enter first number"))
        b = int(input("enter first number"))
        print("select operation:")
        print("1.add")
        print("2.subtract")
        print("3.multiply")
        print("4.division")
        choice = input("Enter choice (1/2/3/4): ")

        if choice == '1':
                result = calculator.add(a, b)
                print(f"The result of addition is: {result}")
        elif choice == '2':
               result = calculator.subtract(a, b)
               print(f"The result of subtraction is: {result}")
        elif choice == '3':
              result = calculator.multiply(a, b)
              print(f"The result of multiplication is: {result}")
        elif choice == '4':
              result = calculator.divide(a, b)
              print(f"The result of division is: {result}")
        else:
              print("Invalid input. Please enter a number between 1 and 4.")

    except ValueError as e:
            print(e)
            print("Invalid input. Please enter numerical values.")

if __name__ == "__main__":
    main()


