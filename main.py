import random
from fumctions.add import add
from fumctions.multiply import multiply
from fumctions.division import divide

def get_valid_input():
    """
    Prompt the user to enter at least two non-zero integers.

    Returns:
        list: A list of integers with at least two non-zero values.
    """
    while True:
        try:
            user_input = input("Enter at least two non-zero integers separated by spaces: ")
            numbers = list(map(int, user_input.strip().split()))
            non_zero_numbers = [num for num in numbers if num != 0]
            if len(non_zero_numbers) >= 2:
                return non_zero_numbers
            else:
                print("Please enter at least two non-zero integers.")
        except ValueError:
            print("Invalid input. Please enter integers only.")

def ensure_even_sum(numbers):
    """
    Ensure the sum of the list is even by adding random non-zero integers.

    Tries up to three times to make the sum even by appending a random non-zero integer.

    Args:
        numbers (list): A list of integers.

    Returns:
        list: Modified list with an even sum.
    """
    attempts = 0
    while add(numbers) % 2 != 0 and attempts < 3:
        rand_num = random.choice([i for i in range(-10, 11) if i != 0])
        print(f"Sum is odd. Adding random number {rand_num} to the list.")
        numbers.append(rand_num)
        attempts += 1
    return numbers

def ensure_even_product(numbers):
    """
    Ensure the product of the list is even by adding random non-zero integers.

    Tries up to three times to make the product even by appending a random non-zero integer.

    Args:
        numbers (list): A list of integers.

    Returns:
        list: Modified list with an even product.
    """
    attempts = 0
    while multiply(numbers) % 2 != 0 and attempts < 3:
        rand_num = random.choice([i for i in range(-10, 11) if i != 0])
        print(f"Product is odd. Adding random number {rand_num} to the list.")
        numbers.append(rand_num)
        attempts += 1
    return numbers

def ensure_non_zero_last(numbers):
    """
    Ensure the last number in the list is non-zero.

    If the last number is zero, replaces it with a random non-zero integer.

    Args:
        numbers (list): A list of integers.

    Returns:
        list: Modified list with a non-zero last element.
    """
    if numbers[-1] == 0:
        rand_num = random.choice([i for i in range(-10, 11) if i != 0])
        print(f"Last number is zero. Replacing with random number {rand_num}.")
        numbers[-1] = rand_num
    return numbers

def main():
    """
    Main function to execute the workflow:
    - Get valid input
    - Ensure even sum
    - Ensure even product
    - Ensure non-zero last element
    - Perform division of first and last number
    """
    numbers = get_valid_input()
    numbers = ensure_even_sum(numbers)
    numbers = ensure_even_product(numbers)
    numbers = ensure_non_zero_last(numbers)

    try:
        result = divide(numbers)
        print(f"Result of dividing first number by last number (rounded): {result}")
    except ValueError as e:
        print(f"Error during division: {e}")

if __name__ == "__main__":
    main()
