# main.py

import random_generator


def main():
    try:
        count = 10
        start = int(input("Enter the start of the range: "))
        end = int(input("Enter the end of the range: "))

        # Ensure start is less than end
        if start >= end:
            print("Invalid range. The start must be less than the end.")
            return

        random_numbers = random_generator.generate_random_numbers(count, start, end)
        print(f"List of {count} random numbers between {start} and {end}:")
        print(random_numbers)
    except ValueError:
        print("Invalid input. Please enter integer values for the range.")


if __name__ == "__main__":
    main()
